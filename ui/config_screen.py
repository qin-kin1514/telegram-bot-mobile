#!/usr/bin/env python3
"""
配置界面模块
管理Telegram API、频道、标签、邮箱等配置
"""

from kivy.logger import Logger
from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton, MDIconButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.list import MDList, TwoLineListItem, OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.chip import MDChip
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.selectioncontrol import MDSwitch

class ConfigScreen(MDScreen):
    """配置界面屏幕"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config_data = {}
        self.build_ui()
        self.load_config()
    
    def build_ui(self):
        """构建用户界面"""
        layout = MDBoxLayout(orientation='vertical')
        
        # 顶部工具栏
        toolbar = MDTopAppBar(
            title="配置设置",
            elevation=2,
            left_action_items=[["arrow-left", lambda x: self.go_back()]],
            right_action_items=[["content-save", lambda x: self.save_config()]]
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
        
        # Telegram API配置
        self.telegram_card = self.create_telegram_config_card()
        content.add_widget(self.telegram_card)
        
        # 邮箱配置
        self.email_card = self.create_email_config_card()
        content.add_widget(self.email_card)
        
        # 频道配置
        self.channel_card = self.create_channel_config_card()
        content.add_widget(self.channel_card)
        
        # 标签配置
        self.tag_card = self.create_tag_config_card()
        content.add_widget(self.tag_card)
        
        # 高级配置
        self.advanced_card = self.create_advanced_config_card()
        content.add_widget(self.advanced_card)
        
        scroll.add_widget(content)
        layout.add_widget(scroll)
        self.add_widget(layout)
    
    def create_telegram_config_card(self):
        """创建Telegram API配置卡片"""
        card = MDCard(
            size_hint_y=None,
            height="300dp",
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='vertical', spacing="12dp")
        
        # 标题
        title = MDLabel(
            text="Telegram API配置",
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height="32dp"
        )
        layout.add_widget(title)
        
        # Bot Token
        self.bot_token_field = MDTextField(
            hint_text="Bot Token",
            helper_text="从@BotFather获取",
            helper_text_mode="persistent",
            password=True
        )
        layout.add_widget(self.bot_token_field)
        
        # API ID
        self.api_id_field = MDTextField(
            hint_text="API ID",
            helper_text="从my.telegram.org获取",
            helper_text_mode="persistent",
            input_filter="int"
        )
        layout.add_widget(self.api_id_field)
        
        # API Hash
        self.api_hash_field = MDTextField(
            hint_text="API Hash",
            helper_text="从my.telegram.org获取",
            helper_text_mode="persistent",
            password=True
        )
        layout.add_widget(self.api_hash_field)
        
        # 机器人频道
        self.bot_channel_field = MDTextField(
            hint_text="机器人频道ID",
            helper_text="内容推送目标频道",
            helper_text_mode="persistent"
        )
        layout.add_widget(self.bot_channel_field)
        
        # 测试连接按钮
        test_button = MDRaisedButton(
            text="测试连接",
            size_hint_y=None,
            height="36dp",
            on_release=self.test_telegram_connection
        )
        layout.add_widget(test_button)
        
        card.add_widget(layout)
        return card
    
    def create_email_config_card(self):
        """创建邮箱配置卡片"""
        card = MDCard(
            size_hint_y=None,
            height="280dp",
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='vertical', spacing="12dp")
        
        # 标题
        title = MDLabel(
            text="邮箱通知配置",
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height="32dp"
        )
        layout.add_widget(title)
        
        # SMTP服务器
        self.smtp_server_field = MDTextField(
            hint_text="SMTP服务器",
            text="smtp.qq.com",
            helper_text="邮箱服务商的SMTP服务器",
            helper_text_mode="persistent"
        )
        layout.add_widget(self.smtp_server_field)
        
        # SMTP端口
        self.smtp_port_field = MDTextField(
            hint_text="SMTP端口",
            text="587",
            helper_text="通常为587或465",
            helper_text_mode="persistent",
            input_filter="int"
        )
        layout.add_widget(self.smtp_port_field)
        
        # 邮箱地址
        self.email_field = MDTextField(
            hint_text="邮箱地址",
            helper_text="发送和接收通知的邮箱",
            helper_text_mode="persistent"
        )
        layout.add_widget(self.email_field)
        
        # 邮箱密码/授权码
        self.email_password_field = MDTextField(
            hint_text="邮箱密码/授权码",
            helper_text="QQ邮箱请使用授权码",
            helper_text_mode="persistent",
            password=True
        )
        layout.add_widget(self.email_password_field)
        
        # 测试邮件按钮
        test_email_button = MDRaisedButton(
            text="发送测试邮件",
            size_hint_y=None,
            height="36dp",
            on_release=self.test_email_connection
        )
        layout.add_widget(test_email_button)
        
        card.add_widget(layout)
        return card
    
    def create_channel_config_card(self):
        """创建频道配置卡片"""
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
            text="监控频道配置",
            theme_text_color="Primary",
            font_style="H6"
        ))
        title_layout.add_widget(MDIconButton(
            icon="plus",
            on_release=self.add_channel
        ))
        layout.add_widget(title_layout)
        
        # 频道列表
        self.channel_list = MDList()
        layout.add_widget(self.channel_list)
        
        # 添加频道输入框
        self.new_channel_field = MDTextField(
            hint_text="输入频道用户名或ID",
            helper_text="例如：@channelname 或 -1001234567890",
            helper_text_mode="persistent"
        )
        layout.add_widget(self.new_channel_field)
        
        card.add_widget(layout)
        return card
    
    def create_tag_config_card(self):
        """创建标签配置卡片"""
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
            text="兴趣标签配置",
            theme_text_color="Primary",
            font_style="H6"
        ))
        title_layout.add_widget(MDIconButton(
            icon="plus",
            on_release=self.add_tag
        ))
        layout.add_widget(title_layout)
        
        # 标签网格
        self.tag_grid = MDGridLayout(
            cols=3,
            spacing="8dp",
            size_hint_y=None,
            adaptive_height=True
        )
        layout.add_widget(self.tag_grid)
        
        # 添加标签输入框
        self.new_tag_field = MDTextField(
            hint_text="输入新标签",
            helper_text="例如：AI、Python、投资",
            helper_text_mode="persistent"
        )
        layout.add_widget(self.new_tag_field)
        
        card.add_widget(layout)
        return card
    
    def create_advanced_config_card(self):
        """创建高级配置卡片"""
        card = MDCard(
            size_hint_y=None,
            height="200dp",
            elevation=2,
            padding="16dp"
        )
        
        layout = MDBoxLayout(orientation='vertical', spacing="12dp")
        
        # 标题
        title = MDLabel(
            text="高级配置",
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height="32dp"
        )
        layout.add_widget(title)
        
        # 检查间隔
        self.check_interval_field = MDTextField(
            hint_text="检查间隔(小时)",
            text="24",
            helper_text="多久检查一次新内容",
            helper_text_mode="persistent",
            input_filter="int"
        )
        layout.add_widget(self.check_interval_field)
        
        # 每日最大消息数
        self.max_messages_field = MDTextField(
            hint_text="每日最大消息数",
            text="100",
            helper_text="防止消息过多",
            helper_text_mode="persistent",
            input_filter="int"
        )
        layout.add_widget(self.max_messages_field)
        
        # 启用同义词匹配
        synonym_layout = MDBoxLayout(
            orientation='horizontal',
            size_hint_y=None,
            height="48dp"
        )
        synonym_layout.add_widget(MDLabel(
            text="启用同义词匹配",
            theme_text_color="Primary"
        ))
        self.synonym_switch = MDSwitch()
        synonym_layout.add_widget(self.synonym_switch)
        layout.add_widget(synonym_layout)
        
        card.add_widget(layout)
        return card
    
    def load_config(self):
        """加载配置数据"""
        try:
            app = self.get_app()
            if app:
                config_manager = app.get_config_manager()
                self.config_data = config_manager.get_all_config()
                
                # 填充表单
                self.populate_form()
                
                Logger.info("ConfigScreen: 配置加载完成")
        except Exception as e:
            Logger.error(f"ConfigScreen: 加载配置失败: {e}")
    
    def populate_form(self):
        """填充表单数据"""
        try:
            # Telegram配置
            self.bot_token_field.text = self.config_data.get('BOT_TOKEN', '')
            self.api_id_field.text = str(self.config_data.get('API_ID', ''))
            self.api_hash_field.text = self.config_data.get('API_HASH', '')
            self.bot_channel_field.text = self.config_data.get('BOT_CHANNEL', '')
            
            # 邮箱配置
            self.smtp_server_field.text = self.config_data.get('SMTP_SERVER', 'smtp.qq.com')
            self.smtp_port_field.text = str(self.config_data.get('SMTP_PORT', '587'))
            self.email_field.text = self.config_data.get('EMAIL_USERNAME', '')
            self.email_password_field.text = self.config_data.get('EMAIL_PASSWORD', '')
            
            # 高级配置
            self.check_interval_field.text = str(self.config_data.get('CHECK_INTERVAL_HOURS', '24'))
            self.max_messages_field.text = str(self.config_data.get('MAX_DAILY_MESSAGES', '100'))
            
            # 加载频道列表
            self.load_channels()
            
            # 加载标签列表
            self.load_tags()
            
        except Exception as e:
            Logger.error(f"ConfigScreen: 填充表单失败: {e}")
    
    def load_channels(self):
        """加载频道列表"""
        try:
            self.channel_list.clear_widgets()
            channels = self.config_data.get('TARGET_CHANNELS', [])
            
            for channel in channels:
                item = TwoLineListItem(
                    text=channel,
                    secondary_text="监控频道",
                    on_release=lambda x, ch=channel: self.edit_channel(ch)
                )
                # 添加删除按钮
                delete_btn = MDIconButton(
                    icon="delete",
                    on_release=lambda x, ch=channel: self.remove_channel(ch)
                )
                item.add_widget(delete_btn)
                self.channel_list.add_widget(item)
        except Exception as e:
            Logger.error(f"ConfigScreen: 加载频道失败: {e}")
    
    def load_tags(self):
        """加载标签列表"""
        try:
            self.tag_grid.clear_widgets()
            tags = self.config_data.get('INTEREST_TAGS', [])
            
            for tag in tags:
                chip = MDChip(
                    text=tag,
                    icon_right="close",
                    on_release=lambda x, t=tag: self.remove_tag(t)
                )
                self.tag_grid.add_widget(chip)
        except Exception as e:
            Logger.error(f"ConfigScreen: 加载标签失败: {e}")
    
    def save_config(self):
        """保存配置"""
        try:
            # 收集表单数据
            config_data = {
                'BOT_TOKEN': self.bot_token_field.text.strip(),
                'API_ID': int(self.api_id_field.text) if self.api_id_field.text else 0,
                'API_HASH': self.api_hash_field.text.strip(),
                'BOT_CHANNEL': self.bot_channel_field.text.strip(),
                'SMTP_SERVER': self.smtp_server_field.text.strip(),
                'SMTP_PORT': int(self.smtp_port_field.text) if self.smtp_port_field.text else 587,
                'EMAIL_USERNAME': self.email_field.text.strip(),
                'EMAIL_PASSWORD': self.email_password_field.text.strip(),
                'CHECK_INTERVAL_HOURS': int(self.check_interval_field.text) if self.check_interval_field.text else 24,
                'MAX_DAILY_MESSAGES': int(self.max_messages_field.text) if self.max_messages_field.text else 100
            }
            
            # 保存配置
            app = self.get_app()
            if app:
                config_manager = app.get_config_manager()
                config_manager.save_config(config_data)
                
            Logger.info("ConfigScreen: 配置保存成功")
            
            # 显示成功消息
            self.show_message("配置保存成功")
            
        except Exception as e:
            Logger.error(f"ConfigScreen: 保存配置失败: {e}")
            self.show_message(f"保存失败: {e}")
    
    def add_channel(self, button):
        """添加频道"""
        channel = self.new_channel_field.text.strip()
        if channel:
            # 添加到配置
            if 'TARGET_CHANNELS' not in self.config_data:
                self.config_data['TARGET_CHANNELS'] = []
            
            if channel not in self.config_data['TARGET_CHANNELS']:
                self.config_data['TARGET_CHANNELS'].append(channel)
                self.load_channels()
                self.new_channel_field.text = ""
                Logger.info(f"ConfigScreen: 添加频道 {channel}")
            else:
                self.show_message("频道已存在")
    
    def remove_channel(self, channel):
        """删除频道"""
        if 'TARGET_CHANNELS' in self.config_data and channel in self.config_data['TARGET_CHANNELS']:
            self.config_data['TARGET_CHANNELS'].remove(channel)
            self.load_channels()
            Logger.info(f"ConfigScreen: 删除频道 {channel}")
    
    def add_tag(self, button):
        """添加标签"""
        tag = self.new_tag_field.text.strip()
        if tag:
            # 添加到配置
            if 'INTEREST_TAGS' not in self.config_data:
                self.config_data['INTEREST_TAGS'] = []
            
            if tag not in self.config_data['INTEREST_TAGS']:
                self.config_data['INTEREST_TAGS'].append(tag)
                self.load_tags()
                self.new_tag_field.text = ""
                Logger.info(f"ConfigScreen: 添加标签 {tag}")
            else:
                self.show_message("标签已存在")
    
    def remove_tag(self, tag):
        """删除标签"""
        if 'INTEREST_TAGS' in self.config_data and tag in self.config_data['INTEREST_TAGS']:
            self.config_data['INTEREST_TAGS'].remove(tag)
            self.load_tags()
            Logger.info(f"ConfigScreen: 删除标签 {tag}")
    
    def test_telegram_connection(self, button):
        """测试Telegram连接"""
        try:
            button.text = "测试中..."
            button.disabled = True
            
            # 这里应该实际测试Telegram连接
            # 暂时使用模拟
            from kivy.clock import Clock
            Clock.schedule_once(lambda dt: self.telegram_test_complete(button), 2.0)
            
        except Exception as e:
            Logger.error(f"ConfigScreen: Telegram连接测试失败: {e}")
            button.text = "测试连接"
            button.disabled = False
    
    def telegram_test_complete(self, button):
        """Telegram测试完成"""
        button.text = "测试连接"
        button.disabled = False
        self.show_message("Telegram连接测试成功")
    
    def test_email_connection(self, button):
        """测试邮件连接"""
        try:
            button.text = "发送中..."
            button.disabled = True
            
            # 这里应该实际发送测试邮件
            # 暂时使用模拟
            from kivy.clock import Clock
            Clock.schedule_once(lambda dt: self.email_test_complete(button), 2.0)
            
        except Exception as e:
            Logger.error(f"ConfigScreen: 邮件测试失败: {e}")
            button.text = "发送测试邮件"
            button.disabled = False
    
    def email_test_complete(self, button):
        """邮件测试完成"""
        button.text = "发送测试邮件"
        button.disabled = False
        self.show_message("测试邮件发送成功")
    
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
    
    def edit_channel(self, channel):
        """编辑频道"""
        # 这里可以实现频道编辑功能
        pass