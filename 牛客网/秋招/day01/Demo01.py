#  母牛生小牛问题
#  母牛从 3-7 岁 年初生一头小牛
# 10岁以后死亡 年初有一头母牛，n年后有几头牛

def getNum(n):
    list = []
    if n == 1:
        return 1

    list.append(1)
    for i in range(1, n):
        # 每头牛的年龄 加一
        for j in range(len(list)):
            list[j] = list[j] + 1
        # 3-7岁的母牛生1头小牛
        for num in list:
            if (num >= 3 and num <= 7):
                list.append(1)
        # 10岁以后死亡
        for j in range(len(list)):
            if (list[j] >= 10):
                del list[j]
    return len(list)


if __name__ == '__main__':
    # n = input("n=")
    n = 8
    count = getNum(n)
    print(count)
