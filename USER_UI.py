from tkinter import *
from tkinter.simpledialog import *

def in_label(label,title,x,y):
    label = Label(mainwindow, text= "{}".format(title))
    label.place(x=x,y=y)

def in_radiobutton(x1,y1,x2,y2):     
    var = IntVar()
    rb1 = Radiobutton(mainwindow, text= "남",variable=var,value=1)
    rb2 = Radiobutton(mainwindow, text= "여",variable=var,value=2)
    rb1.place(x=x1,y=y1)
    rb2.place(x=x2,y=y2)

def input(input_text,x,y):
    input_text = Entry(mainwindow, width=60)
    input_text.place(x=x,y=y)
    


mainwindow = Tk()
mainwindow.title("회원 등록")
mainwindow.geometry("800x800")

name_label = None
birth_label=None
sex_rbutton=None
phone_label=None
mail_label=None
image_label=None

in_label(name_label,'이름',60,100)
in_label(birth_label,'생년월일',60,140)
in_label(sex_rbutton,'성별',60,180)
in_radiobutton(140,180,260,180)
in_label(phone_label,'전화번호',60,220)
in_label(mail_label,'이메일 주소',60,260)
in_label(image_label,'사진',60,300)

name = None
birth=None
phone=None
mail=None
image=None
input(name,140,100)
input(birth,140,140)
input(mail,140,220)
input(image,140,260)

mainwindow.mainloop()