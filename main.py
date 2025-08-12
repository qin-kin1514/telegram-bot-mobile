#!/usr/bin/env python3
"""
Telegram内容抓取机器人 - Android移动应用
主入口文件
"""

import os
import sys
import asyncio
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Kivy配置
os.environ['KIVY_NO_CONSOLELOG'] = '1'  # 禁用控制台日志
os.environ['KIVY_LOG_MODE'] = 'MIXED'   # 混合日志模式

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.logger import Logger
from kivy.clock import Clock
from kivy.utils import platform

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.screenmanager import MDScreenManager

# 导入界面模块
from ui.main_screen import MainScreen
from ui.config_screen import ConfigScreen
from ui.schedule_screen import ScheduleScreen
from ui.log_screen import LogScreen

# 导入核心模块
from core.config import android_config
from core.database import android_db_manager
from core.bot_manager import android_bot_manager
from core.scheduler import initialize_scheduler, get_scheduler
from core.permission_manager import android_permission_manager
from android.service import ServiceManager

class TelegramBotApp(MDApp):
    """Telegram机器人Android应用主类"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Telegram内容抓取机器人"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Amber"
        
        # 应用状态
        self.is_initialized = False
        self.service_manager = None
        
        # 界面管理器
        self.screen_manager = None
        
        # 定时更新任务
        self.update_event = None
        
    def build(self):
        """构建应用界面"""
        try:
            Logger.info("TelegramBotApp: 开始构建应用界面")
            
            # 创建屏幕管理器
            self.screen_manager = MDScreenManager()
            
            # 添加各个界面
            self.screen_manager.add_widget(MainScreen(name='main'))
            self.screen_manager.add_widget(ConfigScreen(name='config'))
            self.screen_manager.add_widget(ScheduleScreen(name='schedule'))
            self.screen_manager.add_widget(LogScreen(name='log'))
            
            # 设置默认界面
            self.screen_manager.current = 'main'
            
            Logger.info("TelegramBotApp: 应用界面构建完成")
            return self.screen_manager
            
        except Exception as e:
            Logger.error(f"TelegramBotApp: 构建应用界面失败 - {e}")
            return None
    
    def on_start(self):
        """应用启动时调用"""
        try:
            Logger.info("TelegramBotApp: 应用启动")
            
            # 延迟初始化，避免阻塞界面
            Clock.schedule_once(self._initialize_app, 0.5)
            
        except Exception as e:
            Logger.error(f"TelegramBotApp: 应用启动失败 - {e}")
    
    def _initialize_app(self, dt):
        """初始化应用"""
        try:
            Logger.info("TelegramBotApp: 开始初始化应用")
            
            # 初始化数据库
            self._initialize_database()
            
            # 初始化配置
            self._initialize_config()
            
            # 请求权限（仅Android平台）
            if platform == 'android':
                self._request_permissions()
            
            # 初始化服务管理器
            self._initialize_service_manager()
            
            # 启动定时更新
            self._start_periodic_updates()
            
            # 标记初始化完成
            self.is_initialized = True
            
            Logger.info("TelegramBotApp: 应用初始化完成")
            
            # 记录启动日志
            android_db_manager.add_log('info', '应用启动成功', 'app')
            
        except Exception as e:
            error_msg = f"应用初始化失败: {str(e)}"
            Logger.error(f"TelegramBotApp: {error_msg}")
            android_db_manager.add_log('error', error_msg, 'app')
    
    def _initialize_database(self):
        """初始化数据库"""
        try:
            Logger.info("TelegramBotApp: 初始化数据库")
            # 数据库在导入时已自动初始化
            db_info = android_db_manager.get_database_info()
            Logger.info(f"TelegramBotApp: 数据库初始化完成 - {db_info}")
        except Exception as e:
            Logger.error(f"TelegramBotApp: 数据库初始化失败 - {e}")
            raise
    
    def _initialize_config(self):
        """初始化配置"""
        try:
            Logger.info("TelegramBotApp: 初始化配置")
            
            # 检查是否首次运行
            if android_config.is_first_run():
                Logger.info("TelegramBotApp: 首次运行，创建默认配置")
                android_config.create_default_config()
            
            # 加载配置
            android_config.load()
            
            # 验证配置
            validation = android_config.validate()
            Logger.info(f"TelegramBotApp: 配置验证结果 - {validation}")
            
        except Exception as e:
            Logger.error(f"TelegramBotApp: 配置初始化失败 - {e}")
            raise
    
    def _request_permissions(self):
        """请求Android权限"""
        try:
            Logger.info("TelegramBotApp: 请求Android权限")
            
            # 检查权限状态
            permission_status = android_permission_manager.get_permission_summary()
            Logger.info(f"TelegramBotApp: 权限状态 - {permission_status}")
            
            # 请求缺失的权限
            missing_permissions = android_permission_manager.get_missing_permissions()
            if missing_permissions:
                Logger.info(f"TelegramBotApp: 请求缺失权限 - {missing_permissions}")
                android_permission_manager.request_permissions(missing_permissions)
            
            # 请求电池优化白名单
            if not android_permission_manager.is_battery_optimization_ignored():
                Logger.info("TelegramBotApp: 请求电池优化白名单")
                android_permission_manager.request_ignore_battery_optimization()
            
        except Exception as e:
            Logger.error(f"TelegramBotApp: 权限请求失败 - {e}")
    
    def _initialize_service_manager(self):
        """初始化服务管理器和调度器"""
        try:
            Logger.info("TelegramBotApp: 初始化服务管理器和调度器")
            
            # 初始化调度器
            from core.scheduler import TaskExecutor
            task_executor = TaskExecutor(android_config)
            self.scheduler = initialize_scheduler(android_config, task_executor)
            
            self.service_manager = ServiceManager()
            
            # 如果配置了自动启动，则启动服务
            schedule_config = android_config.get_schedule_config()
            if schedule_config.get('ENABLE_SCHEDULE', False):
                Logger.info("TelegramBotApp: 自动启动后台服务")
                self.service_manager.start_service()
            
        except Exception as e:
            Logger.error(f"TelegramBotApp: 服务管理器初始化失败 - {e}")
    
    def _start_periodic_updates(self):
        """启动定时更新"""
        try:
            Logger.info("TelegramBotApp: 启动定时更新")
            
            # 每30秒更新一次状态
            self.update_event = Clock.schedule_interval(self._update_status, 30)
            
        except Exception as e:
            Logger.error(f"TelegramBotApp: 启动定时更新失败 - {e}")
    
    def _update_status(self, dt):
        """定时更新状态"""
        try:
            # 更新机器人状态
            status = android_bot_manager.get_status()
            
            # 更新调度器状态
            scheduler_status = android_scheduler.get_status()
            
            # 通知界面更新（如果当前界面需要）
            current_screen = self.screen_manager.current_screen
            if hasattr(current_screen, 'update_status'):
                current_screen.update_status({
                    'bot': status,
                    'scheduler': scheduler_status
                })
            
        except Exception as e:
            Logger.error(f"TelegramBotApp: 状态更新失败 - {e}")
    
    def switch_screen(self, screen_name: str):
        """切换界面"""
        try:
            if self.screen_manager and screen_name in [s.name for s in self.screen_manager.screens]:
                self.screen_manager.current = screen_name
                Logger.info(f"TelegramBotApp: 切换到界面 - {screen_name}")
            else:
                Logger.warning(f"TelegramBotApp: 界面不存在 - {screen_name}")
        except Exception as e:
            Logger.error(f"TelegramBotApp: 切换界面失败 - {e}")
    
    def on_pause(self):
        """应用暂停时调用"""
        try:
            Logger.info("TelegramBotApp: 应用暂停")
            
            # 记录暂停日志
            android_db_manager.add_log('info', '应用暂停', 'app')
            
            # 返回True表示应用可以在后台运行
            return True
            
        except Exception as e:
            Logger.error(f"TelegramBotApp: 应用暂停处理失败 - {e}")
            return True
    
    def on_resume(self):
        """应用恢复时调用"""
        try:
            Logger.info("TelegramBotApp: 应用恢复")
            
            # 记录恢复日志
            android_db_manager.add_log('info', '应用恢复', 'app')
            
            # 刷新状态
            if self.is_initialized:
                self._update_status(0)
            
        except Exception as e:
            Logger.error(f"TelegramBotApp: 应用恢复处理失败 - {e}")
    
    def on_stop(self):
        """应用停止时调用"""
        try:
            Logger.info("TelegramBotApp: 应用停止")
            
            # 停止定时更新
            if self.update_event:
                self.update_event.cancel()
            
            # 记录停止日志
            android_db_manager.add_log('info', '应用停止', 'app')
            
            # 保存配置
            android_config.save()
            
        except Exception as e:
            Logger.error(f"TelegramBotApp: 应用停止处理失败 - {e}")
    
    def get_screen_manager(self):
        """获取屏幕管理器"""
        return self.screen_manager
    
    def get_bot_manager(self):
        """获取机器人管理器"""
        return android_bot_manager
    
    def get_scheduler(self):
        """获取调度器"""
        return get_scheduler()
    
    def get_service_manager(self):
        """获取服务管理器"""
        return self.service_manager
    
    def get_config_manager(self):
        """获取配置管理器"""
        return android_config
    
    def get_database_manager(self):
        """获取数据库管理器"""
        return android_db_manager
    
    def get_permission_manager(self):
        """获取权限管理器"""
        return android_permission_manager

def main():
    """主函数"""
    try:
        Logger.info("启动Telegram内容抓取机器人Android应用")
        
        # 创建并运行应用
        app = TelegramBotApp()
        app.run()
        
    except Exception as e:
        Logger.error(f"应用启动失败: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()