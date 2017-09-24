# Python3迭代器和生成器
# 迭代器是一个可以记住遍历的位置的对象
# 迭代器对象从集合的第一个元素开始访问，知道所有的元素
# 被访问完结束。迭代器只能往前不会往后
# 迭代器有两个基本的方法:iter()和next()
import sys

list2 = [1, 2, 3, 4]
it = iter(list2)
print(next(it))
print(next(it))
print(next(it))

# 迭代器对象可以使用常规的for语句进行遍历
list3 = [1, 2, 3, 4]
it2 = iter(list3)
# for x in it2:
#     print(x, end="")
#
# while True:
#     try:
#         print(next(it2))
#     except StopIteration:
#         sys.exit()

# 在python中，使用yield的函数被称为生成器
# 与普通的函数不用，生成器是一个返回迭代器的函数，
# 只能进行迭代操作
# 生成器函数 - 斐波那契数列
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a+b
        counter += 1
f = fibonacci(10)

while True:
    try:
        print(next(f), end=" \n")
    except StopIteration:
        sys.exit()
