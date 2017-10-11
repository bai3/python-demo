# python 日期和时间
# python 提供一个time和calendar模块可以用于格式化日期和时间
# 每个时间戳都自1970年1月1日午夜经过多长时间来表示

import time,calendar  # 引入时间模块

ticks = time.time()
# print("当前的时间戳为:", ticks)

# 获取当前时间

localtime = time.localtime(time.time())
# print("本地时间为:", localtime)

# 获取格式化时间

localtime = time.asctime(time.localtime(time.time()))
# print("本地时间为:", localtime)

# 格式化日期
# 可以使用time模块的strftime方法来格式化日期

# 格式化2016-03-20 11:11:11 形式
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式化字符串转换时间戳
a = "Sat Mar 28 22:24:24 2016"
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))

# 获取某月日历

cal = calendar.month(2016, 1)
print("将输出2016年一月份的日历:")
print(cal)

