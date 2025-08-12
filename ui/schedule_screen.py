#!/usr/bin/env python3
"""
定时任务配置界面模块
管理抓取任务的执行时间和频率设置
"""

from kivy.logger import Logger
from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import MDList, TwoLineListItem, OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.selectioncontrol import MDSwitch
from kivymd.uix.slider import MDSlider
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.chip import MDChip
from datetime import datetime, timedelta

class ScheduleScreen(MDScreen):
    """定时任务配置界面屏幕"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.schedule_config = {}
        self.selected_times = []
        self.build_ui()
        self.load_schedule_config()
        
        # 定时更新界面
        Clock.schedule_interval(self.update_status, 30.0)
    
    def build_ui(self):
        """构建用户界面"""
        layout = MDBoxLayout(orientation='vertical')
        
        # 顶部工具栏
        toolbar = MDTopAppBar(
            title="定时任务设置",
            elevation=2,
            left_action_items=[["arrow-left", lambda x: self.go_back()]],
            right_action_items=[["content-save", lambda x: self.save_schedule()]]
        )
        layout.add_widget(toolbar)
        
        # 滚动内容区域
        scroll = MDScrollView()
        content = MDBoxLayout(
            orientation='vertical',
            padding="16dp",
            spacing="16dp",
            size_hint_y=None
        )
        content.bind(minimum_height=content.setter('height'))
        
        # 任务状态卡片
        self.status_card = self.create_status_card()
        content.add_widget(self.status_card)
        
        # 基础设置卡片
        self.basic_card = self.create_basic_settings_card()
        content.add_widget(self.basic_card)
        
        # 时间设置卡片
        self.time_card = self.create_time_settings_card()
        content.add_widget(self.time_card)
        
        # 高级设置卡片
        self.advanced_card = self.create_advanced_settings_card()
        content.add_widget(self.advanced_card)
        
        # 控制按钮卡片
        self.control_card = self.create_control_card()
        content.add_widget(self.control_card)
        
        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)
    
    def create_status_card(self):
        """创建任务状态卡片"""
        card = MDCard(
            size_hint_y=None,
            height="120dp",
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='vertical', spacing="8dp")
        
        # 标题
        title = MDLabel(
            text="任务状态",
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height="32dp"
        )
        layout.add_widget(title)
        
        # 状态信息
        status_layout = MDBoxLayout(orientation='horizontal')
        
        # 当前状态
        self.status_label = MDLabel(
            text="状态: 未启动",
            theme_text_color="Secondary"
        )
        status_layout.add_widget(self.status_label)
        
        # 下次执行时间
        self.next_run_label = MDLabel(
            text="下次执行: --",
            theme_text_color="Secondary"
        )
        status_layout.add_widget(self.next_run_label)
        
        layout.add_widget(status_layout)
        
        # 最后执行时间
        self.last_run_label = MDLabel(
            text="最后执行: --",
            theme_text_color="Hint",
            font_style="Caption"
        )
        layout.add_widget(self.last_run_label)
        
        card.add_widget(layout)
        return card
    
    def create_basic_settings_card(self):
        """创建基础设置卡片"""
        card = MDCard(
            size_hint_y=None,
            height="200dp",
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='vertical', spacing="12dp")
        
        # 标题
        title = MDLabel(
            text="基础设置",
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height="32dp"
        )
        layout.add_widget(title)
        
        # 启用定时任务
        enable_layout = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height="48dp"
        )
        enable_layout.add_widget(MDLabel(
            text="启用定时任务",
            theme_text_color="Primary"
        ))
        self.enable_switch = MDSwitch(
            active=False,
            on_active=self.on_enable_changed
        )
        enable_layout.add_widget(self.enable_switch)
        layout.add_widget(enable_layout)
        
        # 执行间隔
        interval_layout = MDBoxLayout(orientation='vertical', spacing="8dp")
        interval_layout.add_widget(MDLabel(
            text="执行间隔 (小时)",
            theme_text_color="Primary",
            size_hint_y=None,
            height="24dp"
        ))
        
        self.interval_slider = MDSlider(
            min=1,
            max=24,
            value=24,
            step=1,
            size_hint_y=None,
            height="32dp"
        )
        interval_layout.add_widget(self.interval_slider)
        
        self.interval_label = MDLabel(
            text="24 小时",
            theme_text_color="Secondary",
            size_hint_y=None,
            height="24dp"
        )
        interval_layout.add_widget(self.interval_label)
        
        # 绑定滑块事件
        self.interval_slider.bind(value=self.on_interval_changed)
        
        layout.add_widget(interval_layout)
        
        card.add_widget(layout)
        return card
    
    def create_time_settings_card(self):
        """创建时间设置卡片"""
        card = MDCard(
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='vertical', spacing="12dp")
        
        # 标题和添加按钮
        title_layout = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height="32dp"
        )
        title_layout.add_widget(MDLabel(
            text="执行时间设置",
            theme_text_color="Primary",
            font_style="H6"
        ))
        title_layout.add_widget(MDIconButton(
            icon="plus",
            on_release=self.add_time_slot
        ))
        layout.add_widget(title_layout)
        
        # 时间模式选择
        mode_layout = MDBoxLayout(orientation='vertical', spacing="8dp")
        mode_layout.add_widget(MDLabel(
            text="执行模式",
            theme_text_color="Primary",
            size_hint_y=None,
            height="24dp"
        ))
        
        # 模式选项
        self.mode_chips = MDBoxLayout(
            orientation='horizontal',
            spacing="8dp",
            size_hint_y=None,
            height="40dp"
        )
        
        self.interval_chip = MDChip(
            text="间隔模式",
            check=True,
            on_release=lambda x: self.set_mode('interval')
        )
        self.mode_chips.add_widget(self.interval_chip)
        
        self.fixed_chip = MDChip(
            text="固定时间",
            on_release=lambda x: self.set_mode('fixed')
        )
        self.mode_chips.add_widget(self.fixed_chip)
        
        mode_layout.add_widget(self.mode_chips)
        layout.add_widget(mode_layout)
        
        # 时间列表
        self.time_list = MDList()
        layout.add_widget(self.time_list)
        
        # 添加时间输入
        time_input_layout = MDBoxLayout(
            orientation='horizontal',
            spacing="8dp",
            size_hint_y=None,
            height="56dp"
        )
        
        self.hour_field = MDTextField(
            hint_text="时",
            input_filter="int",
            size_hint_x=0.3
        )
        time_input_layout.add_widget(self.hour_field)
        
        time_input_layout.add_widget(MDLabel(
            text=":",
            size_hint_x=0.1
        ))
        
        self.minute_field = MDTextField(
            hint_text="分",
            input_filter="int",
            size_hint_x=0.3
        )
        time_input_layout.add_widget(self.minute_field)
        
        add_time_btn = MDIconButton(
            icon="plus",
            size_hint_x=0.3,
            on_release=self.add_time_from_input
        )
        time_input_layout.add_widget(add_time_btn)
        
        layout.add_widget(time_input_layout)
        
        card.add_widget(layout)
        return card
    
    def create_advanced_settings_card(self):
        """创建高级设置卡片"""
        card = MDCard(
            size_hint_y=None,
            height="280dp",
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='vertical', spacing="12dp")
        
        # 标题
        title = MDLabel(
            text="高级设置",
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height="32dp"
        )
        layout.add_widget(title)
        
        # 重试设置
        retry_layout = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height="48dp"
        )
        retry_layout.add_widget(MDLabel(
            text="失败时自动重试",
            theme_text_color="Primary"
        ))
        self.retry_switch = MDSwitch(active=True)
        retry_layout.add_widget(self.retry_switch)
        layout.add_widget(retry_layout)
        
        # 重试次数
        self.retry_count_field = MDTextField(
            hint_text="重试次数",
            text="3",
            helper_text="失败后重试的次数",
            helper_text_mode="persistent",
            input_filter="int"
        )
        layout.add_widget(self.retry_count_field)
        
        # 重试间隔
        self.retry_interval_field = MDTextField(
            hint_text="重试间隔(分钟)",
            text="30",
            helper_text="两次重试之间的间隔",
            helper_text_mode="persistent",
            input_filter="int"
        )
        layout.add_widget(self.retry_interval_field)
        
        # 网络检查
        network_layout = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height="48dp"
        )
        network_layout.add_widget(MDLabel(
            text="执行前检查网络",
            theme_text_color="Primary"
        ))
        self.network_check_switch = MDSwitch(active=True)
        network_layout.add_widget(self.network_check_switch)
        layout.add_widget(network_layout)
        
        # 电池优化提醒
        battery_layout = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height="48dp"
        )
        battery_layout.add_widget(MDLabel(
            text="电池优化提醒",
            theme_text_color="Primary"
        ))
        self.battery_reminder_switch = MDSwitch(active=True)
        battery_layout.add_widget(self.battery_reminder_switch)
        layout.add_widget(battery_layout)
        
        card.add_widget(layout)
        return card
    
    def create_control_card(self):
        """创建控制按钮卡片"""
        card = MDCard(
            size_hint_y=None,
            height="120dp",
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='vertical', spacing="12dp")
        
        # 标题
        title = MDLabel(
            text="任务控制",
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height="32dp"
        )
        layout.add_widget(title)
        
        # 控制按钮
        button_layout = MDBoxLayout(
            orientation='horizontal',
            spacing="16dp",
            size_hint_y=None,
            height="48dp"
        )
        
        self.start_button = MDRaisedButton(
            text="启动任务",
            md_bg_color=(0.2, 0.7, 0.3, 1),
            on_release=self.start_schedule
        )
        button_layout.add_widget(self.start_button)
        
        self.stop_button = MDRaisedButton(
            text="停止任务",
            md_bg_color=(0.8, 0.3, 0.3, 1),
            disabled=True,
            on_release=self.stop_schedule
        )
        button_layout.add_widget(self.stop_button)
        
        self.test_button = MDRaisedButton(
            text="立即执行",
            md_bg_color=(0.3, 0.5, 0.8, 1),
            on_release=self.test_run
        )
        button_layout.add_widget(self.test_button)
        
        layout.add_widget(button_layout)
        
        card.add_widget(layout)
        return card
    
    def load_schedule_config(self):
        """加载定时任务配置"""
        try:
            app = self.get_app()
            if app:
                scheduler = app.get_scheduler()
                self.schedule_config = scheduler.get_config()
                
                # 更新界面
                self.update_ui_from_config()
                
                Logger.info("ScheduleScreen: 定时任务配置加载完成")
        except Exception as e:
            Logger.error(f"ScheduleScreen: 加载配置失败: {e}")
    
    def update_ui_from_config(self):
        """根据配置更新界面"""
        try:
            # 基础设置
            self.enable_switch.active = self.schedule_config.get('enabled', False)
            interval = self.schedule_config.get('interval_hours', 24)
            self.interval_slider.value = interval
            self.interval_label.text = f"{int(interval)} 小时"
            
            # 高级设置
            self.retry_switch.active = self.schedule_config.get('auto_retry', True)
            self.retry_count_field.text = str(self.schedule_config.get('retry_count', 3))
            self.retry_interval_field.text = str(self.schedule_config.get('retry_interval_minutes', 30))
            self.network_check_switch.active = self.schedule_config.get('check_network', True)
            self.battery_reminder_switch.active = self.schedule_config.get('battery_reminder', True)
            
            # 更新时间列表
            self.load_time_slots()
            
            # 更新按钮状态
            self.update_button_states()
            
        except Exception as e:
            Logger.error(f"ScheduleScreen: 更新界面失败: {e}")
    
    def load_time_slots(self):
        """加载时间段列表"""
        try:
            self.time_list.clear_widgets()
            time_slots = self.schedule_config.get('time_slots', [])
            
            for time_slot in time_slots:
                item = TwoLineListItem(
                    text=f"{time_slot['hour']:02d}:{time_slot['minute']:02d}",
                    secondary_text="执行时间",
                    on_release=lambda x, ts=time_slot: self.edit_time_slot(ts)
                )
                # 添加删除按钮
                delete_btn = MDIconButton(
                    icon="delete",
                    on_release=lambda x, ts=time_slot: self.remove_time_slot(ts)
                )
                item.add_widget(delete_btn)
                self.time_list.add_widget(item)
        except Exception as e:
            Logger.error(f"ScheduleScreen: 加载时间段失败: {e}")
    
    def save_schedule(self):
        """保存定时任务配置"""
        try:
            # 收集配置数据
            config_data = {
                'enabled': self.enable_switch.active,
                'interval_hours': int(self.interval_slider.value),
                'auto_retry': self.retry_switch.active,
                'retry_count': int(self.retry_count_field.text) if self.retry_count_field.text else 3,
                'retry_interval_minutes': int(self.retry_interval_field.text) if self.retry_interval_field.text else 30,
                'check_network': self.network_check_switch.active,
                'battery_reminder': self.battery_reminder_switch.active,
                'time_slots': self.schedule_config.get('time_slots', [])
            }
            
            # 保存配置
            app = self.get_app()
            if app:
                scheduler = app.get_scheduler()
                scheduler.save_config(config_data)
                
            Logger.info("ScheduleScreen: 定时任务配置保存成功")
            self.show_message("配置保存成功")
            
        except Exception as e:
            Logger.error(f"ScheduleScreen: 保存配置失败: {e}")
            self.show_message(f"保存失败: {e}")
    
    def on_enable_changed(self, switch, value):
        """启用状态改变"""
        self.update_button_states()
    
    def on_interval_changed(self, slider, value):
        """间隔时间改变"""
        self.interval_label.text = f"{int(value)} 小时"
    
    def set_mode(self, mode):
        """设置执行模式"""
        if mode == 'interval':
            self.interval_chip.check = True
            self.fixed_chip.check = False
        else:
            self.interval_chip.check = False
            self.fixed_chip.check = True
    
    def add_time_slot(self, button):
        """添加时间段"""
        # 显示时间选择对话框
        self.show_time_picker()
    
    def add_time_from_input(self, button):
        """从输入框添加时间"""
        try:
            hour = int(self.hour_field.text) if self.hour_field.text else 0
            minute = int(self.minute_field.text) if self.minute_field.text else 0
            
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                time_slot = {'hour': hour, 'minute': minute}
                
                # 添加到配置
                if 'time_slots' not in self.schedule_config:
                    self.schedule_config['time_slots'] = []
                
                # 检查是否已存在
                exists = any(ts['hour'] == hour and ts['minute'] == minute 
                           for ts in self.schedule_config['time_slots'])
                
                if not exists:
                    self.schedule_config['time_slots'].append(time_slot)
                    self.load_time_slots()
                    self.hour_field.text = ""
                    self.minute_field.text = ""
                    Logger.info(f"ScheduleScreen: 添加时间段 {hour:02d}:{minute:02d}")
                else:
                    self.show_message("该时间已存在")
            else:
                self.show_message("请输入有效的时间 (0-23:0-59)")
                
        except ValueError:
            self.show_message("请输入有效的数字")
    
    def remove_time_slot(self, time_slot):
        """删除时间段"""
        if 'time_slots' in self.schedule_config:
            self.schedule_config['time_slots'] = [
                ts for ts in self.schedule_config['time_slots']
                if not (ts['hour'] == time_slot['hour'] and ts['minute'] == time_slot['minute'])
            ]
            self.load_time_slots()
            Logger.info(f"ScheduleScreen: 删除时间段 {time_slot['hour']:02d}:{time_slot['minute']:02d}")
    
    def start_schedule(self, button):
        """启动定时任务"""
        try:
            app = self.get_app()
            if app:
                scheduler = app.get_scheduler()
                scheduler.start()
                
                self.update_button_states()
                self.show_message("定时任务已启动")
                Logger.info("ScheduleScreen: 定时任务启动")
                
        except Exception as e:
            Logger.error(f"ScheduleScreen: 启动任务失败: {e}")
            self.show_message(f"启动失败: {e}")
    
    def stop_schedule(self, button):
        """停止定时任务"""
        try:
            app = self.get_app()
            if app:
                scheduler = app.get_scheduler()
                scheduler.stop()
                
                self.update_button_states()
                self.show_message("定时任务已停止")
                Logger.info("ScheduleScreen: 定时任务停止")
                
        except Exception as e:
            Logger.error(f"ScheduleScreen: 停止任务失败: {e}")
            self.show_message(f"停止失败: {e}")
    
    def test_run(self, button):
        """立即执行测试"""
        try:
            button.text = "执行中..."
            button.disabled = True
            
            app = self.get_app()
            if app:
                # 这里应该调用实际的抓取任务
                # 暂时使用模拟
                Clock.schedule_once(lambda dt: self.test_run_complete(button), 3.0)
                
        except Exception as e:
            Logger.error(f"ScheduleScreen: 测试执行失败: {e}")
            button.text = "立即执行"
            button.disabled = False
    
    def test_run_complete(self, button):
        """测试执行完成"""
        button.text = "立即执行"
        button.disabled = False
        self.show_message("测试执行完成")
    
    def update_button_states(self):
        """更新按钮状态"""
        try:
            app = self.get_app()
            if app:
                scheduler = app.get_scheduler()
                is_running = scheduler.is_running()
                
                self.start_button.disabled = is_running or not self.enable_switch.active
                self.stop_button.disabled = not is_running
                
        except Exception as e:
            Logger.error(f"ScheduleScreen: 更新按钮状态失败: {e}")
    
    def update_status(self, dt):
        """更新状态信息"""
        try:
            app = self.get_app()
            if app:
                scheduler = app.get_scheduler()
                
                # 更新状态
                if scheduler.is_running():
                    self.status_label.text = "状态: 运行中"
                else:
                    self.status_label.text = "状态: 已停止"
                
                # 更新下次执行时间
                next_run = scheduler.get_next_run_time()
                if next_run:
                    self.next_run_label.text = f"下次执行: {next_run.strftime('%H:%M')}"
                else:
                    self.next_run_label.text = "下次执行: --"
                
                # 更新最后执行时间
                last_run = scheduler.get_last_run_time()
                if last_run:
                    self.last_run_label.text = f"最后执行: {last_run.strftime('%m-%d %H:%M')}"
                else:
                    self.last_run_label.text = "最后执行: --"
                
        except Exception as e:
            Logger.error(f"ScheduleScreen: 更新状态失败: {e}")
    
    def show_time_picker(self):
        """显示时间选择器"""
        # 这里可以实现一个时间选择对话框
        # 暂时使用简单的输入提示
        self.show_message("请在下方输入框中输入时间")
    
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
    
    def edit_time_slot(self, time_slot):
        """编辑时间段"""
        # 这里可以实现时间段编辑功能
        pass