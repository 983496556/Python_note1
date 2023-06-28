# 单行注释：用一个#
"""
多行注释
用三个"来实现
"""

# type()语句使用方式
print(type(123))        # <class 'int'>
print(type('abc'))      # <class 'str'>
print(type(12.3))       # <class 'float'>

# 字符串不同定义方式
str1 = "abc"
str2 = 'abc'
str3 = """abc"""

# 类型转化
print(int('56'))
print(str(56))
print(int(56.6))

# 算数运算符
print(5 // 2)       # 求整除  2
print(5 % 2)        # 求余数  1
print(5 ** 2)       # 求幂   25

# 字符串拼接
name = 'Jordan'
print("My name is " + name + ".")

# 字符串格式化
# %s-字符串  %d-整数  %f-浮点型
# 可以用%m.nf来控制浮点型数据精度，m表示宽度，n控制小数点精度
year = 2021
day = 4.28
print("My name is %s, I born on %d %f." % (name, year, day))
print("My name is %s, I born on %d %9f." % (name, year, day))
print("My name is %s, I born on %d %.2f." % (name, year, day))
print(f"My name is {name}, I born on {year} {day}.")    # 不做精度控制原样输出

# 获取键盘输入
name = input()
print(name)