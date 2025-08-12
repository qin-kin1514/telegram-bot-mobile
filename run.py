#!/usr/bin/env python3
"""
应用启动脚本
用于开发和测试
"""

import os
import sys
from pathlib import Path

# 添加项目根目录到Python路径
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# 设置环境变量
os.environ['KIVY_NO_CONSOLELOG'] = '0'  # 开发时启用控制台日志
os.environ['KIVY_LOG_MODE'] = 'MIXED'

if __name__ == '__main__':
    try:
        print("启动Telegram内容抓取机器人Android应用...")
        print(f"项目根目录: {project_root}")
        
        # 导入并运行主应用
        from main import main
        main()
        
    except ImportError as e:
        print(f"导入错误: {e}")
        print("请确保所有依赖已正确安装")
        sys.exit(1)
    except Exception as e:
        print(f"启动失败: {e}")
        sys.exit(1)