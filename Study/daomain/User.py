import json
import time
# data = {
#     "egon":{"password":"123",'status':False,'timeout':0},
#     "alex":{"password":"456",'status':False,'timeout':0},
# }
#
# with open("user_info", "w", encoding="utf-8") as f:
#     json.dump(data, f)  # 序列化


class User:
    """用户类"""
    def __init__(self):
        self.user_dic = self.read()  # 初始化时将用户信息读取出来
        self.username = ""  # 记录当前登录用户

    def write(self):
        """序列化"""
        with open("user_info", "w", encoding="utf-8") as f:
            json.dump(self.user_dic, f)  # 序列化

    def read(self):
        """拿到用户数据"""
        with open("user_info", "r", encoding="utf-8") as f:
            user_dic = json.load(f)  # 反序列化
            return user_dic

    def db(self):
        print("用户数据结构：", self.user_dic)

    def login(self):
        """登录"""
        i = 0
        while i < 3:
            username = input("username:").strip()
            password = input("password:").strip()
            if username in self.user_dic and password == self.user_dic[username]["password"]:
                time_now = time.time()  # 获取当前时间
                period = time_now - self.user_dic[username]["timeout"]  # 时间差
                if period >= 30:  # 判断时间间隔是否满足登录条件
                    print("------%s登陆成功-----" % username)
                    self.username = username
                    self.user_dic[username]["status"] = True  # 记录用户登录状态
                    self.write()  # 将修改保存到文件
                    break
                else:
                    print("用户处于锁定状态，请%s S后再试" % (30 - period))
                    break
            else:
                print("用户名或密码错误！")
                i += 1
                if i == 3 and username in self.user_dic:
                    self.user_dic[username]["timeout"] = time.time()  # 记录3次登录失败的时间点
                    self.write()  # 将修改保存到文件
                    exit("退出")

    def exit(self):
        """退出"""
        if self.username:  # 用户处于登录状态
            self.user_dic[self.username]["status"] = False  # 修改用户登录状态
            self.write()  # 将修改保存到文件
            exit("用户%s退出登录" % self.username)

    def help_info(self):
        """帮助信息"""
        print("""命令列表：
         查看数据结构：db
         登录：login
         查看帮助: help_info
         退出登录：exit""")

    def handle(self):
        """处理用户输入命令"""
        while True:
            cmd = input("请输入命令:").strip()
            cmd = cmd.split()
            if hasattr(self, cmd[0]):  # 使用反射
                func = getattr(self, cmd[0])  # 拿到方法名
                func()
            else:
                self.help_info()  # 打印帮助信息


user = User()
if __name__ == "__main__":
    print("""命令列表：
            查看数据结构：db
            登录：login
            查看帮助: help_info
            退出登录：exit""")
    user.handle()

"""
输出：
请输入命令:login
username:egon
password:123
------egon登陆成功-----
请输入命令:exit
用户egon退出登录
"""