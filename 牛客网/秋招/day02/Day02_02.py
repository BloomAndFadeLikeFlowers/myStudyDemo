# 题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 假设该数为 x。
# x + 100 = m^2
# x + 100 + 168 = n^2
# n^2 - m^2 = 168
# (n + m) * (n - m) = 168
# n > m >= 0
# n - m 最小值为 1
# n + m 最大为 168
# n 最大值为 168
# m 最大值为 167

def fun():
    result = {}
    for m in range(0, 168):
        for n in range(m + 1, 169):
            # print('n=%s,m=%s' % (n, m))
            if (n + m) * (n - m) == 168:
                # print("该数为:" + str(n * n - 168 - 100))
                # print("该数为:" + str(m * m - 100))
                # print('n为%s,m为%s' % (n, m))
                key = str(m * m - 100)
                value = [n, m]
                result[key]=value
    return result

if __name__ == '__main__':
    result = fun();
    print(result)
    print(result.keys())

