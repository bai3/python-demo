# coding:utf-8
'''
python支持三种不同的数值类型
- 整型（int）
- 浮点型（float）
- 复数（complex）
'''
number = 0xA0F
#十六进制
print(number)
# => 2575
number = 0o37
#八进制
print(number)
# => 31

#python的数字类型的转换
'''
- int(x)将x转换一个整数
- float(x)将x转换一个浮点数
- complex(x)将x转换一个复数，实数部分为x，虚数部分为0
- complex(x,y)将x和y转换到一个复数，实数部分为x，虚数部分为y
'''
a = 1.0
print(int(a))
# => 1
print(8/5)
# => 1.6
print(8//5)
# => 1
print(8%5)
# => 3
print(8**2)
# 进行平方运算 => 64

# print((8***2))
# 测试 => error 并不是三次方

# 不同类型的数混合运算时会将整数转换为浮点数
print(3*3.75/1.5)
# =>7.5

# 常用的数学函数
print(abs(-5))
# 绝对值 =>5
import  math
print(math.ceil(4.1))
# 向上取整 => 5
print(math.fabs(-5))
# 绝对值 => 5.0
print(math.floor(4.1))
# 向下取整 => 4
print(max(-5,2,3,100,10))
# 取最大值 => 100
print(min(-5, -2 ,-100 ,1))
# 取最小值 =>-100
print(pow(2,3))
# 2^3

# 随机数函数
'''
随机数可以用于数学，游戏，安全领域中，还经常
被嵌入算法中，用以提高算法效率，并提高程序的
安全性
'''
import  random
# choice 从序列的元素中随机挑选一个元素，比如random.choice(range(10)),从0到9随机挑选一个整数
print('随机数:'+str(random.choice(range(10))))
# random()随机在[0,1)中随机生成一个数
print(random.random())

# shuffle(list)将序列中的所有元素随机排列
# uniform(x.y)随机生成一个实数，它在[x,y]范围内。

# 数学常量
print(math.pi);
# 圆周率
print(math.e);
# 自然常数

