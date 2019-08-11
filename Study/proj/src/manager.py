# manager.py
"""创建教师，删除教师，查看教师"""
from proj.src.my_pickle import MyPickle
from proj.config.settings import *
from proj.src.teacher import Teacher


class Manager:
    """管理员类"""
    info = [("查看教师", "show_teacher"),("创建教师", "create_teacher"),
            ("删除教师", "delete_teacher"), ("退出", "exit")]

    def __init__(self):
        self.teacher_pickle_obj = MyPickle(teacher_file)  # 实例化MyPickle类，teacher_file是settings中的教师文件路径

    def show(self, pickle_obj):
        """从文件中读取信息"""
        pick_obj = getattr(self, pickle_obj)
        data_g = pick_obj.readiter()  # 读取对象信息
        for teacher_obj in data_g:
            for key in teacher_obj.__dict__:
                print(key, teacher_obj.__dict__[key])  # 打印对象信息
            print("-" * 50)

    def show_teacher(self):
        """查看教师信息"""
        print("教师信息".center(45, "-"))
        self.show("teacher_pickle_obj")

    def create_teacher(self):
        """创建教师信息"""
        name = input("输入要创建的教师姓名：").strip()
        school = input("输入教师所在学校：").strip()
        teacher = Teacher(name, school)  # 实例化一个教师对象
        self.teacher_pickle_obj.write(teacher)  # 将对象写入文件
        print("创建教师成功！")

    def delete_teacher(self):
        """删除教师信息"""
        self.show_teacher()
        inp = input("输入要删除的教师姓名：").strip()
        self.teacher_pickle_obj.delete(inp)  # 删除
        print("删除成功！")

    def exit(self):
        exit()
