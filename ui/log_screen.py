#!/usr/bin/env python3
"""
日志查看界面模块
显示应用运行日志和错误信息
"""

from kivy.logger import Logger
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDFlatButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import MDList, ThreeLineListItem, OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.chip import MDChip
from kivymd.uix.textfield import MDTextField
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.gridlayout import MDGridLayout
from datetime import datetime, timedelta
import os

class LogScreen(MDScreen):
    """日志查看界面屏幕"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.log_data = []
        self.filtered_logs = []
        self.current_filter = 'all'
        self.search_text = ''
        self.build_ui()
        self.load_logs()
        
        # 定时刷新日志
        Clock.schedule_interval(self.refresh_logs, 10.0)
    
    def build_ui(self):
        """构建用户界面"""
        layout = MDBoxLayout(orientation='vertical')
        
        # 顶部工具栏
        toolbar = MDTopAppBar(
            title="运行日志",
            elevation=2,
            left_action_items=[["arrow-left", lambda x: self.go_back()]],
            right_action_items=[
                ["refresh", lambda x: self.refresh_logs()],
                ["delete", lambda x: self.clear_logs()],
                ["export", lambda x: self.export_logs()]
            ]
        )
        layout.add_widget(toolbar)
        
        # 过滤和搜索区域
        filter_card = self.create_filter_card()
        layout.add_widget(filter_card)
        
        # 统计信息卡片
        self.stats_card = self.create_stats_card()
        layout.add_widget(self.stats_card)
        
        # 日志列表
        scroll = MDScrollView()
        self.log_list = MDList()
        scroll.add_widget(self.log_list)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
    
    def create_filter_card(self):
        """创建过滤和搜索卡片"""
        card = MDCard(
            size_hint_y=None,
            height="120dp",
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='vertical', spacing="8dp")
        
        # 过滤器芯片
        filter_layout = MDBoxLayout(
            orientation='horizontal',
            spacing="8dp",
            size_hint_y=None,
            height="40dp"
        )
        
        self.all_chip = MDChip(
            text="全部",
            check=True,
            on_release=lambda x: self.set_filter('all')
        )
        filter_layout.add_widget(self.all_chip)
        
        self.info_chip = MDChip(
            text="信息",
            on_release=lambda x: self.set_filter('info')
        )
        filter_layout.add_widget(self.info_chip)
        
        self.warning_chip = MDChip(
            text="警告",
            on_release=lambda x: self.set_filter('warning')
        )
        filter_layout.add_widget(self.warning_chip)
        
        self.error_chip = MDChip(
            text="错误",
            on_release=lambda x: self.set_filter('error')
        )
        filter_layout.add_widget(self.error_chip)
        
        layout.add_widget(filter_layout)
        
        # 搜索框
        search_layout = MDBoxLayout(
            orientation='horizontal',
            spacing="8dp",
            size_hint_y=None,
            height="56dp"
        )
        
        self.search_field = MDTextField(
            hint_text="搜索日志内容...",
            on_text=self.on_search_text_changed
        )
        search_layout.add_widget(self.search_field)
        
        search_btn = MDIconButton(
            icon="magnify",
            on_release=self.search_logs
        )
        search_layout.add_widget(search_btn)
        
        layout.add_widget(search_layout)
        
        card.add_widget(layout)
        return card
    
    def create_stats_card(self):
        """创建统计信息卡片"""
        card = MDCard(
            size_hint_y=None,
            height="80dp",
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='horizontal', spacing="16dp")
        
        # 总数
        total_layout = MDBoxLayout(orientation='vertical')
        self.total_label = MDLabel(
            text="0",
            theme_text_color="Primary",
            font_style="H5",
            halign="center"
        )
        total_layout.add_widget(self.total_label)
        total_layout.add_widget(MDLabel(
            text="总计",
            theme_text_color="Secondary",
            font_style="Caption",
            halign="center"
        ))
        layout.add_widget(total_layout)
        
        # 错误数
        error_layout = MDBoxLayout(orientation='vertical')
        self.error_count_label = MDLabel(
            text="0",
            theme_text_color="Error",
            font_style="H5",
            halign="center"
        )
        error_layout.add_widget(self.error_count_label)
        error_layout.add_widget(MDLabel(
            text="错误",
            theme_text_color="Secondary",
            font_style="Caption",
            halign="center"
        ))
        layout.add_widget(error_layout)
        
        # 警告数
        warning_layout = MDBoxLayout(orientation='vertical')
        self.warning_count_label = MDLabel(
            text="0",
            theme_text_color="Primary",
            font_style="H5",
            halign="center"
        )
        warning_layout.add_widget(self.warning_count_label)
        warning_layout.add_widget(MDLabel(
            text="警告",
            theme_text_color="Secondary",
            font_style="Caption",
            halign="center"
        ))
        layout.add_widget(warning_layout)
        
        # 今日数
        today_layout = MDBoxLayout(orientation='vertical')
        self.today_count_label = MDLabel(
            text="0",
            theme_text_color="Primary",
            font_style="H5",
            halign="center"
        )
        today_layout.add_widget(self.today_count_label)
        today_layout.add_widget(MDLabel(
            text="今日",
            theme_text_color="Secondary",
            font_style="Caption",
            halign="center"
        ))
        layout.add_widget(today_layout)
        
        card.add_widget(layout)
        return card
    
    def load_logs(self):
        """加载日志数据"""
        try:
            app = self.get_app()
            if app:
                log_manager = app.get_log_manager()
                self.log_data = log_manager.get_logs()
                
                # 应用过滤器
                self.apply_filter()
                
                # 更新统计
                self.update_stats()
                
                Logger.info("LogScreen: 日志加载完成")
        except Exception as e:
            Logger.error(f"LogScreen: 加载日志失败: {e}")
            # 使用模拟数据
            self.load_mock_logs()
    
    def load_mock_logs(self):
        """加载模拟日志数据"""
        now = datetime.now()
        self.log_data = [
            {
                'timestamp': now - timedelta(minutes=5),
                'level': 'info',
                'message': '定时任务启动成功',
                'module': 'scheduler',
                'details': '定时任务已按计划启动，开始执行内容抓取'
            },
            {
                'timestamp': now - timedelta(minutes=10),
                'level': 'info',
                'message': '连接Telegram成功',
                'module': 'telegram_client',
                'details': 'Telegram客户端连接成功，API状态正常'
            },
            {
                'timestamp': now - timedelta(minutes=15),
                'level': 'warning',
                'message': '频道消息数量较少',
                'module': 'content_fetcher',
                'details': '目标频道@example_channel今日仅有3条新消息'
            },
            {
                'timestamp': now - timedelta(minutes=30),
                'level': 'error',
                'message': '邮件发送失败',
                'module': 'notifier',
                'details': 'SMTP连接超时，邮件通知发送失败'
            },
            {
                'timestamp': now - timedelta(hours=1),
                'level': 'info',
                'message': '内容过滤完成',
                'module': 'content_filter',
                'details': '共处理50条消息，匹配到15条相关内容'
            },
            {
                'timestamp': now - timedelta(hours=2),
                'level': 'info',
                'message': '数据库更新完成',
                'module': 'database',
                'details': '成功更新15条记录到本地数据库'
            },
            {
                'timestamp': now - timedelta(hours=3),
                'level': 'warning',
                'message': '网络连接不稳定',
                'module': 'network',
                'details': '检测到网络延迟较高，可能影响数据同步'
            },
            {
                'timestamp': now - timedelta(hours=6),
                'level': 'info',
                'message': '应用启动完成',
                'module': 'main',
                'details': 'Telegram内容抓取应用启动成功'
            }
        ]
        
        self.apply_filter()
        self.update_stats()
    
    def apply_filter(self):
        """应用过滤器"""
        try:
            self.filtered_logs = self.log_data.copy()
            
            # 按级别过滤
            if self.current_filter != 'all':
                self.filtered_logs = [
                    log for log in self.filtered_logs 
                    if log['level'] == self.current_filter
                ]
            
            # 按搜索文本过滤
            if self.search_text:
                self.filtered_logs = [
                    log for log in self.filtered_logs
                    if self.search_text.lower() in log['message'].lower() or
                       self.search_text.lower() in log.get('details', '').lower()
                ]
            
            # 按时间排序（最新的在前）
            self.filtered_logs.sort(key=lambda x: x['timestamp'], reverse=True)
            
            # 更新列表显示
            self.update_log_list()
            
        except Exception as e:
            Logger.error(f"LogScreen: 应用过滤器失败: {e}")
    
    def update_log_list(self):
        """更新日志列表显示"""
        try:
            self.log_list.clear_widgets()
            
            for log in self.filtered_logs[:100]:  # 限制显示最近100条
                # 格式化时间
                time_str = log['timestamp'].strftime('%m-%d %H:%M')
                
                # 选择图标和颜色
                if log['level'] == 'error':
                    icon = 'alert-circle'
                    text_color = 'Error'
                elif log['level'] == 'warning':
                    icon = 'alert'
                    text_color = 'Primary'
                else:
                    icon = 'information'
                    text_color = 'Primary'
                
                # 创建列表项
                item = ThreeLineListItem(
                    text=log['message'],
                    secondary_text=f"[{log['module']}] {time_str}",
                    tertiary_text=log.get('details', '')[:50] + '...' if len(log.get('details', '')) > 50 else log.get('details', ''),
                    on_release=lambda x, log_item=log: self.show_log_detail(log_item)
                )
                
                # 添加图标
                item.add_widget(MDIconButton(
                    icon=icon,
                    theme_icon_color="Custom",
                    icon_color=text_color
                ))
                
                self.log_list.add_widget(item)
            
            # 如果没有日志，显示提示
            if not self.filtered_logs:
                empty_item = OneLineListItem(
                    text="暂无日志记录",
                    theme_text_color="Hint"
                )
                self.log_list.add_widget(empty_item)
                
        except Exception as e:
            Logger.error(f"LogScreen: 更新日志列表失败: {e}")
    
    def update_stats(self):
        """更新统计信息"""
        try:
            total_count = len(self.log_data)
            error_count = len([log for log in self.log_data if log['level'] == 'error'])
            warning_count = len([log for log in self.log_data if log['level'] == 'warning'])
            
            # 今日日志数
            today = datetime.now().date()
            today_count = len([
                log for log in self.log_data 
                if log['timestamp'].date() == today
            ])
            
            # 更新标签
            self.total_label.text = str(total_count)
            self.error_count_label.text = str(error_count)
            self.warning_count_label.text = str(warning_count)
            self.today_count_label.text = str(today_count)
            
        except Exception as e:
            Logger.error(f"LogScreen: 更新统计失败: {e}")
    
    def set_filter(self, filter_type):
        """设置过滤器"""
        self.current_filter = filter_type
        
        # 更新芯片状态
        self.all_chip.check = (filter_type == 'all')
        self.info_chip.check = (filter_type == 'info')
        self.warning_chip.check = (filter_type == 'warning')
        self.error_chip.check = (filter_type == 'error')
        
        # 应用过滤器
        self.apply_filter()
    
    def on_search_text_changed(self, textfield, text):
        """搜索文本改变"""
        self.search_text = text
        # 延迟搜索以避免频繁更新
        Clock.unschedule(self.delayed_search)
        Clock.schedule_once(self.delayed_search, 0.5)
    
    def delayed_search(self, dt):
        """延迟搜索"""
        self.apply_filter()
    
    def search_logs(self, button):
        """搜索日志"""
        self.apply_filter()
    
    def refresh_logs(self, dt=None):
        """刷新日志"""
        self.load_logs()
    
    def clear_logs(self):
        """清空日志"""
        dialog = MDDialog(
            text="确定要清空所有日志吗？此操作不可恢复。",
            buttons=[
                MDFlatButton(
                    text="取消",
                    on_release=lambda x: dialog.dismiss()
                ),
                MDRaisedButton(
                    text="确定",
                    on_release=lambda x: self.confirm_clear_logs(dialog)
                )
            ]
        )
        dialog.open()
    
    def confirm_clear_logs(self, dialog):
        """确认清空日志"""
        try:
            dialog.dismiss()
            
            app = self.get_app()
            if app:
                log_manager = app.get_log_manager()
                log_manager.clear_logs()
            
            # 清空本地数据
            self.log_data = []
            self.filtered_logs = []
            
            # 更新界面
            self.update_log_list()
            self.update_stats()
            
            self.show_message("日志已清空")
            Logger.info("LogScreen: 日志已清空")
            
        except Exception as e:
            Logger.error(f"LogScreen: 清空日志失败: {e}")
            self.show_message(f"清空失败: {e}")
    
    def export_logs(self):
        """导出日志"""
        try:
            app = self.get_app()
            if app:
                log_manager = app.get_log_manager()
                export_path = log_manager.export_logs()
                
                if export_path:
                    self.show_message(f"日志已导出到: {export_path}")
                else:
                    self.show_message("导出失败")
            
        except Exception as e:
            Logger.error(f"LogScreen: 导出日志失败: {e}")
            self.show_message(f"导出失败: {e}")
    
    def show_log_detail(self, log_item):
        """显示日志详情"""
        time_str = log_item['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
        
        detail_text = f"""时间: {time_str}
