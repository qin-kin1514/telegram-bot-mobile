#!/usr/bin/env python3
"""
主界面模块
显示应用运行状态和基本控制功能
"""

from kivy.clock import Clock
from kivy.logger import Logger
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import MDList, TwoLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.progressbar import MDProgressBar
from datetime import datetime
import asyncio

class MainScreen(MDScreen):
    """主界面屏幕"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_running = False
        self.last_run_time = None
        self.today_stats = {'processed': 0, 'sent': 0}
        
        self.build_ui()
        
        # 定时更新界面
        Clock.schedule_interval(self.update_status, 5.0)
    
    def build_ui(self):
        """构建用户界面"""
        layout = MDBoxLayout(orientation='vertical')
        
        # 顶部工具栏
        toolbar = MDTopAppBar(
            title="Telegram内容抓取机器人",
            elevation=2,
            left_action_items=[["menu", lambda x: self.open_navigation()]],
            right_action_items=[["refresh", lambda x: self.refresh_status()]]
        )
        layout.add_widget(toolbar)
        
        # 主内容区域
        content = MDBoxLayout(
            orientation='vertical',
            padding="16dp",
            spacing="16dp"
        )
        
        # 状态卡片
        self.status_card = self.create_status_card()
        content.add_widget(self.status_card)
        
        # 统计卡片
        self.stats_card = self.create_stats_card()
        content.add_widget(self.stats_card)
        
        # 控制按钮
        self.control_buttons = self.create_control_buttons()
        content.add_widget(self.control_buttons)
        
        # 最近日志
        self.log_card = self.create_log_card()
        content.add_widget(self.log_card)
        
        layout.add_widget(content)
        self.add_widget(layout)
    
    def create_status_card(self):
        """创建状态卡片"""
        card = MDCard(
            size_hint_y=None,
            height="120dp",
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='vertical')
        
        # 状态标题
        status_label = MDLabel(
            text="运行状态",
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height="32dp"
        )
        layout.add_widget(status_label)
        
        # 状态信息
        self.status_text = MDLabel(
            text="未运行",
            theme_text_color="Secondary",
            font_style="Body1"
        )
        layout.add_widget(self.status_text)
        
        # 最后运行时间
        self.last_run_text = MDLabel(
            text="最后运行：从未运行",
            theme_text_color="Hint",
            font_style="Caption"
        )
        layout.add_widget(self.last_run_text)
        
        card.add_widget(layout)
        return card
    
    def create_stats_card(self):
        """创建统计卡片"""
        card = MDCard(
            size_hint_y=None,
            height="100dp",
            elevation=2,
            padding="16dp"
        )
        
        layout = MDGridLayout(
            cols=3,
            spacing="8dp"
        )
        
        # 今日处理数
        processed_layout = MDBoxLayout(orientation='vertical')
        processed_layout.add_widget(MDLabel(
            text="今日处理",
            theme_text_color="Primary",
            font_style="Caption",
            halign="center"
        ))
        self.processed_count = MDLabel(
            text="0",
            theme_text_color="Primary",
            font_style="H5",
            halign="center"
        )
        processed_layout.add_widget(self.processed_count)
        layout.add_widget(processed_layout)
        
        # 今日发送数
        sent_layout = MDBoxLayout(orientation='vertical')
        sent_layout.add_widget(MDLabel(
            text="今日发送",
            theme_text_color="Primary",
            font_style="Caption",
            halign="center"
        ))
        self.sent_count = MDLabel(
            text="0",
            theme_text_color="Primary",
            font_style="H5",
            halign="center"
        )
        sent_layout.add_widget(self.sent_count)
        layout.add_widget(sent_layout)
        
        # 成功率
        rate_layout = MDBoxLayout(orientation='vertical')
        rate_layout.add_widget(MDLabel(
            text="成功率",
            theme_text_color="Primary",
            font_style="Caption",
            halign="center"
        ))
        self.success_rate = MDLabel(
            text="100%",
            theme_text_color="Primary",
            font_style="H5",
            halign="center"
        )
        rate_layout.add_widget(self.success_rate)
        layout.add_widget(rate_layout)
        
        card.add_widget(layout)
        return card
    
    def create_control_buttons(self):
        """创建控制按钮"""
        layout = MDGridLayout(
            cols=2,
            spacing="16dp",
            size_hint_y=None,
            height="56dp"
        )
        
        # 立即运行按钮
        self.run_button = MDRaisedButton(
            text="立即运行",
            on_release=self.run_now
        )
        layout.add_widget(self.run_button)
        
        # 配置按钮
        config_button = MDRaisedButton(
            text="配置设置",
            on_release=self.open_config
        )
        layout.add_widget(config_button)
        
        return layout
    
    def create_log_card(self):
        """创建日志卡片"""
        card = MDCard(
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='vertical')
        
        # 日志标题
        log_title = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height="32dp"
        )
        log_title.add_widget(MDLabel(
            text="最近日志",
            theme_text_color="Primary",
            font_style="H6"
        ))
        log_title.add_widget(MDIconButton(
            icon="open-in-new",
            on_release=self.open_full_log
        ))
        layout.add_widget(log_title)
        
        # 日志列表
        self.log_list = MDList()
        layout.add_widget(self.log_list)
        
        card.add_widget(layout)
        return card
    
    def update_status(self, dt):
        """更新状态信息"""
        try:
            app = self.get_app()
            if app:
                # 更新运行状态
                scheduler = app.get_scheduler()
                if scheduler.is_scheduled():
                    self.status_text.text = "定时任务已启动"
                    self.is_running = True
                else:
                    self.status_text.text = "未运行"
                    self.is_running = False
                
                # 更新最后运行时间
                if self.last_run_time:
                    self.last_run_text.text = f"最后运行：{self.last_run_time.strftime('%Y-%m-%d %H:%M:%S')}"
                
                # 更新统计信息
                self.update_stats()
                
                # 更新日志
                self.update_recent_logs()
        except Exception as e:
            Logger.error(f"MainScreen: 更新状态失败: {e}")
    
    def update_stats(self):
        """更新统计信息"""
        try:
            # 这里应该从数据库获取今日统计
            # 暂时使用模拟数据
            self.processed_count.text = str(self.today_stats['processed'])
            self.sent_count.text = str(self.today_stats['sent'])
            
            # 计算成功率
            if self.today_stats['processed'] > 0:
                rate = (self.today_stats['sent'] / self.today_stats['processed']) * 100
                self.success_rate.text = f"{rate:.1f}%"
            else:
                self.success_rate.text = "100%"
        except Exception as e:
            Logger.error(f"MainScreen: 更新统计失败: {e}")
    
    def update_recent_logs(self):
        """更新最近日志"""
        try:
            # 清空现有日志
            self.log_list.clear_widgets()
            
            # 添加最近的日志条目（这里使用模拟数据）
            recent_logs = [
                ("2024-01-20 10:30:00", "成功处理3条消息"),
                ("2024-01-20 08:00:00", "定时任务启动"),
                ("2024-01-19 20:15:00", "发送每日汇总邮件")
            ]
            
            for timestamp, message in recent_logs[:5]:  # 只显示最近5条
                item = TwoLineListItem(
                    text=message,
                    secondary_text=timestamp
                )
                self.log_list.add_widget(item)
        except Exception as e:
            Logger.error(f"MainScreen: 更新日志失败: {e}")
    
    def get_app(self):
        """获取应用实例"""
        from kivy.app import App
        return App.get_running_app()
    
    def open_navigation(self):
        """打开导航菜单"""
        # 这里应该打开侧边导航栏
        pass
    
    def refresh_status(self):
        """刷新状态"""
        self.update_status(None)
    
    def run_now(self, button):
        """立即运行抓取任务"""
        try:
            Logger.info("MainScreen: 开始立即运行任务")
            button.text = "运行中..."
            button.disabled = True
            
            # 这里应该启动抓取任务
            # 暂时使用模拟
            Clock.schedule_once(lambda dt: self.run_complete(button), 3.0)
            
        except Exception as e:
            Logger.error(f"MainScreen: 立即运行失败: {e}")
            button.text = "立即运行"
            button.disabled = False
    
    def run_complete(self, button):
        """运行完成回调"""
        button.text = "立即运行"
        button.disabled = False
        self.last_run_time = datetime.now()
        
        # 更新统计（模拟）
        self.today_stats['processed'] += 3
        self.today_stats['sent'] += 2
        
        Logger.info("MainScreen: 任务运行完成")
    
    def open_config(self, button):
        """打开配置界面"""
        app = self.get_app()
        if app:
            app.switch_screen('config')
    
    def open_full_log(self, button):
        """打开完整日志界面"""
        app = self.get_app()
        if app:
            app.switch_screen('log')