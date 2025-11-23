__all__=['test'] # 指定从模块中导入的内容
"""
    当使用from my_module2 import *语句时，只有在__all__列表中列出的名称才会被导入。
"""
def test(a,b):
    print(a + b)
def test2(a,b):
    print(a - b)
