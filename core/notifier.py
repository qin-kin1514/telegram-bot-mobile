#!/usr/bin/env python3
"""
邮件通知模块 - Android适配版本
处理邮件发送功能，适配Android环境
"""

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from kivy.logger import Logger

from .config import android_config
from .database import android_db_manager

class AndroidEmailNotifier:
    """Android适配的邮件通知器"""
    
    def __init__(self):
        """初始化邮件通知器"""
        self.smtp_server = None
        self.is_connected = False
    
    def _get_email_config(self) -> Dict[str, Any]:
        """获取邮件配置"""
        return {
            'smtp_server': android_config.get('SMTP_SERVER', 'smtp.gmail.com'),
            'smtp_port': android_config.get('SMTP_PORT', 587),
            'username': android_config.get('EMAIL_USERNAME', ''),
            'password': android_config.get('EMAIL_PASSWORD', ''),
            'to_email': android_config.get('EMAIL_TO', '')
        }
    
    def _validate_config(self) -> bool:
        """验证邮件配置"""
        config = self._get_email_config()
        required_fields = ['smtp_server', 'smtp_port', 'username', 'password', 'to_email']
        
        for field in required_fields:
            if not config.get(field):
                Logger.error(f"AndroidEmailNotifier: 邮件配置缺失 - {field}")
                return False
        
        return True
    
    def _connect_smtp(self) -> bool:
        """连接SMTP服务器"""
        try:
            if not self._validate_config():
                return False
            
            config = self._get_email_config()
            
            # 创建SMTP连接
            self.smtp_server = smtplib.SMTP(config['smtp_server'], config['smtp_port'])
            self.smtp_server.starttls(context=ssl.create_default_context())
            self.smtp_server.login(config['username'], config['password'])
            
            self.is_connected = True
            Logger.info("AndroidEmailNotifier: SMTP连接成功")
            return True
            
        except Exception as e:
            Logger.error(f"AndroidEmailNotifier: SMTP连接失败 - {e}")
            self.is_connected = False
            return False
    
    def _disconnect_smtp(self):
        """断开SMTP连接"""
        try:
            if self.smtp_server and self.is_connected:
                self.smtp_server.quit()
                self.is_connected = False
                Logger.info("AndroidEmailNotifier: SMTP连接已断开")
        except Exception as e:
            Logger.error(f"AndroidEmailNotifier: 断开SMTP连接失败 - {e}")
    
    def send_email(self, subject: str, body: str, is_html: bool = False) -> bool:
        """发送邮件"""
        try:
            if not self._connect_smtp():
                return False
            
            config = self._get_email_config()
            
            # 创建邮件消息
            message = MIMEMultipart('alternative')
            message['Subject'] = subject
            message['From'] = config['username']
            message['To'] = config['to_email']
            
            # 添加邮件内容
            if is_html:
                html_part = MIMEText(body, 'html', 'utf-8')
                message.attach(html_part)
            else:
                text_part = MIMEText(body, 'plain', 'utf-8')
                message.attach(text_part)
            
            # 发送邮件
            self.smtp_server.send_message(message)
            
            Logger.info(f"AndroidEmailNotifier: 邮件发送成功 - {subject}")
            return True
            
        except Exception as e:
            Logger.error(f"AndroidEmailNotifier: 邮件发送失败 - {e}")
            return False
        finally:
            self._disconnect_smtp()
    
    def send_daily_summary(self, date: Optional[str] = None) -> bool:
        """发送每日汇总邮件"""
        try:
            if date is None:
                date = datetime.now().strftime('%Y-%m-%d')
            
            # 获取统计数据
            stats = android_db_manager.get_daily_stats(date)
            
            # 获取最近的消息
            recent_messages = self._get_recent_messages(date)
            
            # 构建邮件内容
            subject = f"Telegram内容机器人 - 每日汇总 ({date})"
            body = self._build_summary_content(date, stats, recent_messages)
            
            return self.send_email(subject, body, is_html=True)
            
        except Exception as e:
            Logger.error(f"AndroidEmailNotifier: 发送每日汇总失败 - {e}")
            return False
    
    def _get_recent_messages(self, date: str, limit: int = 10) -> List[Dict[str, Any]]:
        """获取最近的消息"""
        try:
            # 这里应该从数据库获取最近的消息
            # 由于数据库模块的限制，我们使用模拟数据
            return [
                {
                    'channel_name': '示例频道1',
                    'content': '这是一条示例消息内容...',
                    'tags': ['AI', 'Python'],
                    'processed_at': datetime.now().strftime('%H:%M:%S')
                },
                {
                    'channel_name': '示例频道2',
                    'content': '另一条示例消息内容...',
                    'tags': ['投资', '理财'],
                    'processed_at': datetime.now().strftime('%H:%M:%S')
                }
            ]
        except Exception as e:
            Logger.error(f"AndroidEmailNotifier: 获取最近消息失败 - {e}")
            return []
    
    def _build_summary_content(self, date: str, stats: Dict[str, Any], 
                             recent_messages: List[Dict[str, Any]]) -> str:
        """构建汇总邮件内容"""
        try:
            html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 20px;
        }}
        .stat-card {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #667eea;
            text-align: center;
        }}
        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
        }}
        .stat-label {{
            color: #666;
            margin-top: 5px;
        }}
        .messages {{
            background: #fff;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .message-item {{
            border-bottom: 1px solid #eee;
            padding: 15px 0;
        }}
        .message-item:last-child {{
            border-bottom: none;
        }}
        .message-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}
        .channel-name {{
            font-weight: bold;
            color: #667eea;
        }}
        .message-time {{
            color: #999;
            font-size: 0.9em;
        }}
        .message-content {{
            margin-bottom: 10px;
            line-height: 1.5;
        }}
        .tags {{
            display: flex;
            gap: 5px;
            flex-wrap: wrap;
        }}
        .tag {{
            background: #e3f2fd;
            color: #1976d2;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.8em;
        }}
        .footer {{
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            background: #f8f9fa;
            border-radius: 8px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>📱 Telegram内容机器人</h1>
        <h2>每日汇总报告</h2>
        <p>{date}</p>
    </div>
    
    <div class="stats">
        <div class="stat-card">
            <div class="stat-number">{stats.get('processed_count', 0)}</div>
            <div class="stat-label">处理消息数</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{stats.get('sent_count', 0)}</div>
            <div class="stat-label">发送消息数</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{stats.get('error_count', 0)}</div>
            <div class="stat-label">错误次数</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{stats.get('success_rate', 0)}%</div>
            <div class="stat-label">成功率</div>
        </div>
    </div>
    
    <div class="messages">
        <h3>📋 最近处理的消息</h3>
        """
            
            if recent_messages:
                for message in recent_messages:
                    tags_html = ''.join([f'<span class="tag">{tag}</span>' for tag in message.get('tags', [])])
                    
                    html_content += f"""
        <div class="message-item">
            <div class="message-header">
                <span class="channel-name">📺 {message.get('channel_name', '未知频道')}</span>
                <span class="message-time">⏰ {message.get('processed_at', '')}</span>
            </div>
            <div class="message-content">
                {message.get('content', '')[:200]}{'...' if len(message.get('content', '')) > 200 else ''}
            </div>
            <div class="tags">
                {tags_html}
            </div>
        </div>
                    """
            else:
                html_content += """
        <div class="message-item">
            <p style="text-align: center; color: #999;">今日暂无处理的消息</p>
        </div>
                """
            
            html_content += f"""
    </div>
    
    <div class="footer">
        <p>🤖 此邮件由 Telegram内容机器人 自动发送</p>
        <p>📱 Android移动端版本 | 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
</body>
</html>
            """
            
            return html_content
            
        except Exception as e:
            Logger.error(f"AndroidEmailNotifier: 构建邮件内容失败 - {e}")
            return f"构建邮件内容时发生错误: {str(e)}"
    
    def send_new_content_notification(self, messages: List[Dict[str, Any]]) -> bool:
        """发送新内容通知"""
        try:
            if not messages:
                return True
            
            subject = f"🔔 Telegram新内容通知 ({len(messages)}条)"
            body = self._build_notification_content(messages)
            
            return self.send_email(subject, body, is_html=True)
            
        except Exception as e:
            Logger.error(f"AndroidEmailNotifier: 发送新内容通知失败 - {e}")
            return False
    
    def _build_notification_content(self, messages: List[Dict[str, Any]]) -> str:
        """构建新内容通知邮件内容"""
        try:
            html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        .header {{
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
        }}
        .message-item {{
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        .message-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
            padding-bottom: 10px;
            border-bottom: 1px solid #eee;
        }}
        .channel-name {{
            font-weight: bold;
            color: #ff6b6b;
        }}
        .message-time {{
            color: #999;
            font-size: 0.9em;
        }}
        .message-content {{
            margin-bottom: 10px;
            line-height: 1.5;
        }}
        .tags {{
            display: flex;
            gap: 5px;
            flex-wrap: wrap;
        }}
        .tag {{
            background: #ffe8e8;
            color: #d63031;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.8em;
        }}
        .footer {{
            text-align: center;
            margin-top: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🔔 新内容通知</h1>
        <p>发现 {len(messages)} 条新消息</p>
    </div>
            """
            
            for message in messages:
                tags_html = ''.join([f'<span class="tag">{tag}</span>' for tag in message.get('tags', [])])
                
                html_content += f"""
    <div class="message-item">
        <div class="message-header">
            <span class="channel-name">📺 {message.get('channel_name', '未知频道')}</span>
            <span class="message-time">⏰ {message.get('processed_at', '')}</span>
        </div>
        <div class="message-content">
            {message.get('content', '')}
        </div>
        <div class="tags">
            {tags_html}
        </div>
    </div>
                """
            
            html_content += f"""
    <div class="footer">
        <p>🤖 此邮件由 Telegram内容机器人 自动发送</p>
        <p>📱 Android移动端版本 | 发送时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
</body>
</html>
            """
            
            return html_content
            
        except Exception as e:
            Logger.error(f"AndroidEmailNotifier: 构建通知内容失败 - {e}")
            return f"构建通知内容时发生错误: {str(e)}"
    
    def send_error_notification(self, error_message: str, error_details: str = None) -> bool:
        """发送错误通知"""
        try:
            subject = "⚠️ Telegram内容机器人 - 错误通知"
            
            body = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        .header {{
            background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 20px;
        }}
        .error-content {{
            background: #fff5f5;
            border: 1px solid #fed7d7;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
        }}
        .error-message {{
            font-weight: bold;
            color: #e53e3e;
            margin-bottom: 10px;
        }}
        .error-details {{
            background: #f7fafc;
            border-left: 4px solid #e53e3e;
            padding: 10px;
            font-family: monospace;
            font-size: 0.9em;
            white-space: pre-wrap;
        }}
        .footer {{
            text-align: center;
            margin-top: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 8px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>⚠️ 错误通知</h1>
        <p>Telegram内容机器人遇到错误</p>
    </div>
    
    <div class="error-content">
        <div class="error-message">
            {error_message}
        </div>
        {f'<div class="error-details">{error_details}</div>' if error_details else ''}
    </div>
    
    <div class="footer">
        <p>🤖 此邮件由 Telegram内容机器人 自动发送</p>
        <p>📱 Android移动端版本 | 发送时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>请检查应用状态并及时处理错误</p>
    </div>
</body>
</html>
            """
            
            return self.send_email(subject, body, is_html=True)
            
        except Exception as e:
            Logger.error(f"AndroidEmailNotifier: 发送错误通知失败 - {e}")
            return False
    
    def test_email_config(self) -> Dict[str, Any]:
        """测试邮件配置"""
        result = {
            'success': False,
            'message': '',
            'config_valid': False
        }
        
        try:
            # 验证配置
            if not self._validate_config():
                result['message'] = '邮件配置不完整'
                return result
            
            result['config_valid'] = True
            
            # 测试连接
            if not self._connect_smtp():
                result['message'] = 'SMTP连接失败'
                return result
            
            # 发送测试邮件
            test_subject = "📧 Telegram内容机器人 - 邮件配置测试"
            test_body = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }}
        .header {{
            background: linear-gradient(135deg, #00b894 0%, #00a085 100%);
            color: white;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>✅ 邮件配置测试成功</h1>
        <p>您的邮件配置工作正常！</p>
        <p>测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </div>
</body>
</html>
            """
            
            if self.send_email(test_subject, test_body, is_html=True):
                result['success'] = True
                result['message'] = '邮件配置测试成功'
            else:
                result['message'] = '发送测试邮件失败'
            
        except Exception as e:
            result['message'] = f'测试邮件配置失败: {str(e)}'
        finally:
            self._disconnect_smtp()
        
        return result

# 模拟邮件通知器
class MockEmailNotifier:
    """模拟邮件通知器，用于测试"""
    
    def send_email(self, subject: str, body: str, is_html: bool = False) -> bool:
        Logger.info(f"MockEmailNotifier: 模拟发送邮件 - {subject}")
        return True
    
    def send_daily_summary(self, date: str = None) -> bool:
        Logger.info(f"MockEmailNotifier: 模拟发送每日汇总 - {date}")
        return True
    
    def send_new_content_notification(self, messages: List[Dict[str, Any]]) -> bool:
        Logger.info(f"MockEmailNotifier: 模拟发送新内容通知 - {len(messages)}条")
        return True
    
    def send_error_notification(self, error_message: str, error_details: str = None) -> bool:
        Logger.info(f"MockEmailNotifier: 模拟发送错误通知 - {error_message}")
        return True
    
    def test_email_config(self) -> Dict[str, Any]:
        return {
            'success': True,
            'message': '模拟邮件配置测试成功',
            'config_valid': True
        }

# 全局邮件通知器实例
android_email_notifier = AndroidEmailNotifier()

# 兼容性别名
class EmailNotifier:
    """兼容性邮件通知器类"""
    
    def __init__(self):
        self._notifier = android_email_notifier
    
    def send_daily_summary(self, date: str = None) -> bool:
        return self._notifier.send_daily_summary(date)
    
    def send_new_content_notification(self, messages: List[Dict[str, Any]]) -> bool:
        return self._notifier.send_new_content_notification(messages)
    
    def send_error_notification(self, error_message: str, error_details: str = None) -> bool:
        return self._notifier.send_error_notification(error_message, error_details)
    
    def test_email_config(self) -> Dict[str, Any]:
        return self._notifier.test_email_config()