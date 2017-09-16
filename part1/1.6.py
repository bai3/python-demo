# coding:utf-8
'''
Python字典
字典是另一种可变容器模型，且可存储任意类型的对象
字典的每个键值对用冒号(:)分割，
每个对之间用逗号(,)分割
整个字典包括在花括号({})中
基本格式
d = {key1: value1, key2: value2}
键必须是唯一，但值则不必。
值可以取任何数据类型，但键必须是不变，
如字符串，数字或元组。
'''

'''
修改字典
'''
dict = {'Name': 'Runoob',"Age": 7,"Class": 'First'}
dict['Age'] = 8; #更新Age
dict['School'] = '菜鸟教程'; #添加信息
print("dict['Age']:",dict['Age'])
print("dict[School]:",dict['School'])

'''
删除字典袁术
能删单一的元素也能清楚字典，清空只需一项操作clear
显示删除一个字典用del命令
执行del操作后 字典就不存在了
'''