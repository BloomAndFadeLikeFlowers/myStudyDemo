# start.py
"""程序启动文件"""

"""
用面向对象的形式编写一个老师角色, 并实现以下功能, 
获取老师列表, 创建老师、删除老师、
创建成功之后通过 pickle 序列化保存到文件里，并在下一次重启程序时能
读取到创建的老师
"""
import os
import sys
BASE_PATH = os.path.dirname(os.getcwd())
sys.path.insert(0, BASE_PATH)  # 将proj的路径添加到模块搜索路径中
from proj.src import main

if __name__ == "__main__":
    print(BASE_PATH)
    main.main()




