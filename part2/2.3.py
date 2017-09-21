# 条件控制
a = 100
if a > 10:
    print("{0}大于10".format(a))
elif a == 10:
    print("{0}等于10".format(a))
else:
    print("{0}小于10".format(a))

# 注意 Python中没有switch-case语句
age = int(input("请输入你家狗狗的年龄: "))
if age <= 0:
    print("你是在逗我吧")
elif age == 1:
    print("相当于14岁人的人")
elif age == 2:
    print("相当于22岁的人")
elif age > 2:
    human = 22 + (age - 2)*5
    print("对应人类年龄:", human)

input("点击enter键退出")

# if的嵌套
num = int(input("请输入一个数字: "))
if num%2 == 0:
    if num%3 == 0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以被2整除，但是不能被3整除")
else:
    if num%3 == 0:
        print("你输入的数字可以整除3，但不能整除2")
    else:
        print("你输入的数字不能整除2和3")