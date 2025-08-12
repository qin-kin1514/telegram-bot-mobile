# Telegram Content Bot Mobile

一个基于Kivy框架开发的Android应用，用于在手机上定时抓取Telegram频道内容并发送邮件通知。

## 功能特性

### 核心功能
- 🤖 **Telegram内容抓取**: 监控指定频道的新消息
- 📧 **邮件通知**: 自动发送抓取结果到指定邮箱
- ⏰ **定时任务**: 支持固定时间和间隔模式的定时执行
- 🔍 **关键词过滤**: 基于兴趣标签筛选相关内容
- 📱 **移动端优化**: 专为Android平台设计的用户界面

### 界面功能
- **主界面**: 显示运行状态、统计信息和最近日志
- **配置界面**: 设置Telegram API、邮箱、频道和标签
- **定时任务界面**: 配置执行时间和任务参数
- **日志界面**: 查看运行日志和错误信息

### Android特性
- 🔋 **后台运行**: 支持前台服务，确保任务正常执行
- 🔔 **系统通知**: 实时显示运行状态
- 🛡️ **权限管理**: 自动请求所需权限
- 🔄 **开机自启**: 支持系统启动后自动运行

## 系统要求

- Android 5.0+ (API 21+)
- 网络连接
- 存储权限（用于保存配置和日志）
- 后台运行权限（用于定时任务）

## 安装说明

### 方式一：直接安装APK
1. 下载预编译的APK文件
2. 在Android设备上启用"未知来源"安装
3. 安装APK文件
4. 授予必要权限

### 方式二：从源码构建

#### 环境准备
```bash
# 安装Python 3.8+
# 安装Kivy和相关依赖
pip install kivy kivymd buildozer

# 安装Android开发工具
# 需要Android SDK和NDK
```

#### 构建APK
```bash
# 进入项目目录
cd telegram_bot_mobile

# 初始化buildozer
buildozer android debug

# 构建发布版本
buildozer android release
```

## 配置说明

### 首次使用
1. 启动应用后，按照引导完成初始配置
2. 配置Telegram API信息
3. 设置邮箱通知
4. 添加监控频道和兴趣标签
5. 配置定时任务

### Telegram API配置
- **Bot Token**: 从@BotFather获取
- **API ID/Hash**: 从https://my.telegram.org获取
- **目标频道**: 接收抓取结果的频道ID

### 邮箱配置
- **SMTP服务器**: 如smtp.gmail.com
- **端口**: 通常为587或465
- **邮箱账号**: 发送邮件的邮箱
- **密码**: 邮箱密码或应用专用密码

### 定时任务配置
- **间隔模式**: 按小时间隔执行
- **固定时间**: 在指定时间点执行
- **重试设置**: 失败后的重试机制

## 使用指南

### 基本操作
1. **启动任务**: 在主界面点击"启动定时任务"
2. **立即执行**: 点击"立即运行"测试抓取功能
3. **查看日志**: 在日志界面查看运行记录
4. **修改配置**: 在配置界面调整参数

### 权限设置
应用需要以下权限：
- **网络访问**: 连接Telegram API和发送邮件
- **存储权限**: 保存配置文件和日志
- **后台运行**: 执行定时任务
- **开机启动**: 系统重启后自动运行

### 电池优化
为确保定时任务正常运行，建议：
1. 将应用加入电池优化白名单
2. 在自启动管理中允许应用自启动
3. 关闭应用的省电模式限制

## 故障排除

### 常见问题

**Q: 定时任务不执行**
A: 检查以下设置：
- 确认定时任务已启用
- 检查电池优化设置
- 验证网络连接
- 查看日志中的错误信息

**Q: 无法连接Telegram**
A: 检查：
- Telegram API配置是否正确
- 网络连接是否正常
- 防火墙设置

**Q: 邮件发送失败**
A: 检查：
- SMTP服务器配置
- 邮箱密码是否正确
- 是否启用了两步验证

**Q: 应用闪退**
A: 尝试：
- 重启应用
- 清除应用数据
- 重新安装应用
- 查看系统日志

### 日志分析
应用会记录详细的运行日志，包括：
- 任务执行记录
- 错误信息
- 网络连接状态
- 配置变更记录

## 技术架构

### 框架选择
- **Kivy**: 跨平台Python GUI框架
- **KivyMD**: Material Design组件库
- **Buildozer**: Android打包工具

### 核心模块
- `main.py`: 应用主入口
- `ui/`: 用户界面模块
- `core/`: 核心功能模块
- `android/`: Android特定功能

### 依赖库
- `telethon`: Telegram客户端库
- `schedule`: 任务调度库
- `smtplib`: 邮件发送库
- `sqlite3`: 数据库支持

## 开发说明

### 项目结构
```
telegram_bot_mobile/
├── main.py                 # 应用入口
├── buildozer.spec         # 打包配置
├── ui/                    # 界面模块
│   ├── main_screen.py     # 主界面
│   ├── config_screen.py   # 配置界面
│   ├── schedule_screen.py # 定时任务界面
│   └── log_screen.py      # 日志界面
├── core/                  # 核心模块
│   ├── config_manager.py  # 配置管理
│   ├── scheduler.py       # 任务调度
│   └── permission_manager.py # 权限管理
└── android/               # Android功能
    └── service.py         # 后台服务
```

### 开发环境
1. Python 3.8+
2. Kivy 2.1.0+
3. KivyMD 1.1.1+
4. Android SDK/NDK

### 调试方法
```bash
# 连接Android设备进行调试
buildozer android debug
adb logcat | grep python

# 查看应用日志
adb shell run-as org.example.telegrambot
```

## 更新日志

### v1.0.0 (2024-01-XX)
- 初始版本发布
- 基础功能实现
- Android平台适配
- Material Design界面

## 许可证

本项目采用MIT许可证，详见LICENSE文件。

## 贡献指南

欢迎提交Issue和Pull Request来改进项目。

### 提交Issue
- 详细描述问题
- 提供复现步骤
- 附上相关日志

### 提交代码
- Fork项目
- 创建功能分支
- 提交代码
- 发起Pull Request

## 联系方式

如有问题或建议，请通过以下方式联系：
- GitHub Issues
- 邮箱: [your-email@example.com]

## 致谢

感谢以下开源项目的支持：
- [Kivy](https://kivy.org/)
- [KivyMD](https://kivymd.readthedocs.io/)
- [Telethon](https://github.com/LonamiWebs/Telethon)
- [Buildozer](https://github.com/kivy/buildozer)