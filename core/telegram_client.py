#!/usr/bin/env python3
"""
Telegram客户端模块 - Android适配版本
处理与Telegram API的交互，适配Android环境
"""

import asyncio
import re
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path
from kivy.logger import Logger

try:
    from telethon import TelegramClient, events
    from telethon.tl.types import Channel, Chat, User, MessageMediaPhoto, MessageMediaDocument
    from telethon.errors import SessionPasswordNeededError, FloodWaitError, ChannelPrivateError
    TELETHON_AVAILABLE = True
except ImportError:
    TELETHON_AVAILABLE = False
    Logger.warning("AndroidTelegramClient: Telethon未安装，将使用模拟模式")

try:
    # Android平台相关导入
    from android.storage import primary_external_storage_path
    ANDROID_AVAILABLE = True
except ImportError:
    # 非Android平台
    ANDROID_AVAILABLE = False

from .config import android_config
from .database import ProcessedMessage, android_db_manager

class AndroidTelegramClient:
    """Android适配的Telegram客户端"""
    
    def __init__(self):
        """初始化Telegram客户端"""
        self.client = None
        self.is_connected = False
        self.session_path = self._get_session_path()
        self._init_client()
    
    def _get_session_path(self) -> str:
        """获取会话文件路径"""
        try:
            if ANDROID_AVAILABLE:
                # Android内部存储路径
                app_dir = Path('/data/data/org.example.telegrambot/files')
                if not app_dir.exists():
                    # 备用路径：外部存储
                    external_path = primary_external_storage_path()
                    app_dir = Path(external_path) / 'TelegramBot'
                
                app_dir.mkdir(parents=True, exist_ok=True)
                return str(app_dir / 'telegram_session')
            else:
                # 非Android平台
                return 'telegram_session'
                
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 获取会话路径失败 - {e}")
            return 'telegram_session'
    
    def _init_client(self):
        """初始化Telegram客户端"""
        try:
            if not TELETHON_AVAILABLE:
                Logger.warning("AndroidTelegramClient: Telethon不可用，使用模拟模式")
                return
            
            api_id = android_config.get('API_ID', 0)
            api_hash = android_config.get('API_HASH', '')
            
            if not api_id or not api_hash:
                Logger.warning("AndroidTelegramClient: API配置不完整")
                return
            
            self.client = TelegramClient(
                self.session_path,
                api_id,
                api_hash,
                device_model='Android Bot',
                system_version='Android',
                app_version='1.0.0',
                lang_code='zh',
                system_lang_code='zh'
            )
            
            Logger.info("AndroidTelegramClient: 客户端初始化成功")
            
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 客户端初始化失败 - {e}")
    
    async def connect(self) -> bool:
        """连接到Telegram"""
        try:
            if not self.client:
                Logger.error("AndroidTelegramClient: 客户端未初始化")
                return False
            
            await self.client.connect()
            
            if not await self.client.is_user_authorized():
                Logger.warning("AndroidTelegramClient: 用户未授权，需要登录")
                return False
            
            self.is_connected = True
            Logger.info("AndroidTelegramClient: 连接成功")
            return True
            
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 连接失败 - {e}")
            return False
    
    async def disconnect(self):
        """断开连接"""
        try:
            if self.client and self.is_connected:
                await self.client.disconnect()
                self.is_connected = False
                Logger.info("AndroidTelegramClient: 连接已断开")
                
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 断开连接失败 - {e}")
    
    async def send_code_request(self, phone_number: str) -> bool:
        """发送验证码请求"""
        try:
            if not self.client:
                return False
            
            await self.client.connect()
            await self.client.send_code_request(phone_number)
            Logger.info(f"AndroidTelegramClient: 验证码已发送到 {phone_number}")
            return True
            
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 发送验证码失败 - {e}")
            return False
    
    async def sign_in(self, phone_number: str, code: str, password: str = None) -> bool:
        """登录"""
        try:
            if not self.client:
                return False
            
            await self.client.connect()
            
            try:
                await self.client.sign_in(phone_number, code)
            except SessionPasswordNeededError:
                if password:
                    await self.client.sign_in(password=password)
                else:
                    Logger.error("AndroidTelegramClient: 需要两步验证密码")
                    return False
            
            self.is_connected = True
            Logger.info("AndroidTelegramClient: 登录成功")
            return True
            
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 登录失败 - {e}")
            return False
    
    async def get_channel_messages(self, channel_username: str, limit: int = 10, 
                                 hours_back: int = 24) -> List[Dict[str, Any]]:
        """获取频道消息"""
        try:
            if not self.is_connected:
                if not await self.connect():
                    return []
            
            # 获取频道实体
            try:
                channel = await self.client.get_entity(channel_username)
            except ChannelPrivateError:
                Logger.error(f"AndroidTelegramClient: 频道 {channel_username} 是私有的或不存在")
                return []
            except Exception as e:
                Logger.error(f"AndroidTelegramClient: 获取频道实体失败 {channel_username} - {e}")
                return []
            
            # 计算时间范围
            offset_date = datetime.now() - timedelta(hours=hours_back)
            
            messages = []
            async for message in self.client.iter_messages(
                channel, 
                limit=limit,
                offset_date=offset_date
            ):
                if message.text or message.media:
                    message_data = await self._extract_message_content(message, channel)
                    if message_data:
                        messages.append(message_data)
            
            Logger.info(f"AndroidTelegramClient: 从 {channel_username} 获取到 {len(messages)} 条消息")
            return messages
            
        except FloodWaitError as e:
            Logger.warning(f"AndroidTelegramClient: 触发限流，等待 {e.seconds} 秒")
            await asyncio.sleep(e.seconds)
            return []
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 获取频道消息失败 - {e}")
            return []
    
    async def _extract_message_content(self, message, channel) -> Optional[Dict[str, Any]]:
        """提取消息内容"""
        try:
            content = ""
            content_type = "text"
            
            # 提取文本内容
            if message.text:
                content = message.text
            
            # 处理媒体内容
            if message.media:
                if isinstance(message.media, MessageMediaPhoto):
                    content_type = "photo"
                    if message.text:
                        content = message.text
                    else:
                        content = "[图片]"
                elif isinstance(message.media, MessageMediaDocument):
                    if message.media.document.mime_type.startswith('video/'):
                        content_type = "video"
                        content = message.text or "[视频]"
                    elif message.media.document.mime_type.startswith('audio/'):
                        content_type = "audio"
                        content = message.text or "[音频]"
                    else:
                        content_type = "document"
                        content = message.text or "[文档]"
            
            # 检查内容是否符合标签
            tags = self._check_tags(content)
            if not tags:
                return None
            
            return {
                'message_id': message.id,
                'channel_id': channel.id,
                'channel_name': getattr(channel, 'title', channel_username),
                'content': content,
                'content_type': content_type,
                'tags': tags,
                'date': message.date,
                'views': getattr(message, 'views', 0),
                'forwards': getattr(message, 'forwards', 0)
            }
            
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 提取消息内容失败 - {e}")
            return None
    
    def _check_tags(self, content: str) -> List[str]:
        """检查内容是否包含感兴趣的标签"""
        if not content:
            return []
        
        interest_tags = android_config.get('INTEREST_TAGS', [])
        if not interest_tags:
            return []
        
        matched_tags = []
        content_lower = content.lower()
        
        # 获取标签匹配配置
        tag_config = android_config.get('TAG_MATCHING', {})
        exact_match = tag_config.get('exact_match', True)
        case_sensitive = tag_config.get('case_sensitive', False)
        partial_match = tag_config.get('partial_match', True)
        include_synonyms = tag_config.get('include_synonyms', True)
        synonyms = tag_config.get('synonyms', {})
        
        for tag in interest_tags:
            tag_to_check = tag if case_sensitive else tag.lower()
            content_to_check = content if case_sensitive else content_lower
            
            # 精确匹配
            if exact_match:
                if tag_to_check in content_to_check.split():
                    matched_tags.append(tag)
                    continue
            
            # 部分匹配
            if partial_match:
                if tag_to_check in content_to_check:
                    matched_tags.append(tag)
                    continue
            
            # 同义词匹配
            if include_synonyms and tag in synonyms:
                for synonym in synonyms[tag]:
                    synonym_to_check = synonym if case_sensitive else synonym.lower()
                    if synonym_to_check in content_to_check:
                        matched_tags.append(tag)
                        break
        
        return list(set(matched_tags))  # 去重
    
    async def get_message_comments(self, channel_username: str, message_id: int, limit: int = 5) -> List[str]:
        """获取消息评论"""
        try:
            if not self.is_connected:
                if not await self.connect():
                    return []
            
            channel = await self.client.get_entity(channel_username)
            
            comments = []
            async for message in self.client.iter_messages(
                channel,
                reply_to=message_id,
                limit=limit
            ):
                if message.text:
                    comments.append(message.text)
            
            return comments
            
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 获取消息评论失败 - {e}")
            return []
    
    async def process_channels(self) -> Dict[str, Any]:
        """处理所有频道内容"""
        results = {
            'processed_count': 0,
            'sent_count': 0,
            'error_count': 0,
            'channels_processed': 0
        }
        
        try:
            channels = android_config.get('TARGET_CHANNELS', [])
            if not channels:
                Logger.warning("AndroidTelegramClient: 没有配置目标频道")
                return results
            
            check_interval_hours = android_config.get('CHECK_INTERVAL_HOURS', 24)
            max_messages = android_config.get('MAX_DAILY_MESSAGES', 100)
            
            for channel_username in channels:
                try:
                    Logger.info(f"AndroidTelegramClient: 处理频道 {channel_username}")
                    
                    # 获取频道消息
                    messages = await self.get_channel_messages(
                        channel_username,
                        limit=50,
                        hours_back=check_interval_hours
                    )
                    
                    for msg_data in messages:
                        try:
                            # 检查是否已处理
                            if android_db_manager.is_message_processed(
                                msg_data['message_id'], 
                                msg_data['channel_id']
                            ):
                                continue
                            
                            # 创建处理消息对象
                            processed_msg = ProcessedMessage(
                                message_id=msg_data['message_id'],
                                channel_id=msg_data['channel_id'],
                                channel_name=msg_data['channel_name'],
                                content=msg_data['content'],
                                content_type=msg_data['content_type'],
                                tags=msg_data['tags'],
                                processed_at=datetime.now()
                            )
                            
                            # 保存到数据库
                            if android_db_manager.add_processed_message(processed_msg):
                                results['processed_count'] += 1
                                
                                # 发送到机器人频道
                                if await self.send_to_bot_channel(processed_msg):
                                    android_db_manager.mark_message_sent(
                                        msg_data['message_id'],
                                        msg_data['channel_id']
                                    )
                                    results['sent_count'] += 1
                                
                                # 检查是否达到每日限制
                                if results['processed_count'] >= max_messages:
                                    Logger.info(f"AndroidTelegramClient: 达到每日消息限制 {max_messages}")
                                    break
                            
                        except Exception as e:
                            Logger.error(f"AndroidTelegramClient: 处理消息失败 - {e}")
                            results['error_count'] += 1
                    
                    # 更新频道检查时间
                    android_db_manager.update_channel_check_time(msg_data.get('channel_id', 0))
                    results['channels_processed'] += 1
                    
                    # 添加延迟避免限流
                    rate_limit_delay = android_config.get('RATE_LIMIT_DELAY', 1.0)
                    await asyncio.sleep(rate_limit_delay)
                    
                except Exception as e:
                    Logger.error(f"AndroidTelegramClient: 处理频道 {channel_username} 失败 - {e}")
                    results['error_count'] += 1
            
            # 更新每日统计
            today = datetime.now().strftime('%Y-%m-%d')
            android_db_manager.update_daily_stats(
                today,
                processed_count=results['processed_count'],
                sent_count=results['sent_count'],
                error_count=results['error_count'],
                channels_checked=results['channels_processed']
            )
            
            Logger.info(f"AndroidTelegramClient: 处理完成 - {results}")
            
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 处理频道失败 - {e}")
            results['error_count'] += 1
        
        return results
    
    async def send_to_bot_channel(self, message: ProcessedMessage) -> bool:
        """发送消息到机器人频道"""
        try:
            bot_channel = android_config.get('BOT_CHANNEL', '')
            if not bot_channel:
                Logger.warning("AndroidTelegramClient: 未配置机器人频道")
                return False
            
            if not self.is_connected:
                if not await self.connect():
                    return False
            
            # 构建消息内容
            content_type_mapping = android_config.get('CONTENT_TYPE_MAPPING', {})
            content_type_text = content_type_mapping.get(message.content_type, message.content_type)
            
            formatted_message = f"""
🔔 **新内容推送**

📺 **频道**: {message.channel_name}
📝 **类型**: {content_type_text}
🏷️ **标签**: {', '.join(message.tags)}
⏰ **时间**: {message.processed_at.strftime('%Y-%m-%d %H:%M:%S')}

📄 **内容**:
{message.content}

---
💡 来自 Telegram 内容机器人
            """.strip()
            
            # 发送消息
            await self.client.send_message(bot_channel, formatted_message)
            Logger.info(f"AndroidTelegramClient: 消息已发送到机器人频道 - {message.message_id}")
            return True
            
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 发送消息到机器人频道失败 - {e}")
            return False
    
    async def get_channel_info(self, channel_username: str) -> Optional[Dict[str, Any]]:
        """获取频道信息"""
        try:
            if not self.is_connected:
                if not await self.connect():
                    return None
            
            channel = await self.client.get_entity(channel_username)
            
            return {
                'id': channel.id,
                'title': getattr(channel, 'title', ''),
                'username': getattr(channel, 'username', ''),
                'participants_count': getattr(channel, 'participants_count', 0),
                'description': getattr(channel, 'about', ''),
                'verified': getattr(channel, 'verified', False),
                'restricted': getattr(channel, 'restricted', False)
            }
            
        except Exception as e:
            Logger.error(f"AndroidTelegramClient: 获取频道信息失败 - {e}")
            return None
    
    async def test_connection(self) -> Dict[str, Any]:
        """测试连接"""
        result = {
            'success': False,
            'message': '',
            'user_info': None
        }
        
        try:
            if not self.client:
                result['message'] = '客户端未初始化'
                return result
            
            if not await self.connect():
                result['message'] = '连接失败'
                return result
            
            # 获取用户信息
            me = await self.client.get_me()
            result['user_info'] = {
                'id': me.id,
                'first_name': me.first_name,
                'last_name': me.last_name,
                'username': me.username,
                'phone': me.phone
            }
            
            result['success'] = True
            result['message'] = '连接成功'
            
        except Exception as e:
            result['message'] = f'测试连接失败: {str(e)}'
        
        return result

