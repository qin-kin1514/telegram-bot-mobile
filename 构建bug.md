Warning: : prerequisites.py is experimental and does not support all prerequisites yet.
Warning: : Please report any issues to the python-for-android issue tracker.
# Check application requirements
# Compile platform
# Run ['/opt/hostedtoolcache/Python/3.9.23/x64/bin/python', '-m', 'pythonforandroid.toolchain', 'create', '--dist_name=telegramcontentbot', '--bootstrap=sdl2', '--requirements=python3,kivy>=2.1.0,kivymd>=1.1.1,requests,telethon,pillow,pyjnius', '--arch=arm64-v8a', '--arch=armeabi-v7a', '--copy-libs', '--color=always', '--storage-dir=/home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a', '--ndk-api=21', '--ignore-setup-py', '--debug']
# Cwd /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform/python-for-android
Warning: : prerequisites.py is experimental and does not support all prerequisites yet.
Warning: : Please report any issues to the python-for-android issue tracker.
[INFO]:    Will compile for the following archs: armeabi-v7a, arm64-v8a
[DEBUG]:   Create directory /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a
[DEBUG]:   Create directory /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build
[DEBUG]:   Create directory /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/dists
[DEBUG]:   Create directory /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/bootstrap_builds
[DEBUG]:   Create directory /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a/build/other_builds
[INFO]:    Found Android API target in $ANDROIDAPI: 31
[INFO]:    Available Android APIs are (31, 33, 33, 34, 34, 34, 34, 34, 35, 35, 35, 36, 36)
[INFO]:    Requested API target 31 is available, continuing.
[INFO]:    Found NDK dir in $ANDROIDNDK: /usr/local/lib/android/sdk/ndk/23.2.8568313
[INFO]:    Found NDK version 23c
[ERROR]:   Build failed: The minimum supported NDK version is 25. You can download it from https://developer.android.com/ndk/downloads/.
[INFO]:    Instructions: Please, go to the android NDK page (https://developer.android.com/ndk/downloads/) and download a supported version.
*** The currently recommended NDK version is 25b ***
# Command failed: ['/opt/hostedtoolcache/Python/3.9.23/x64/bin/python', '-m', 'pythonforandroid.toolchain', 'create', '--dist_name=telegramcontentbot', '--bootstrap=sdl2', '--requirements=python3,kivy>=2.1.0,kivymd>=1.1.1,requests,telethon,pillow,pyjnius', '--arch=arm64-v8a', '--arch=armeabi-v7a', '--copy-libs', '--color=always', '--storage-dir=/home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a', '--ndk-api=21', '--ignore-setup-py', '--debug']
# ENVIRONMENT:
#     SHELL = '/bin/bash'
#     SELENIUM_JAR_PATH = '/usr/share/java/selenium-server.jar'
#     CONDA = '/usr/share/miniconda'
#     GITHUB_WORKSPACE = '/home/runner/work/telegram-bot-mobile/telegram-bot-mobile'
#     JAVA_HOME_11_X64 = '/usr/lib/jvm/temurin-11-jdk-amd64'
#     PKG_CONFIG_PATH = '/opt/hostedtoolcache/Python/3.9.23/x64/lib/pkgconfig'
#     GITHUB_PATH = '/home/runner/work/_temp/_runner_file_commands/add_path_9b60f58c-5b50-4848-808b-db0fdcfe9ca4'
#     GITHUB_ACTION = '__run_6'
#     JAVA_HOME = '/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/17.0.16-8/x64'
#     GITHUB_RUN_NUMBER = '18'
#     RUNNER_NAME = 'GitHub Actions 1000000017'
#     GRADLE_HOME = '/usr/share/gradle-9.0.0'
#     GITHUB_REPOSITORY_OWNER_ID = '216374626'
#     ACTIONS_RUNNER_ACTION_ARCHIVE_CACHE = '/opt/actionarchivecache'
#     XDG_CONFIG_HOME = '/home/runner/.config'
#     Python_ROOT_DIR = '/opt/hostedtoolcache/Python/3.9.23/x64'
#     MEMORY_PRESSURE_WRITE = 'c29tZSAyMDAwMDAgMjAwMDAwMAA='
#     DOTNET_SKIP_FIRST_TIME_EXPERIENCE = '1'
#     JAVA_OPTS = '-Xmx2048m'
#     ANT_HOME = '/usr/share/ant'
#     JAVA_HOME_8_X64 = '/usr/lib/jvm/temurin-8-jdk-amd64'
#     GITHUB_TRIGGERING_ACTOR = 'qin-kin1514'
#     pythonLocation = '/opt/hostedtoolcache/Python/3.9.23/x64'
#     GITHUB_REF_TYPE = 'branch'
#     HOMEBREW_CLEANUP_PERIODIC_FULL_DAYS = '3650'
#     ANDROID_NDK = '/usr/local/lib/android/sdk/ndk/27.3.13750724'
#     BOOTSTRAP_HASKELL_NONINTERACTIVE = '1'
#     PWD = '/home/runner/work/telegram-bot-mobile/telegram-bot-mobile'
#     PIPX_BIN_DIR = '/opt/pipx_bin'
#     LOGNAME = 'runner'
#     GITHUB_REPOSITORY_ID = '1036615462'
#     GITHUB_ACTIONS = 'true'
#     ANDROID_NDK_LATEST_HOME = '/usr/local/lib/android/sdk/ndk/28.2.13676358'
#     SYSTEMD_EXEC_PID = '1940'
#     GITHUB_SHA = 'ff45c6cb938ed0c77173f55d18eb66b4a0d0b391'
#     GITHUB_WORKFLOW_REF = 'qin-kin1514/telegram-bot-mobile/.github/workflows/build-android.yml@refs/heads/main'
#     POWERSHELL_DISTRIBUTION_CHANNEL = 'GitHub-Actions-ubuntu24'
#     RUNNER_ENVIRONMENT = 'github-hosted'
#     DOTNET_MULTILEVEL_LOOKUP = '0'
#     GITHUB_REF = 'refs/heads/main'
#     RUNNER_OS = 'Linux'
#     GITHUB_REF_PROTECTED = 'false'
#     HOME = '/home/runner'
#     GITHUB_API_URL = 'https://api.github.com'
#     LANG = 'C.UTF-8'
#     RUNNER_TRACKING_ID = 'github_6a89e0ac-ee27-4d78-bc2e-2e5c883b5691'
#     RUNNER_ARCH = 'X64'
#     MEMORY_PRESSURE_WATCH = '/sys/fs/cgroup/system.slice/hosted-compute-agent.service/memory.pressure'
#     RUNNER_TEMP = '/home/runner/work/_temp'
#     GITHUB_STATE = '/home/runner/work/_temp/_runner_file_commands/save_state_9b60f58c-5b50-4848-808b-db0fdcfe9ca4'
#     EDGEWEBDRIVER = '/usr/local/share/edge_driver'
#     JAVA_HOME_21_X64 = '/usr/lib/jvm/temurin-21-jdk-amd64'
#     GITHUB_ENV = '/home/runner/work/_temp/_runner_file_commands/set_env_9b60f58c-5b50-4848-808b-db0fdcfe9ca4'
#     GITHUB_EVENT_PATH = '/home/runner/work/_temp/_github_workflow/event.json'
#     INVOCATION_ID = '67ef7a461382452d809f2a68940e1376'
#     GITHUB_EVENT_NAME = 'push'
#     GITHUB_RUN_ID = '16909103612'
#     JAVA_HOME_17_X64 = '/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/17.0.16-8/x64'
#     ANDROID_NDK_HOME = '/usr/local/lib/android/sdk/ndk/23.2.8568313'
#     GITHUB_STEP_SUMMARY = '/home/runner/work/_temp/_runner_file_commands/step_summary_9b60f58c-5b50-4848-808b-db0fdcfe9ca4'
#     HOMEBREW_NO_AUTO_UPDATE = '1'
#     GITHUB_ACTOR = 'qin-kin1514'
#     NVM_DIR = '/home/runner/.nvm'
#     SGX_AESM_ADDR = '1'
#     GITHUB_RUN_ATTEMPT = '1'
#     ANDROID_HOME = '/usr/local/lib/android/sdk'
#     GITHUB_GRAPHQL_URL = 'https://api.github.com/graphql'
#     ACCEPT_EULA = 'Y'
#     USER = 'runner'
#     GITHUB_SERVER_URL = 'https://github.com'
#     PIPX_HOME = '/opt/pipx'
#     GECKOWEBDRIVER = '/usr/local/share/gecko_driver'
#     CHROMEWEBDRIVER = '/usr/local/share/chromedriver-linux64'
#     SHLVL = '1'
#     ANDROID_SDK_ROOT = '/usr/local/lib/android/sdk'
#     VCPKG_INSTALLATION_ROOT = '/usr/local/share/vcpkg'
#     GITHUB_ACTOR_ID = '216374626'
#     RUNNER_TOOL_CACHE = '/opt/hostedtoolcache'
#     ImageVersion = '20250804.2.0'
#     Python3_ROOT_DIR = '/opt/hostedtoolcache/Python/3.9.23/x64'
#     DOTNET_NOLOGO = '1'
#     GOROOT_1_23_X64 = '/opt/hostedtoolcache/go/1.23.11/x64'
#     GITHUB_WORKFLOW_SHA = 'ff45c6cb938ed0c77173f55d18eb66b4a0d0b391'
#     GOROOT_1_24_X64 = '/opt/hostedtoolcache/go/1.24.5/x64'
#     GITHUB_REF_NAME = 'main'
#     GITHUB_JOB = 'build'
#     LD_LIBRARY_PATH = '/opt/hostedtoolcache/Python/3.9.23/x64/lib'
#     XDG_RUNTIME_DIR = '/run/user/1001'
#     AZURE_EXTENSION_DIR = '/opt/az/azcliextensions'
#     GITHUB_REPOSITORY = 'qin-kin1514/telegram-bot-mobile'
#     Python2_ROOT_DIR = '/opt/hostedtoolcache/Python/3.9.23/x64'
#     ANDROID_NDK_ROOT = '/usr/local/lib/android/sdk/ndk/23.2.8568313'
#     CHROME_BIN = '/usr/bin/google-chrome'
#     GOROOT_1_22_X64 = '/opt/hostedtoolcache/go/1.22.12/x64'
#     GRADLE_OPTS = '-Xmx2048m -Dorg.gradle.jvmargs=-Xmx2048m'
#     GITHUB_RETENTION_DAYS = '90'
#     JOURNAL_STREAM = '9:11620'
#     RUNNER_WORKSPACE = '/home/runner/work/telegram-bot-mobile'
#     GITHUB_ACTION_REPOSITORY = ''
#     PATH = '/usr/share/ant/bin:/usr/local/lib/android/sdk/ndk/23.2.8568313:/usr/local/lib/android/sdk/cmdline-tools/latest/bin:/usr/local/lib/android/sdk/platform-tools:/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/17.0.16-8/x64/bin:/opt/hostedtoolcache/Python/3.9.23/x64/bin:/opt/hostedtoolcache/Python/3.9.23/x64:/snap/bin:/home/runner/.local/bin:/opt/pipx_bin:/home/runner/.cargo/bin:/home/runner/.config/composer/vendor/bin:/usr/local/.ghcup/bin:/home/runner/.dotnet/tools:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin'
#     GITHUB_BASE_REF = ''
#     GHCUP_INSTALL_BASE_PREFIX = '/usr/local'
#     CI = 'true'
#     SWIFT_PATH = '/usr/share/swift/usr/bin'
#     ImageOS = 'ubuntu24'
#     GITHUB_REPOSITORY_OWNER = 'qin-kin1514'
#     GITHUB_HEAD_REF = ''
#     GITHUB_ACTION_REF = ''
#     ENABLE_RUNNER_TRACING = 'true'
#     GITHUB_WORKFLOW = 'Build Android APK'
#     DEBIAN_FRONTEND = 'noninteractive'
#     GITHUB_OUTPUT = '/home/runner/work/_temp/_runner_file_commands/set_output_9b60f58c-5b50-4848-808b-db0fdcfe9ca4'
#     AGENT_TOOLSDIRECTORY = '/opt/hostedtoolcache'
#     _ = '/opt/hostedtoolcache/Python/3.9.23/x64/bin/buildozer'
#     PACKAGES_PATH = '/home/runner/.buildozer/android/packages'
#     ANDROIDSDK = '/usr/local/lib/android/sdk'
#     ANDROIDNDK = '/usr/local/lib/android/sdk/ndk/23.2.8568313'
#     ANDROIDAPI = '31'
#     ANDROIDMINAPI = '21'
# 
# Buildozer failed to execute the last command
# The error might be hidden in the log above this error
# Please read the full log, and search for it before
# raising an issue with buildozer itself.
# In case of a bug report, please add a full log with log_level = 2
Error: Process completed with exit code 1.