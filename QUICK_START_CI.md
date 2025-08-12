# 🚀 快速开始：使用GitHub Actions构建APK

## 📋 准备工作清单

- [ ] GitHub账号
- [ ] 项目代码已准备就绪
- [ ] 已创建CI/CD配置文件

## 🔥 5分钟快速部署

### 第1步：创建GitHub仓库

1. 访问 [GitHub](https://github.com)
2. 点击右上角 **"+"** → **"New repository"**
3. 填写信息：
   - Repository name: `telegram-bot-mobile`
   - Description: `Telegram Bot Mobile App`
   - 选择 **Public** 或 **Private**
4. 点击 **"Create repository"**

### 第2步：上传代码到GitHub

在项目目录中执行：

```bash
# 初始化Git仓库
git init

# 添加所有文件
git add .

# 提交代码
git commit -m "Initial commit with CI/CD setup"

# 设置主分支
git branch -M main

# 添加远程仓库（替换YOUR_USERNAME为您的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/telegram-bot-mobile.git

# 推送代码
git push -u origin main
```

### 第3步：触发自动构建

代码推送后，GitHub Actions会自动开始构建：

1. 访问您的GitHub仓库
2. 点击 **"Actions"** 标签
3. 查看 **"Build Android APK"** 工作流状态

### 第4步：下载APK

构建完成后（通常需要15-30分钟）：

1. 在Actions页面点击最新的构建任务
2. 滚动到底部找到 **"Artifacts"** 部分
3. 点击 **"android-apk"** 下载APK文件

## 🎯 手动触发构建

如果需要手动触发构建：

1. 访问仓库的 **Actions** 页面
2. 选择 **"Build Android APK"** 工作流
3. 点击 **"Run workflow"** 按钮
4. 选择分支（通常是main）
5. 点击绿色的 **"Run workflow"** 按钮

## 📊 构建状态说明

- 🟡 **黄色圆圈**：构建进行中
- ✅ **绿色对勾**：构建成功
- ❌ **红色叉号**：构建失败

## 🔧 常见问题解决

### 问题1：构建失败

**解决方案**：
1. 点击失败的构建任务
2. 查看错误日志
3. 常见问题：
   - 依赖版本冲突 → 检查requirements.txt
   - 权限问题 → 检查buildozer.spec中的permissions
   - 内存不足 → 减少并发构建

### 问题2：APK无法安装

**解决方案**：
1. 确保手机开启"未知来源"安装
2. 检查Android版本兼容性（最低API 21）
3. 如需发布，需要签名APK

### 问题3：构建时间过长

**优化方案**：
1. 启用缓存（已在配置中包含）
2. 减少不必要的依赖
3. 使用更快的runner（付费版本）

## 🎉 成功标志

当您看到以下内容时，说明设置成功：

1. ✅ GitHub Actions工作流显示绿色
2. ✅ Artifacts中有APK文件
3. ✅ APK可以在Android设备上安装
4. ✅ 应用可以正常启动

## 📱 测试APK

下载APK后：

1. **传输到手机**：
   - 通过USB传输
   - 发送到邮箱下载
   - 使用云存储服务

2. **安装APK**：
   - 在手机上找到APK文件
   - 点击安装
   - 如提示"未知来源"，请在设置中允许

3. **测试功能**：
   - 启动应用
   - 测试基本功能
   - 检查权限是否正常

## 🔄 持续集成流程

每次代码更新时：

1. **本地开发** → 修改代码
2. **提交推送** → `git push`
3. **自动构建** → GitHub Actions触发
4. **获取APK** → 从Artifacts下载
5. **测试验证** → 在设备上测试

## 🎯 下一步

- [ ] 设置发布版本签名
- [ ] 配置自动发布到Google Play
- [ ] 添加测试自动化
- [ ] 设置通知机制

---

**💡 提示**：首次构建可能需要较长时间，因为需要下载Android SDK和NDK。后续构建会因为缓存而更快。

**🆘 需要帮助？** 查看详细的 [CI_CD_GUIDE.md](./CI_CD_GUIDE.md) 文档。