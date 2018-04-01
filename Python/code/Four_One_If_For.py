#if statement example

# number = 59
# guess = int(input('Enter on integer : '))
# print('guess is :',guess)
# #低版本
# # print('guess is :',str(guess))
#
# if guess == number:
#     # New block starts here
#     print('Bingo ! you guessed it right .')
#     print('but you do not win any prizes !')
#     # New block ends here
# elif guess < number:
#     print('No, the number is higher than that .')
# else:
#     print('No,the number is a lower than that .')
#
# print('Done')
#This last statement is always executed,
#after the if statement is executed.


#for loop example
for i in range(1,10):
    print(i)
else:
    print('the for loop is over .')

#List
a_list = [1,3,5,7,9]
for i in a_list:
    print(i)

#tuple

#dictionary
a_dict = {'Tom':'111','Jerry':'222','Cathy':'333'}
for key,elem in a_dict.items():
    print(key,elem)