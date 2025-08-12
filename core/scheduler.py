#!/usr/bin/env python3
"""
定时任务调度器模块
管理Android平台的定时任务执行，包括前台服务和AlarmManager集成
"""

import asyncio
import threading
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional, Callable
from kivy.logger import Logger
from kivy.clock import Clock

try:
    # Android平台相关导入
    from jnius import autoclass, PythonJavaClass, java_method
    from android.runnable import run_on_ui_thread
    from android import activity, mActivity
    ANDROID_AVAILABLE = True
except ImportError:
    # 非Android平台
    ANDROID_AVAILABLE = False
    Logger.warning("Scheduler: Android APIs不可用，使用模拟模式")

class AndroidScheduler:
    """Android定时任务调度器"""
    
    def __init__(self, config_manager, task_executor):
        """初始化调度器"""
        self.config_manager = config_manager
        self.task_executor = task_executor
        self.is_running = False
        self.current_task = None
        self.last_run_time = None
        self.next_run_time = None
        self.task_thread = None
        self.stop_event = threading.Event()
        
        # Android相关组件
        self.alarm_manager = None
        self.pending_intent = None
        self.service_connection = None
        
        # 初始化Android组件
        if ANDROID_AVAILABLE:
            self._init_android_components()
        
        # 定时更新状态
        Clock.schedule_interval(self._update_status, 30.0)
    
    def _init_android_components(self):
        """初始化Android组件"""
        try:
            # 获取Android系统服务
            Context = autoclass('android.content.Context')
            AlarmManager = autoclass('android.app.AlarmManager')
            Intent = autoclass('android.content.Intent')
            PendingIntent = autoclass('android.app.PendingIntent')
            
            # 获取AlarmManager
            context = mActivity.getApplicationContext()
            self.alarm_manager = context.getSystemService(Context.ALARM_SERVICE)
            
            Logger.info("Scheduler: Android组件初始化成功")
            
        except Exception as e:
            Logger.error(f"Scheduler: Android组件初始化失败 - {e}")
            self.alarm_manager = None
    
    def start(self) -> bool:
        """启动定时任务"""
        try:
            if self.is_running:
                Logger.warning("Scheduler: 定时任务已在运行")
                return True
            
            # 获取配置
            config = self.config_manager.get_schedule_config()
            if not config.get('ENABLE_SCHEDULE', False):
                Logger.warning("Scheduler: 定时任务未启用")
                return False
            
            # 启动任务线程
            self.stop_event.clear()
            self.task_thread = threading.Thread(target=self._run_scheduler, daemon=True)
            self.task_thread.start()
            
            self.is_running = True
            
            # 设置Android AlarmManager
            if ANDROID_AVAILABLE:
                self._setup_android_alarm()
            
            Logger.info("Scheduler: 定时任务启动成功")
            return True
            
        except Exception as e:
            Logger.error(f"Scheduler: 启动定时任务失败 - {e}")
            return False
    
    def stop(self) -> bool:
        """停止定时任务"""
        try:
            if not self.is_running:
                Logger.warning("Scheduler: 定时任务未运行")
                return True
            
            # 停止任务线程
            self.stop_event.set()
            
            if self.task_thread and self.task_thread.is_alive():
                self.task_thread.join(timeout=5.0)
            
            self.is_running = False
            self.current_task = None
            
            # 取消Android AlarmManager
            if ANDROID_AVAILABLE and self.alarm_manager and self.pending_intent:
                self._cancel_android_alarm()
            
            Logger.info("Scheduler: 定时任务停止成功")
            return True
            
        except Exception as e:
            Logger.error(f"Scheduler: 停止定时任务失败 - {e}")
            return False
    
    def _run_scheduler(self):
        """运行调度器主循环"""
        Logger.info("Scheduler: 调度器线程启动")
        
        while not self.stop_event.is_set():
            try:
                # 计算下次执行时间
                next_time = self._calculate_next_run_time()
                self.next_run_time = next_time
                
                if next_time:
                    # 等待到执行时间
                    wait_seconds = (next_time - datetime.now()).total_seconds()
                    
                    if wait_seconds > 0:
                        Logger.info(f"Scheduler: 等待 {wait_seconds:.0f} 秒后执行任务")
                        
                        # 分段等待，以便能够响应停止信号
                        while wait_seconds > 0 and not self.stop_event.is_set():
                            sleep_time = min(60, wait_seconds)  # 每次最多等待60秒
                            if self.stop_event.wait(sleep_time):
                                break
                            wait_seconds -= sleep_time
                    
                    # 执行任务
                    if not self.stop_event.is_set():
                        self._execute_task()
                else:
                    # 没有计划的执行时间，等待配置更新
                    self.stop_event.wait(300)  # 等待5分钟
                    
            except Exception as e:
                Logger.error(f"Scheduler: 调度器运行出错 - {e}")
                self.stop_event.wait(60)  # 出错后等待1分钟
        
        Logger.info("Scheduler: 调度器线程结束")
    
    def _calculate_next_run_time(self) -> Optional[datetime]:
        """计算下次执行时间"""
        try:
            config = self.config_manager.get_schedule_config()
            
            if not config.get('ENABLE_SCHEDULE', False):
                return None
            
            now = datetime.now()
            schedule_times = config.get('SCHEDULE_TIMES', [])
            interval_hours = config.get('CHECK_INTERVAL_HOURS', 24)
            
            if schedule_times:
                # 固定时间模式
                next_times = []
                
                for time_config in schedule_times:
                    hour = time_config.get('hour', 0)
                    minute = time_config.get('minute', 0)
                    
                    # 今天的执行时间
                    today_time = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
                    
                    if today_time > now:
                        next_times.append(today_time)
                    else:
                        # 明天的执行时间
                        tomorrow_time = today_time + timedelta(days=1)
                        next_times.append(tomorrow_time)
                
                if next_times:
                    return min(next_times)
            
            else:
                # 间隔模式
                if self.last_run_time:
                    return self.last_run_time + timedelta(hours=interval_hours)
                else:
                    # 首次运行，立即执行
                    return now + timedelta(minutes=1)
            
            return None
            
        except Exception as e:
            Logger.error(f"Scheduler: 计算下次执行时间失败 - {e}")
            return None
    
    def _execute_task(self):
        """执行抓取任务"""
        try:
            Logger.info("Scheduler: 开始执行抓取任务")
            self.current_task = 'running'
            
            # 检查网络连接
            if not self._check_network():
                Logger.warning("Scheduler: 网络连接不可用，跳过任务执行")
                return
            
            # 执行抓取任务
            success = self.task_executor.execute_fetch_task()
            
            if success:
                Logger.info("Scheduler: 抓取任务执行成功")
                self.last_run_time = datetime.now()
            else:
                Logger.error("Scheduler: 抓取任务执行失败")
                
                # 检查是否需要重试
                config = self.config_manager.get_schedule_config()
                if config.get('auto_retry', True):
                    self._schedule_retry()
            
        except Exception as e:
            Logger.error(f"Scheduler: 执行任务出错 - {e}")
        finally:
            self.current_task = None
    
    def _schedule_retry(self):
        """安排重试任务"""
        try:
            config = self.config_manager.get_schedule_config()
            retry_count = config.get('retry_count', 3)
            retry_interval = config.get('retry_interval_minutes', 30)
            
            # 这里可以实现重试逻辑
            Logger.info(f"Scheduler: 将在 {retry_interval} 分钟后重试")
            
        except Exception as e:
            Logger.error(f"Scheduler: 安排重试失败 - {e}")
    
    def _check_network(self) -> bool:
        """检查网络连接"""
        try:
            if ANDROID_AVAILABLE:
                # 使用Android API检查网络
                Context = autoclass('android.content.Context')
                ConnectivityManager = autoclass('android.net.ConnectivityManager')
                
                context = mActivity.getApplicationContext()
                cm = context.getSystemService(Context.CONNECTIVITY_SERVICE)
                
                if hasattr(cm, 'getActiveNetworkInfo'):
                    network_info = cm.getActiveNetworkInfo()
                    return network_info is not None and network_info.isConnected()
                else:
                    # Android 6.0+
                    network = cm.getActiveNetwork()
                    return network is not None
            else:
                # 非Android平台，假设网络可用
                return True
                
        except Exception as e:
            Logger.error(f"Scheduler: 检查网络失败 - {e}")
            return True  # 出错时假设网络可用
    
    def _setup_android_alarm(self):
        """设置Android AlarmManager"""
        try:
            if not self.alarm_manager:
                return
            
            # 创建Intent和PendingIntent
            Intent = autoclass('android.content.Intent')
            PendingIntent = autoclass('android.app.PendingIntent')
            AlarmManager = autoclass('android.app.AlarmManager')
            
            context = mActivity.getApplicationContext()
            
            # 创建Intent
            intent = Intent(context, autoclass('org.kivy.android.PythonService'))
            intent.putExtra('action', 'telegram_fetch')
            
            # 创建PendingIntent
            self.pending_intent = PendingIntent.getService(
                context, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT
            )
            
            # 设置重复闹钟
            if self.next_run_time:
                trigger_time = int(self.next_run_time.timestamp() * 1000)
                interval = 24 * 60 * 60 * 1000  # 24小时间隔
                
                self.alarm_manager.setRepeating(
                    AlarmManager.RTC_WAKEUP,
                    trigger_time,
                    interval,
                    self.pending_intent
                )
                
                Logger.info("Scheduler: Android AlarmManager设置成功")
            
        except Exception as e:
            Logger.error(f"Scheduler: 设置Android AlarmManager失败 - {e}")
    
    def _cancel_android_alarm(self):
        """取消Android AlarmManager"""
        try:
            if self.alarm_manager and self.pending_intent:
                self.alarm_manager.cancel(self.pending_intent)
                self.pending_intent = None
                Logger.info("Scheduler: Android AlarmManager取消成功")
                
        except Exception as e:
            Logger.error(f"Scheduler: 取消Android AlarmManager失败 - {e}")
    
    def _update_status(self, dt):
        """更新状态信息"""
        try:
            # 这里可以更新UI状态
            pass
        except Exception as e:
            Logger.error(f"Scheduler: 更新状态失败 - {e}")
    
    def execute_now(self) -> bool:
        """立即执行一次任务"""
        try:
            if self.current_task == 'running':
                Logger.warning("Scheduler: 任务正在执行中")
                return False
            
            # 在新线程中执行任务
            task_thread = threading.Thread(target=self._execute_task, daemon=True)
            task_thread.start()
            
            return True
            
        except Exception as e:
            Logger.error(f"Scheduler: 立即执行任务失败 - {e}")
            return False
    
    def get_status(self) -> Dict[str, Any]:
        """获取调度器状态"""
        return {
            'is_running': self.is_running,
            'current_task': self.current_task,
            'last_run_time': self.last_run_time,
            'next_run_time': self.next_run_time,
            'android_available': ANDROID_AVAILABLE
        }
    
    def get_config(self) -> Dict[str, Any]:
        """获取调度器配置"""
        return self.config_manager.get_schedule_config()
    
    def save_config(self, config_data: Dict[str, Any]) -> bool:
        """保存调度器配置"""
        try:
            # 更新配置
            current_config = self.config_manager.get_all_config()
            current_config.update(config_data)
            
            success = self.config_manager.save_config(current_config)
            
            if success and self.is_running:
                # 重新启动调度器以应用新配置
                self.stop()
                self.start()
            
            return success
            
        except Exception as e:
            Logger.error(f"Scheduler: 保存配置失败 - {e}")
            return False
    
    def is_running(self) -> bool:
        """检查调度器是否运行中"""
        return self.is_running
    
    def get_next_run_time(self) -> Optional[datetime]:
        """获取下次执行时间"""
        return self.next_run_time
    
    def get_last_run_time(self) -> Optional[datetime]:
        """获取最后执行时间"""
        return self.last_run_time
    
    def request_battery_optimization_whitelist(self):
        """请求加入电池优化白名单"""
        try:
            if not ANDROID_AVAILABLE:
                return
            
            Intent = autoclass('android.content.Intent')
            Settings = autoclass('android.provider.Settings')
            Uri = autoclass('android.net.Uri')
            
            context = mActivity.getApplicationContext()
            package_name = context.getPackageName()
            
            intent = Intent()
            intent.setAction(Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS)
            intent.setData(Uri.parse(f"package:{package_name}"))
            
            mActivity.startActivity(intent)
            
            Logger.info("Scheduler: 请求电池优化白名单")
            
        except Exception as e:
            Logger.error(f"Scheduler: 请求电池优化白名单失败 - {e}")
    
    def check_permissions(self) -> Dict[str, bool]:
        """检查所需权限"""
        permissions = {
            'internet': True,  # 默认有网络权限
            'wake_lock': True,  # 默认有唤醒锁权限
            'battery_optimization': False
        }
        
        try:
            if ANDROID_AVAILABLE:
                # 检查电池优化白名单
                PowerManager = autoclass('android.os.PowerManager')
                Context = autoclass('android.content.Context')
                
                context = mActivity.getApplicationContext()
                pm = context.getSystemService(Context.POWER_SERVICE)
                package_name = context.getPackageName()
                
                if hasattr(pm, 'isIgnoringBatteryOptimizations'):
                    permissions['battery_optimization'] = pm.isIgnoringBatteryOptimizations(package_name)
            
        except Exception as e:
            Logger.error(f"Scheduler: 检查权限失败 - {e}")
        
        return permissions

class TaskExecutor:
    """任务执行器"""
    
    def __init__(self, config_manager):
        """初始化任务执行器"""
        self.config_manager = config_manager
    
    def execute_fetch_task(self) -> bool:
        """执行抓取任务"""
        try:
            Logger.info("TaskExecutor: 开始执行抓取任务")
            
            # 这里应该调用实际的抓取逻辑
            # 暂时使用模拟
            import time
            time.sleep(2)  # 模拟任务执行时间
            
            Logger.info("TaskExecutor: 抓取任务执行完成")
            return True
            
        except Exception as e:
            Logger.error(f"TaskExecutor: 执行抓取任务失败 - {e}")
            return False


# 创建全局实例
# 注意：这些实例需要在应用启动时通过set_dependencies方法设置依赖
android_scheduler = None

def initialize_scheduler(config_manager, task_executor):
    """初始化调度器实例"""
    global android_scheduler
    android_scheduler = AndroidScheduler(config_manager, task_executor)
    return android_scheduler

def get_scheduler():
    """获取调度器实例"""
    return android_scheduler