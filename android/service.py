#!/usr/bin/env python3
"""
Android服务模块
实现后台服务和前台服务功能，确保应用在后台正常运行
"""

import os
import sys
import threading
import time
from datetime import datetime
from typing import Dict, Any, Optional

try:
    # Android平台相关导入
    from jnius import autoclass, PythonJavaClass, java_method
    from android import mActivity
    ANDROID_AVAILABLE = True
except ImportError:
    # 非Android平台
    ANDROID_AVAILABLE = False
    print("Service: Android APIs不可用，使用模拟模式")
    
    # 为非Android平台提供替代类
    class PythonJavaClass:
        def __init__(self):
            pass
    
    def java_method(signature):
        def decorator(func):
            return func
        return decorator

class TelegramBotService(PythonJavaClass):
    """Telegram Bot Android服务"""
    
    __javainterfaces__ = ['org/kivy/android/PythonService']
    
    def __init__(self):
        """初始化服务"""
        super().__init__()
        self.is_running = False
        self.service_thread = None
        self.stop_event = threading.Event()
        self.notification_manager = None
        self.notification_channel_id = "telegram_bot_service"
        
        # 初始化通知管理器
        if ANDROID_AVAILABLE:
            self._init_notification_manager()
    
    def _init_notification_manager(self):
        """初始化通知管理器"""
        try:
            Context = autoclass('android.content.Context')
            NotificationManager = autoclass('android.app.NotificationManager')
            
            context = mActivity.getApplicationContext()
            self.notification_manager = context.getSystemService(Context.NOTIFICATION_SERVICE)
            
            # 创建通知渠道（Android 8.0+）
            self._create_notification_channel()
            
            print("Service: 通知管理器初始化成功")
            
        except Exception as e:
            print(f"Service: 通知管理器初始化失败 - {e}")
    
    def _create_notification_channel(self):
        """创建通知渠道"""
        try:
            Build = autoclass('android.os.Build')
            
            # Android 8.0+ 需要通知渠道
            if Build.VERSION.SDK_INT >= Build.VERSION_CODES.O:
                NotificationChannel = autoclass('android.app.NotificationChannel')
                NotificationManager = autoclass('android.app.NotificationManager')
                
                channel = NotificationChannel(
                    self.notification_channel_id,
                    "Telegram Bot Service",
                    NotificationManager.IMPORTANCE_LOW
                )
                channel.setDescription("Telegram内容抓取服务")
                channel.setShowBadge(False)
                
                self.notification_manager.createNotificationChannel(channel)
                
                print("Service: 通知渠道创建成功")
        
        except Exception as e:
            print(f"Service: 创建通知渠道失败 - {e}")
    
    @java_method('(Landroid/content/Intent;)I')
    def onStartCommand(self, intent, flags, startId):
        """服务启动命令"""
        try:
            print("Service: 收到启动命令")
            
            if intent:
                action = intent.getStringExtra('action')
                print(f"Service: 执行动作 - {action}")
                
                if action == 'start_service':
                    self.start_foreground_service()
                elif action == 'stop_service':
                    self.stop_service()
                elif action == 'telegram_fetch':
                    self.execute_telegram_fetch()
            
            # 返回START_STICKY，确保服务被系统杀死后重启
            Service = autoclass('android.app.Service')
            return Service.START_STICKY
            
        except Exception as e:
            print(f"Service: 处理启动命令失败 - {e}")
            return 1  # START_STICKY
    
    @java_method('()V')
    def onCreate(self):
        """服务创建"""
        try:
            print("Service: 服务创建")
            super().onCreate()
            
        except Exception as e:
            print(f"Service: 服务创建失败 - {e}")
    
    @java_method('()V')
    def onDestroy(self):
        """服务销毁"""
        try:
            print("Service: 服务销毁")
            self.stop_service()
            super().onDestroy()
            
        except Exception as e:
            print(f"Service: 服务销毁失败 - {e}")
    
    def start_foreground_service(self):
        """启动前台服务"""
        try:
            if self.is_running:
                print("Service: 服务已在运行")
                return
            
            print("Service: 启动前台服务")
            
            # 创建前台通知
            notification = self._create_foreground_notification()
            
            if ANDROID_AVAILABLE and notification:
                # 启动前台服务
                self.startForeground(1, notification)
            
            # 启动服务线程
            self.is_running = True
            self.stop_event.clear()
            self.service_thread = threading.Thread(target=self._service_loop, daemon=True)
            self.service_thread.start()
            
            print("Service: 前台服务启动成功")
            
        except Exception as e:
            print(f"Service: 启动前台服务失败 - {e}")
    
    def stop_service(self):
        """停止服务"""
        try:
            if not self.is_running:
                print("Service: 服务未运行")
                return
            
            print("Service: 停止服务")
            
            # 停止服务线程
            self.is_running = False
            self.stop_event.set()
            
            if self.service_thread and self.service_thread.is_alive():
                self.service_thread.join(timeout=5.0)
            
            # 停止前台服务
            if ANDROID_AVAILABLE:
                self.stopForeground(True)
            
            print("Service: 服务停止成功")
            
        except Exception as e:
            print(f"Service: 停止服务失败 - {e}")
    
    def _create_foreground_notification(self):
        """创建前台服务通知"""
        try:
            if not ANDROID_AVAILABLE:
                return None
            
            NotificationCompat = autoclass('androidx.core.app.NotificationCompat')
            PendingIntent = autoclass('android.app.PendingIntent')
            Intent = autoclass('android.content.Intent')
            
            context = mActivity.getApplicationContext()
            
            # 创建点击通知的Intent
            intent = Intent(context, mActivity.getClass())
            intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP)
            
            pending_intent = PendingIntent.getActivity(
                context, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT
            )
            
            # 构建通知
            builder = NotificationCompat.Builder(context, self.notification_channel_id)
            builder.setContentTitle("Telegram内容抓取")
            builder.setContentText("服务正在后台运行")
            builder.setSmallIcon(android.R.drawable.ic_dialog_info)  # 使用系统图标
            builder.setContentIntent(pending_intent)
            builder.setOngoing(True)  # 不可滑动删除
            builder.setPriority(NotificationCompat.PRIORITY_LOW)
            
            return builder.build()
            
        except Exception as e:
            print(f"Service: 创建前台通知失败 - {e}")
            return None
    
    def _service_loop(self):
        """服务主循环"""
        print("Service: 服务线程启动")
        
        while self.is_running and not self.stop_event.is_set():
            try:
                # 更新通知状态
                self._update_notification()
                
                # 检查是否需要执行定时任务
                self._check_scheduled_tasks()
                
                # 等待30秒
                if self.stop_event.wait(30):
                    break
                    
            except Exception as e:
                print(f"Service: 服务循环出错 - {e}")
                time.sleep(60)  # 出错后等待1分钟
        
        print("Service: 服务线程结束")
    
    def _update_notification(self):
        """更新通知内容"""
        try:
            if not ANDROID_AVAILABLE or not self.notification_manager:
                return
            
            # 获取当前状态
            current_time = datetime.now().strftime("%H:%M:%S")
            
            # 更新通知
            notification = self._create_status_notification(f"运行中 - {current_time}")
            if notification:
                self.notification_manager.notify(1, notification)
                
        except Exception as e:
            print(f"Service: 更新通知失败 - {e}")
    
    def _create_status_notification(self, status_text: str):
        """创建状态通知"""
        try:
            if not ANDROID_AVAILABLE:
                return None
            
            NotificationCompat = autoclass('androidx.core.app.NotificationCompat')
            PendingIntent = autoclass('android.app.PendingIntent')
            Intent = autoclass('android.content.Intent')
            
            context = mActivity.getApplicationContext()
            
            # 创建点击通知的Intent
            intent = Intent(context, mActivity.getClass())
            intent.setFlags(Intent.FLAG_ACTIVITY_CLEAR_TOP | Intent.FLAG_ACTIVITY_SINGLE_TOP)
            
            pending_intent = PendingIntent.getActivity(
                context, 0, intent, PendingIntent.FLAG_UPDATE_CURRENT
            )
            
            # 构建通知
            builder = NotificationCompat.Builder(context, self.notification_channel_id)
            builder.setContentTitle("Telegram内容抓取")
            builder.setContentText(status_text)
            builder.setSmallIcon(android.R.drawable.ic_dialog_info)
            builder.setContentIntent(pending_intent)
            builder.setOngoing(True)
            builder.setPriority(NotificationCompat.PRIORITY_LOW)
            
            return builder.build()
            
        except Exception as e:
            print(f"Service: 创建状态通知失败 - {e}")
            return None
    
    def _check_scheduled_tasks(self):
        """检查定时任务"""
        try:
            # 这里应该检查是否有需要执行的定时任务
            # 暂时使用简单的时间检查
            current_hour = datetime.now().hour
            
            # 示例：每天上午9点执行
            if current_hour == 9:
                self.execute_telegram_fetch()
                
        except Exception as e:
            print(f"Service: 检查定时任务失败 - {e}")
    
    def execute_telegram_fetch(self):
        """执行Telegram抓取任务"""
        try:
            print("Service: 开始执行Telegram抓取任务")
            
            # 更新通知状态
            if ANDROID_AVAILABLE and self.notification_manager:
                notification = self._create_status_notification("正在抓取内容...")
                if notification:
                    self.notification_manager.notify(1, notification)
            
            # 这里应该调用实际的抓取逻辑
            # 暂时使用模拟
            self._simulate_fetch_task()
            
            print("Service: Telegram抓取任务完成")
            
            # 恢复正常状态通知
            if ANDROID_AVAILABLE and self.notification_manager:
                current_time = datetime.now().strftime("%H:%M:%S")
                notification = self._create_status_notification(f"运行中 - {current_time}")
                if notification:
                    self.notification_manager.notify(1, notification)
            
        except Exception as e:
            print(f"Service: 执行Telegram抓取失败 - {e}")
    
    def _simulate_fetch_task(self):
        """模拟抓取任务"""
        try:
            # 模拟任务执行时间
            for i in range(5):
                if self.stop_event.is_set():
                    break
                
                print(f"Service: 模拟抓取步骤 {i+1}/5")
                time.sleep(2)
            
            print("Service: 模拟抓取任务完成")
            
        except Exception as e:
            print(f"Service: 模拟抓取任务失败 - {e}")

