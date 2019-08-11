class B:
    """类B"""
    def __init__(self):
        pass

    def handle(self):
        print("B.handle")

class A(B):
    """类A"""

    def __init__(self):
        super().__init__()

    def handle(self):
        super().handle() # super 依赖于继承父类

def main():
    print('this message is from main function')
    a = A()
    a.handle()


if __name__ == '__main__':
    main()
    # print(__name__)