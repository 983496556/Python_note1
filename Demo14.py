# 模块

# 使用import导入time模块使用sleep功能（函数）
import time  # 导入Python内置的time模块（time.py这个代码文件）

print("你好")
time.sleep(5)  # 通过. 就可以使用模块内部的全部功能（类、函数、变量）
print("我好")

# 使用from导入time的sleep功能（函数）
from time import sleep

print("你好")
sleep(5)
print("我好")

# 使用 * 导入time模块的全部功能
from time import *  # *表示全部的意思

print("你好")
sleep(5)
print("我好")

# 使用as给特定功能加上别名
import time as t

print("你好")
t.sleep(5)
print("我好")

from time import sleep as sl

print("你好")
sl(5)
print("我好")

# 导入自定义模块使用
# import My_Module1
from My_Module1 import test
test(1, 2)

# 导入不同模块的同名功能
# from my_module1 import test
# from my_module2 import test
# test(1, 2)    # 执行后来的

# __main__变量,调用后不会自动执行
# from my_module1 import test

# __all__变量，不在变量范围内的函数需要手动调用
from My_Module2 import *
test1(1, 2)
# test_b(2, 1)
