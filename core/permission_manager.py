#!/usr/bin/env python3
"""
Android权限管理模块
处理应用所需的各种权限请求和检查
"""

from typing import Dict, List, Callable, Optional
from kivy.logger import Logger
from kivy.clock import Clock

try:
    # Android平台相关导入
    from android.permissions import request_permissions, Permission, check_permission
    from android import activity, mActivity
    from jnius import autoclass
    ANDROID_AVAILABLE = True
except ImportError:
    # 非Android平台
    ANDROID_AVAILABLE = False
    Logger.warning("PermissionManager: Android APIs不可用，使用模拟模式")

class PermissionManager:
    """Android权限管理器"""
    
    # 应用所需权限列表
    REQUIRED_PERMISSIONS = [
        'android.permission.INTERNET',
        'android.permission.ACCESS_NETWORK_STATE',
        'android.permission.WAKE_LOCK',
        'android.permission.WRITE_EXTERNAL_STORAGE',
        'android.permission.READ_EXTERNAL_STORAGE',
        'android.permission.RECEIVE_BOOT_COMPLETED',
        'android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS'
    ]
    
    # 权限描述
    PERMISSION_DESCRIPTIONS = {
        'android.permission.INTERNET': '网络访问权限，用于连接Telegram API和发送邮件',
        'android.permission.ACCESS_NETWORK_STATE': '网络状态检查权限，用于检测网络连接',
        'android.permission.WAKE_LOCK': '保持唤醒权限，用于后台任务执行',
        'android.permission.WRITE_EXTERNAL_STORAGE': '存储写入权限，用于保存配置和日志文件',
        'android.permission.READ_EXTERNAL_STORAGE': '存储读取权限，用于读取配置文件',
        'android.permission.RECEIVE_BOOT_COMPLETED': '开机启动权限，用于系统启动后自动运行',
        'android.permission.REQUEST_IGNORE_BATTERY_OPTIMIZATIONS': '电池优化白名单权限，确保后台正常运行'
    }
    
    def __init__(self):
        """初始化权限管理器"""
        self.permission_callbacks = {}
        self.pending_requests = set()
        self.granted_permissions = set()
        self.denied_permissions = set()
        
        # 绑定权限回调
        if ANDROID_AVAILABLE:
            activity.bind(on_activity_result=self._on_activity_result)
    
    def check_all_permissions(self) -> Dict[str, bool]:
        """检查所有必需权限"""
        permission_status = {}
        
        for permission in self.REQUIRED_PERMISSIONS:
            permission_status[permission] = self.check_permission(permission)
        
        return permission_status
    
    def check_permission(self, permission: str) -> bool:
        """检查单个权限"""
        try:
            if not ANDROID_AVAILABLE:
                # 非Android平台，假设所有权限都已授予
                return True
            
            # 使用Kivy的权限检查
            if hasattr(Permission, permission.split('.')[-1]):
                perm_attr = getattr(Permission, permission.split('.')[-1])
                return check_permission(perm_attr)
            else:
                # 使用Android原生API检查
                return self._check_permission_native(permission)
                
        except Exception as e:
            Logger.error(f"PermissionManager: 检查权限失败 {permission} - {e}")
            return False
    
    def _check_permission_native(self, permission: str) -> bool:
        """使用Android原生API检查权限"""
        try:
            Context = autoclass('android.content.Context')
            PackageManager = autoclass('android.content.pm.PackageManager')
            
            context = mActivity.getApplicationContext()
            result = context.checkSelfPermission(permission)
            
            return result == PackageManager.PERMISSION_GRANTED
            
        except Exception as e:
            Logger.error(f"PermissionManager: 原生权限检查失败 {permission} - {e}")
            return False
    
    def request_permissions(self, permissions: List[str], callback: Optional[Callable] = None) -> bool:
        """请求权限"""
        try:
            if not ANDROID_AVAILABLE:
                Logger.info("PermissionManager: 非Android平台，跳过权限请求")
                if callback:
                    callback(True, {})
                return True
            
            # 过滤已授予的权限
            needed_permissions = []
            for permission in permissions:
                if not self.check_permission(permission):
                    needed_permissions.append(permission)
                else:
                    self.granted_permissions.add(permission)
            
            if not needed_permissions:
                Logger.info("PermissionManager: 所有权限已授予")
                if callback:
                    callback(True, {})
                return True
            
            # 记录回调
            request_id = str(len(self.permission_callbacks))
            self.permission_callbacks[request_id] = callback
            
            # 请求权限
            Logger.info(f"PermissionManager: 请求权限 {needed_permissions}")
            
            # 转换为Kivy权限格式
            kivy_permissions = []
            for perm in needed_permissions:
                perm_name = perm.split('.')[-1]
                if hasattr(Permission, perm_name):
                    kivy_permissions.append(getattr(Permission, perm_name))
                else:
                    Logger.warning(f"PermissionManager: 未知权限 {perm}")
            
            if kivy_permissions:
                request_permissions(kivy_permissions, self._on_permissions_result)
                self.pending_requests.update(needed_permissions)
            
            return True
            
        except Exception as e:
            Logger.error(f"PermissionManager: 请求权限失败 - {e}")
            if callback:
                callback(False, {'error': str(e)})
            return False
    
    def _on_permissions_result(self, permissions, grant_results):
        """权限请求结果回调"""
        try:
            Logger.info(f"PermissionManager: 权限请求结果 {permissions} -> {grant_results}")
            
            granted = []
            denied = []
            
            for i, permission in enumerate(permissions):
                if i < len(grant_results) and grant_results[i]:
                    granted.append(permission)
                    self.granted_permissions.add(permission)
                    self.pending_requests.discard(permission)
                else:
                    denied.append(permission)
                    self.denied_permissions.add(permission)
                    self.pending_requests.discard(permission)
            
            # 调用所有等待的回调
            for callback in self.permission_callbacks.values():
                if callback:
                    callback(len(denied) == 0, {
                        'granted': granted,
                        'denied': denied
                    })
            
            self.permission_callbacks.clear()
            
        except Exception as e:
            Logger.error(f"PermissionManager: 处理权限结果失败 - {e}")
    
    def _on_activity_result(self, request_code, result_code, intent):
        """Activity结果回调"""
        try:
            # 处理特殊权限请求结果
            if request_code == 1001:  # 电池优化白名单请求
                self._check_battery_optimization_result()
            
        except Exception as e:
            Logger.error(f"PermissionManager: 处理Activity结果失败 - {e}")
    
    def request_battery_optimization_whitelist(self, callback: Optional[Callable] = None) -> bool:
        """请求加入电池优化白名单"""
        try:
            if not ANDROID_AVAILABLE:
                Logger.info("PermissionManager: 非Android平台，跳过电池优化设置")
                if callback:
                    callback(True)
                return True
            
            # 检查是否已在白名单中
            if self.is_battery_optimization_ignored():
                Logger.info("PermissionManager: 已在电池优化白名单中")
                if callback:
                    callback(True)
                return True
            
            # 请求加入白名单
            Intent = autoclass('android.content.Intent')
            Settings = autoclass('android.provider.Settings')
            Uri = autoclass('android.net.Uri')
            
            context = mActivity.getApplicationContext()
            package_name = context.getPackageName()
            
            intent = Intent()
            intent.setAction(Settings.ACTION_REQUEST_IGNORE_BATTERY_OPTIMIZATIONS)
            intent.setData(Uri.parse(f"package:{package_name}"))
            
            mActivity.startActivityForResult(intent, 1001)
            
            # 延迟检查结果
            if callback:
                Clock.schedule_once(lambda dt: self._delayed_battery_check(callback), 2.0)
            
            Logger.info("PermissionManager: 请求电池优化白名单")
            return True
            
        except Exception as e:
            Logger.error(f"PermissionManager: 请求电池优化白名单失败 - {e}")
            if callback:
                callback(False)
            return False
    
    def _delayed_battery_check(self, callback):
        """延迟检查电池优化结果"""
        try:
            result = self.is_battery_optimization_ignored()
            callback(result)
        except Exception as e:
            Logger.error(f"PermissionManager: 延迟检查电池优化失败 - {e}")
            callback(False)
    
    def _check_battery_optimization_result(self):
        """检查电池优化白名单结果"""
        try:
            is_ignored = self.is_battery_optimization_ignored()
            Logger.info(f"PermissionManager: 电池优化白名单状态 - {is_ignored}")
            
        except Exception as e:
            Logger.error(f"PermissionManager: 检查电池优化结果失败 - {e}")
    
    def is_battery_optimization_ignored(self) -> bool:
        """检查是否在电池优化白名单中"""
        try:
            if not ANDROID_AVAILABLE:
                return True
            
            PowerManager = autoclass('android.os.PowerManager')
            Context = autoclass('android.content.Context')
            
            context = mActivity.getApplicationContext()
            pm = context.getSystemService(Context.POWER_SERVICE)
            package_name = context.getPackageName()
            
            if hasattr(pm, 'isIgnoringBatteryOptimizations'):
                return pm.isIgnoringBatteryOptimizations(package_name)
            else:
                # 旧版本Android，假设不受电池优化影响
                return True
                
        except Exception as e:
            Logger.error(f"PermissionManager: 检查电池优化状态失败 - {e}")
            return False
    
    def request_autostart_permission(self, callback: Optional[Callable] = None) -> bool:
        """请求自启动权限（部分厂商需要）"""
        try:
            if not ANDROID_AVAILABLE:
                if callback:
                    callback(True)
                return True
            
            # 尝试打开自启动设置页面
            Intent = autoclass('android.content.Intent')
            ComponentName = autoclass('android.content.ComponentName')
            
            context = mActivity.getApplicationContext()
            package_name = context.getPackageName()
            
            # 不同厂商的自启动设置页面
            autostart_intents = [
                # 华为
                ('com.huawei.systemmanager', 'com.huawei.systemmanager.startupmgr.ui.StartupNormalAppListActivity'),
                # 小米
                ('com.miui.securitycenter', 'com.miui.permcenter.autostart.AutoStartManagementActivity'),
                # OPPO
                ('com.coloros.safecenter', 'com.coloros.safecenter.permission.startup.FakeActivity'),
                # Vivo
                ('com.iqoo.secure', 'com.iqoo.secure.ui.phoneoptimize.AddWhiteListActivity'),
                # 魅族
                ('com.meizu.safe', 'com.meizu.safe.permission.SmartBGActivity'),
            ]
            
            for pkg, cls in autostart_intents:
                try:
                    intent = Intent()
                    intent.setComponent(ComponentName(pkg, cls))
                    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                    
                    mActivity.startActivity(intent)
                    
                    Logger.info(f"PermissionManager: 打开自启动设置页面 - {pkg}")
                    
                    if callback:
                        callback(True)
                    return True
                    
                except Exception:
                    continue
            
            # 如果没有找到特定的自启动设置，打开应用详情页面
            try:
                Settings = autoclass('android.provider.Settings')
                Uri = autoclass('android.net.Uri')
                
                intent = Intent()
                intent.setAction(Settings.ACTION_APPLICATION_DETAILS_SETTINGS)
                intent.setData(Uri.parse(f"package:{package_name}"))
                intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
                
                mActivity.startActivity(intent)
                
                Logger.info("PermissionManager: 打开应用详情页面")
                
                if callback:
                    callback(True)
                return True
                
            except Exception as e:
                Logger.error(f"PermissionManager: 打开应用详情页面失败 - {e}")
            
            if callback:
                callback(False)
            return False
            
        except Exception as e:
            Logger.error(f"PermissionManager: 请求自启动权限失败 - {e}")
            if callback:
                callback(False)
            return False
    
    def get_permission_status_summary(self) -> Dict[str, any]:
        """获取权限状态摘要"""
        all_permissions = self.check_all_permissions()
        
        granted_count = sum(1 for granted in all_permissions.values() if granted)
        total_count = len(all_permissions)
        
        return {
            'all_granted': granted_count == total_count,
            'granted_count': granted_count,
            'total_count': total_count,
            'permissions': all_permissions,
            'battery_optimization_ignored': self.is_battery_optimization_ignored(),
            'pending_requests': list(self.pending_requests)
        }
    
    def get_permission_description(self, permission: str) -> str:
        """获取权限描述"""
        return self.PERMISSION_DESCRIPTIONS.get(permission, f"权限: {permission}")
    
    def request_all_permissions(self, callback: Optional[Callable] = None) -> bool:
        """请求所有必需权限"""
        try:
            Logger.info("PermissionManager: 开始请求所有必需权限")
            
            def on_permissions_granted(success, result):
                if success:
                    Logger.info("PermissionManager: 基础权限请求完成")
                    # 请求电池优化白名单
                    self.request_battery_optimization_whitelist(
                        lambda battery_success: self._on_all_permissions_complete(
                            success and battery_success, callback
                        )
                    )
                else:
                    Logger.warning(f"PermissionManager: 基础权限请求失败 - {result}")
                    if callback:
                        callback(False, result)
            
            # 首先请求基础权限
            return self.request_permissions(self.REQUIRED_PERMISSIONS, on_permissions_granted)
            
        except Exception as e:
            Logger.error(f"PermissionManager: 请求所有权限失败 - {e}")
            if callback:
                callback(False, {'error': str(e)})
            return False
    
    def _on_all_permissions_complete(self, success: bool, callback: Optional[Callable]):
        """所有权限请求完成回调"""
        try:
            status = self.get_permission_status_summary()
            
            Logger.info(f"PermissionManager: 权限请求完成 - 成功: {success}")
            Logger.info(f"PermissionManager: 权限状态 - {status['granted_count']}/{status['total_count']}")
            
            if callback:
                callback(success, status)
                
        except Exception as e:
            Logger.error(f"PermissionManager: 权限完成回调失败 - {e}")
            if callback:
                callback(False, {'error': str(e)})
    
    def show_permission_rationale(self, permission: str) -> str:
        """显示权限说明"""
        description = self.get_permission_description(permission)
        
        rationale = f"应用需要以下权限才能正常工作：\n\n{description}\n\n"
        rationale += "请在系统设置中授予此权限，以确保应用功能正常运行。"
        
        return rationale
    
    def open_app_settings(self) -> bool:
        """打开应用设置页面"""
        try:
            if not ANDROID_AVAILABLE:
                return True
            
            Intent = autoclass('android.content.Intent')
            Settings = autoclass('android.provider.Settings')
            Uri = autoclass('android.net.Uri')
            
            context = mActivity.getApplicationContext()
            package_name = context.getPackageName()
            
            intent = Intent()
            intent.setAction(Settings.ACTION_APPLICATION_DETAILS_SETTINGS)
            intent.setData(Uri.parse(f"package:{package_name}"))
            intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
            
            mActivity.startActivity(intent)
            
            Logger.info("PermissionManager: 打开应用设置页面")
            return True
            
        except Exception as e:
            Logger.error(f"PermissionManager: 打开应用设置失败 - {e}")
            return False


# 创建全局实例
android_permission_manager = PermissionManager()