from daomain.Student import Student

stu1 = Student(1,"jack",33)
stu2 = Student(2,"any",12)

def main():
    print('this message is from main function')
    print("实例化了%s个学生" % Student.count)


if __name__ == '__main__':
    main()
    # print(__name__)