#!/usr/bin/env python3
"""
配置管理模块
管理应用的所有配置信息，包括Telegram API、邮箱、频道等设置
"""

import os
import json
from typing import Dict, Any, List
from kivy.logger import Logger

class ConfigManager:
    """配置管理器"""
    
    def __init__(self, config_dir: str = None):
        """初始化配置管理器"""
        if config_dir is None:
            # Android内部存储路径
            from android.storage import app_storage_path
            config_dir = app_storage_path()
        
        self.config_dir = config_dir
        self.config_file = os.path.join(config_dir, 'config.json')
        self.default_config = self._get_default_config()
        self.config = {}
        
        # 确保配置目录存在
        os.makedirs(config_dir, exist_ok=True)
        
        # 加载配置
        self.load_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """获取默认配置"""
        return {
            # Telegram配置
            'BOT_TOKEN': '',
            'API_ID': 0,
            'API_HASH': '',
            'BOT_CHANNEL': '',
            'TARGET_CHANNELS': [],
            
            # 邮箱配置
            'SMTP_SERVER': 'smtp.qq.com',
            'SMTP_PORT': 587,
            'EMAIL_USERNAME': '',
            'EMAIL_PASSWORD': '',
            'EMAIL_TO': '',
            
            # 内容过滤配置
            'INTEREST_TAGS': [],
            'EXCLUDE_KEYWORDS': [],
            'MIN_MESSAGE_LENGTH': 10,
            'MAX_MESSAGE_LENGTH': 1000,
            
            # 定时任务配置
            'CHECK_INTERVAL_HOURS': 24,
            'MAX_DAILY_MESSAGES': 100,
            'ENABLE_SCHEDULE': False,
            'SCHEDULE_TIMES': [],
            
            # 高级配置
            'ENABLE_SYNONYM_MATCHING': False,
            'ENABLE_AI_FILTERING': False,
            'LOG_LEVEL': 'INFO',
            'MAX_LOG_FILES': 10,
            'DATABASE_PATH': 'telegram_content.db',
            
            # 应用配置
            'FIRST_RUN': True,
            'APP_VERSION': '1.0.0',
            'LAST_UPDATE_CHECK': '',
            'THEME': 'light',
            'LANGUAGE': 'zh-CN'
        }
    
    def load_config(self) -> bool:
        """加载配置文件"""
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    loaded_config = json.load(f)
                
                # 合并默认配置和加载的配置
                self.config = self.default_config.copy()
                self.config.update(loaded_config)
                
                Logger.info(f"ConfigManager: 配置加载成功 - {self.config_file}")
                return True
            else:
                # 使用默认配置
                self.config = self.default_config.copy()
                self.save_config()
                Logger.info("ConfigManager: 使用默认配置")
                return True
                
        except Exception as e:
            Logger.error(f"ConfigManager: 加载配置失败 - {e}")
            self.config = self.default_config.copy()
            return False
    
    def save_config(self, config_data: Dict[str, Any] = None) -> bool:
        """保存配置文件"""
        try:
            if config_data:
                # 更新配置
                self.config.update(config_data)
            
            # 保存到文件
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
            
            Logger.info(f"ConfigManager: 配置保存成功 - {self.config_file}")
            return True
            
        except Exception as e:
            Logger.error(f"ConfigManager: 保存配置失败 - {e}")
            return False
    
    def get_config(self, key: str, default: Any = None) -> Any:
        """获取配置项"""
        return self.config.get(key, default)
    
    def set_config(self, key: str, value: Any) -> bool:
        """设置配置项"""
        try:
            self.config[key] = value
            return self.save_config()
        except Exception as e:
            Logger.error(f"ConfigManager: 设置配置失败 - {key}: {e}")
            return False
    
    def get_all_config(self) -> Dict[str, Any]:
        """获取所有配置"""
        return self.config.copy()
    
    def reset_config(self) -> bool:
        """重置配置为默认值"""
        try:
            self.config = self.default_config.copy()
            return self.save_config()
        except Exception as e:
            Logger.error(f"ConfigManager: 重置配置失败 - {e}")
            return False
    
    def validate_config(self) -> List[str]:
        """验证配置的有效性"""
        errors = []
        
        try:
            # 验证Telegram配置
            if not self.config.get('BOT_TOKEN'):
                errors.append('Bot Token未设置')
            
            if not self.config.get('API_ID') or self.config.get('API_ID') == 0:
                errors.append('API ID未设置')
            
            if not self.config.get('API_HASH'):
                errors.append('API Hash未设置')
            
            if not self.config.get('BOT_CHANNEL'):
                errors.append('机器人频道未设置')
            
            # 验证邮箱配置
            if not self.config.get('EMAIL_USERNAME'):
                errors.append('邮箱地址未设置')
            
            if not self.config.get('EMAIL_PASSWORD'):
                errors.append('邮箱密码未设置')
            
            # 验证端口号
            smtp_port = self.config.get('SMTP_PORT', 587)
            if not isinstance(smtp_port, int) or smtp_port <= 0 or smtp_port > 65535:
                errors.append('SMTP端口号无效')
            
            # 验证间隔时间
            interval = self.config.get('CHECK_INTERVAL_HOURS', 24)
            if not isinstance(interval, int) or interval <= 0:
                errors.append('检查间隔时间无效')
            
            # 验证最大消息数
            max_messages = self.config.get('MAX_DAILY_MESSAGES', 100)
            if not isinstance(max_messages, int) or max_messages <= 0:
                errors.append('每日最大消息数无效')
            
        except Exception as e:
            errors.append(f'配置验证出错: {e}')
        
        return errors
    
    def is_first_run(self) -> bool:
        """检查是否首次运行"""
        return self.config.get('FIRST_RUN', True)
    
    def set_first_run_complete(self) -> bool:
        """标记首次运行完成"""
        return self.set_config('FIRST_RUN', False)
    
    def get_telegram_config(self) -> Dict[str, Any]:
        """获取Telegram相关配置"""
        return {
            'BOT_TOKEN': self.config.get('BOT_TOKEN', ''),
            'API_ID': self.config.get('API_ID', 0),
            'API_HASH': self.config.get('API_HASH', ''),
            'BOT_CHANNEL': self.config.get('BOT_CHANNEL', ''),
            'TARGET_CHANNELS': self.config.get('TARGET_CHANNELS', [])
        }
    
    def get_email_config(self) -> Dict[str, Any]:
        """获取邮箱相关配置"""
        return {
            'SMTP_SERVER': self.config.get('SMTP_SERVER', 'smtp.qq.com'),
            'SMTP_PORT': self.config.get('SMTP_PORT', 587),
            'EMAIL_USERNAME': self.config.get('EMAIL_USERNAME', ''),
            'EMAIL_PASSWORD': self.config.get('EMAIL_PASSWORD', ''),
            'EMAIL_TO': self.config.get('EMAIL_TO', '')
        }
    
    def get_filter_config(self) -> Dict[str, Any]:
        """获取内容过滤相关配置"""
        return {
            'INTEREST_TAGS': self.config.get('INTEREST_TAGS', []),
            'EXCLUDE_KEYWORDS': self.config.get('EXCLUDE_KEYWORDS', []),
            'MIN_MESSAGE_LENGTH': self.config.get('MIN_MESSAGE_LENGTH', 10),
            'MAX_MESSAGE_LENGTH': self.config.get('MAX_MESSAGE_LENGTH', 1000),
            'ENABLE_SYNONYM_MATCHING': self.config.get('ENABLE_SYNONYM_MATCHING', False),
            'ENABLE_AI_FILTERING': self.config.get('ENABLE_AI_FILTERING', False)
        }
    
    def get_schedule_config(self) -> Dict[str, Any]:
        """获取定时任务相关配置"""
        return {
            'CHECK_INTERVAL_HOURS': self.config.get('CHECK_INTERVAL_HOURS', 24),
            'MAX_DAILY_MESSAGES': self.config.get('MAX_DAILY_MESSAGES', 100),
            'ENABLE_SCHEDULE': self.config.get('ENABLE_SCHEDULE', False),
            'SCHEDULE_TIMES': self.config.get('SCHEDULE_TIMES', [])
        }
    
    def add_target_channel(self, channel: str) -> bool:
        """添加目标频道"""
        try:
            channels = self.config.get('TARGET_CHANNELS', [])
            if channel not in channels:
                channels.append(channel)
                return self.set_config('TARGET_CHANNELS', channels)
            return True
        except Exception as e:
            Logger.error(f"ConfigManager: 添加频道失败 - {e}")
            return False
    
    def remove_target_channel(self, channel: str) -> bool:
        """删除目标频道"""
        try:
            channels = self.config.get('TARGET_CHANNELS', [])
            if channel in channels:
                channels.remove(channel)
                return self.set_config('TARGET_CHANNELS', channels)
            return True
        except Exception as e:
            Logger.error(f"ConfigManager: 删除频道失败 - {e}")
            return False
    
    def add_interest_tag(self, tag: str) -> bool:
        """添加兴趣标签"""
        try:
            tags = self.config.get('INTEREST_TAGS', [])
            if tag not in tags:
                tags.append(tag)
                return self.set_config('INTEREST_TAGS', tags)
            return True
        except Exception as e:
            Logger.error(f"ConfigManager: 添加标签失败 - {e}")
            return False
    
    def remove_interest_tag(self, tag: str) -> bool:
        """删除兴趣标签"""
        try:
            tags = self.config.get('INTEREST_TAGS', [])
            if tag in tags:
                tags.remove(tag)
                return self.set_config('INTEREST_TAGS', tags)
            return True
        except Exception as e:
            Logger.error(f"ConfigManager: 删除标签失败 - {e}")
            return False
    
    def add_schedule_time(self, hour: int, minute: int) -> bool:
        """添加定时执行时间"""
        try:
            times = self.config.get('SCHEDULE_TIMES', [])
            time_dict = {'hour': hour, 'minute': minute}
            
            # 检查是否已存在
            exists = any(t['hour'] == hour and t['minute'] == minute for t in times)
            if not exists:
                times.append(time_dict)
                return self.set_config('SCHEDULE_TIMES', times)
            return True
        except Exception as e:
            Logger.error(f"ConfigManager: 添加定时时间失败 - {e}")
            return False
    
    def remove_schedule_time(self, hour: int, minute: int) -> bool:
        """删除定时执行时间"""
        try:
            times = self.config.get('SCHEDULE_TIMES', [])
            times = [t for t in times if not (t['hour'] == hour and t['minute'] == minute)]
            return self.set_config('SCHEDULE_TIMES', times)
        except Exception as e:
            Logger.error(f"ConfigManager: 删除定时时间失败 - {e}")
            return False
    
    def export_config(self, export_path: str) -> bool:
        """导出配置到指定路径"""
        try:
            with open(export_path, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
            
            Logger.info(f"ConfigManager: 配置导出成功 - {export_path}")
            return True
            
        except Exception as e:
            Logger.error(f"ConfigManager: 导出配置失败 - {e}")
            return False
    
    def import_config(self, import_path: str) -> bool:
        """从指定路径导入配置"""
        try:
            if not os.path.exists(import_path):
                Logger.error(f"ConfigManager: 配置文件不存在 - {import_path}")
                return False
            
            with open(import_path, 'r', encoding='utf-8') as f:
                imported_config = json.load(f)
            
            # 验证导入的配置
            if not isinstance(imported_config, dict):
                Logger.error("ConfigManager: 无效的配置文件格式")
                return False
            
            # 合并配置
            self.config.update(imported_config)
            
            # 保存配置
            if self.save_config():
                Logger.info(f"ConfigManager: 配置导入成功 - {import_path}")
                return True
            else:
                return False
                
        except Exception as e:
            Logger.error(f"ConfigManager: 导入配置失败 - {e}")
            return False
    
    def get_config_summary(self) -> Dict[str, str]:
        """获取配置摘要信息"""
        try:
            telegram_configured = bool(self.config.get('BOT_TOKEN') and 
                                     self.config.get('API_ID') and 
                                     self.config.get('API_HASH'))
            
            email_configured = bool(self.config.get('EMAIL_USERNAME') and 
                                  self.config.get('EMAIL_PASSWORD'))
            
            channels_count = len(self.config.get('TARGET_CHANNELS', []))
            tags_count = len(self.config.get('INTEREST_TAGS', []))
            
            return {
                'telegram_status': '已配置' if telegram_configured else '未配置',
                'email_status': '已配置' if email_configured else '未配置',
                'channels_count': f'{channels_count}个频道',
                'tags_count': f'{tags_count}个标签',
                'schedule_status': '已启用' if self.config.get('ENABLE_SCHEDULE') else '未启用'
            }
            
        except Exception as e:
            Logger.error(f"ConfigManager: 获取配置摘要失败 - {e}")
            return {
                'telegram_status': '未知',
                'email_status': '未知',
                'channels_count': '0个频道',
                'tags_count': '0个标签',
                'schedule_status': '未知'
            }