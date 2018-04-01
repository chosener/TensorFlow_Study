
#注意中文编码
# print("你好!")
#
# print("你好!\n世界!")
#
# print("What's your name ? \nTom")

#创建List
number_list = [1,3,5,7,9]
print("number_list : ",str(number_list))

string_list = ["abc","def","python"]
print("string_list : ",str(string_list))

mixed_list = ["python","java",3,12]
print("mixed_list : ",str(mixed_list))

#访问List中的元素
first_ele = mixed_list[1]
second_ele = string_list[2]
print("first_ele : {0} , secend_ele : {1}".format(first_ele,second_ele))

#修改更新元素
number_list[1] = 30
print("number_list ofter : ",str(number_list))

#删除
del number_list[1]
print("number_list ofter del : ",str(number_list))

#======
print(len([1,2,3]))
print([1,2,3] + [4,5,6])
print(['hello'] * 4)
print(3 in [1,2,3])

abcd_list = ['a','b','c','d']
print(abcd_list[1])
print(abcd_list[-2])
print(abcd_list[1:])

'''
3
[1, 2, 3, 4, 5, 6]
['hello', 'hello', 'hello', 'hello']
True
b
c
['b', 'c', 'd']
'''