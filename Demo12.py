# 文件的读取
import time

# 打开文件
f = open("D:/aaa/a.txt", "r", encoding="utf-8")
print(type(f))

# 读取文件 - read()
print(f"读取10个字节的结果：{f.read(10)}")
print(f"read方法读取全部内容的结果是：{f.read()}")
print()

# 读取文件 - readLines()
lines = f.readlines()  # 读取文件的全部行，封装到列表中
print(f"lines对象的类型：{type(lines)}")
print(f"lines对象的内容是：{lines}")

# 读取文件 - readline()
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行数据是：{line1}")
print(f"第二行数据是：{line2}")
print(f"第三行数据是：{line3}")

# for循环读取文件行
for line in f:
    print(f"每一行数据是:{line}")

# 文件的关闭
f.close()

# with open 语法操作文件
with open("D:/aaa/a.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"每一行数据是：{line}")

# 文件的写入
# w：文件不存在-创建文件，文件存在-清空原有内容
f = open("D:/aaa/a.txt", "w", encoding="UTF-8")
# write写入、flush刷新
f.write("黑马程序员")
# close关闭
f.close()  # close方法，内置了flush的功能的

# 文件的追加写入
f = open("D:/aaa/a.txt", "a", encoding="UTF-8")
# write写入、flush刷新
f.write("\n月薪过万")
# close关闭
f.close()

