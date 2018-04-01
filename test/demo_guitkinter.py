#图形界面库
from tkinter import *

import tkinter.simpledialog as dl
import tkinter.messagebox as mb

'''
root  = Tk()

w = Label(root,text = "label title")
w.pack()

#信息框
mb.showinfo("Welcome","Welcome Message")
#又弹一个新的对话框
guess = dl.askinteger("Number","Enter a number")

output = 'This is output message'
mb.showinfo("Output:",output)
'''
root = Tk()
#创建一个Label
w = Label(root,text = "Guess Number Game")
w.pack()
#显示信息框
mb.showinfo("Welcome","Welcome to Guess Number Game")

#定义一个数字
number = 59
#循环猜
while True:
    guess = dl.askinteger("Number","What's your guess ?")
    if guess == number:
        output = "Bingo! you guessed it right. but you do not win any prizes !"
        mb.showinfo("Hint:",output)
        break
    elif guess < number:
        output = "No,the number is a biger than that."
        mb.showinfo("Hint:",output)
    else:
        output = "No,the number is a lower than that."
        mb.showinfo("Hint:",output)
print("Done")
