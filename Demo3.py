# 函数
def fun1(x, y):
    """
    :param x: 参数1
    :param y: 参数2
    :return: 参数之和
    """
    return x + y


def fun2(x, y):
    return fun1(x * x, y * y)


def fun3():
    global num
    num = 200
    print(num)


def fun4():
    num = 200
    print(num)


print(fun1(5, 6))
print(fun2(2, 3))

# global关键字 可以在函数内部声明变量为全局变量
num = 100

fun4()
print(num)
fun3()
print(num)
