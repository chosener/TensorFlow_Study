#while example

# number = 59
# guess_flag = False
#
# while guess_flag == False:
#     guess = int(input('Enter an integer:'))
#     if guess == number:
#         guess_flag = True
#     elif guess < number:
#         print('No,the number is higher than that,keep guessing')
#     else:
#         print('No,the number is lower than that,keep guessing')
#
# print('Bingo! you guessed it right.')
# print('but you do not win any prizes !')
# print('Done')

#range example
number = 59
num_chances = 3
print('you have only 3 chances to guess .')

#range(1,4) 取的是1,2,3
for i in range(1,num_chances + 1):
    print('chance : ' + str(i))
    guess = int(input('Enter an integer :'))
    if guess == number:
        print('Bingo! you guessed it right.')
        print('but you do not win any prizes !')
        break
    elif guess < number:
        print('No,the number is higher than that,keep guessing,you have ' + str(num_chances - i) + ' chances left.')
    else:
        print('No,the number is lower than that,keep guessing,you have ' + str(num_chances - i) + 'chances left.')

print('Done')