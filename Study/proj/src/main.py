# main.py
"""程序运行主体，可进行菜单选择"""
from proj.src.manager import Manager


def main():
    li = Manager.info
    for i in range(len(li)):
        print(i+1, li[i][0])
    while True:
        ch = input("输入序号进行操作：").strip()
        getattr(Manager(), li[int(ch)-1][1])()  # 反射， 找到对象相应的方法并执行