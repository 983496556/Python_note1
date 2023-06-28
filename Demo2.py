# 比较运算符
result = 5 > 3
print(f"5 > 3的结果是{result}, 数据类型是{type(result)}")

# 条件判断语句
age = 18
if age >= 18:
    print("已成年")
    if age > 60:
        print("年龄太大")
    else:
        print("欢迎光临")
elif age <= 0:
    print("输入错误")
else:
    print("未成年")

# 循环语句
i = 1
while i < 10:
    j = 1
    while j <= i:
        print(f"{i} * {j} = {i * j}", end='\t')
        j += 1
    i += 1
    print()

"""
for语法
语法1:range(num)                  语法1从0开始，到num结束（不含num本身）
语法2:range(num1, num2)           语法2从num1开始，到num2结束（不含num2本身）
语法3:range(num1, num2, step)     语法3从num1开始，到num2结束（不含num2本身），步长以step值为准
"""
for i in range(5):
    print(i)


