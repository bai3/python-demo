# coding:utf-8
# 单行注释
'''
多行注释
多行注释
多行注释
'''

"""
多行注释
多行注释
多行注释
"""
print('Hello world')

'''
python3中的变量不需要声明，每个变量在使用前
都必须赋值，变量赋值以后该变量才会被创建。
'''

'''
标准数据类型
Python3中有6个标准的数据类型
- Number 数字
- String 字符串
- List 列表
- Tuple 元祖
- Sets 集合
- Dictionary 字典

内置的type函数可以来查询变量所指的的对象类型
'''
a = 1.1
print(type(a))
# => class 'float'

'''
isinstance也可以判断类型
'''
print(isinstance(a,float))
# => true