# 模拟模式的Telegram客户端
class MockTelegramClient:
    """模拟Telegram客户端，用于测试"""
    
    def __init__(self):
        self.is_connected = False
    
    async def connect(self) -> bool:
        self.is_connected = True
        Logger.info("MockTelegramClient: 模拟连接成功")
        return True
    
    async def disconnect(self):
        self.is_connected = False
        Logger.info("MockTelegramClient: 模拟断开连接")
    
    async def get_channel_messages(self, channel_username: str, limit: int = 10, 
                                 hours_back: int = 24) -> List[Dict[str, Any]]:
        # 返回模拟数据
        import random
        messages = []
        
        for i in range(min(limit, 3)):
            messages.append({
                'message_id': random.randint(1000, 9999),
                'channel_id': random.randint(100000, 999999),
                'channel_name': f'测试频道_{channel_username}',
                'content': f'这是一条测试消息 {i+1}，包含AI和Python相关内容',
                'content_type': 'text',
                'tags': ['AI', 'Python'],
                'date': datetime.now(),
                'views': random.randint(100, 1000),
                'forwards': random.randint(10, 100)
            })
        
        Logger.info(f"MockTelegramClient: 模拟获取到 {len(messages)} 条消息")
        return messages
    
    async def process_channels(self) -> Dict[str, Any]:
        # 模拟处理结果
        import random
        return {
            'processed_count': random.randint(5, 15),
            'sent_count': random.randint(3, 10),
            'error_count': random.randint(0, 2),
            'channels_processed': random.randint(1, 3)
        }
    
    async def send_to_bot_channel(self, message) -> bool:
        Logger.info(f"MockTelegramClient: 模拟发送消息到机器人频道 - {message.message_id}")
        return True
    
    async def test_connection(self) -> Dict[str, Any]:
        return {
            'success': True,
            'message': '模拟连接成功',
            'user_info': {
                'id': 123456789,
                'first_name': '测试',
                'last_name': '用户',
                'username': 'test_user',
                'phone': '+1234567890'
            }
        }

# 全局客户端实例
if TELETHON_AVAILABLE:
    android_telegram_client = AndroidTelegramClient()
else:
    android_telegram_client = MockTelegramClient()

# 兼容性别名
class TelegramClient:
    """兼容性Telegram客户端类"""
    
    def __init__(self):
        self._client = android_telegram_client
    
    async def connect(self) -> bool:
        return await self._client.connect()
    
    async def disconnect(self):
        await self._client.disconnect()
    
    async def get_channel_messages(self, channel_username: str, limit: int = 10, 
                                 hours_back: int = 24) -> List[Dict[str, Any]]:
        return await self._client.get_channel_messages(channel_username, limit, hours_back)
    
    async def process_channels(self) -> Dict[str, Any]:
        return await self._client.process_channels()
    
    async def test_connection(self) -> Dict[str, Any]:
        return await self._client.test_connection()