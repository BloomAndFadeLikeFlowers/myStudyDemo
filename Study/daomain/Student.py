class Student:
    """学生类"""
    count = 0  # 计数

    def __init__(self, sno=-1, name="", age=0):
        self.sno = sno
        self.name = name
        self.age = age
        Student.count += 1  # 要使得变量全局有效，就定义为类的属性

    def learn(self):
        print("is learniung")
