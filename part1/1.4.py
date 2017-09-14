# coding:utf-8

'''
Python3列表
序列式Python中最基本的数据结构，序列中的每个元素都分配一个数字，
即是它的位置，或叫做索引，第一个索引是0。
python有6个序列的内置类型，最常见的是列表和元素组。
序列都可以进行的操作包括索引，切片，加，乘，检查成员
'''

list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
print(list1[0])
# => Google
print(list2[1:4])
# => [2, 3, 4]
del list2[1]
print(list2[1])
print(list2)

'''
更新列表
- 修改数据  直接对数据进行跟新
- 删除列表元素 可以使用del语句来删除列表的元素
'''

# python列表脚本操作符

print(len([1, 2, 3]))
# => 3

print([1, 2, 3] + [4, 5, 6])
# =>[1, 2, 3, 4, 5, 6]

print(['bai']*4)
# => ['bai', 'bai', 'bai', 'bai']

print(2 in [4, 5])
# => false

for x in [1, 2, 3, 4]:
    print(x)
'''
=>
1 
2
3
4
'''

'''
python列表其他方法
- list.append(obj) 在列表末尾添加新的对象
- list.count(obj) 统计某个元素在列表中出现的次数
- list.extend(seq) 在列表末尾一次性追加另一序列的多个值
- list.index(obj) 在列表中找出某个值第一个匹配项的索引位置
- list.insert(index,obk) 将对象插入列表
- list.pop(obj = list[-1]) 移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值
- list.remove(obj) 移除列表中某个值第一个匹配项
- list.reverse() 反向列表中的数据
- list.sort([func]) 对原列表进行排序
- list.clear() 清空列表
- list.copy() 复制列表
'''
