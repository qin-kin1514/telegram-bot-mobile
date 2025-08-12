#!/usr/bin/env python3
"""
机器人管理模块 - Android适配版本
整合所有核心功能，提供统一的业务逻辑接口
"""

import asyncio
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from kivy.logger import Logger
from kivy.clock import Clock

from .config import android_config
from .database import android_db_manager, ProcessedMessage
from .telegram_client import android_telegram_client
from .notifier import android_email_notifier

class AndroidBotManager:
    """Android适配的机器人管理器"""
    
    def __init__(self):
        """初始化机器人管理器"""
        self.is_running = False
        self.last_run_time = None
        self.next_run_time = None
        self.current_task = None
        self.stats = {
            'total_processed': 0,
            'total_sent': 0,
            'total_errors': 0,
            'last_error': None
        }
    
    def get_status(self) -> Dict[str, Any]:
        """获取机器人状态"""
        try:
            # 获取今日统计
            today_stats = android_db_manager.get_daily_stats()
            
            # 获取配置验证状态
            config_validation = android_config.validate()
            
            return {
                'is_running': self.is_running,
                'last_run_time': self.last_run_time,
                'next_run_time': self.next_run_time,
                'today_stats': today_stats,
                'config_valid': all(config_validation.values()),
                'config_validation': config_validation,
                'total_stats': self.stats
            }
        except Exception as e:
            Logger.error(f"AndroidBotManager: 获取状态失败 - {e}")
            return {
                'is_running': False,
                'error': str(e)
            }
    
    async def run_once(self) -> Dict[str, Any]:
        """执行一次抓取任务"""
        result = {
            'success': False,
            'processed_count': 0,
            'sent_count': 0,
            'error_count': 0,
            'errors': [],
            'start_time': datetime.now(),
            'end_time': None
        }
        
        try:
            Logger.info("AndroidBotManager: 开始执行抓取任务")
            self.is_running = True
            
            # 验证配置
            config_validation = android_config.validate()
            if not all(config_validation.values()):
                missing_configs = [k for k, v in config_validation.items() if not v]
                error_msg = f"配置不完整: {', '.join(missing_configs)}"
                result['errors'].append(error_msg)
                Logger.error(f"AndroidBotManager: {error_msg}")
                return result
            
            # 执行Telegram内容抓取
            telegram_result = await android_telegram_client.process_channels()
            
            result['processed_count'] = telegram_result.get('processed_count', 0)
            result['sent_count'] = telegram_result.get('sent_count', 0)
            result['error_count'] = telegram_result.get('error_count', 0)
            
            # 更新统计
            self.stats['total_processed'] += result['processed_count']
            self.stats['total_sent'] += result['sent_count']
            self.stats['total_errors'] += result['error_count']
            
            # 发送邮件通知（如果有新内容）
            if result['sent_count'] > 0:
                try:
                    # 获取今日处理的消息用于邮件通知
                    recent_messages = self._get_recent_processed_messages()
                    if recent_messages:
                        email_sent = android_email_notifier.send_new_content_notification(recent_messages)
                        if not email_sent:
                            result['errors'].append('邮件通知发送失败')
                except Exception as e:
                    error_msg = f"邮件通知失败: {str(e)}"
                    result['errors'].append(error_msg)
                    Logger.error(f"AndroidBotManager: {error_msg}")
            
            # 记录运行时间
            self.last_run_time = datetime.now()
            result['end_time'] = self.last_run_time
            
            # 计算下次运行时间
            self._calculate_next_run_time()
            
            result['success'] = True
            Logger.info(f"AndroidBotManager: 抓取任务完成 - 处理:{result['processed_count']}, 发送:{result['sent_count']}, 错误:{result['error_count']}")
            
            # 记录日志到数据库
            android_db_manager.add_log(
                'info',
                f"抓取任务完成 - 处理:{result['processed_count']}, 发送:{result['sent_count']}, 错误:{result['error_count']}",
                'bot_manager'
            )
            
        except Exception as e:
            error_msg = f"执行抓取任务失败: {str(e)}"
            result['errors'].append(error_msg)
            result['error_count'] += 1
            self.stats['last_error'] = error_msg
            self.stats['total_errors'] += 1
            
            Logger.error(f"AndroidBotManager: {error_msg}")
            
            # 记录错误日志
            android_db_manager.add_log('error', error_msg, 'bot_manager')
            
            # 发送错误通知邮件
            try:
                android_email_notifier.send_error_notification(error_msg, str(e))
            except Exception as email_error:
                Logger.error(f"AndroidBotManager: 发送错误通知邮件失败 - {email_error}")
        
        finally:
            self.is_running = False
            result['end_time'] = datetime.now()
        
        return result
    
    def _get_recent_processed_messages(self, limit: int = 10) -> List[Dict[str, Any]]:
        """获取最近处理的消息"""
        try:
            # 这里应该从数据库获取最近的消息
            # 由于当前数据库接口限制，返回模拟数据
            return [
                {
                    'channel_name': '示例频道',
                    'content': '这是一条示例消息内容...',
                    'tags': ['AI', 'Python'],
                    'processed_at': datetime.now().strftime('%H:%M:%S')
                }
            ]
        except Exception as e:
            Logger.error(f"AndroidBotManager: 获取最近消息失败 - {e}")
            return []
    
    def _calculate_next_run_time(self):
        """计算下次运行时间"""
        try:
            schedule_config = android_config.get_schedule_config()
            
            if not schedule_config.get('ENABLE_SCHEDULE', False):
                self.next_run_time = None
                return
            
            schedule_times = schedule_config.get('SCHEDULE_TIMES', [])
            check_interval_hours = schedule_config.get('CHECK_INTERVAL_HOURS', 24)
            
            if schedule_times:
                # 基于固定时间计算
                now = datetime.now()
                next_times = []
                
                for time_config in schedule_times:
                    hour = time_config.get('hour', 9)
                    minute = time_config.get('minute', 0)
                    
                    # 今天的时间
                    today_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
                    if today_time > now:
                        next_times.append(today_time)
                    
                    # 明天的时间
                    tomorrow_time = today_time + timedelta(days=1)
                    next_times.append(tomorrow_time)
                
                if next_times:
                    self.next_run_time = min(next_times)
            else:
                # 基于间隔时间计算
                if self.last_run_time:
                    self.next_run_time = self.last_run_time + timedelta(hours=check_interval_hours)
                else:
                    self.next_run_time = datetime.now() + timedelta(hours=check_interval_hours)
            
            Logger.info(f"AndroidBotManager: 下次运行时间 - {self.next_run_time}")
            
        except Exception as e:
            Logger.error(f"AndroidBotManager: 计算下次运行时间失败 - {e}")
            self.next_run_time = None
    
    async def send_daily_summary(self, date: Optional[str] = None) -> bool:
        """发送每日汇总"""
        try:
            if date is None:
                date = datetime.now().strftime('%Y-%m-%d')
            
            Logger.info(f"AndroidBotManager: 发送每日汇总 - {date}")
            
            success = android_email_notifier.send_daily_summary(date)
            
            if success:
                android_db_manager.add_log('info', f'每日汇总邮件发送成功 - {date}', 'bot_manager')
            else:
                android_db_manager.add_log('error', f'每日汇总邮件发送失败 - {date}', 'bot_manager')
            
            return success
            
        except Exception as e:
            error_msg = f"发送每日汇总失败: {str(e)}"
            Logger.error(f"AndroidBotManager: {error_msg}")
            android_db_manager.add_log('error', error_msg, 'bot_manager')
            return False
    
    async def test_connections(self) -> Dict[str, Any]:
        """测试所有连接"""
        result = {
            'telegram': {'success': False, 'message': ''},
            'email': {'success': False, 'message': ''},
            'database': {'success': False, 'message': ''}
        }
        
        try:
            # 测试Telegram连接
            Logger.info("AndroidBotManager: 测试Telegram连接")
            telegram_result = await android_telegram_client.test_connection()
            result['telegram'] = {
                'success': telegram_result.get('success', False),
                'message': telegram_result.get('message', ''),
                'user_info': telegram_result.get('user_info')
            }
            
            # 测试邮件连接
            Logger.info("AndroidBotManager: 测试邮件连接")
            email_result = android_email_notifier.test_email_config()
            result['email'] = {
                'success': email_result.get('success', False),
                'message': email_result.get('message', ''),
                'config_valid': email_result.get('config_valid', False)
            }
            
            # 测试数据库连接
            Logger.info("AndroidBotManager: 测试数据库连接")
            try:
                db_info = android_db_manager.get_database_info()
                result['database'] = {
                    'success': True,
                    'message': '数据库连接正常',
                    'info': db_info
                }
            except Exception as e:
                result['database'] = {
                    'success': False,
                    'message': f'数据库连接失败: {str(e)}'
                }
            
        except Exception as e:
            Logger.error(f"AndroidBotManager: 测试连接失败 - {e}")
        
        return result
    
    def get_recent_logs(self, limit: int = 50, level: str = None) -> List[Dict[str, Any]]:
        """获取最近的日志"""
        try:
            return android_db_manager.get_logs(limit, level)
        except Exception as e:
            Logger.error(f"AndroidBotManager: 获取日志失败 - {e}")
            return []
    
    def clear_old_data(self, days: int = 30) -> bool:
        """清理旧数据"""
        try:
            Logger.info(f"AndroidBotManager: 清理{days}天前的旧数据")
            success = android_db_manager.clear_old_data(days)
            
            if success:
                android_db_manager.add_log('info', f'清理旧数据成功 - {days}天前', 'bot_manager')
            else:
                android_db_manager.add_log('error', f'清理旧数据失败 - {days}天前', 'bot_manager')
            
            return success
            
        except Exception as e:
            error_msg = f"清理旧数据失败: {str(e)}"
            Logger.error(f"AndroidBotManager: {error_msg}")
            android_db_manager.add_log('error', error_msg, 'bot_manager')
            return False
    
    def get_database_info(self) -> Dict[str, Any]:
        """获取数据库信息"""
        try:
            return android_db_manager.get_database_info()
        except Exception as e:
            Logger.error(f"AndroidBotManager: 获取数据库信息失败 - {e}")
            return {}
    
    def backup_data(self, backup_path: str) -> bool:
        """备份数据"""
        try:
            Logger.info(f"AndroidBotManager: 备份数据到 {backup_path}")
            success = android_db_manager.backup_database(backup_path)
            
            if success:
                android_db_manager.add_log('info', f'数据备份成功 - {backup_path}', 'bot_manager')
            else:
                android_db_manager.add_log('error', f'数据备份失败 - {backup_path}', 'bot_manager')
            
            return success
            
        except Exception as e:
            error_msg = f"数据备份失败: {str(e)}"
            Logger.error(f"AndroidBotManager: {error_msg}")
            android_db_manager.add_log('error', error_msg, 'bot_manager')
            return False
    
    def restore_data(self, backup_path: str) -> bool:
        """恢复数据"""
        try:
            Logger.info(f"AndroidBotManager: 从 {backup_path} 恢复数据")
            success = android_db_manager.restore_database(backup_path)
            
            if success:
                android_db_manager.add_log('info', f'数据恢复成功 - {backup_path}', 'bot_manager')
            else:
                android_db_manager.add_log('error', f'数据恢复失败 - {backup_path}', 'bot_manager')
            
            return success
            
        except Exception as e:
            error_msg = f"数据恢复失败: {str(e)}"
            Logger.error(f"AndroidBotManager: {error_msg}")
            android_db_manager.add_log('error', error_msg, 'bot_manager')
            return False
    
    def get_config_summary(self) -> Dict[str, Any]:
        """获取配置摘要"""
        try:
            return android_config.get_config_summary()
        except Exception as e:
            Logger.error(f"AndroidBotManager: 获取配置摘要失败 - {e}")
            return {}
    
    def update_config(self, config_data: Dict[str, Any]) -> bool:
        """更新配置"""
        try:
            Logger.info("AndroidBotManager: 更新配置")
            success = android_config.update(config_data)
            
            if success:
                android_db_manager.add_log('info', '配置更新成功', 'bot_manager')
                # 重新计算下次运行时间
                self._calculate_next_run_time()
            else:
                android_db_manager.add_log('error', '配置更新失败', 'bot_manager')
            
            return success
            
        except Exception as e:
            error_msg = f"更新配置失败: {str(e)}"
            Logger.error(f"AndroidBotManager: {error_msg}")
            android_db_manager.add_log('error', error_msg, 'bot_manager')
            return False
    
    def reset_config(self) -> bool:
        """重置配置"""
        try:
            Logger.info("AndroidBotManager: 重置配置")
            success = android_config.reset_to_default()
            
            if success:
                android_db_manager.add_log('info', '配置重置成功', 'bot_manager')
                self.next_run_time = None
            else:
                android_db_manager.add_log('error', '配置重置失败', 'bot_manager')
            
            return success
            
        except Exception as e:
            error_msg = f"重置配置失败: {str(e)}"
            Logger.error(f"AndroidBotManager: {error_msg}")
            android_db_manager.add_log('error', error_msg, 'bot_manager')
            return False
    
    def export_config(self) -> str:
        """导出配置"""
        try:
            return android_config.export_config()
        except Exception as e:
            Logger.error(f"AndroidBotManager: 导出配置失败 - {e}")
            return '{}'
    
    def import_config(self, config_json: str) -> bool:
        """导入配置"""
        try:
            Logger.info("AndroidBotManager: 导入配置")
            success = android_config.import_config(config_json)
            
            if success:
                android_db_manager.add_log('info', '配置导入成功', 'bot_manager')
                self._calculate_next_run_time()
            else:
                android_db_manager.add_log('error', '配置导入失败', 'bot_manager')
            
            return success
            
        except Exception as e:
            error_msg = f"导入配置失败: {str(e)}"
            Logger.error(f"AndroidBotManager: {error_msg}")
            android_db_manager.add_log('error', error_msg, 'bot_manager')
            return False

# 全局机器人管理器实例
android_bot_manager = AndroidBotManager()

# 兼容性别名
class BotManager:
    """兼容性机器人管理器类"""
    
    def __init__(self):
        self._manager = android_bot_manager
    
    def get_status(self) -> Dict[str, Any]:
        return self._manager.get_status()
    
    async def run_once(self) -> Dict[str, Any]:
        return await self._manager.run_once()
    
    async def send_daily_summary(self, date: str = None) -> bool:
        return await self._manager.send_daily_summary(date)
    
    async def test_connections(self) -> Dict[str, Any]:
        return await self._manager.test_connections()
    
    def get_recent_logs(self, limit: int = 50, level: str = None) -> List[Dict[str, Any]]:
        return self._manager.get_recent_logs(limit, level)
    
    def clear_old_data(self, days: int = 30) -> bool:
        return self._manager.clear_old_data(days)