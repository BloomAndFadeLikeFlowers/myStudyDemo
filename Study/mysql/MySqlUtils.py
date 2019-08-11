"""
一时间戳作为对象的id
"""
import time
import os
import pickle
import pymysql
import mysql.settings as settings


class MySqlUtils:
    """MySql类"""

    def __init__(self, host=settings.JDBC_HOST,
                 username=settings.JDBC_USERNAME,
                 password=settings.JDBC_PASSWORD,
                 dbname=settings.DB_NAME):
        try:
            self.db = pymysql.connect(host, username, password, dbname)
            self.cursor = self.db.cursor()
        except Exception as e:
            print("Exception: {0}".format(e))

    def save(self, student):
        # SQL 插入语句
        sql = "INSERT INTO Student(\
               sname, age) \
               VALUES ('%s',  %s)" % \
              (student.name, student.age)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()

    def update(self, student):
        # SQL 插入语句
        sql = "UPDATE Student SET sname = '{0}',age='{1}' " \
              "WHERE sno = '{2}'".format(student.name, student.age,student.sno)
        print(sql)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()

    def delete(self, sno):
        # SQL 插入语句
        sql = "DELETE FROM Student\
                WHERE SNO IN ({0})".format(sno)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()

    def getAll(self, tableName):
        sql = "SELECT * FROM {0}".format(tableName)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def getAllTableName(self):
        self.cursor.execute("SHOW TABLES")
        data = self.cursor.fetchall()
        return "TableList : %s " % str(list(data))

    def getVersion(self):
        self.cursor.execute("SELECT VERSION()")
        return "Database version : %s " % self.cursor.fetchone()

    def createTable(self, tableName):
        # 使用 execute() 方法执行 SQL，如果表存在则删除
        self.cursor.execute("DROP TABLE IF EXISTS {0}".format(tableName))

        # 使用预处理语句创建表
        sql = """CREATE TABLE {0} (
                 FIRST_NAME  CHAR(20) NOT NULL,
                 LAST_NAME  CHAR(20),
                 AGE INT,  
                 SEX CHAR(1),
                 INCOME FLOAT )""".format(tableName)
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def close(self):
        self.db.close()
        # print("Database Conn Close")
