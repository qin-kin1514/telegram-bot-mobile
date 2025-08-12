#!/usr/bin/env python3
"""
数据库管理模块 - Android适配版本
处理SQLite数据库操作，适配Android文件系统
"""

import sqlite3
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path
from kivy.logger import Logger

try:
    # Android平台相关导入
    from android.storage import primary_external_storage_path
    ANDROID_AVAILABLE = True
except ImportError:
    # 非Android平台
    ANDROID_AVAILABLE = False

@dataclass
class ProcessedMessage:
    """处理过的消息数据类"""
    message_id: int
    channel_id: int
    channel_name: str
    content: str
    content_type: str
    tags: List[str]
    processed_at: datetime
    sent_to_bot: bool = False
    sent_at: Optional[datetime] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """转换为字典"""
        data = asdict(self)
        data['tags'] = json.dumps(self.tags, ensure_ascii=False)
        data['processed_at'] = self.processed_at.isoformat()
        if self.sent_at:
            data['sent_at'] = self.sent_at.isoformat()
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ProcessedMessage':
        """从字典创建实例"""
        data['tags'] = json.loads(data.get('tags', '[]'))
        data['processed_at'] = datetime.fromisoformat(data['processed_at'])
        if data.get('sent_at'):
            data['sent_at'] = datetime.fromisoformat(data['sent_at'])
        return cls(**data)

