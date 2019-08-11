from mysql.MySqlUtils import MySqlUtils
from daomain.Student import Student

if __name__ == '__main__':
    mysqlUtils = MySqlUtils()

    # print(mysqlUtils.getVersion()) # 获取数据库版本号


    # print(mysqlUtils.createTable("EMPLOYEE"))  # 创建新表
    # print(mysqlUtils.getAllTableName())  # 获取所有表名

    # stu = Student(name="王五",age=15)
    # mysqlUtils.save(stu) #保存数据

    for stu in mysqlUtils.getAll("Student"):
        print(stu)  # 获取表中所有数据

    # # mysqlUtils.delete("4,5")
    mysqlUtils.update(Student("8","赵柳","12"))  # 更新用户信息
    print("------------------")  # 获取表中所有数据
    for stu in mysqlUtils.getAll("Student"):
        print(stu)  # 获取表中所有数据

    mysqlUtils.close()
