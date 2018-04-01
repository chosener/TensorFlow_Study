#函数

#定义一个函数
def say_hi():
    print("hi!")

def say(info):
    print(info)

say_hi()
say_hi()

say("我是一个函数!")

def print_sum_two(a,b):
    c = a + b
    print(c)

print_sum_two(2,3)

#有返回值
def repeat_str(str,times):
    repeat_strs = str * times
    return repeat_strs

repeat_strings = repeat_str("Happy Birthday !",4)
print(repeat_strings)

#全局 局部变量
# x = 60
#
# def foo(x):
#     print("x is:" + str(x))
#     x = 3
#     print("change local x to " + str(x))
#
# foo(x)
# print("x is still ",str(x))

x = 60
def foo():
    global x
    print("x is :",str(x))
    x = 3
    print("change local x to ",str(x))

foo()
print("value of x is ",str(x))