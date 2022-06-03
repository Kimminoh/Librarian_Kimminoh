from tkinter import *
from tkinter.simpledialog import *

def in_label():
    sub_label = Label(mainwindow, text ="회원 등록",font=("맑은 고딕",15,"bold"),bg='gray',height=3)


    var = IntVar()
    
    name_text = Entry(mainwindow, width=40)
    birth_text = Entry(mainwindow, width=40)
    male_rbutton = Radiobutton(mainwindow, text= "남",variable=var,value=1)
    female_rbutton = Radiobutton(mainwindow, text= "여",variable=var,value=2)
    phone_text = Entry(mainwindow, width=40)
    mail_text = Entry(mainwindow, width=40)
    image_text = Entry(mainwindow, width=40)
  
    sub_label.pack(fill=X)
    name_text.place(x= 220,y= 140)
    birth_text.place(x= 220,y= 180)
    male_rbutton.place(x= 220,y= 220)
    female_rbutton.place(x= 220,y= 260)
    phone_text.place(x= 220,y= 300)
    mail_text.place(x= 220,y= 340)
    image_text.place(x= 220,y= 380)

mainwindow = Tk()
in_label()
mainwindow.title("회원 등록")
mainwindow.geometry("800x800")
mainwindow.resizable(width=FALSE, height=FALSE)
mainwindow.mainloop()
