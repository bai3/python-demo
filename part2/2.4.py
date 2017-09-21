# 循环语句
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1到%d之和为:%d" % (n, sum))

# 无限循环
# var = 1
# while var == 1:
#     num = int(input("请输入一个数字:"))
#     print("你输入的数字式: ", num)
# print("Good bye5")

# for语句
# lanuages = ["C", "C++", "Perl", "Python"]
# for x in lanuages:
#     print(x)

# break跳出循环
sites = ["baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据" + site)
else:
    print("没有循环数据")
print("完成循环")

# range()函数
# 如果你想遍历数字序列，可以使用内置range()函数，它会生成数列
# example
for i in range(5):
    print(i)

# 指定范围
for i in range(4,12):
    print(i)

# 指定步长
for i in range(4,12,2):
    print(i)

# break
# break语句可以跳出for和while的循环体。
# break是跳出整个for或者while循环

# continue
# continue语句被用来告诉Python跳过循环块中的剩余语句，然后继续进行下一轮循环
# continue是跳出本次循环
# pass
# Python pass是空语句，是为了保持程序结构的完整性
# pass 不做任何事情，一般用作占位语句。