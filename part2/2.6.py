# python3 函数
# 定义一个函数
# - 函数代码块以def关键词开头，后接函数标示符名称和圆括号()
# - 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数
# - 函数第一行语句可以选择性地使用文档字符串用于存放函数说明
# - 函数内容以冒号起始，并且缩进
# - return[表达式]结束函数，选择性地返回一个值给调用方，不带表达式的return相当于返回None


def hello(n):
    print("{0} Hello word".format(n))

hello("baizhix")

# 参数传递
# 在python中，类型属于对象，变量是没有类型的

# 可更改与不可更改的对象
# 在python中，string，tuples,和numbers是不可更改的对象
# list，dict是可更改的对象