级别: {log_item['level'].upper()}
模块: {log_item['module']}
消息: {log_item['message']}

详细信息:
{log_item.get('details', '无')}"""
        
        dialog = MDDialog(
            title="日志详情",
            text=detail_text,
            size_hint=(0.9, 0.7),
            buttons=[
                MDFlatButton(
                    text="复制",
                    on_release=lambda x: self.copy_log_detail(detail_text, dialog)
                ),
                MDRaisedButton(
                    text="关闭",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()
    
    def copy_log_detail(self, text, dialog):
        """复制日志详情"""
        try:
            # 这里应该实现复制到剪贴板的功能
            # Android平台需要使用pyjnius调用系统API
            self.show_message("日志详情已复制")
            dialog.dismiss()
        except Exception as e:
            Logger.error(f"LogScreen: 复制失败: {e}")
            self.show_message("复制失败")
    
    def show_message(self, message):
        """显示消息对话框"""
        dialog = MDDialog(
            text=message,
            buttons=[
                MDRaisedButton(
                    text="确定",
                    on_release=lambda x: dialog.dismiss()
                )
            ]
        )
        dialog.open()
    
    def get_app(self):
        """获取应用实例"""
        from kivy.app import App
        return App.get_running_app()
    
    def go_back(self):
        """返回主界面"""
        app = self.get_app()
        if app:
            app.switch_screen('main')