class AndroidDatabaseManager:
    """Android适配的数据库管理器"""
    
    def __init__(self, db_path: Optional[str] = None):
        """初始化数据库管理器"""
        self.db_path = db_path or self._get_database_path()
        self._ensure_database_directory()
        self._init_database()
    
    def _get_database_path(self) -> str:
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
            Logger.error(f"AndroidDatabaseManager: 获取数据库路径失败 - {e}")
            return 'telegram_content_bot.db'
    
    def _ensure_database_directory(self):
        """确保数据库目录存在"""
        try:
            db_dir = Path(self.db_path).parent
            db_dir.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 创建数据库目录失败 - {e}")
    
    def _init_database(self):
        """初始化数据库表"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 创建处理消息表
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS processed_messages (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        message_id INTEGER NOT NULL,
                        channel_id INTEGER NOT NULL,
                        channel_name TEXT NOT NULL,
                        content TEXT NOT NULL,
                        content_type TEXT NOT NULL,
                        tags TEXT NOT NULL,
                        processed_at TEXT NOT NULL,
                        sent_to_bot BOOLEAN DEFAULT FALSE,
                        sent_at TEXT,
                        UNIQUE(message_id, channel_id)
                    )
                ''')
                
                # 创建用户标签表
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS user_tags (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        tag_name TEXT UNIQUE NOT NULL,
                        created_at TEXT NOT NULL,
                        usage_count INTEGER DEFAULT 0
                    )
                ''')
                
                # 创建目标频道表
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS target_channels (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        channel_id INTEGER UNIQUE NOT NULL,
                        channel_name TEXT NOT NULL,
                        channel_username TEXT,
                        added_at TEXT NOT NULL,
                        is_active BOOLEAN DEFAULT TRUE,
                        last_checked TEXT
                    )
                ''')
                
                # 创建配置表
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS config_values (
                        key TEXT PRIMARY KEY,
                        value TEXT NOT NULL,
                        updated_at TEXT NOT NULL
                    )
                ''')
                
                # 创建日志表
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS app_logs (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        level TEXT NOT NULL,
                        message TEXT NOT NULL,
                        module TEXT,
                        created_at TEXT NOT NULL
                    )
                ''')
                
                # 创建统计表
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS daily_stats (
                        date TEXT PRIMARY KEY,
                        processed_count INTEGER DEFAULT 0,
                        sent_count INTEGER DEFAULT 0,
                        error_count INTEGER DEFAULT 0,
                        channels_checked INTEGER DEFAULT 0,
                        last_updated TEXT NOT NULL
                    )
                ''')
                
                conn.commit()
                Logger.info(f"AndroidDatabaseManager: 数据库初始化成功 - {self.db_path}")
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 数据库初始化失败 - {e}")
            raise
    
    def add_processed_message(self, message: ProcessedMessage) -> bool:
        """添加处理过的消息"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                message_data = message.to_dict()
                cursor.execute('''
                    INSERT OR REPLACE INTO processed_messages 
                    (message_id, channel_id, channel_name, content, content_type, 
                     tags, processed_at, sent_to_bot, sent_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    message_data['message_id'],
                    message_data['channel_id'],
                    message_data['channel_name'],
                    message_data['content'],
                    message_data['content_type'],
                    message_data['tags'],
                    message_data['processed_at'],
                    message_data['sent_to_bot'],
                    message_data.get('sent_at')
                ))
                
                conn.commit()
                Logger.debug(f"AndroidDatabaseManager: 消息添加成功 - {message.message_id}")
                return True
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 添加消息失败 - {e}")
            return False
    
    def is_message_processed(self, message_id: int, channel_id: int) -> bool:
        """检查消息是否已处理"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    'SELECT 1 FROM processed_messages WHERE message_id = ? AND channel_id = ?',
                    (message_id, channel_id)
                )
                return cursor.fetchone() is not None
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 检查消息状态失败 - {e}")
            return False
    
    def mark_message_sent(self, message_id: int, channel_id: int) -> bool:
        """标记消息已发送"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE processed_messages 
                    SET sent_to_bot = TRUE, sent_at = ?
                    WHERE message_id = ? AND channel_id = ?
                ''', (datetime.now().isoformat(), message_id, channel_id))
                
                conn.commit()
                return cursor.rowcount > 0
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 标记消息发送失败 - {e}")
            return False
    
    def get_daily_stats(self, date: Optional[str] = None) -> Dict[str, int]:
        """获取每日统计"""
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 从处理消息表获取统计
                cursor.execute('''
                    SELECT 
                        COUNT(*) as processed_count,
                        SUM(CASE WHEN sent_to_bot = 1 THEN 1 ELSE 0 END) as sent_count
                    FROM processed_messages 
                    WHERE DATE(processed_at) = ?
                ''', (date,))
                
                result = cursor.fetchone()
                processed_count = result[0] if result else 0
                sent_count = result[1] if result else 0
                
                # 从统计表获取错误数
                cursor.execute(
                    'SELECT error_count FROM daily_stats WHERE date = ?',
                    (date,)
                )
                error_result = cursor.fetchone()
                error_count = error_result[0] if error_result else 0
                
                return {
                    'processed_count': processed_count,
                    'sent_count': sent_count,
                    'error_count': error_count,
                    'success_rate': round((sent_count / processed_count * 100) if processed_count > 0 else 0, 1)
                }
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 获取每日统计失败 - {e}")
            return {'processed_count': 0, 'sent_count': 0, 'error_count': 0, 'success_rate': 0}
    
    def update_daily_stats(self, date: str, **kwargs) -> bool:
        """更新每日统计"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 获取当前统计
                cursor.execute('SELECT * FROM daily_stats WHERE date = ?', (date,))
                existing = cursor.fetchone()
                
                if existing:
                    # 更新现有记录
                    update_fields = []
                    update_values = []
                    
                    for key, value in kwargs.items():
                        if key in ['processed_count', 'sent_count', 'error_count', 'channels_checked']:
                            update_fields.append(f'{key} = ?')
                            update_values.append(value)
                    
                    if update_fields:
                        update_values.extend([datetime.now().isoformat(), date])
                        cursor.execute(f'''
                            UPDATE daily_stats 
                            SET {', '.join(update_fields)}, last_updated = ?
                            WHERE date = ?
                        ''', update_values)
                else:
                    # 插入新记录
                    cursor.execute('''
                        INSERT INTO daily_stats 
                        (date, processed_count, sent_count, error_count, channels_checked, last_updated)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                        date,
                        kwargs.get('processed_count', 0),
                        kwargs.get('sent_count', 0),
                        kwargs.get('error_count', 0),
                        kwargs.get('channels_checked', 0),
                        datetime.now().isoformat()
                    ))
                
                conn.commit()
                return True
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 更新每日统计失败 - {e}")
            return False
    
    def add_user_tag(self, tag_name: str) -> bool:
        """添加用户标签"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR IGNORE INTO user_tags (tag_name, created_at)
                    VALUES (?, ?)
                ''', (tag_name, datetime.now().isoformat()))
                
                conn.commit()
                return True
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 添加标签失败 - {e}")
            return False
    
    def remove_user_tag(self, tag_name: str) -> bool:
        """移除用户标签"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM user_tags WHERE tag_name = ?', (tag_name,))
                
                conn.commit()
                return cursor.rowcount > 0
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 移除标签失败 - {e}")
            return False
    
    def get_user_tags(self) -> List[str]:
        """获取用户标签列表"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT tag_name FROM user_tags ORDER BY usage_count DESC, tag_name')
                
                return [row[0] for row in cursor.fetchall()]
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 获取标签列表失败 - {e}")
            return []
    
    def add_target_channel(self, channel_id: int, channel_name: str, channel_username: str = None) -> bool:
        """添加目标频道"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO target_channels 
                    (channel_id, channel_name, channel_username, added_at, is_active)
                    VALUES (?, ?, ?, ?, TRUE)
                ''', (channel_id, channel_name, channel_username, datetime.now().isoformat()))
                
                conn.commit()
                return True
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 添加频道失败 - {e}")
            return False
    
    def remove_target_channel(self, channel_id: int) -> bool:
        """移除目标频道"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM target_channels WHERE channel_id = ?', (channel_id,))
                
                conn.commit()
                return cursor.rowcount > 0
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 移除频道失败 - {e}")
            return False
    
    def get_target_channels(self) -> List[Dict[str, Any]]:
        """获取目标频道列表"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT channel_id, channel_name, channel_username, added_at, is_active, last_checked
                    FROM target_channels 
                    WHERE is_active = TRUE
                    ORDER BY channel_name
                ''')
                
                columns = ['channel_id', 'channel_name', 'channel_username', 'added_at', 'is_active', 'last_checked']
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 获取频道列表失败 - {e}")
            return []
    
    def update_channel_check_time(self, channel_id: int) -> bool:
        """更新频道检查时间"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    UPDATE target_channels 
                    SET last_checked = ?
                    WHERE channel_id = ?
                ''', (datetime.now().isoformat(), channel_id))
                
                conn.commit()
                return cursor.rowcount > 0
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 更新频道检查时间失败 - {e}")
            return False
    
    def set_config_value(self, key: str, value: str) -> bool:
        """设置配置值"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO config_values (key, value, updated_at)
                    VALUES (?, ?, ?)
                ''', (key, value, datetime.now().isoformat()))
                
                conn.commit()
                return True
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 设置配置值失败 - {e}")
            return False
    
    def get_config_value(self, key: str, default: str = None) -> Optional[str]:
        """获取配置值"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT value FROM config_values WHERE key = ?', (key,))
                
                result = cursor.fetchone()
                return result[0] if result else default
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 获取配置值失败 - {e}")
            return default
    
    def add_log(self, level: str, message: str, module: str = None) -> bool:
        """添加日志记录"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO app_logs (level, message, module, created_at)
                    VALUES (?, ?, ?, ?)
                ''', (level, message, module, datetime.now().isoformat()))
                
                conn.commit()
                return True
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 添加日志失败 - {e}")
            return False
    
    def get_logs(self, limit: int = 100, level: str = None) -> List[Dict[str, Any]]:
        """获取日志记录"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                if level:
                    cursor.execute('''
                        SELECT level, message, module, created_at
                        FROM app_logs 
                        WHERE level = ?
                        ORDER BY created_at DESC 
                        LIMIT ?
                    ''', (level, limit))
                else:
                    cursor.execute('''
                        SELECT level, message, module, created_at
                        FROM app_logs 
                        ORDER BY created_at DESC 
                        LIMIT ?
                    ''', (limit,))
                
                columns = ['level', 'message', 'module', 'created_at']
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 获取日志失败 - {e}")
            return []
    
    def clear_old_data(self, days: int = 30) -> bool:
        """清理旧数据"""
        try:
            cutoff_date = (datetime.now() - timedelta(days=days)).isoformat()
            
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 清理旧消息
                cursor.execute(
                    'DELETE FROM processed_messages WHERE processed_at < ?',
                    (cutoff_date,)
                )
                
                # 清理旧日志
                cursor.execute(
                    'DELETE FROM app_logs WHERE created_at < ?',
                    (cutoff_date,)
                )
                
                # 清理旧统计（保留最近90天）
                stats_cutoff = (datetime.now() - timedelta(days=90)).strftime('%Y-%m-%d')
                cursor.execute(
                    'DELETE FROM daily_stats WHERE date < ?',
                    (stats_cutoff,)
                )
                
                conn.commit()
                Logger.info(f"AndroidDatabaseManager: 清理旧数据完成，删除{days}天前的数据")
                return True
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 清理旧数据失败 - {e}")
            return False
    
    def get_database_info(self) -> Dict[str, Any]:
        """获取数据库信息"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # 获取各表记录数
                tables_info = {}
                tables = ['processed_messages', 'user_tags', 'target_channels', 'config_values', 'app_logs', 'daily_stats']
                
                for table in tables:
                    cursor.execute(f'SELECT COUNT(*) FROM {table}')
                    tables_info[table] = cursor.fetchone()[0]
                
                # 获取数据库文件大小
                db_size = Path(self.db_path).stat().st_size if Path(self.db_path).exists() else 0
                
                return {
                    'db_path': self.db_path,
                    'db_size_bytes': db_size,
                    'db_size_mb': round(db_size / 1024 / 1024, 2),
                    'tables_info': tables_info,
                    'total_records': sum(tables_info.values())
                }
                
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 获取数据库信息失败 - {e}")
            return {}
    
    def backup_database(self, backup_path: str) -> bool:
        """备份数据库"""
        try:
            import shutil
            shutil.copy2(self.db_path, backup_path)
            Logger.info(f"AndroidDatabaseManager: 数据库备份成功 - {backup_path}")
            return True
            
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 数据库备份失败 - {e}")
            return False
    
    def restore_database(self, backup_path: str) -> bool:
        """恢复数据库"""
        try:
            import shutil
            shutil.copy2(backup_path, self.db_path)
            Logger.info(f"AndroidDatabaseManager: 数据库恢复成功 - {backup_path}")
            return True
            
        except Exception as e:
            Logger.error(f"AndroidDatabaseManager: 数据库恢复失败 - {e}")
            return False

# 全局数据库管理器实例
android_db_manager = AndroidDatabaseManager()

# 兼容性别名，保持与原项目的接口一致
class DatabaseManager:
    """兼容性数据库管理类"""
    
    def __init__(self, db_path: str = None):
        self._manager = android_db_manager if db_path is None else AndroidDatabaseManager(db_path)
    
    def add_processed_message(self, message: ProcessedMessage) -> bool:
        return self._manager.add_processed_message(message)
    
    def is_message_processed(self, message_id: int, channel_id: int) -> bool:
        return self._manager.is_message_processed(message_id, channel_id)
    
    def mark_message_sent(self, message_id: int, channel_id: int) -> bool:
        return self._manager.mark_message_sent(message_id, channel_id)
    
    def get_daily_stats(self, date: str = None) -> Dict[str, int]:
        return self._manager.get_daily_stats(date)
    
    def add_user_tag(self, tag_name: str) -> bool:
        return self._manager.add_user_tag(tag_name)
    
    def remove_user_tag(self, tag_name: str) -> bool:
        return self._manager.remove_user_tag(tag_name)
    
    def get_user_tags(self) -> List[str]:
        return self._manager.get_user_tags()
    
    def add_target_channel(self, channel_id: int, channel_name: str, channel_username: str = None) -> bool:
        return self._manager.add_target_channel(channel_id, channel_name, channel_username)
    
    def remove_target_channel(self, channel_id: int) -> bool:
        return self._manager.remove_target_channel(channel_id)
    
    def get_target_channels(self) -> List[Dict[str, Any]]:
        return self._manager.get_target_channels()
    
    def set_config_value(self, key: str, value: str) -> bool:
        return self._manager.set_config_value(key, value)
    
    def get_config_value(self, key: str, default: str = None) -> Optional[str]:
        return self._manager.get_config_value(key, default)
    
    def clear_old_data(self, days: int = 30) -> bool:
        return self._manager.clear_old_data(days)