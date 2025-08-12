Warning: Unexpected input(s) 'api-level', 'build-tools', 'ndk-version', 'cmake-version', valid inputs are ['cmdline-tools-version', 'accept-android-sdk-licenses', 'log-accepted-android-sdk-licenses', 'packages']
Run android-actions/setup-android@v3
Found preinstalled sdkmanager in /usr/local/lib/android/sdk/cmdline-tools/latest with following source.properties:
Pkg.Revision=12.0
Pkg.Path=cmdline-tools;12.0
Pkg.Desc=Android SDK Command-line Tools

Wrong version in preinstalled sdkmanager
Downloading commandline tools from https://dl.google.com/android/repository/commandlinetools-linux-12266719_latest.zip
/usr/bin/unzip -o -q /home/runner/work/_temp/cfc7ce76-6393-4bec-8b98-8342a409dc11
Accepting Android SDK licenses
/usr/local/lib/android/sdk/cmdline-tools/16.0/bin/sdkmanager --licenses
This tool requires JDK 17 or later. Your version was detected as 1.8.0_462.
To override this check, set SKIP_JDK_VERSION_CHECK.
/home/runner/work/_actions/android-actions/setup-android/v3/dist/index.js:1823
                error = new Error(`The process '${this.toolPath}' failed with exit code ${this.processExitCode}`);
                        ^

Error: The process '/usr/local/lib/android/sdk/cmdline-tools/16.0/bin/sdkmanager' failed with exit code 1
    at ExecState._setResult (/home/runner/work/_actions/android-actions/setup-android/v3/dist/index.js:1823:25)
    at ExecState.CheckComplete (/home/runner/work/_actions/android-actions/setup-android/v3/dist/index.js:1806:18)
    at ChildProcess.<anonymous> (/home/runner/work/_actions/android-actions/setup-android/v3/dist/index.js:1700:27)
    at ChildProcess.emit (node:events:524:28)
    at maybeClose (node:internal/child_process:1104:16)
    at Socket.<anonymous> (node:internal/child_process:456:11)
    at Socket.emit (node:events:524:28)
    at Pipe.<anonymous> (node:net:343:12)

Node.js v20.19.3