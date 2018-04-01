#函数

#默认参数
def repeat_str(s,times = 1):
    repeat_strs = s * times
    return repeat_strs

repeat_strings = repeat_str("Happy Birthday !")
print(repeat_strings)

repeat_strings_2 = repeat_str("Happy Birthday !",4)
print(repeat_strings_2)

#关键字参数
def func(a,b = 4,c = 8):
    print("a is ",a,', and b is ',b,", and c is ",c)

func(13,17)
func(125,c = 24)
func(c = 40,a = 90)

#VarArgs函数
#nums作为一个元组
#words作为一个词典
def print_paras(fpara,*nums,**words):
    print("fpara:" + str(fpara))
    print("nums:" + str(nums))
    print("words:" + str(words))

print_paras("hello",1,3,5,7,word = "python",another_word = "java")