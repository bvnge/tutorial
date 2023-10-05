from msilib.schema import CheckBox
import random
from tkinter import *
import string
import tkinter 

window = Tk()
window.title('Project_Password')
window.geometry('400x800')

Label(window,font=('bold',30),text='PASSWORD GENERATOR PYTHON').pack()

len1=tkinter.IntVar()
len2=tkinter.IntVar()
len3=tkinter.IntVar()

def password_generate(leng):
    valid_char='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_#$%^&'
    password=''.join(random.sample(valid_char,leng))
    l =Label(window, text = password, font=('bold', 20)) 
    l.place(x=180,y=50)

def get_len():
    if len1.get() == 4:
        password_generate(4)
    elif len2.get() == 6:
        password_generate(6)
    elif len3.get() == 8:
        password_generate(8)
    else:
        password_generate(6)    

Button(window,text='Generate',font=('normal',10), bg='green',command=get_len).place(x=400,y=200)

Checkbutton(text='6 characters',onvalue=6, offvalue=0,variable=len1).place(x=200,y=150)
Checkbutton(text='8 characters',onvalue=8, offvalue=0,variable=len2).place(x=200,y=170)
Checkbutton(text='10 characters',onvalue=10, offvalue=0,variable=len3).place(x=200,y=190)

window.mainloop()


