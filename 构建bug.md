1秒
8秒
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
# Apache ANT found at /usr/share/ant
# Android SDK found at /usr/local/lib/android/sdk
# Android NDK found at /usr/local/lib/android/sdk/ndk/23.2.8568313
# Recommended android's NDK version by p4a is: 25b
# Skipping Android SDK update due to spec file setting
# Note: this also prevents installing missing SDK components
# Updating SDK build tools if necessary
# Run ['/usr/local/lib/android/sdk/tools/bin/sdkmanager', '--sdk_root=/usr/local/lib/android/sdk', '--list']
# Cwd /usr/local/lib/android/sdk
Warning: Observed package id 'cmdline-tools;latest' in inconsistent location '/usr/local/lib/android/sdk/cmdline-tools/latest-2' (Expected '/usr/local/lib/android/sdk/cmdline-tools/latest')
Loading package information...                                                  
Warning: Observed package id 'cmdline-tools;latest' in inconsistent location '/usr/local/lib/android/sdk/cmdline-tools/latest-2' (Expected '/usr/local/lib/android/sdk/cmdline-tools/latest')
Loading local repository...                                                     
[=========                              ] 25% Loading local repository...       
[=========                              ] 25% Fetch remote repository...        
[==========                             ] 26% Fetch remote repository...        
[============                           ] 31% Fetch remote repository...        
[============                           ] 32% Fetch remote repository...        
[=============                          ] 33% Fetch remote repository...        
[=============                          ] 35% Fetch remote repository...        
[==============                         ] 36% Fetch remote repository...        
[==============                         ] 37% Fetch remote repository...        
[===============                        ] 38% Fetch remote repository...        
[===============                        ] 39% Fetch remote repository...        
[================                       ] 40% Fetch remote repository...        
[================                       ] 41% Fetch remote repository...        
[================                       ] 42% Fetch remote repository...        
[=================                      ] 44% Fetch remote repository...        
[=================                      ] 45% Fetch remote repository...        
[==================                     ] 46% Fetch remote repository...        
[==================                     ] 47% Fetch remote repository...        
[===================                    ] 48% Fetch remote repository...        
[===================                    ] 49% Fetch remote repository...        
[====================                   ] 50% Fetch remote repository...        
[====================                   ] 51% Fetch remote repository...        
[====================                   ] 53% Fetch remote repository...        
[=====================                  ] 54% Fetch remote repository...        
[=====================                  ] 55% Fetch remote repository...        
[======================                 ] 56% Fetch remote repository...        
[======================                 ] 57% Fetch remote repository...        
[=======================                ] 58% Fetch remote repository...        
[=======================                ] 59% Fetch remote repository...        
[========================               ] 60% Fetch remote repository...        
[========================               ] 61% Fetch remote repository...        
[=========================              ] 63% Fetch remote repository...        
[=========================              ] 64% Fetch remote repository...        
[=========================              ] 65% Fetch remote repository...        
[==========================             ] 66% Fetch remote repository...        
[==========================             ] 67% Fetch remote repository...        
[===========================            ] 68% Fetch remote repository...        
[===========================            ] 69% Fetch remote repository...        
[============================           ] 70% Fetch remote repository...        
[============================           ] 72% Fetch remote repository...        
[=============================          ] 73% Fetch remote repository...        
[=============================          ] 74% Fetch remote repository...        
[=============================          ] 75% Fetch remote repository...        
[=============================          ] 75% Computing updates...              
[=======================================] 100% Computing updates...             
Installed packages:
  Path                               | Version       | Description                             | Location                          
  -------                            | -------       | -------                                 | -------                           
  build-tools;31.0.0                 | 31.0.0        | Android SDK Build-Tools 31              | build-tools/31.0.0                
  build-tools;34.0.0                 | 34.0.0        | Android SDK Build-Tools 34              | build-tools/34.0.0                
  build-tools;35.0.0                 | 35.0.0        | Android SDK Build-Tools 35              | build-tools/35.0.0                
  build-tools;35.0.1                 | 35.0.1        | Android SDK Build-Tools 35.0.1          | build-tools/35.0.1                
  build-tools;36.0.0                 | 36.0.0        | Android SDK Build-Tools 36              | build-tools/36.0.0                
  cmake;3.18.1                       | 3.18.1        | CMake 3.18.1                            | cmake/3.18.1                      
  cmake;3.31.5                       | 3.31.5        | CMake 3.31.5                            | cmake/3.31.5                      
  cmdline-tools;latest               | 19.0          | Android SDK Command-line Tools (latest) | cmdline-tools/latest-2            
  extras;android;m2repository        | 47.0.0        | Android Support Repository              | extras/android/m2repository       
  extras;google;google_play_services | 49            | Google Play services                    | extras/google/google_play_services
  extras;google;m2repository         | 58            | Google Repository                       | extras/google/m2repository        
  ndk;23.2.8568313                   | 23.2.8568313  | NDK (Side by side) 23.2.8568313         | ndk/23.2.8568313                  
  ndk;26.3.11579264                  | 26.3.11579264 | NDK (Side by side) 26.3.11579264        | ndk/26.3.11579264                 
  ndk;27.3.13750724                  | 27.3.13750724 | NDK (Side by side) 27.3.13750724        | ndk/27.3.13750724                 
  ndk;28.2.13676358                  | 28.2.13676358 | NDK (Side by side) 28.2.13676358        | ndk/28.2.13676358                 
  platform-tools                     | 36.0.0        | Android SDK Platform-Tools              | platform-tools                    
  platforms;android-31               | 1             | Android SDK Platform 31                 | platforms/android-31              
  platforms;android-33-ext4          | 1             | Android SDK Platform 33-ext4            | platforms/android-33-ext4         
  platforms;android-33-ext5          | 1             | Android SDK Platform 33-ext5            | platforms/android-33-ext5         
  platforms;android-34               | 3             | Android SDK Platform 34                 | platforms/android-34              
  platforms;android-34-ext10         | 1             | Android SDK Platform 34-ext10           | platforms/android-34-ext10        
  platforms;android-34-ext11         | 1             | Android SDK Platform 34-ext11           | platforms/android-34-ext11        
  platforms;android-34-ext12         | 1             | Android SDK Platform 34-ext12           | platforms/android-34-ext12        
  platforms;android-34-ext8          | 1             | Android SDK Platform 34-ext8            | platforms/android-34-ext8         
  platforms;android-35               | 2             | Android SDK Platform 35                 | platforms/android-35              
  platforms;android-35-ext14         | 1             | Android SDK Platform 35-ext14           | platforms/android-35-ext14        
  platforms;android-35-ext15         | 1             | Android SDK Platform 35-ext15           | platforms/android-35-ext15        
  platforms;android-36               | 2             | Android SDK Platform 36                 | platforms/android-36              
  platforms;android-36-ext18         | 1             | Android SDK Platform 36-ext18           | platforms/android-36-ext18        

