#打开文件
f = open("/home/a/python_practise/test.txt","r",encoding="UTF-8")
print(type(f))
#读取文件- read()
print(f.read(1))
print(f.read())
print("------")
#读取文件- readLines()
lines = f.readlines()
print(f"lines对象的类型是{type(lines)}")
f = open("/home/a/python_practise/test.txt","r",encoding="UTF-8")
print(lines)
#读取文件- readline()
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行的内容{line1}")
print(f"第二行的内容{line2}")
print(f"第三行的内容{line3}")
# for循环读取文件行
for line in f:
    print(f"每一行的内容是{line}")
#文件的关闭
f.close()
#with open语法操作文件
with open("/home/a/python_practise/test.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(f"每一行的内容是{line}")

"""
    with open用法总结：
    1.使用with open语法打开文件时，不需要手动调用close()方法关闭文件
    2.使用with open语法可以更简洁地处理文件操作，避免了显式的try-finally结构，使代码更易读。
    3.推荐在Python中使用with open语法来处理文件操作，以确保文件正确关闭并提高代码的可读性。
    用法示例：
    with open("文件路径", "模式", encoding="编码格式") as 变量名:
        # 在这里进行文件操作
"""
