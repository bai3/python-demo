# python3 函数
# 定义一个函数
# - 函数代码块以def关键词开头，后接函数标示符名称和圆括号()
# - 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数
# - 函数第一行语句可以选择性地使用文档字符串用于存放函数说明
# - 函数内容以冒号起始，并且缩进
# - return[表达式]结束函数，选择性地返回一个值给调用方，不带表达式的return相当于返回None


def hello(n):
    print("{0} Hello word".format(n))

# hello("baiZhiXi")

# 计算面积

def area(width, height):
    return width*height


def print_welcome(name):
    print("Welcome", name)
print_welcome("bai zhi xi")
w = 4
h = 5
print(area(w, h))

# 参数传递
# 在python中，类型属于对象，变量是没有类型的
a = [1, 2, 3]
a = "RUNOOB"

# 参数传递
# 在python中，类型属于对象，变量是没有类型的

# 可更改与不可更改的对象
# 在python中，string，tuples,和numbers是不可更改的对象
# list，dict是可更改的对象
# 传不可变对象实例


def ChangeInt(a):
    a = 10
    print(a)
    return a
b = 2
ChangeInt(b)
c = ChangeInt(b)
print(b)
print(c)


# 传可变对象实例


def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print("函数内取值:", mylist)
    return
# 调用changeme函数
mylist = [10, 20, 30]
changeme(mylist)
print("函数外取值:", mylist)

# 不定长参数
# 你可能需要一个函数能处理比当初声明时更多的参数
# 这些参数叫做不定长参数，和上述2种参数不用，声明
# 时不会命名，基本语法如下


def printinfo(arg1, *vartuple):  # 打印任何传入的参数
    print("输出:")
    print(arg1)
    for var in vartuple:
        print(var)
    return
printinfo(10)
printinfo(70, 60, 50)

# 匿名函数
# python使用lambda来创建匿名函数
# 所谓匿名，即不再使用def语句这样标准的形式定义一个函数
# - lambda只是一个表达式，函数体比def简单很多
# - lambda的主体是一个表达式，而不是一个代码块，仅仅能在lambda表达式中封装有限的逻辑进去
# - lambda函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间的参数
# - 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调小函数时不占用栈内存从而增加运行效率


sum = lambda arg1, arg2: arg1+arg2
print("相加后的值为:", sum(10, 20))

# 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字

num = 1
def fun1():
    global num
    print(num)
    num = 123
    print(num)
fun1()

# 如果想修改嵌套作用域（闭包函数作用域，外层非全局作用域）中的变量则需要nonlocal关键字


def outer():
    num = 10
    def inner():
        nonlocal num