Available Packages:
  Path                                                                            | Version           | Description                                                           
  -------                                                                         | -------           | -------                                                               
  add-ons;addon-google_apis-google-15                                             | 3                 | Google APIs                                                           
  add-ons;addon-google_apis-google-16                                             | 4                 | Google APIs                                                           
  add-ons;addon-google_apis-google-17                                             | 4                 | Google APIs                                                           
  add-ons;addon-google_apis-google-18                                             | 4                 | Google APIs                                                           
  add-ons;addon-google_apis-google-19                                             | 20                | Google APIs                                                           
  add-ons;addon-google_apis-google-21                                             | 1                 | Google APIs                                                           
  add-ons;addon-google_apis-google-22                                             | 1                 | Google APIs                                                           
  add-ons;addon-google_apis-google-23                                             | 1                 | Google APIs                                                           
  add-ons;addon-google_apis-google-24                                             | 1                 | Google APIs                                                           
  build-tools;19.1.0                                                              | 19.1.0            | Android SDK Build-Tools 19.1                                          
  build-tools;20.0.0                                                              | 20.0.0            | Android SDK Build-Tools 20                                            
  build-tools;21.1.2                                                              | 21.1.2            | Android SDK Build-Tools 21.1.2                                        
  build-tools;22.0.1                                                              | 22.0.1            | Android SDK Build-Tools 22.0.1                                        
  build-tools;23.0.1                                                              | 23.0.1            | Android SDK Build-Tools 23.0.1                                        
  build-tools;23.0.2                                                              | 23.0.2            | Android SDK Build-Tools 23.0.2                                        
  build-tools;23.0.3                                                              | 23.0.3            | Android SDK Build-Tools 23.0.3                                        
  build-tools;24.0.0                                                              | 24.0.0            | Android SDK Build-Tools 24                                            
  build-tools;24.0.1                                                              | 24.0.1            | Android SDK Build-Tools 24.0.1                                        
  build-tools;24.0.2                                                              | 24.0.2            | Android SDK Build-Tools 24.0.2                                        
  build-tools;24.0.3                                                              | 24.0.3            | Android SDK Build-Tools 24.0.3                                        
  build-tools;25.0.0                                                              | 25.0.0            | Android SDK Build-Tools 25                                            
  build-tools;25.0.1                                                              | 25.0.1            | Android SDK Build-Tools 25.0.1                                        
  build-tools;25.0.2                                                              | 25.0.2            | Android SDK Build-Tools 25.0.2                                        
  build-tools;25.0.3                                                              | 25.0.3            | Android SDK Build-Tools 25.0.3                                        
  build-tools;26.0.0                                                              | 26.0.0            | Android SDK Build-Tools 26                                            
  build-tools;26.0.1                                                              | 26.0.1            | Android SDK Build-Tools 26.0.1                                        
  build-tools;26.0.2                                                              | 26.0.2            | Android SDK Build-Tools 26.0.2                                        
  build-tools;26.0.3                                                              | 26.0.3            | Android SDK Build-Tools 26.0.3                                        
  build-tools;27.0.0                                                              | 27.0.0            | Android SDK Build-Tools 27                                            
  build-tools;27.0.1                                                              | 27.0.1            | Android SDK Build-Tools 27.0.1                                        
  build-tools;27.0.2                                                              | 27.0.2            | Android SDK Build-Tools 27.0.2                                        
  build-tools;27.0.3                                                              | 27.0.3            | Android SDK Build-Tools 27.0.3                                        
  build-tools;28.0.0                                                              | 28.0.0            | Android SDK Build-Tools 28                                            
  build-tools;28.0.1                                                              | 28.0.1            | Android SDK Build-Tools 28.0.1                                        
  build-tools;28.0.2                                                              | 28.0.2            | Android SDK Build-Tools 28.0.2                                        
  build-tools;28.0.3                                                              | 28.0.3            | Android SDK Build-Tools 28.0.3                                        
  build-tools;29.0.0                                                              | 29.0.0            | Android SDK Build-Tools 29                                            
  build-tools;29.0.1                                                              | 29.0.1            | Android SDK Build-Tools 29.0.1                                        
  build-tools;29.0.2                                                              | 29.0.2            | Android SDK Build-Tools 29.0.2                                        
  build-tools;29.0.3                                                              | 29.0.3            | Android SDK Build-Tools 29.0.3                                        
  build-tools;30.0.0                                                              | 30.0.0            | Android SDK Build-Tools 30                                            
  build-tools;30.0.1                                                              | 30.0.1            | Android SDK Build-Tools 30.0.1                                        
  build-tools;30.0.2                                                              | 30.0.2            | Android SDK Build-Tools 30.0.2                                        
  build-tools;30.0.3                                                              | 30.0.3            | Android SDK Build-Tools 30.0.3                                        
  build-tools;31.0.0                                                              | 31.0.0            | Android SDK Build-Tools 31                                            
  build-tools;32.0.0                                                              | 32.0.0            | Android SDK Build-Tools 32                                            
  build-tools;32.1.0-rc1                                                          | 32.1.0 rc1        | Android SDK Build-Tools 32.1-rc1                                      
  build-tools;33.0.0                                                              | 33.0.0            | Android SDK Build-Tools 33                                            
  build-tools;33.0.1                                                              | 33.0.1            | Android SDK Build-Tools 33.0.1                                        
  build-tools;33.0.2                                                              | 33.0.2            | Android SDK Build-Tools 33.0.2                                        
  build-tools;33.0.3                                                              | 33.0.3            | Android SDK Build-Tools 33.0.3                                        
  build-tools;34.0.0                                                              | 34.0.0            | Android SDK Build-Tools 34                                            
  build-tools;34.0.0-rc1                                                          | 34.0.0 rc1        | Android SDK Build-Tools 34-rc1                                        
  build-tools;34.0.0-rc2                                                          | 34.0.0 rc2        | Android SDK Build-Tools 34-rc2                                        
  build-tools;34.0.0-rc3                                                          | 34.0.0 rc3        | Android SDK Build-Tools 34-rc3                                        
  build-tools;35.0.0                                                              | 35.0.0            | Android SDK Build-Tools 35                                            
  build-tools;35.0.0-rc1                                                          | 35.0.0 rc1        | Android SDK Build-Tools 35-rc1                                        
  build-tools;35.0.0-rc2                                                          | 35.0.0 rc2        | Android SDK Build-Tools 35-rc2                                        
  build-tools;35.0.0-rc3                                                          | 35.0.0 rc3        | Android SDK Build-Tools 35-rc3                                        
  build-tools;35.0.0-rc4                                                          | 35.0.0 rc4        | Android SDK Build-Tools 35-rc4                                        
  build-tools;35.0.1                                                              | 35.0.1            | Android SDK Build-Tools 35.0.1                                        
  build-tools;36.0.0                                                              | 36.0.0            | Android SDK Build-Tools 36                                            
  build-tools;36.0.0-rc1                                                          | 36.0.0 rc1        | Android SDK Build-Tools 36-rc1                                        
  build-tools;36.0.0-rc3                                                          | 36.0.0 rc3        | Android SDK Build-Tools 36-rc3                                        
  build-tools;36.0.0-rc4                                                          | 36.0.0 rc4        | Android SDK Build-Tools 36-rc4                                        
  build-tools;36.0.0-rc5                                                          | 36.0.0 rc5        | Android SDK Build-Tools 36-rc5                                        
  cmake;3.10.2.4988404                                                            | 3.10.2            | CMake 3.10.2.4988404                                                  
  cmake;3.18.1                                                                    | 3.18.1            | CMake 3.18.1                                                          
  cmake;3.22.1                                                                    | 3.22.1            | CMake 3.22.1                                                          
  cmake;3.30.3                                                                    | 3.30.3            | CMake 3.30.3                                                          
  cmake;3.30.4                                                                    | 3.30.4            | CMake 3.30.4                                                          
  cmake;3.30.5                                                                    | 3.30.5            | CMake 3.30.5                                                          
  cmake;3.31.0                                                                    | 3.31.0            | CMake 3.31.0                                                          
  cmake;3.31.1                                                                    | 3.31.1            | CMake 3.31.1                                                          
  cmake;3.31.4                                                                    | 3.31.4            | CMake 3.31.4                                                          
  cmake;3.31.5                                                                    | 3.31.5            | CMake 3.31.5                                                          
  cmake;3.31.6                                                                    | 3.31.6            | CMake 3.31.6                                                          
  cmake;3.6.4111459                                                               | 3.6.4111459       | CMake 3.6.4111459                                                     
  cmake;4.0.2                                                                     | 4.0.2             | CMake 4.0.2                                                           
  cmake;4.0.3                                                                     | 4.0.3             | CMake 4.0.3                                                           
  cmdline-tools;1.0                                                               | 1.0               | Android SDK Command-line Tools                                        
  cmdline-tools;10.0                                                              | 10.0              | Android SDK Command-line Tools                                        
  cmdline-tools;11.0                                                              | 11.0              | Android SDK Command-line Tools                                        
  cmdline-tools;12.0                                                              | 12.0              | Android SDK Command-line Tools                                        
  cmdline-tools;13.0                                                              | 13.0              | Android SDK Command-line Tools                                        
  cmdline-tools;16.0                                                              | 16.0              | Android SDK Command-line Tools                                        
  cmdline-tools;16.0-alpha01                                                      | 16.0.0 rc1        | Android SDK Command-line Tools                                        
  cmdline-tools;17.0                                                              | 17.0              | Android SDK Command-line Tools                                        
  cmdline-tools;19.0                                                              | 19.0              | Android SDK Command-line Tools                                        
  cmdline-tools;19.0-alpha01                                                      | 19.0.0 rc1        | Android SDK Command-line Tools                                        
  cmdline-tools;2.1                                                               | 2.1               | Android SDK Command-line Tools                                        
  cmdline-tools;3.0                                                               | 3.0               | Android SDK Command-line Tools                                        
  cmdline-tools;4.0                                                               | 4.0               | Android SDK Command-line Tools                                        
  cmdline-tools;5.0                                                               | 5.0               | Android SDK Command-line Tools                                        
  cmdline-tools;6.0                                                               | 6.0               | Android SDK Command-line Tools                                        
  cmdline-tools;7.0                                                               | 7.0               | Android SDK Command-line Tools                                        
  cmdline-tools;8.0                                                               | 8.0               | Android SDK Command-line Tools                                        
  cmdline-tools;9.0                                                               | 9.0               | Android SDK Command-line Tools                                        
  cmdline-tools;latest                                                            | 19.0              | Android SDK Command-line Tools (latest)                               
  emulator                                                                        | 36.1.9            | Android Emulator                                                      
  extras;android;m2repository                                                     | 47.0.0            | Android Support Repository                                            
  extras;google;auto                                                              | 2.0               | Android Auto Desktop Head Unit Emulator                               
  extras;google;google_play_services                                              | 49                | Google Play services                                                  
  extras;google;instantapps                                                       | 1.9.0             | Google Play Instant Development SDK (Deprecated)                      
  extras;google;m2repository                                                      | 58                | Google Repository                                                     
  extras;google;market_apk_expansion                                              | 1                 | Google Play APK Expansion library                                     
  extras;google;market_licensing                                                  | 1                 | Google Play Licensing Library                                         
  extras;google;simulators                                                        | 1                 | Android Auto API Simulators                                           
  extras;google;webdriver                                                         | 2                 | Google Web Driver                                                     
  ndk-bundle                                                                      | 22.1.7171670      | NDK                                                                   
  ndk;16.1.4479499                                                                | 16.1.4479499      | NDK (Side by side) 16.1.4479499                                       
  ndk;17.2.4988734                                                                | 17.2.4988734      | NDK (Side by side) 17.2.4988734                                       
  ndk;18.1.5063045                                                                | 18.1.5063045      | NDK (Side by side) 18.1.5063045                                       
  ndk;19.2.5345600                                                                | 19.2.5345600      | NDK (Side by side) 19.2.5345600                                       
  ndk;20.0.5594570                                                                | 20.0.5594570      | NDK (Side by side) 20.0.5594570                                       
  ndk;20.1.5948944                                                                | 20.1.5948944      | NDK (Side by side) 20.1.5948944                                       
  ndk;21.0.6113669                                                                | 21.0.6113669      | NDK (Side by side) 21.0.6113669                                       
  ndk;21.1.6352462                                                                | 21.1.6352462      | NDK (Side by side) 21.1.6352462                                       
  ndk;21.2.6472646                                                                | 21.2.6472646      | NDK (Side by side) 21.2.6472646                                       
  ndk;21.3.6528147                                                                | 21.3.6528147      | NDK (Side by side) 21.3.6528147                                       
  ndk;21.4.7075529                                                                | 21.4.7075529      | NDK (Side by side) 21.4.7075529                                       
  ndk;22.0.7026061                                                                | 22.0.7026061      | NDK (Side by side) 22.0.7026061                                       
  ndk;22.1.7171670                                                                | 22.1.7171670      | NDK (Side by side) 22.1.7171670                                       
  ndk;23.0.7599858                                                                | 23.0.7599858      | NDK (Side by side) 23.0.7599858                                       
  ndk;23.1.7779620                                                                | 23.1.7779620      | NDK (Side by side) 23.1.7779620                                       
  ndk;23.2.8568313                                                                | 23.2.8568313      | NDK (Side by side) 23.2.8568313                                       
  ndk;24.0.8215888                                                                | 24.0.8215888      | NDK (Side by side) 24.0.8215888                                       
  ndk;25.0.8775105                                                                | 25.0.8775105      | NDK (Side by side) 25.0.8775105                                       
  ndk;25.1.8937393                                                                | 25.1.8937393      | NDK (Side by side) 25.1.8937393                                       
  ndk;25.2.9519653                                                                | 25.2.9519653      | NDK (Side by side) 25.2.9519653                                       
  ndk;26.0.10792818                                                               | 26.0.10792818     | NDK (Side by side) 26.0.10792818                                      
  ndk;26.1.10909125                                                               | 26.1.10909125     | NDK (Side by side) 26.1.10909125                                      
  ndk;26.2.11394342                                                               | 26.2.11394342     | NDK (Side by side) 26.2.11394342                                      
  ndk;26.3.11579264                                                               | 26.3.11579264     | NDK (Side by side) 26.3.11579264                                      
  ndk;27.0.11718014                                                               | 27.0.11718014 rc1 | NDK (Side by side) 27.0.11718014                                      
  ndk;27.0.11902837                                                               | 27.0.11902837 rc2 | NDK (Side by side) 27.0.11902837                                      
  ndk;27.0.12077973                                                               | 27.0.12077973     | NDK (Side by side) 27.0.12077973                                      
  ndk;27.1.12297006                                                               | 27.1.12297006     | NDK (Side by side) 27.1.12297006                                      
  ndk;27.2.12479018                                                               | 27.2.12479018     | NDK (Side by side) 27.2.12479018                                      
  ndk;27.3.13750724                                                               | 27.3.13750724     | NDK (Side by side) 27.3.13750724                                      
  ndk;28.0.12433566                                                               | 28.0.12433566 rc1 | NDK (Side by side) 28.0.12433566                                      
  ndk;28.0.12674087                                                               | 28.0.12674087 rc2 | NDK (Side by side) 28.0.12674087                                      
  ndk;28.0.12916984                                                               | 28.0.12916984 rc3 | NDK (Side by side) 28.0.12916984                                      
  ndk;28.0.13004108                                                               | 28.0.13004108     | NDK (Side by side) 28.0.13004108                                      
  ndk;28.1.13356709                                                               | 28.1.13356709     | NDK (Side by side) 28.1.13356709                                      
  ndk;28.2.13676358                                                               | 28.2.13676358     | NDK (Side by side) 28.2.13676358                                      
  ndk;29.0.13113456                                                               | 29.0.13113456 rc1 | NDK (Side by side) 29.0.13113456                                      
  ndk;29.0.13599879                                                               | 29.0.13599879 rc2 | NDK (Side by side) 29.0.13599879                                      
  ndk;29.0.13846066                                                               | 29.0.13846066 rc3 | NDK (Side by side) 29.0.13846066                                      
  platform-tools                                                                  | 36.0.0            | Android SDK Platform-Tools                                            
  platforms;android-10                                                            | 2                 | Android SDK Platform 10                                               
  platforms;android-11                                                            | 2                 | Android SDK Platform 11                                               
  platforms;android-12                                                            | 3                 | Android SDK Platform 12                                               
  platforms;android-13                                                            | 1                 | Android SDK Platform 13                                               
  platforms;android-14                                                            | 4                 | Android SDK Platform 14                                               
  platforms;android-15                                                            | 5                 | Android SDK Platform 15                                               
  platforms;android-16                                                            | 5                 | Android SDK Platform 16                                               
  platforms;android-17                                                            | 3                 | Android SDK Platform 17                                               
  platforms;android-18                                                            | 3                 | Android SDK Platform 18                                               
  platforms;android-19                                                            | 4                 | Android SDK Platform 19                                               
  platforms;android-20                                                            | 2                 | Android SDK Platform 20                                               
  platforms;android-21                                                            | 2                 | Android SDK Platform 21                                               
  platforms;android-22                                                            | 2                 | Android SDK Platform 22                                               
  platforms;android-23                                                            | 3                 | Android SDK Platform 23                                               
  platforms;android-24                                                            | 2                 | Android SDK Platform 24                                               
  platforms;android-25                                                            | 3                 | Android SDK Platform 25                                               
  platforms;android-26                                                            | 2                 | Android SDK Platform 26                                               
  platforms;android-27                                                            | 3                 | Android SDK Platform 27                                               
  platforms;android-28                                                            | 6                 | Android SDK Platform 28                                               
  platforms;android-29                                                            | 5                 | Android SDK Platform 29                                               
  platforms;android-30                                                            | 3                 | Android SDK Platform 30                                               
  platforms;android-31                                                            | 1                 | Android SDK Platform 31                                               
  platforms;android-32                                                            | 1                 | Android SDK Platform 32                                               
  platforms;android-33                                                            | 3                 | Android SDK Platform 33                                               
  platforms;android-33-ext4                                                       | 1                 | Android SDK Platform 33-ext4                                          
  platforms;android-33-ext5                                                       | 1                 | Android SDK Platform 33-ext5                                          
  platforms;android-34                                                            | 3                 | Android SDK Platform 34                                               
  platforms;android-34-ext10                                                      | 1                 | Android SDK Platform 34-ext10                                         
  platforms;android-34-ext11                                                      | 1                 | Android SDK Platform 34-ext11                                         
  platforms;android-34-ext12                                                      | 1                 | Android SDK Platform 34-ext12                                         
  platforms;android-34-ext8                                                       | 1                 | Android SDK Platform 34-ext8                                          
  platforms;android-35                                                            | 2                 | Android SDK Platform 35                                               
  platforms;android-35-ext14                                                      | 1                 | Android SDK Platform 35-ext14                                         
  platforms;android-35-ext15                                                      | 1                 | Android SDK Platform 35-ext15                                         
  platforms;android-36                                                            | 2                 | Android SDK Platform 36                                               
  platforms;android-36-ext18                                                      | 1                 | Android SDK Platform 36-ext18                                         
  platforms;android-36-ext19                                                      | 1                 | Android SDK Platform 36-ext19                                         
  platforms;android-7                                                             | 3                 | Android SDK Platform 7                                                
  platforms;android-8                                                             | 3                 | Android SDK Platform 8                                                
  platforms;android-9                                                             | 2                 | Android SDK Platform 9                                                
  platforms;android-Baklava                                                       | 5                 | Android SDK Platform Baklava                                          
  skiaparser;1                                                                    | 6                 | Layout Inspector image server for API 29-30                           
  skiaparser;2                                                                    | 3                 | Layout Inspector image server for API S                               
  skiaparser;3                                                                    | 7                 | Layout Inspector image server for API 31-36                           
  sources;android-15                                                              | 2                 | Sources for Android 15                                                
  sources;android-16                                                              | 2                 | Sources for Android 16                                                
  sources;android-17                                                              | 1                 | Sources for Android 17                                                
  sources;android-18                                                              | 1                 | Sources for Android 18                                                
  sources;android-19                                                              | 2                 | Sources for Android 19                                                
  sources;android-20                                                              | 1                 | Sources for Android 20                                                
  sources;android-21                                                              | 1                 | Sources for Android 21                                                
  sources;android-22                                                              | 1                 | Sources for Android 22                                                
  sources;android-23                                                              | 1                 | Sources for Android 23                                                
  sources;android-24                                                              | 1                 | Sources for Android 24                                                
  sources;android-25                                                              | 1                 | Sources for Android 25                                                
  sources;android-26                                                              | 1                 | Sources for Android 26                                                
  sources;android-27                                                              | 1                 | Sources for Android 27                                                
  sources;android-28                                                              | 1                 | Sources for Android 28                                                
  sources;android-29                                                              | 1                 | Sources for Android 29                                                
  sources;android-30                                                              | 1                 | Sources for Android 30                                                
  sources;android-31                                                              | 1                 | Sources for Android 31                                                
  sources;android-32                                                              | 1                 | Sources for Android 32                                                
  sources;android-33                                                              | 1                 | Sources for Android 33                                                
  sources;android-34                                                              | 2                 | Sources for Android 34                                                
  sources;android-35                                                              | 1                 | Sources for Android 35                                                
  sources;android-36                                                              | 1                 | Sources for Android 36                                                
  system-images;android-10;default;armeabi-v7a                                    | 5                 | ARM EABI v7a System Image                                             
  system-images;android-10;default;x86                                            | 5                 | Intel x86 Atom System Image                                           
  system-images;android-10;google_apis;armeabi-v7a                                | 6                 | Google APIs ARM EABI v7a System Image                                 
  system-images;android-10;google_apis;x86                                        | 6                 | Google APIs Intel x86 Atom System Image                               
  system-images;android-14;default;armeabi-v7a                                    | 2                 | ARM EABI v7a System Image                                             
  system-images;android-15;default;armeabi-v7a                                    | 5                 | ARM EABI v7a System Image                                             
  system-images;android-15;default;x86                                            | 7                 | Intel x86 Atom System Image                                           
  system-images;android-15;google_apis;armeabi-v7a                                | 6                 | Google APIs ARM EABI v7a System Image                                 
  system-images;android-15;google_apis;x86                                        | 7                 | Google APIs Intel x86 Atom System Image                               
  system-images;android-16;default;armeabi-v7a                                    | 6                 | ARM EABI v7a System Image                                             
  system-images;android-16;default;mips                                           | 1                 | MIPS System Image                                                     
  system-images;android-16;default;x86                                            | 7                 | Intel x86 Atom System Image                                           
  system-images;android-16;google_apis;armeabi-v7a                                | 6                 | Google APIs ARM EABI v7a System Image                                 
  system-images;android-16;google_apis;x86                                        | 7                 | Google APIs Intel x86 Atom System Image                               
  system-images;android-17;default;armeabi-v7a                                    | 6                 | ARM EABI v7a System Image                                             
  system-images;android-17;default;mips                                           | 1                 | MIPS System Image                                                     
  system-images;android-17;default;x86                                            | 7                 | Intel x86 Atom System Image                                           
  system-images;android-17;google_apis;armeabi-v7a                                | 6                 | Google APIs ARM EABI v7a System Image                                 
  system-images;android-17;google_apis;x86                                        | 7                 | Google APIs Intel x86 Atom System Image                               
  system-images;android-18;default;armeabi-v7a                                    | 5                 | ARM EABI v7a System Image                                             
  system-images;android-18;default;x86                                            | 4                 | Intel x86 Atom System Image                                           
  system-images;android-18;google_apis;armeabi-v7a                                | 6                 | Google APIs ARM EABI v7a System Image                                 
  system-images;android-18;google_apis;x86                                        | 6                 | Google APIs Intel x86 Atom System Image                               
  system-images;android-19;default;armeabi-v7a                                    | 5                 | ARM EABI v7a System Image                                             
  system-images;android-19;default;x86                                            | 6                 | Intel x86 Atom System Image                                           
  system-images;android-19;google_apis;armeabi-v7a                                | 40                | Google APIs ARM EABI v7a System Image                                 
  system-images;android-19;google_apis;x86                                        | 40                | Google APIs Intel x86 Atom System Image                               
  system-images;android-21;android-tv;armeabi-v7a                                 | 3                 | Android TV ARM EABI v7a System Image                                  
  system-images;android-21;android-tv;x86                                         | 3                 | Android TV Intel x86 Atom System Image                                
  system-images;android-21;default;arm64-v8a                                      | 4                 | ARM 64 v8a System Image                                               
  system-images;android-21;default;armeabi-v7a                                    | 4                 | ARM EABI v7a System Image                                             
  system-images;android-21;default;x86                                            | 5                 | Intel x86 Atom System Image                                           
  system-images;android-21;default;x86_64                                         | 5                 | Intel x86_64 Atom System Image                                        
  system-images;android-21;google_apis;arm64-v8a                                  | 32                | Google APIs ARM 64 v8a System Image                                   
  system-images;android-21;google_apis;armeabi-v7a                                | 32                | Google APIs ARM EABI v7a System Image                                 
  system-images;android-21;google_apis;x86                                        | 32                | Google APIs Intel x86 Atom System Image                               
  system-images;android-21;google_apis;x86_64                                     | 32                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-22;android-tv;x86                                         | 3                 | Android TV Intel x86 Atom System Image                                
  system-images;android-22;default;arm64-v8a                                      | 2                 | ARM 64 v8a System Image                                               
  system-images;android-22;default;armeabi-v7a                                    | 2                 | ARM EABI v7a System Image                                             
  system-images;android-22;default;x86                                            | 6                 | Intel x86 Atom System Image                                           
  system-images;android-22;default;x86_64                                         | 6                 | Intel x86_64 Atom System Image                                        
  system-images;android-22;google_apis;arm64-v8a                                  | 26                | Google APIs ARM 64 v8a System Image                                   
  system-images;android-22;google_apis;armeabi-v7a                                | 26                | Google APIs ARM EABI v7a System Image                                 
  system-images;android-22;google_apis;x86                                        | 26                | Google APIs Intel x86 Atom System Image                               
  system-images;android-22;google_apis;x86_64                                     | 26                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-23;android-tv;armeabi-v7a                                 | 12                | Android TV ARM EABI v7a System Image                                  
  system-images;android-23;android-tv;x86                                         | 21                | Android TV Intel x86 Atom System Image                                
  system-images;android-23;default;arm64-v8a                                      | 7                 | ARM 64 v8a System Image                                               
  system-images;android-23;default;armeabi-v7a                                    | 6                 | ARM EABI v7a System Image                                             
  system-images;android-23;default;x86                                            | 10                | Intel x86 Atom System Image                                           
  system-images;android-23;default;x86_64                                         | 10                | Intel x86_64 Atom System Image                                        
  system-images;android-23;google_apis;arm64-v8a                                  | 33                | Google APIs ARM 64 v8a System Image                                   
  system-images;android-23;google_apis;armeabi-v7a                                | 33                | Google APIs ARM EABI v7a System Image                                 
  system-images;android-23;google_apis;x86                                        | 33                | Google APIs Intel x86 Atom System Image                               
  system-images;android-23;google_apis;x86_64                                     | 33                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-24;android-tv;x86                                         | 22                | Android TV Intel x86 Atom System Image                                
  system-images;android-24;default;arm64-v8a                                      | 9                 | ARM 64 v8a System Image                                               
  system-images;android-24;default;armeabi-v7a                                    | 7                 | ARM EABI v7a System Image                                             
  system-images;android-24;default;x86                                            | 8                 | Intel x86 Atom System Image                                           
  system-images;android-24;default;x86_64                                         | 8                 | Intel x86_64 Atom System Image                                        
  system-images;android-24;google_apis;arm64-v8a                                  | 29                | Google APIs ARM 64 v8a System Image                                   
  system-images;android-24;google_apis;x86                                        | 27                | Google APIs Intel x86 Atom System Image                               
  system-images;android-24;google_apis;x86_64                                     | 27                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-24;google_apis_playstore;x86                              | 19                | Google Play Intel x86 Atom System Image                               
  system-images;android-25;android-tv;x86                                         | 16                | Android TV Intel x86 Atom System Image                                
  system-images;android-25;android-wear;armeabi-v7a                               | 3                 | Android Wear ARM EABI v7a System Image                                
  system-images;android-25;android-wear;x86                                       | 3                 | Android Wear Intel x86 Atom System Image                              
  system-images;android-25;default;arm64-v8a                                      | 2                 | ARM 64 v8a System Image                                               
  system-images;android-25;default;x86                                            | 1                 | Intel x86 Atom System Image                                           
  system-images;android-25;default;x86_64                                         | 1                 | Intel x86_64 Atom System Image                                        
  system-images;android-25;google_apis;arm64-v8a                                  | 20                | Google APIs ARM 64 v8a System Image                                   
  system-images;android-25;google_apis;armeabi-v7a                                | 18                | Google APIs ARM EABI v7a System Image                                 
  system-images;android-25;google_apis;x86                                        | 18                | Google APIs Intel x86 Atom System Image                               
  system-images;android-25;google_apis;x86_64                                     | 18                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-25;google_apis_playstore;x86                              | 9                 | Google Play Intel x86 Atom System Image                               
  system-images;android-26;android-tv;x86                                         | 14                | Android TV Intel x86 Atom System Image                                
  system-images;android-26;android-wear;x86                                       | 4                 | Android Wear Intel x86 Atom System Image                              
  system-images;android-26;default;arm64-v8a                                      | 2                 | ARM 64 v8a System Image                                               
  system-images;android-26;default;x86                                            | 1                 | Intel x86 Atom System Image                                           
  system-images;android-26;default;x86_64                                         | 1                 | Intel x86_64 Atom System Image                                        
  system-images;android-26;google_apis;arm64-v8a                                  | 3                 | Google APIs ARM 64 v8a System Image                                   
  system-images;android-26;google_apis;x86                                        | 16                | Google APIs Intel x86 Atom System Image                               
  system-images;android-26;google_apis;x86_64                                     | 16                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-26;google_apis_playstore;x86                              | 7                 | Google Play Intel x86 Atom System Image                               
  system-images;android-27;android-tv;x86                                         | 9                 | Android TV Intel x86 Atom System Image                                
  system-images;android-27;default;arm64-v8a                                      | 2                 | ARM 64 v8a System Image                                               
  system-images;android-27;default;x86                                            | 1                 | Intel x86 Atom System Image                                           
  system-images;android-27;default;x86_64                                         | 1                 | Intel x86_64 Atom System Image                                        
  system-images;android-27;google_apis;arm64-v8a                                  | 3                 | Google APIs ARM 64 v8a System Image                                   
  system-images;android-27;google_apis;x86                                        | 11                | Google APIs Intel x86 Atom System Image                               
  system-images;android-27;google_apis_playstore;x86                              | 3                 | Google Play Intel x86 Atom System Image                               
  system-images;android-28;android-tv;x86                                         | 10                | Android TV Intel x86 Atom System Image                                
  system-images;android-28;android-wear;x86                                       | 9                 | Wear OS Intel x86 Atom System Image                                   
  system-images;android-28;default;arm64-v8a                                      | 2                 | ARM 64 v8a System Image                                               
  system-images;android-28;default;x86                                            | 4                 | Intel x86 Atom System Image                                           
  system-images;android-28;default;x86_64                                         | 4                 | Intel x86_64 Atom System Image                                        
  system-images;android-28;google_apis;arm64-v8a                                  | 2                 | Google APIs ARM 64 v8a System Image                                   
  system-images;android-28;google_apis;x86                                        | 12                | Google APIs Intel x86 Atom System Image                               
  system-images;android-28;google_apis;x86_64                                     | 11                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-28;google_apis_playstore;arm64-v8a                        | 2                 | Google ARM64-V8a Play ARM 64 v8a System Image                         
  system-images;android-28;google_apis_playstore;x86                              | 9                 | Google Play Intel x86 Atom System Image                               
  system-images;android-28;google_apis_playstore;x86_64                           | 8                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-29;android-tv;x86                                         | 3                 | Android TV Intel x86 Atom System Image                                
  system-images;android-29;default;arm64-v8a                                      | 8                 | ARM 64 v8a System Image                                               
  system-images;android-29;default;x86                                            | 8                 | Intel x86 Atom System Image                                           
  system-images;android-29;default;x86_64                                         | 8                 | Intel x86_64 Atom System Image                                        
  system-images;android-29;google_apis;arm64-v8a                                  | 13                | Google APIs ARM 64 v8a System Image                                   
  system-images;android-29;google_apis;x86                                        | 13                | Google APIs Intel x86 Atom System Image                               
  system-images;android-29;google_apis;x86_64                                     | 13                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-29;google_apis_playstore;arm64-v8a                        | 9                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-29;google_apis_playstore;x86                              | 9                 | Google Play Intel x86 Atom System Image                               
  system-images;android-29;google_apis_playstore;x86_64                           | 9                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-30;android-tv;x86                                         | 4                 | Android TV Intel x86 Atom System Image                                
  system-images;android-30;android-wear-cn;arm64-v8a                              | 12                | China version of Wear OS 3 ARM 64 v8a System Image                    
  system-images;android-30;android-wear-cn;x86                                    | 12                | China version of Wear OS 3 Intel x86 Atom System Image                
  system-images;android-30;android-wear;arm64-v8a                                 | 12                | Wear OS 3 ARM 64 v8a System Image                                     
  system-images;android-30;android-wear;x86                                       | 12                | Wear OS 3 Intel x86 Atom System Image                                 
  system-images;android-30;aosp_atd;arm64-v8a                                     | 2                 | AOSP ATD ARM 64 v8a System Image                                      
  system-images;android-30;aosp_atd;x86                                           | 1                 | AOSP ATD Intel x86 Atom System Image                                  
  system-images;android-30;aosp_atd;x86_64                                        | 2                 | AOSP ATD Intel x86_64 Atom System Image                               
  system-images;android-30;default;arm64-v8a                                      | 2                 | ARM 64 v8a System Image                                               
  system-images;android-30;default;x86_64                                         | 11                | Intel x86_64 Atom System Image                                        
  system-images;android-30;google-tv;x86                                          | 4                 | Google TV Intel x86 Atom System Image                                 
  system-images;android-30;google_apis;arm64-v8a                                  | 16                | Google APIs ARM 64 v8a System Image                                   
  system-images;android-30;google_apis;x86                                        | 16                | Google APIs Intel x86 Atom System Image                               
  system-images;android-30;google_apis;x86_64                                     | 16                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-30;google_apis_playstore;arm64-v8a                        | 10                | Google Play ARM 64 v8a System Image                                   
  system-images;android-30;google_apis_playstore;x86                              | 9                 | Google Play Intel x86 Atom System Image                               
  system-images;android-30;google_apis_playstore;x86_64                           | 10                | Google Play Intel x86_64 Atom System Image                            
  system-images;android-30;google_atd;arm64-v8a                                   | 2                 | Google APIs ATD ARM 64 v8a System Image                               
  system-images;android-30;google_atd;x86                                         | 1                 | Google APIs ATD Intel x86 Atom System Image                           
  system-images;android-30;google_atd;x86_64                                      | 2                 | Google APIs ATD Intel x86_64 Atom System Image                        
  system-images;android-31;android-tv;arm64-v8a                                   | 4                 | Android TV ARM 64 v8a System Image                                    
  system-images;android-31;android-tv;x86                                         | 4                 | Android TV Intel x86 Atom System Image                                
  system-images;android-31;aosp_atd;arm64-v8a                                     | 1                 | AOSP ATD ARM 64 v8a System Image                                      
  system-images;android-31;aosp_atd;x86_64                                        | 2                 | AOSP ATD Intel x86_64 Atom System Image                               
  system-images;android-31;default;arm64-v8a                                      | 4                 | ARM 64 v8a System Image                                               
  system-images;android-31;default;x86_64                                         | 5                 | Intel x86_64 Atom System Image                                        
  system-images;android-31;google-tv;arm64-v8a                                    | 4                 | Google TV ARM 64 v8a System Image                                     
  system-images;android-31;google-tv;x86                                          | 4                 | Google TV Intel x86 Atom System Image                                 
  system-images;android-31;google_apis;arm64-v8a                                  | 11                | Google APIs ARM 64 v8a System Image                                   
  system-images;android-31;google_apis;x86_64                                     | 14                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-31;google_apis_playstore;arm64-v8a                        | 9                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-31;google_apis_playstore;x86_64                           | 9                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-31;google_atd;arm64-v8a                                   | 1                 | Google APIs ATD ARM 64 v8a System Image                               
  system-images;android-31;google_atd;x86_64                                      | 2                 | Google APIs ATD Intel x86_64 Atom System Image                        
  system-images;android-32;android-desktop;arm64-v8a                              | 5                 | Desktop ARM 64 v8a System Image                                       
  system-images;android-32;android-desktop;x86_64                                 | 5                 | Desktop Intel x86_64 Atom System Image                                
  system-images;android-32;aosp_atd;arm64-v8a                                     | 1                 | AOSP ATD ARM 64 v8a System Image                                      
  system-images;android-32;aosp_atd;x86_64                                        | 1                 | AOSP ATD Intel x86_64 Atom System Image                               
  system-images;android-32;default;arm64-v8a                                      | 2                 | ARM 64 v8a System Image                                               
  system-images;android-32;default;x86_64                                         | 2                 | Intel x86_64 Atom System Image                                        
  system-images;android-32;google_apis;arm64-v8a                                  | 8                 | Google APIs ARM 64 v8a System Image                                   
  system-images;android-32;google_apis;x86_64                                     | 8                 | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-32;google_apis_playstore;arm64-v8a                        | 4                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-32;google_apis_playstore;x86_64                           | 4                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-32;google_atd;arm64-v8a                                   | 1                 | Google APIs ATD ARM 64 v8a System Image                               
  system-images;android-32;google_atd;x86_64                                      | 1                 | Google APIs ATD Intel x86_64 Atom System Image                        
  system-images;android-33-ext4;google_apis_playstore;arm64-v8a                   | 1                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-33-ext4;google_apis_playstore;x86_64                      | 1                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-33-ext5;google_apis_playstore;arm64-v8a                   | 2                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-33-ext5;google_apis_playstore;x86_64                      | 2                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-33;android-automotive-distant-display-playstore;arm64-v8a | 2                 | Automotive Distant Display with Google Play arm64-v8a System Image    
  system-images;android-33;android-automotive-distant-display-playstore;x86_64    | 2                 | Automotive Distant Display with Google Play x86_64 System Image       
  system-images;android-33;android-automotive;arm64-v8a                           | 5                 | Android Automotive with Google APIs arm64-v8a System Image            
  system-images;android-33;android-automotive;x86_64                              | 5                 | Android Automotive with Google APIs x86_64 System Image               
  system-images;android-33;android-desktop;arm64-v8a                              | 4                 | Desktop ARM 64 v8a System Image                                       
  system-images;android-33;android-desktop;x86_64                                 | 4                 | Desktop Intel x86_64 Atom System Image                                
  system-images;android-33;android-tv;arm64-v8a                                   | 5                 | Android TV ARM 64 v8a System Image                                    
  system-images;android-33;android-tv;x86                                         | 5                 | Android TV Intel x86 Atom System Image                                
  system-images;android-33;android-wear;arm64-v8a                                 | 4                 | Wear OS 4 ARM 64 v8a System Image                                     
  system-images;android-33;android-wear;x86_64                                    | 4                 | Wear OS 4 Intel x86_64 Atom System Image                              
  system-images;android-33;aosp_atd;arm64-v8a                                     | 2                 | AOSP ATD ARM 64 v8a System Image                                      
  system-images;android-33;aosp_atd;x86_64                                        | 2                 | AOSP ATD Intel x86_64 Atom System Image                               
  system-images;android-33;default;arm64-v8a                                      | 2                 | ARM 64 v8a System Image                                               
  system-images;android-33;default;x86_64                                         | 2                 | Intel x86_64 Atom System Image                                        
  system-images;android-33;google-tv;arm64-v8a                                    | 5                 | Google TV ARM 64 v8a System Image                                     
  system-images;android-33;google-tv;x86                                          | 5                 | Google TV Intel x86 Atom System Image                                 
  system-images;android-33;google_apis;arm64-v8a                                  | 17                | Google APIs ARM 64 v8a System Image                                   
  system-images;android-33;google_apis;x86_64                                     | 17                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-33;google_apis_playstore;arm64-v8a                        | 9                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-33;google_apis_playstore;x86_64                           | 9                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-33;google_atd;arm64-v8a                                   | 2                 | Google APIs ATD ARM 64 v8a System Image                               
  system-images;android-33;google_atd;x86_64                                      | 2                 | Google APIs ATD Intel x86_64 Atom System Image                        
  system-images;android-34-ext10;google_apis_playstore;arm64-v8a                  | 2                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-34-ext10;google_apis_playstore;x86_64                     | 2                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-34-ext11;google_apis_playstore;arm64-v8a                  | 1                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-34-ext11;google_apis_playstore;x86_64                     | 1                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-34-ext12;google_apis_playstore;arm64-v8a                  | 1                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-34-ext12;google_apis_playstore;x86_64                     | 1                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-34-ext8;google_apis_playstore;arm64-v8a                   | 2                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-34-ext8;google_apis_playstore;x86_64                      | 2                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-34-ext9;android-automotive-playstore;arm64-v8a            | 4                 | Android Automotive with Google Play arm64-v8a System Image            
  system-images;android-34-ext9;android-automotive-playstore;x86_64               | 4                 | Android Automotive with Google Play x86_64 System Image               
  system-images;android-34-ext9;android-automotive;arm64-v8a                      | 5                 | Android Automotive with Google APIs arm64-v8a System Image            
  system-images;android-34-ext9;android-automotive;x86_64                         | 5                 | Android Automotive with Google APIs x86_64 System Image               
  system-images;android-34;android-desktop;arm64-v8a                              | 1                 | Desktop ARM 64 v8a System Image                                       
  system-images;android-34;android-desktop;x86_64                                 | 1                 | Desktop Intel x86_64 Atom System Image                                
  system-images;android-34;android-tv;arm64-v8a                                   | 3                 | Android TV ARM 64 v8a System Image                                    
  system-images;android-34;android-tv;x86                                         | 3                 | Android TV Intel x86 Atom System Image                                
  system-images;android-34;android-wear;arm64-v8a                                 | 1                 | Wear OS 5 ARM 64 v8a System Image                                     
  system-images;android-34;android-wear;x86_64                                    | 1                 | Wear OS 5 Intel x86_64 Atom System Image                              
  system-images;android-34;aosp_atd;arm64-v8a                                     | 2                 | AOSP ATD ARM 64 v8a System Image                                      
  system-images;android-34;aosp_atd;x86_64                                        | 2                 | AOSP ATD Intel x86_64 Atom System Image                               
  system-images;android-34;default;arm64-v8a                                      | 4                 | ARM 64 v8a System Image                                               
  system-images;android-34;default;x86_64                                         | 4                 | Intel x86_64 Atom System Image                                        
  system-images;android-34;google-tv;arm64-v8a                                    | 3                 | Google TV ARM 64 v8a System Image                                     
  system-images;android-34;google-tv;x86                                          | 3                 | Google TV Intel x86 Atom System Image                                 
  system-images;android-34;google-xr;arm64-v8a                                    | 5                 | Google Play XR ARM 64 v8a System Image                                
  system-images;android-34;google-xr;x86_64                                       | 5                 | Google Play XR Intel x86_64 Atom System Image                         
  system-images;android-34;google_apis;arm64-v8a                                  | 14                | Google APIs ARM 64 v8a System Image                                   
  system-images;android-34;google_apis;x86_64                                     | 14                | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-34;google_apis_playstore;arm64-v8a                        | 14                | Google Play ARM 64 v8a System Image                                   
  system-images;android-34;google_apis_playstore;x86_64                           | 14                | Google Play Intel x86_64 Atom System Image                            
  system-images;android-34;google_atd;arm64-v8a                                   | 1                 | Google APIs ATD ARM 64 System Image                                   
  system-images;android-34;google_atd;x86_64                                      | 1                 | Google APIs ATD Intel x86_64 Atom System Image                        
  system-images;android-35-ext14;google_apis_playstore;arm64-v8a                  | 1                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-35-ext14;google_apis_playstore;x86_64                     | 1                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-35-ext15;android-wear;arm64-v8a                           | 1                 | Wear OS 5.1 ARM 64 v8a System Image                                   
  system-images;android-35-ext15;android-wear;x86_64                              | 1                 | Wear OS 5.1 Intel x86_64 Atom System Image                            
  system-images;android-35-ext15;google_apis;arm64-v8a                            | 1                 | Google APIs ARM 64 v8a System Image                                   
  system-images;android-35-ext15;google_apis;x86_64                               | 1                 | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-35-ext15;google_apis_playstore;arm64-v8a                  | 1                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-35-ext15;google_apis_playstore;x86_64                     | 1                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-35;aosp_atd;arm64-v8a                                     | 1                 | AOSP ATD ARM 64 System Image                                          
  system-images;android-35;aosp_atd;x86_64                                        | 1                 | AOSP ATD Intel x86_64 Atom System Image                               
  system-images;android-35;default;arm64-v8a                                      | 2                 | ARM 64 v8a System Image                                               
  system-images;android-35;default;x86_64                                         | 2                 | Intel x86_64 Atom System Image                                        
  system-images;android-35;google_apis;arm64-v8a                                  | 9                 | Google APIs ARM 64 v8a System Image                                   
  system-images;android-35;google_apis;x86_64                                     | 9                 | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-35;google_apis_playstore;arm64-v8a                        | 9                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-35;google_apis_playstore;x86_64                           | 9                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-35;google_apis_playstore_ps16k;arm64-v8a                  | 5                 | Pre-Release 16 KB Page Size Google Play ARM 64 v8a System Image       
  system-images;android-35;google_apis_playstore_ps16k;x86_64                     | 5                 | Pre-Release 16 KB Page Size Google Play Intel x86_64 Atom System Image
  system-images;android-35;google_apis_playstore_tablet;arm64-v8a                 | 9                 | Google Play Tablet ARM 64 v8a System Image                            
  system-images;android-35;google_apis_playstore_tablet;x86_64                    | 9                 | Google Play Tablet Intel x86_64 Atom System Image                     
  system-images;android-35;google_apis_ps16k;arm64-v8a                            | 5                 | Pre-Release 16 KB Page Size Google APIs ARM 64 v8a System Image       
  system-images;android-35;google_apis_ps16k;x86_64                               | 5                 | Pre-Release 16 KB Page Size Google APIs Intel x86_64 Atom System Image
  system-images;android-35;google_apis_tablet;arm64-v8a                           | 2                 | Google APIs Tablet ARM 64 v8a System Image                            
  system-images;android-35;google_apis_tablet;x86_64                              | 2                 | Google APIs Tablet Intel x86_64 Atom System Image                     
  system-images;android-35;google_atd;arm64-v8a                                   | 1                 | Google APIs ATD ARM 64 System Image                                   
  system-images;android-35;google_atd;x86_64                                      | 1                 | Google APIs ATD Intel x86_64 Atom System Image                        
  system-images;android-36-ext18;google_apis;arm64-v8a                            | 1                 | Google APIs ARM 64 v8a System Image                                   
  system-images;android-36-ext18;google_apis;x86_64                               | 1                 | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-36-ext18;google_apis_playstore;arm64-v8a                  | 1                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-36-ext18;google_apis_playstore;x86_64                     | 1                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-36-ext19;google_apis;arm64-v8a                            | 1                 | Google APIs ARM 64 v8a System Image                                   
  system-images;android-36-ext19;google_apis;x86_64                               | 1                 | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-36-ext19;google_apis_playstore;arm64-v8a                  | 1                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-36-ext19;google_apis_playstore;x86_64                     | 1                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-36;android-wear-signed;arm64-v8a                          | 1                 | Wear OS 6.0 ARM 64 v8a System Image (signed)                          
  system-images;android-36;android-wear-signed;x86_64                             | 1                 | Wear OS 6.0 Intel x86_64 Atom System Image (signed)                   
  system-images;android-36;google-tv;arm64-v8a                                    | 1                 | Google TV ARM 64 v8a System Image                                     
  system-images;android-36;google-tv;x86                                          | 1                 | Google TV Intel x86 Atom System Image                                 
  system-images;android-36;google_apis;arm64-v8a                                  | 6                 | Google APIs ARM 64 v8a System Image                                   
  system-images;android-36;google_apis;x86_64                                     | 6                 | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-36;google_apis_playstore;arm64-v8a                        | 7                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-36;google_apis_playstore;x86_64                           | 7                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-36;google_apis_playstore_ps16k;arm64-v8a                  | 6                 | Pre-Release 16 KB Page Size Google Play ARM 64 v8a System Image       
  system-images;android-36;google_apis_playstore_ps16k;x86_64                     | 6                 | Pre-Release 16 KB Page Size Google Play Intel x86_64 Atom System Image
  system-images;android-36;google_apis_ps16k;arm64-v8a                            | 6                 | Pre-Release 16 KB Page Size Google APIs ARM 64 v8a System Image       
  system-images;android-36;google_apis_ps16k;x86_64                               | 6                 | Pre-Release 16 KB Page Size Google APIs Intel x86_64 Atom System Image
  system-images;android-Baklava;google_apis;arm64-v8a                             | 4                 | Google APIs ARM 64 v8a System Image                                   
  system-images;android-Baklava;google_apis;x86_64                                | 4                 | Google APIs Intel x86_64 Atom System Image                            
  system-images;android-Baklava;google_apis_playstore;arm64-v8a                   | 4                 | Google Play ARM 64 v8a System Image                                   
  system-images;android-Baklava;google_apis_playstore;x86_64                      | 4                 | Google Play Intel x86_64 Atom System Image                            
  system-images;android-Baklava;google_apis_playstore_ps16k;arm64-v8a             | 4                 | Pre-Release 16 KB Page Size Google Play ARM 64 v8a System Image       
  system-images;android-Baklava;google_apis_playstore_ps16k;x86_64                | 4                 | Pre-Release 16 KB Page Size Google Play Intel x86_64 Atom System Image
  system-images;android-Baklava;google_apis_ps16k;arm64-v8a                       | 4                 | Pre-Release 16 KB Page Size Google APIs ARM 64 v8a System Image       
  system-images;android-Baklava;google_apis_ps16k;x86_64                          | 4                 | Pre-Release 16 KB Page Size Google APIs Intel x86_64 Atom System Image

