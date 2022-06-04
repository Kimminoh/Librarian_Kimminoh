from tkinter import *
from tkinter.simpledialog import *

def in_label(label,title,x,y):
    label = Label(mainwindow, text= "{}".format(title))
    label.place(x=x,y=y)


def input(input_text,x,y):
    input_text = Entry(mainwindow, width=60)
    input_text.place(x=x,y=y)


mainwindow = Tk()
mainwindow.title("회원 등록")
mainwindow.geometry("800x800")

name_label = None
birth_label=None
phone_label=None
mail_label=None
image_label=None

in_label(name_label,'이름',60,100)
in_label(birth_label,'생년월일',60,140)
in_label(phone_label,'전화번호',60,180)
in_label(mail_label,'이메일 주소',60,220)
in_label(image_label,'사진',60,260)


name = None
birth=None
phone=None
mail=None
image=None
input(name,140,100)
input(birth,140,140)
input(phone,140,180)
input(mail,140,220)
input(image,140,260)

mainwindow.mainloop()