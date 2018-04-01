

#创建只包一个元素的tuple
#加个逗号来区分
a_tuple = (2,)
#tuple元素不可以被更改
mixed_tuple = (1,2,['a','b'])
print("mixed_tuple : ",str(mixed_tuple))

mixed_tuple[2][0] = 'c'
mixed_tuple[2][1] = 'd'
print("mixed_tuple : ",str(mixed_tuple))
#这里为什么更改了呢?
#因为只是更改了tuple里面的list
'''
mixed_tuple :  (1, 2, ['a', 'b'])
mixed_tuple :  (1, 2, ['c', 'd'])
'''

# mixed_tuple[1] = 3
# print("mixed_tuple : ",str(mixed_tuple))
#TypeError: 'tuple' object does not support item assignment

#不能删除tuple中某个元素,可以直接删除tuple
del mixed_tuple
print("mixed_tuple : ",str(mixed_tuple))
#NameError: name 'mixed_tuple' is not defined

#其它方法同List中方法