# Check that aidl can be executed
# Search for Aidl
# Run '/usr/local/lib/android/sdk/build-tools/36.0.0/aidl'
# Cwd None
Warning: : prerequisites.py is experimental and does not support all prerequisites yet.
# Downloading platform api target if necessary
Warning: : Please report any issues to the python-for-android issue tracker.
# Android packages installation done.
# Run ['/opt/hostedtoolcache/Python/3.9.23/x64/bin/python', '-m', 'pythonforandroid.toolchain', 'aab', '-h', '--color=always', '--storage-dir=/home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform/build-arm64-v8a_armeabi-v7a', '--ndk-api=21', '--ignore-setup-py', '--debug']
# Cwd /home/runner/work/telegram-bot-mobile/telegram-bot-mobile/.buildozer/android/platform/python-for-android
Warning: : prerequisites.py is experimental and does not support all prerequisites yet.
Warning: : Please report any issues to the python-for-android issue tracker.
usage: toolchain.py aab [-h] [--debug] [--color {always,never,auto}]
                        [--sdk-dir SDK_DIR] [--ndk-dir NDK_DIR]
                        [--android-api ANDROID_API]
                        [--ndk-version NDK_VERSION] [--ndk-api NDK_API]
                        [--symlink-bootstrap-files]
                        [--storage-dir STORAGE_DIR] [--arch ARCH]
                        [--dist-name DIST_NAME] [--requirements REQUIREMENTS]
                        [--recipe-blacklist RECIPE_BLACKLIST]
                        [--blacklist-requirements BLACKLIST_REQUIREMENTS]
                        [--bootstrap BOOTSTRAP] [--hook HOOK] [--force-build]
                        [--no-force-build] [--require-perfect-match]
                        [--no-require-perfect-match] [--allow-replace-dist]
                        [--no-allow-replace-dist]
                        [--local-recipes LOCAL_RECIPES]
                        [--activity-class-name ACTIVITY_CLASS_NAME]
                        [--service-class-name SERVICE_CLASS_NAME]
                        [--java-build-tool {auto,ant,gradle}] [--copy-libs]
                        [--no-copy-libs] [--add-asset ASSETS]
                        [--add-resource RESOURCES] [--private PRIVATE]
                        [--use-setup-py] [--ignore-setup-py] [--release]
                        [--with-debug-symbols] [--keystore KEYSTORE]
                        [--signkey SIGNKEY] [--keystorepw KEYSTOREPW]
                        [--signkeypw SIGNKEYPW]