class ServiceManager:
    """服务管理器"""
    
    def __init__(self):
        """初始化服务管理器"""
        self.service_instance = None
        self.is_service_running = False
    
    def start_service(self) -> bool:
        """启动服务"""
        try:
            if not ANDROID_AVAILABLE:
                print("ServiceManager: 非Android平台，使用模拟服务")
                return self._start_mock_service()
            
            print("ServiceManager: 启动Android服务")
            
            # 创建服务Intent
            Intent = autoclass('android.content.Intent')
            context = mActivity.getApplicationContext()
            
            intent = Intent(context, autoclass('org.kivy.android.PythonService'))
            intent.putExtra('action', 'start_service')
            
            # 启动前台服务
            context.startForegroundService(intent)
            
            self.is_service_running = True
            print("ServiceManager: Android服务启动成功")
            return True
            
        except Exception as e:
            print(f"ServiceManager: 启动服务失败 - {e}")
            return False
    
    def stop_service(self) -> bool:
        """停止服务"""
        try:
            if not ANDROID_AVAILABLE:
                return self._stop_mock_service()
            
            print("ServiceManager: 停止Android服务")
            
            # 创建停止服务Intent
            Intent = autoclass('android.content.Intent')
            context = mActivity.getApplicationContext()
            
            intent = Intent(context, autoclass('org.kivy.android.PythonService'))
            intent.putExtra('action', 'stop_service')
            
            context.startService(intent)
            
            self.is_service_running = False
            print("ServiceManager: Android服务停止成功")
            return True
            
        except Exception as e:
            print(f"ServiceManager: 停止服务失败 - {e}")
            return False
    
    def _start_mock_service(self) -> bool:
        """启动模拟服务"""
        try:
            if self.service_instance:
                print("ServiceManager: 模拟服务已运行")
                return True
            
            self.service_instance = TelegramBotService()
            self.service_instance.start_foreground_service()
            self.is_service_running = True
            
            print("ServiceManager: 模拟服务启动成功")
            return True
            
        except Exception as e:
            print(f"ServiceManager: 启动模拟服务失败 - {e}")
            return False
    
    def _stop_mock_service(self) -> bool:
        """停止模拟服务"""
        try:
            if not self.service_instance:
                print("ServiceManager: 模拟服务未运行")
                return True
            
            self.service_instance.stop_service()
            self.service_instance = None
            self.is_service_running = False
            
            print("ServiceManager: 模拟服务停止成功")
            return True
            
        except Exception as e:
            print(f"ServiceManager: 停止模拟服务失败 - {e}")
            return False
    
    def is_running(self) -> bool:
        """检查服务是否运行"""
        return self.is_service_running
    
    def execute_immediate_task(self) -> bool:
        """立即执行任务"""
        try:
            if not ANDROID_AVAILABLE:
                if self.service_instance:
                    self.service_instance.execute_telegram_fetch()
                    return True
                return False
            
            print("ServiceManager: 执行立即任务")
            
            # 发送执行任务的Intent
            Intent = autoclass('android.content.Intent')
            context = mActivity.getApplicationContext()
            
            intent = Intent(context, autoclass('org.kivy.android.PythonService'))
            intent.putExtra('action', 'telegram_fetch')
            
            context.startService(intent)
            
            print("ServiceManager: 立即任务执行成功")
            return True
            
        except Exception as e:
            print(f"ServiceManager: 执行立即任务失败 - {e}")
            return False
    
    def get_service_status(self) -> Dict[str, Any]:
        """获取服务状态"""
        return {
            'is_running': self.is_service_running,
            'android_available': ANDROID_AVAILABLE,
            'service_type': 'android' if ANDROID_AVAILABLE else 'mock'
        }

# 全局服务管理器实例
service_manager = ServiceManager()

def start_background_service() -> bool:
    """启动后台服务"""
    return service_manager.start_service()

def stop_background_service() -> bool:
    """停止后台服务"""
    return service_manager.stop_service()

def is_service_running() -> bool:
    """检查服务是否运行"""
    return service_manager.is_running()

def execute_fetch_now() -> bool:
    """立即执行抓取任务"""
    return service_manager.execute_immediate_task()

def get_service_status() -> Dict[str, Any]:
    """获取服务状态"""
    return service_manager.get_service_status()