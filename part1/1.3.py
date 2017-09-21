# coding:utf-8
# 字符串是py中常见的数据类型，可以用''和""创建
'''
常见的转义字符
- \\ 反斜杠符号
- \' 单引号
- \b 退格
- \000 空
- \n 换行
- \r 回车
'''
# 字符串的相关操作
a = 'bai'
b = 'zhi'
print(a+b)
# =>baizhi
print(a*2)
# => baibai
print(a[1])
# => a
print((a+b)[0:5])
# =>baizh
print('q' in a)
# =>false
print('b' in a)
# =>true
print('q' not in a)
# => true

# python字符串格式化
'''
python支持格式化字符串的输出。尽管这样可能会用到非常复杂的表达式
但最基本的用法是讲一个值插入到一个有字符串格式符%s的字符串中
'''
print("我叫%s今年%d岁！"%('小明',10))
'''
- %c 格式化字符及其ASCII码
- %s 格式化字符串
- %d 格式化整数
- %u 格式化无符号整数
- %o 格式化无符号的八进制
- %x 格式化无符号十六进制
- %X 格式化无符号十六进制（大写）
- %f 格式话浮点数字，可指定小数点后的精度
- %e 用科学计数法格式化浮点数
'''
# Python format格式化函数
'''
Python2.6开始，新增了一种格式化字符串的函数 str.format(),它增强了字符串格式化的功能
基本语法是通过 {} 和 : 来代替以前的%
format函数可以接受不限个参数，位置可以不按顺序
'''
# 不指定位置，按默认顺序
print("{}{}".format("hello",",world"))
# => hello,world

# 可以指定位置
print("{0}{1}".format("hello", ",world1"))
# => hello,world1

#设置指定位置
print("{1}{0}{1}".format("hello ", "world "))
# => world hello world

#示例测试

print("网站名:{name},地址:{url}".format(name="菜鸟教程",url="wwww.runoob.com"))

#通过字典设置参数

site = {"name": "菜鸟教程","url": "www.runoob.com"}
print("网站名: {name},地址 {url}".format(**site))

#通过列表索引设置参数,0是可选

my_list = ['菜鸟教程','www.runoob.com']
print("网站名: {0[0]},地址 {0[1]}".format(my_list))

#向str.format()传入对象
class AssignValue(object):
    def __init__(self,value):
        self.value = value
my_value = AssignValue(6)
print('value 为 : {.value}'.format(my_value))


#数字格式化
print("{:.2f}".format(3.1415926))
# => 3.14

print("{:0>2d}".format(8))
'''
- {:+.2f} +3.14 带符号保留小数点后两位
- {:.0f} 3 不带小数
- {:0>2d} 08 数字补零(填充左边，宽度为2)
- {:x<4d} 填充右边，宽度为4 格式形如 10xx
- {:,} 以逗号分隔的数字格式
- {:.2%} 百分比格式
'''

'''
python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符
以及其他特殊字符
'''
str = '''
测试测试测试测试测试
测试测试测试测试测试
测试测试测试测试
测试测试测试
测试测试
测试
'''
print(str)