optional arguments:
  -h, --help            show this help message and exit
  --debug               Display debug output and all build info
  --color {always,never,auto}
                        Enable or disable color output (default enabled on
                        tty)
  --sdk-dir SDK_DIR, --sdk_dir SDK_DIR
                        The filepath where the Android SDK is installed
  --ndk-dir NDK_DIR, --ndk_dir NDK_DIR
                        The filepath where the Android NDK is installed
  --android-api ANDROID_API, --android_api ANDROID_API
                        The Android API level to build against defaults to 33
                        if not specified.
  --ndk-version NDK_VERSION, --ndk_version NDK_VERSION
                        DEPRECATED: the NDK version is now found automatically
                        or not at all.
  --ndk-api NDK_API     The Android API level to compile against. This should
                        be your *minimal supported* API, not normally the same
                        as your --android-api. Defaults to min(ANDROID_API,
                        21) if not specified.
  --symlink-bootstrap-files, --ssymlink_bootstrap_files
                        If True, symlinks the bootstrap files creation. This
                        is useful for development only, it could also cause
                        weird problems.
  --storage-dir STORAGE_DIR
                        Primary storage directory for downloads and builds
                        (default: /home/runner/.local/share/python-for-
                        android)
  --arch ARCH           The archs to build for.
  --dist-name DIST_NAME, --dist_name DIST_NAME
                        The name of the distribution to use or create
  --requirements REQUIREMENTS
                        Dependencies of your app, should be recipe names or
                        Python modules. NOT NECESSARY if you are using Python
                        3 with --use-setup-py
  --recipe-blacklist RECIPE_BLACKLIST
                        Blacklist an internal recipe from use. Allows
                        disabling Python 3 core modules to save size
  --blacklist-requirements BLACKLIST_REQUIREMENTS
                        Blacklist an internal recipe from use. Allows
                        disabling Python 3 core modules to save size
  --bootstrap BOOTSTRAP
                        The bootstrap to build with. Leave unset to choose
                        automatically.
  --hook HOOK           Filename to a module that contains python-for-android
                        hooks
  --local-recipes LOCAL_RECIPES, --local_recipes LOCAL_RECIPES
                        Directory to look for local recipes
  --activity-class-name ACTIVITY_CLASS_NAME
                        The full java class name of the main activity
  --service-class-name SERVICE_CLASS_NAME
                        Full java package name of the PythonService class
  --java-build-tool {auto,ant,gradle}
                        The java build tool to use when packaging the APK,
                        defaults to automatically selecting an appropriate
                        tool.
  --add-asset ASSETS    Put this in the assets folder in the apk.
  --add-resource RESOURCES
                        Put this in the res folder in the apk.
  --private PRIVATE     the directory with the app source code files
                        (containing your main.py entrypoint)
  --use-setup-py        Process the setup.py of a project if present.
                        (Experimental!
  --ignore-setup-py     Don't run the setup.py of a project if present. This
                        may be required if the setup.py is not designed to
                        work inside p4a (e.g. by installing dependencies that
                        won't work or aren't desired on Android
  --release             Build your app as a non-debug release build. (Disables
                        gdb debugging among other things)
  --with-debug-symbols  Will keep debug symbols from `.so` files.
  --keystore KEYSTORE   Keystore for JAR signing key, will use jarsigner
                        default if not specified (release build only)
  --signkey SIGNKEY     Key alias to sign PARSER_APK. with (release build
                        only)
  --keystorepw KEYSTOREPW
                        Password for keystore
  --signkeypw SIGNKEYPW
                        Password for key alias

  Whether to force compilation of a new distribution

  --force-build
  --no-force-build      (this is the default)
  --require-perfect-match
  --no-require-perfect-match
                        (this is the default)
  --allow-replace-dist  (this is the default)
  --no-allow-replace-dist
  --copy-libs
  --no-copy-libs        (this is the default)
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
#     GITHUB_PATH = '/home/runner/work/_temp/_runner_file_commands/add_path_59e74bce-61d5-468c-a01c-632b3d034e7f'
#     GITHUB_ACTION = '__run_6'
#     JAVA_HOME = '/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/17.0.16-8/x64'
#     GITHUB_RUN_NUMBER = '17'
#     RUNNER_NAME = 'GitHub Actions 1000000016'
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
#     SYSTEMD_EXEC_PID = '1888'
#     GITHUB_SHA = '77b5cb5d8851291e653293543b83a54398dc96cf'
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
#     RUNNER_TRACKING_ID = 'github_7a36cde4-aaf4-4f81-b07d-b0c1a70d4c4b'
#     RUNNER_ARCH = 'X64'
#     MEMORY_PRESSURE_WATCH = '/sys/fs/cgroup/system.slice/hosted-compute-agent.service/memory.pressure'
#     RUNNER_TEMP = '/home/runner/work/_temp'
#     GITHUB_STATE = '/home/runner/work/_temp/_runner_file_commands/save_state_59e74bce-61d5-468c-a01c-632b3d034e7f'
#     EDGEWEBDRIVER = '/usr/local/share/edge_driver'
#     JAVA_HOME_21_X64 = '/usr/lib/jvm/temurin-21-jdk-amd64'
#     GITHUB_ENV = '/home/runner/work/_temp/_runner_file_commands/set_env_59e74bce-61d5-468c-a01c-632b3d034e7f'
#     GITHUB_EVENT_PATH = '/home/runner/work/_temp/_github_workflow/event.json'
#     INVOCATION_ID = '53ec6e3dff624281a15f9925b02ba7cf'
#     GITHUB_EVENT_NAME = 'push'
#     GITHUB_RUN_ID = '16908960890'
#     JAVA_HOME_17_X64 = '/opt/hostedtoolcache/Java_Temurin-Hotspot_jdk/17.0.16-8/x64'
#     ANDROID_NDK_HOME = '/usr/local/lib/android/sdk/ndk/23.2.8568313'
#     GITHUB_STEP_SUMMARY = '/home/runner/work/_temp/_runner_file_commands/step_summary_59e74bce-61d5-468c-a01c-632b3d034e7f'
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
#     GITHUB_WORKFLOW_SHA = '77b5cb5d8851291e653293543b83a54398dc96cf'
#     GOROOT_1_24_X64 = '/opt/hostedtoolcache/go/1.24.5/x64'
#     GITHUB_REF_NAME = 'main'
#     GITHUB_JOB = 'build'
#     LD_LIBRARY_PATH = '/opt/hostedtoolcache/Python/3.9.23/x64/lib'
#     XDG_RUNTIME_DIR = '/run/user/1001'
#     AZURE_EXTENSION_DIR = '/opt/az/azcliextensions'
#     GITHUB_REPOSITORY = 'qin-kin1514/telegram-bot-mobile'
#     Python2_ROOT_DIR = '/opt/hostedtoolcache/Python/3.9.23/x64'
#     GOROOT_1_22_X64 = '/opt/hostedtoolcache/go/1.22.12/x64'
#     CHROME_BIN = '/usr/bin/google-chrome'
#     ANDROID_NDK_ROOT = '/usr/local/lib/android/sdk/ndk/23.2.8568313'
#     GRADLE_OPTS = '-Xmx2048m -Dorg.gradle.jvmargs=-Xmx2048m'
#     GITHUB_RETENTION_DAYS = '90'
#     JOURNAL_STREAM = '9:11599'
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
#     GITHUB_OUTPUT = '/home/runner/work/_temp/_runner_file_commands/set_output_59e74bce-61d5-468c-a01c-632b3d034e7f'
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