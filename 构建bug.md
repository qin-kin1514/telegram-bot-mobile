Run # Set environment variables for better build stability
Cloning into 'python-for-android'...
# Check configuration tokens
# Ensure build layout
# Create directory /home/runner/.buildozer
# Create directory /home/runner/.buildozer/cache
# Create directory /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer
# Create directory /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/bin
# Create directory /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/applibs
# Create directory /home/runner/.buildozer/android/platform/android/platform
# Create directory /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform
# Create directory /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/app
# Check configuration tokens
# Preparing build
# Check requirements for android
# Search for Git (git)
#  -> found at /usr/bin/git
# Search for Cython (cython)
#  -> found at /opt/hostedtoolcache/Python/3.9.23/x64/bin/cython
# Search for Java compiler (javac)
#  -> found at /usr/lib/jvm/temurin-17-jdk-amd64/bin/javac
# Search for Java keytool (keytool)
#  -> found at /usr/lib/jvm/temurin-17-jdk-amd64/bin/keytool
# Install platform
# Run ['git', 'clone', '-b', 'master', '--single-branch', 'https://github.com/kivy/python-for-android.git', 'python-for-android']
# Cwd /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform
# Run ['/opt/hostedtoolcache/Python/3.9.23/x64/bin/python', '-m', 'pip', 'install', '-q', '--user', 'appdirs', 'colorama>=0.3.3', 'jinja2', 'sh>=1.10, <2.0; sys_platform!="win32"', 'build', 'toml', 'packaging', 'setuptools']
# Cwd None
Traceback (most recent call last):
  File "/opt/hostedtoolcache/Python/3.9.23/x64/bin/buildozer", line 7, in <module>
# Android ANT is missing, downloading
    sys.exit(main())
  File "/opt/hostedtoolcache/Python/3.9.23/x64/lib/python3.9/site-packages/buildozer/scripts/client.py", line 13, in main
    Buildozer().run_command(sys.argv[1:])
  File "/opt/hostedtoolcache/Python/3.9.23/x64/lib/python3.9/site-packages/buildozer/__init__.py", line 1024, in run_command
    self.target.run_commands(args)
  File "/opt/hostedtoolcache/Python/3.9.23/x64/lib/python3.9/site-packages/buildozer/target.py", line 93, in run_commands
    func(args)
  File "/opt/hostedtoolcache/Python/3.9.23/x64/lib/python3.9/site-packages/buildozer/target.py", line 103, in cmd_debug
    self.buildozer.prepare_for_build()
  File "/opt/hostedtoolcache/Python/3.9.23/x64/lib/python3.9/site-packages/buildozer/__init__.py", line 172, in prepare_for_build
    self.target.install_platform()
  File "/opt/hostedtoolcache/Python/3.9.23/x64/lib/python3.9/site-packages/buildozer/targets/android.py", line 615, in install_platform
    self._install_android_ndk()
  File "/opt/hostedtoolcache/Python/3.9.23/x64/lib/python3.9/site-packages/buildozer/targets/android.py", line 438, in _install_android_ndk
    self.buildozer.download(url,
  File "/opt/hostedtoolcache/Python/3.9.23/x64/lib/python3.9/site-packages/buildozer/__init__.py", line 658, in download
    urlretrieve(url, filename, report_hook)
  File "/opt/hostedtoolcache/Python/3.9.23/x64/lib/python3.9/urllib/request.py", line 1847, in retrieve
# Downloading https://archive.apache.org/dist/ant/binaries/apache-ant-1.9.4-bin.tar.gz
# Run ['tar', 'xzf', 'apache-ant-1.9.4-bin.tar.gz']
# Cwd /home/runner/.buildozer/android/platform/apache-ant-1.9.4
# Apache ANT installation done.
# Android SDK is missing, downloading
# Downloading https://dl.google.com/android/repository/commandlinetools-linux-6514223_latest.zip
# Unpacking Android SDK
# Run ['unzip', '-q', '/home/runner/.buildozer/android/platform/android-sdk/commandlinetools-linux-6514223_latest.zip']
# Cwd /home/runner/.buildozer/android/platform/android-sdk
# Android SDK tools base installation done.
# Recommended android's NDK version by p4a is: 25b
# Android NDK is missing, downloading
# Downloading https://dl.google.com/android/repository/android-ndk-r23.2.8568313-linux.zip
    block = fp.read(bs)
  File "/opt/hostedtoolcache/Python/3.9.23/x64/lib/python3.9/tempfile.py", line 494, in func_wrapper
    return func(*args, **kwargs)
ValueError: read of closed file
Error: Process completed with exit code 1.