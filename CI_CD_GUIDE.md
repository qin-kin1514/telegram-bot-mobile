# 使用在线CI/CD服务打包Android APK指南

## 方案1：GitHub Actions（推荐）

### 步骤1：准备GitHub仓库

1. **创建GitHub仓库**：
   - 访问 https://github.com
   - 点击 "New repository"
   - 输入仓库名称（如：telegram-bot-mobile）
   - 设置为Public或Private
   - 点击 "Create repository"

2. **上传项目代码**：
   ```bash
   cd telegram_bot_mobile
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/qin-kin1514/telegram-bot-mobile.git
   git push -u origin main
   ```

### 步骤2：创建GitHub Actions工作流

1. **创建工作流目录**：
   ```
   mkdir -p .github/workflows
   ```

2. **创建工作流文件** `.github/workflows/build-android.yml`：

```yaml
name: Build Android APK

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  workflow_dispatch:  # 允许手动触发

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install system dependencies
      run: |
        sudo apt update
        sudo apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
        sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
    
    - name: Set up Java
      uses: actions/setup-java@v3
      with:
        distribution: 'temurin'
        java-version: '8'
    
    - name: Install Python dependencies
      run: |
        python -m pip install --upgrade pip
        pip install buildozer cython
        pip install -r requirements.txt
    
    - name: Cache Buildozer global directory
      uses: actions/cache@v3
      with:
        path: .buildozer_global
        key: buildozer-global-${{ hashFiles('buildozer.spec') }}
    
    - name: Cache Buildozer directory
      uses: actions/cache@v3
      with:
        path: .buildozer
        key: buildozer-${{ hashFiles('buildozer.spec') }}
    
    - name: Build APK
      run: |
        buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v3
      with:
        name: android-apk
        path: bin/*.apk
```

### 步骤3：配置buildozer.spec文件

确保您的 `buildozer.spec` 文件配置正确：

```ini
[app]
title = Telegram Bot Mobile
package.name = telegram_bot_mobile
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.1
requirements = python3,kivy,kivymd,requests,telethon,cryptg,pillow,sqlite3

[buildozer]
log_level = 2

[android]
permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
api = 30
minapi = 21
ndk = 23b
sdk = 30
```

### 步骤4：触发构建

1. **自动触发**：推送代码到main分支
   ```bash
   git add .
   git commit -m "Add GitHub Actions workflow"
   git push
   ```

2. **手动触发**：
   - 访问GitHub仓库页面
   - 点击 "Actions" 标签
   - 选择 "Build Android APK" 工作流
   - 点击 "Run workflow"

### 步骤5：下载APK

1. 构建完成后，访问Actions页面
2. 点击最新的构建任务
3. 在 "Artifacts" 部分下载 "android-apk"

---

## 方案2：GitLab CI

### 步骤1：创建GitLab项目

1. 访问 https://gitlab.com
2. 点击 "New project"
3. 选择 "Create blank project"
4. 填写项目信息并创建

### 步骤2：创建CI/CD配置文件

创建 `.gitlab-ci.yml` 文件：

```yaml
stages:
  - build

variables:
  PIP_CACHE_DIR: "$CI_PROJECT_DIR/.cache/pip"

cache:
  paths:
    - .cache/pip
    - .buildozer
    - .buildozer_global

build_android:
  stage: build
  image: ubuntu:20.04
  
  before_script:
    - apt update
    - apt install -y git zip unzip openjdk-8-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev
    - apt install -y build-essential libssl-dev libffi-dev python3-dev
    - python3 -m pip install --upgrade pip
    - pip3 install buildozer cython
    - pip3 install -r requirements.txt
  
  script:
    - buildozer android debug
  
  artifacts:
    paths:
      - bin/*.apk
    expire_in: 1 week
  
  only:
    - main
    - merge_requests
```

### 步骤3：推送代码并触发构建

```bash
git add .
git commit -m "Add GitLab CI configuration"
git push
```

### 步骤4：监控构建和下载APK

1. 访问GitLab项目页面
2. 点击 "CI/CD" > "Pipelines"
3. 查看构建状态
4. 构建完成后，在 "Jobs" 页面下载artifacts

---

## 高级配置选项

### 1. 环境变量配置

在GitHub/GitLab中设置敏感信息：

**GitHub Secrets**：
- 访问仓库 Settings > Secrets and variables > Actions
- 添加secrets（如API密钥）

**GitLab Variables**：
- 访问项目 Settings > CI/CD > Variables
- 添加变量

### 2. 签名APK（发布版本）

```yaml
# 在工作流中添加签名步骤
- name: Sign APK
  run: |
    # 使用jarsigner签名APK
    jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ${{ secrets.KEYSTORE_FILE }} bin/*.apk ${{ secrets.KEY_ALIAS }}
```

### 3. 多平台构建

```yaml
strategy:
  matrix:
    os: [ubuntu-latest]
    python-version: ['3.8', '3.9', '3.10']
```

### 4. 构建优化

- 使用缓存加速构建
- 并行构建多个架构
- 增量构建

---

## 故障排除

### 常见问题

1. **构建超时**：
   - 增加timeout设置
   - 优化依赖安装
   - 使用更强的runner

2. **依赖安装失败**：
   - 检查requirements.txt
   - 更新系统包
   - 使用特定版本

3. **NDK/SDK问题**：
   - 在buildozer.spec中指定版本
   - 使用缓存避免重复下载

### 调试技巧

1. **启用详细日志**：
   ```yaml
   - name: Build with verbose logging
     run: buildozer -v android debug
   ```

2. **SSH调试**（GitHub Actions）：
   ```yaml
   - name: Setup tmate session
     uses: mxschmitt/action-tmate@v3
   ```

---

## 总结

使用在线CI/CD服务的优势：
- ✅ 无需本地环境配置
- ✅ 自动化构建流程
- ✅ 版本控制集成
- ✅ 多人协作友好
- ✅ 免费额度充足

推荐使用GitHub Actions，因为：
- 社区支持更好
- 文档更完善
- 免费额度更多
- 集成生态更丰富

开始使用时，建议先用简单配置测试，然后逐步添加高级功能。