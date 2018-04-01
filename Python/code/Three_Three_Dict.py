#词典Dictionary

#创建一个词典
phone_book = {'Tom':123,'Jerry':456,'Kim':789}

# print("phone_book:",str(phone_book))

mixed_dict = {'Tom':'boy',11:23.5}
# print("mixed_dict:",str(mixed_dict))

#访问其中的值
# print("Tom has phone number :" + str(phone_book['Tom']))

#修改词典中的值
phone_book['Tom'] = 999
# print("Tom has phone number :" + str(phone_book['Tom']))

#添加一个新的元素
phone_book['Heath'] = 888
# print("phone_book:",str(phone_book))

#删除元素及词典本身
del phone_book['Tom']
# print("phone_book:",str(phone_book))

phone_book.clear()
# print("phone_book:",str(phone_book))

#把词典完全删除
del phone_book
#print("phone_book:",str(phone_book))

#词典的特性
#不允许重复key
# rep_test = {'Name':aa,'age':5,'Name':bb}
#NameError: name 'aa' is not defined
# print("rep_test:",str(rep_test))

#key是不可变的,所以可以用数字,字符串,元组但是不能用列表
#list_dict = {['Name']:'John','Age':13}
#TypeError: unhashable type: 'list'
list_dict = {('Name'):'John','Age':13}