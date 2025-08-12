#!/usr/bin/env python3
"""
应用测试脚本
用于验证项目基本功能是否正常
"""

import os
import sys
import traceback
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

def test_imports():
    """测试模块导入"""
    print("\n=== 测试模块导入 ===")
    
    try:
        print("测试Kivy导入...")
        import kivy
        print(f"✓ Kivy版本: {kivy.__version__}")
    except ImportError as e:
        print(f"✗ Kivy导入失败: {e}")
        return False
    
    try:
        print("测试KivyMD导入...")
        import kivymd
        print(f"✓ KivyMD版本: {kivymd.__version__}")
    except ImportError as e:
        print(f"✗ KivyMD导入失败: {e}")
        return False
    
    try:
        print("测试Telethon导入...")
        import telethon
        print(f"✓ Telethon版本: {telethon.__version__}")
    except ImportError as e:
        print(f"⚠ Telethon导入失败: {e} (可选依赖)")
    
    try:
        print("测试核心模块导入...")
        from core.config import android_config
        from core.database import android_db_manager
        from core.bot_manager import android_bot_manager
        print("✓ 核心模块导入成功")
    except ImportError as e:
        print(f"✗ 核心模块导入失败: {e}")
        return False
    
    try:
        print("测试界面模块导入...")
        from ui.main_screen import MainScreen
        from ui.config_screen import ConfigScreen
        print("✓ 界面模块导入成功")
    except ImportError as e:
        print(f"✗ 界面模块导入失败: {e}")
        return False
    
    return True

def test_database():
    """测试数据库功能"""
    print("\n=== 测试数据库功能 ===")
    
    try:
        from core.database import android_db_manager
        
        # 获取数据库信息
        db_info = android_db_manager.get_database_info()
        print(f"✓ 数据库信息: {db_info}")
        
        # 测试添加日志
        android_db_manager.add_log('info', '测试日志消息', 'test')
        print("✓ 日志添加成功")
        
        # 获取日志
        logs = android_db_manager.get_logs(limit=5)
        print(f"✓ 获取到 {len(logs)} 条日志")
        
        return True
        
    except Exception as e:
        print(f"✗ 数据库测试失败: {e}")
        traceback.print_exc()
        return False

def test_config():
    """测试配置功能"""
    print("\n=== 测试配置功能 ===")
    
    try:
        from core.config import android_config
        
        # 检查是否首次运行
        is_first_run = android_config.is_first_run()
        print(f"✓ 首次运行检查: {is_first_run}")
        
        # 创建默认配置（如果需要）
        if is_first_run:
            android_config.create_default_config()
            print("✓ 默认配置创建成功")
        
        # 加载配置
        android_config.load()
        print("✓ 配置加载成功")
        
        # 验证配置
        validation = android_config.validate()
        print(f"✓ 配置验证结果: {validation}")
        
        # 获取配置摘要
        summary = android_config.get_config_summary()
        print(f"✓ 配置摘要: {summary}")
        
        return True
        
    except Exception as e:
        print(f"✗ 配置测试失败: {e}")
        traceback.print_exc()
        return False

def test_bot_manager():
    """测试机器人管理器"""
    print("\n=== 测试机器人管理器 ===")
    
    try:
        from core.bot_manager import android_bot_manager
        
        # 获取状态
        status = android_bot_manager.get_status()
        print(f"✓ 机器人状态: {status}")
        
        # 获取配置摘要
        config_summary = android_bot_manager.get_config_summary()
        print(f"✓ 配置摘要: {config_summary}")
        
        return True
        
    except Exception as e:
        print(f"✗ 机器人管理器测试失败: {e}")
        traceback.print_exc()
        return False

def test_ui_creation():
    """测试界面创建（不启动应用）"""
    print("\n=== 测试界面创建 ===")
    
    try:
        # 设置Kivy环境变量
        os.environ['KIVY_NO_CONSOLELOG'] = '1'
        os.environ['KIVY_LOG_MODE'] = 'MIXED'
        
        # 导入KivyMD应用
        from kivymd.app import MDApp
        
        # 创建一个临时应用实例来初始化KivyMD
        class TestApp(MDApp):
            def build(self):
                return None
        
        # 初始化应用（但不运行）
        test_app = TestApp()
        
        # 现在可以安全地导入和测试界面模块
        from ui.main_screen import MainScreen
        from ui.config_screen import ConfigScreen
        from ui.schedule_screen import ScheduleScreen
        from ui.log_screen import LogScreen
        
        print("✓ 主界面模块导入成功")
        print("✓ 配置界面模块导入成功")
        print("✓ 定时任务界面模块导入成功")
        print("✓ 日志界面模块导入成功")
        
        # 清理
        test_app.stop()
        
        return True
        
    except Exception as e:
        print(f"✗ 界面创建测试失败: {e}")
        traceback.print_exc()
        return False

def main():
    """主测试函数"""
    print("Telegram内容抓取机器人Android应用 - 功能测试")
    print("=" * 50)
    
    test_results = []
    
    # 运行各项测试
    test_results.append(("模块导入", test_imports()))
    test_results.append(("数据库功能", test_database()))
    test_results.append(("配置功能", test_config()))
    test_results.append(("机器人管理器", test_bot_manager()))
    test_results.append(("界面创建", test_ui_creation()))
    
    # 输出测试结果
    print("\n" + "=" * 50)
    print("测试结果汇总:")
    print("=" * 50)
    
    all_passed = True
    for test_name, result in test_results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"{test_name:<15} {status}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 所有测试通过！项目可以正常运行。")
        print("\n下一步操作:")
        print("1. 运行 'python run.py' 启动应用进行完整测试")
        print("2. 如果应用运行正常，可以使用 buildozer 打包成APK")
        print("3. 打包命令: 'buildozer android debug'")
    else:
        print("❌ 部分测试失败，请检查错误信息并修复问题。")
        print("\n建议操作:")
        print("1. 检查是否安装了所有必需的依赖包")
        print("2. 运行 'pip install -r requirements.txt' 安装依赖")
        print("3. 修复报错的模块后重新测试")
    
    return all_passed

if __name__ == '__main__':
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n测试被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n测试过程中发生未预期的错误: {e}")
        traceback.print_exc()
        sys.exit(1)