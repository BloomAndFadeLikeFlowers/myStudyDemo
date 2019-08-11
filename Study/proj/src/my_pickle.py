# my_pickle.py
"""读写文件信息"""
import pickle
import os
from proj.config.settings import *


class MyPickle:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):  # 写入
        with open(self.filename, "ab") as f:
            pickle.dump(data, f)

    def readiter(self):  # 读取
        with open(self.filename, "rb") as f:
            while True:
                try:
                    data = pickle.load(f)
                    yield data
                except:
                    break

    def delete(self, name):  # 删除
        f2 = MyPickle(self.filename+".bak")  # 新建一个文件
        for item in self.readiter():  # 从文件中load数据
            if item.name == name:
                pass  # 找到了就不写入
            else:
                f2.write(item)  # 没找到就将对象写入文件
        os.remove(self.filename)  # 删除旧文件
        os.rename(self.filename+".bak", self.filename)  # 新文件名重命名为旧文件名

