#!/usr/bin/env python3
"""
配置文件模块 - Android适配版本
处理所有配置和敏感信息，适配Android文件系统
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
from kivy.logger import Logger

try:
    # Android平台相关导入
    from android.storage import primary_external_storage_path
    ANDROID_AVAILABLE = True
except ImportError:
    # 非Android平台
    ANDROID_AVAILABLE = False

class AndroidConfig:
    """Android适配的配置类"""
    
    def __init__(self):
        """初始化配置"""
        self._config_data = {}
        self._config_file_path = self._get_config_file_path()
        self._load_config()
    
    def _get_config_file_path(self) -> str:
        """获取配置文件路径"""
        try:
            if ANDROID_AVAILABLE:
                # Android内部存储路径
                app_dir = Path('/data/data/org.example.telegrambot/files')
                if not app_dir.exists():
                    # 备用路径：外部存储
                    external_path = primary_external_storage_path()
                    app_dir = Path(external_path) / 'TelegramBot'
                
                app_dir.mkdir(parents=True, exist_ok=True)
                return str(app_dir / 'config.json')
            else:
                # 非Android平台，使用当前目录
                return 'config.json'
                
        except Exception as e:
            Logger.error(f"AndroidConfig: 获取配置文件路径失败 - {e}")
            return 'config.json'
    
    def _get_default_config(self) -> Dict[str, Any]:
        """获取默认配置"""
        return {
            # Telegram配置
            'BOT_TOKEN': '',
            'API_ID': 0,
            'API_HASH': '',
            'BOT_CHANNEL': '',
            
            # 邮件配置
            'SMTP_SERVER': 'smtp.gmail.com',
            'SMTP_PORT': 587,
            'EMAIL_USERNAME': '',
            'EMAIL_PASSWORD': '',
            'EMAIL_TO': '',
            
            # 监控配置
            'TARGET_CHANNELS': [],
            'INTEREST_TAGS': [],
            'CHECK_INTERVAL_HOURS': 24,
            
            # 定时任务配置
            'ENABLE_SCHEDULE': False,
            'SCHEDULE_TIMES': [],  # [{'hour': 9, 'minute': 0}]
            'auto_retry': True,
            'retry_count': 3,
            'retry_interval_minutes': 30,
            'check_network': True,
            
            # 高级配置
            'MAX_DAILY_MESSAGES': 100,
            'RATE_LIMIT_DELAY': 1.0,
            'LOG_LEVEL': 'INFO',
            
            # 标签匹配配置
            'TAG_MATCHING': {
                'exact_match': True,
                'case_sensitive': False,
                'partial_match': True,
                'include_synonyms': True,
                'synonyms': {
                    'AI': ['人工智能', '机器学习', '深度学习'],
                    'Python': ['python', 'py', 'Python编程'],
                    '投资': ['理财', '股票', '基金', '投资学']
                }
            },
            
            # 内容类型映射
            'CONTENT_TYPE_MAPPING': {
                'text': '文本',
                'photo': '图片',
                'video': '视频',
                'audio': '音频',
                'document': '文档',
                'voice': '语音',
                'video_note': '视频笔记',
                'animation': '动画',
                'sticker': '贴纸'
            }
        }
    
    def _load_config(self) -> bool:
        """加载配置文件"""
        try:
            if os.path.exists(self._config_file_path):
                with open(self._config_file_path, 'r', encoding='utf-8') as f:
                    self._config_data = json.load(f)
                Logger.info(f"AndroidConfig: 配置文件加载成功 - {self._config_file_path}")
            else:
                # 使用默认配置
                self._config_data = self._get_default_config()
                self._save_config()
                Logger.info("AndroidConfig: 使用默认配置并保存")
            
            return True
            
        except Exception as e:
            Logger.error(f"AndroidConfig: 加载配置文件失败 - {e}")
            self._config_data = self._get_default_config()
            return False
    
    def _save_config(self) -> bool:
        """保存配置文件"""
        try:
            # 确保目录存在
            config_dir = os.path.dirname(self._config_file_path)
            if config_dir:
                os.makedirs(config_dir, exist_ok=True)
            
            with open(self._config_file_path, 'w', encoding='utf-8') as f:
                json.dump(self._config_data, f, ensure_ascii=False, indent=2)
            
            Logger.info(f"AndroidConfig: 配置文件保存成功 - {self._config_file_path}")
            return True
            
        except Exception as e:
            Logger.error(f"AndroidConfig: 保存配置文件失败 - {e}")
            return False
    
    def load(self) -> bool:
        """加载配置（公共接口）"""
        return self._load_config()
    
    def save(self) -> bool:
        """保存配置（公共接口）"""
        return self._save_config()
    
    def create_default_config(self) -> bool:
        """创建默认配置"""
        try:
            self.config = self._get_default_config()
            return self.save()
        except Exception as e:
            Logger.error(f"AndroidConfig: 创建默认配置失败 - {e}")
            return False
    
    def get(self, key: str, default: Any = None) -> Any:
        """获取配置值"""
        return self._config_data.get(key, default)
    
    def set(self, key: str, value: Any) -> bool:
        """设置配置值"""
        try:
            self._config_data[key] = value
            return self._save_config()
        except Exception as e:
            Logger.error(f"AndroidConfig: 设置配置失败 {key} - {e}")
            return False
    
    def update(self, config_dict: Dict[str, Any]) -> bool:
        """批量更新配置"""
        try:
            self._config_data.update(config_dict)
            return self._save_config()
        except Exception as e:
            Logger.error(f"AndroidConfig: 批量更新配置失败 - {e}")
            return False
    
    def get_all(self) -> Dict[str, Any]:
        """获取所有配置"""
        return self._config_data.copy()
    
    def reset_to_default(self) -> bool:
        """重置为默认配置"""
        try:
            self._config_data = self._get_default_config()
            return self._save_config()
        except Exception as e:
            Logger.error(f"AndroidConfig: 重置配置失败 - {e}")
            return False
    
    def validate(self) -> Dict[str, bool]:
        """验证配置"""
        validation_result = {
            'telegram_api': False,
            'email_config': False,
            'channels': False,
            'tags': False
        }
        
        try:
            # 验证Telegram API配置
            bot_token = self.get('BOT_TOKEN', '')
            api_id = self.get('API_ID', 0)
            api_hash = self.get('API_HASH', '')
            
            if bot_token and api_id and api_hash:
                validation_result['telegram_api'] = True
            
            # 验证邮件配置
            email_username = self.get('EMAIL_USERNAME', '')
            email_password = self.get('EMAIL_PASSWORD', '')
            email_to = self.get('EMAIL_TO', '')
            
            if email_username and email_password and email_to:
                validation_result['email_config'] = True
            
            # 验证频道配置
            channels = self.get('TARGET_CHANNELS', [])
            if channels:
                validation_result['channels'] = True
            
            # 验证标签配置
            tags = self.get('INTEREST_TAGS', [])
            if tags:
                validation_result['tags'] = True
            
        except Exception as e:
            Logger.error(f"AndroidConfig: 验证配置失败 - {e}")
        
        return validation_result
    
    def get_telegram_config(self) -> Dict[str, Any]:
        """获取Telegram配置"""
        return {
            'BOT_TOKEN': self.get('BOT_TOKEN', ''),
            'API_ID': self.get('API_ID', 0),
            'API_HASH': self.get('API_HASH', ''),
            'BOT_CHANNEL': self.get('BOT_CHANNEL', '')
        }
    
    def get_email_config(self) -> Dict[str, Any]:
        """获取邮件配置"""
        return {
            'SMTP_SERVER': self.get('SMTP_SERVER', 'smtp.gmail.com'),
            'SMTP_PORT': self.get('SMTP_PORT', 587),
            'EMAIL_USERNAME': self.get('EMAIL_USERNAME', ''),
            'EMAIL_PASSWORD': self.get('EMAIL_PASSWORD', ''),
            'EMAIL_TO': self.get('EMAIL_TO', '')
        }
    
    def get_schedule_config(self) -> Dict[str, Any]:
        """获取定时任务配置"""
        return {
            'ENABLE_SCHEDULE': self.get('ENABLE_SCHEDULE', False),
            'CHECK_INTERVAL_HOURS': self.get('CHECK_INTERVAL_HOURS', 24),
            'SCHEDULE_TIMES': self.get('SCHEDULE_TIMES', []),
            'auto_retry': self.get('auto_retry', True),
            'retry_count': self.get('retry_count', 3),
            'retry_interval_minutes': self.get('retry_interval_minutes', 30),
            'check_network': self.get('check_network', True)
        }
    
    def get_channels(self) -> List[str]:
        """获取目标频道列表"""
        return self.get('TARGET_CHANNELS', [])
    
    def get_tags(self) -> List[str]:
        """获取兴趣标签列表"""
        return self.get('INTEREST_TAGS', [])
    
    def add_channel(self, channel: str) -> bool:
        """添加频道"""
        try:
            channels = self.get_channels()
            if channel not in channels:
                channels.append(channel)
                return self.set('TARGET_CHANNELS', channels)
            return True
        except Exception as e:
            Logger.error(f"AndroidConfig: 添加频道失败 - {e}")
            return False
    
    def remove_channel(self, channel: str) -> bool:
        """移除频道"""
        try:
            channels = self.get_channels()
            if channel in channels:
                channels.remove(channel)
                return self.set('TARGET_CHANNELS', channels)
            return True
        except Exception as e:
            Logger.error(f"AndroidConfig: 移除频道失败 - {e}")
            return False
    
    def add_tag(self, tag: str) -> bool:
        """添加标签"""
        try:
            tags = self.get_tags()
            if tag not in tags:
                tags.append(tag)
                return self.set('INTEREST_TAGS', tags)
            return True
        except Exception as e:
            Logger.error(f"AndroidConfig: 添加标签失败 - {e}")
            return False
    
    def remove_tag(self, tag: str) -> bool:
        """移除标签"""
        try:
            tags = self.get_tags()
            if tag in tags:
                tags.remove(tag)
                return self.set('INTEREST_TAGS', tags)
            return True
        except Exception as e:
            Logger.error(f"AndroidConfig: 移除标签失败 - {e}")
            return False
    
    def get_database_path(self) -> str:
        """获取数据库文件路径"""
        try:
            if ANDROID_AVAILABLE:
                # Android内部存储路径
                app_dir = Path('/data/data/org.example.telegrambot/files')
                if not app_dir.exists():
                    # 备用路径：外部存储
                    external_path = primary_external_storage_path()
                    app_dir = Path(external_path) / 'TelegramBot'
                
                app_dir.mkdir(parents=True, exist_ok=True)
                return str(app_dir / 'telegram_content_bot.db')
            else:
                # 非Android平台
                return 'telegram_content_bot.db'
                
        except Exception as e:
            Logger.error(f"AndroidConfig: 获取数据库路径失败 - {e}")
            return 'telegram_content_bot.db'
    
    def get_session_path(self) -> str:
        """获取Telegram会话文件路径"""
        try:
            if ANDROID_AVAILABLE:
                # Android内部存储路径
                app_dir = Path('/data/data/org.example.telegrambot/files')
                if not app_dir.exists():
                    # 备用路径：外部存储
                    external_path = primary_external_storage_path()
                    app_dir = Path(external_path) / 'TelegramBot'
                
                app_dir.mkdir(parents=True, exist_ok=True)
                return str(app_dir / 'telegram_content_session')
            else:
                # 非Android平台
                return 'telegram_content_session'
                
        except Exception as e:
            Logger.error(f"AndroidConfig: 获取会话路径失败 - {e}")
            return 'telegram_content_session'
    
    def get_log_path(self) -> str:
        """获取日志文件路径"""
        try:
            if ANDROID_AVAILABLE:
                # Android内部存储路径
                app_dir = Path('/data/data/org.example.telegrambot/files')
                if not app_dir.exists():
                    # 备用路径：外部存储
                    external_path = primary_external_storage_path()
                    app_dir = Path(external_path) / 'TelegramBot'
                
                app_dir.mkdir(parents=True, exist_ok=True)
                return str(app_dir / 'bot.log')
            else:
                # 非Android平台
                return 'bot.log'
                
        except Exception as e:
            Logger.error(f"AndroidConfig: 获取日志路径失败 - {e}")
            return 'bot.log'
    
    def export_config(self) -> str:
        """导出配置为JSON字符串"""
        try:
            return json.dumps(self._config_data, ensure_ascii=False, indent=2)
        except Exception as e:
            Logger.error(f"AndroidConfig: 导出配置失败 - {e}")
            return '{}'
    
    def import_config(self, config_json: str) -> bool:
        """从JSON字符串导入配置"""
        try:
            config_data = json.loads(config_json)
            self._config_data = config_data
            return self._save_config()
        except Exception as e:
            Logger.error(f"AndroidConfig: 导入配置失败 - {e}")
            return False
    
    def is_first_run(self) -> bool:
        """检查是否首次运行"""
        return not os.path.exists(self._config_file_path)
    
    def get_config_summary(self) -> Dict[str, Any]:
        """获取配置摘要"""
        validation = self.validate()
        
        return {
            'telegram_configured': validation['telegram_api'],
            'email_configured': validation['email_config'],
            'channels_count': len(self.get_channels()),
            'tags_count': len(self.get_tags()),
            'schedule_enabled': self.get('ENABLE_SCHEDULE', False),
            'config_file_path': self._config_file_path,
            'is_first_run': self.is_first_run()
        }

# 全局配置实例
android_config = AndroidConfig()

# 兼容性别名，保持与原项目的接口一致
class Config:
    """兼容性配置类"""
    
    @classmethod
    def validate(cls) -> bool:
        """验证必要配置"""
        validation = android_config.validate()
        return all(validation.values())
    
    @classmethod
    def get_channels(cls) -> List[str]:
        """获取频道列表"""
        return android_config.get_channels()
    
    @classmethod
    def get_tags(cls) -> List[str]:
        """获取标签列表"""
        return android_config.get_tags()
    
    @classmethod
    def get_database_path(cls) -> str:
        """获取数据库路径"""
        return android_config.get_database_path()
    
    # 动态属性访问
    def __getattr__(self, name):
        return android_config.get(name)

# 标签匹配配置
TAG_MATCHING_CONFIG = {
    'exact_match': True,
    'case_sensitive': False,
    'partial_match': True,
    'include_synonyms': True,
    'synonyms': {
        'AI': ['人工智能', '机器学习', '深度学习'],
        'Python': ['python', 'py', 'Python编程'],
        '投资': ['理财', '股票', '基金', '投资学']
    }
}

# 内容类型映射
CONTENT_TYPE_MAPPING = {
    'text': '文本',
    'photo': '图片',
    'video': '视频',
    'audio': '音频',
    'document': '文档',
    'voice': '语音',
    'video_note': '视频笔记',
    'animation': '动画',
    'sticker': '贴纸'
}

# 日志格式
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'