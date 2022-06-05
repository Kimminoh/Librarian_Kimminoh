import pandas as pd
from tabulate import tabulate
from tkinter import *
from tkinter.simpledialog import *

def create_button(button_name,color,text,width,x,y):                   # 버튼 배치 함수
    button_name = Button(mainwindow,bg=color,text=text,width=width)
    button_name.place(x=x, y = y)
    return button_name

def create_label(label_name,x,y):                                       # 라벨 배치 함수
    label_name.place(x=x, y = y)

def create_entry(entry_name,text,font,width,x,y):                             # 엔트리 배치 함수
    entry_name = Entry(mainwindow,font=font,width=width)
    entry_name.insert(0,text)
    entry_name.place(x=x, y = y)
    return entry_name


def user_search():
    sub_label = Label(mainwindow, text ="회원 검색",font=("맑은 고딕",9),bg='gray',height=3)
    user_list = Listbox(mainwindow,width=65,height=10,font=("맑은 고딕",12))


    user_list.place(x=50,y=220)
    sub_label.pack(fill=X)

mainwindow = Tk()
mainwindow.title("회원 검색/수정/탈퇴")
mainwindow.geometry("700x500")
user_search()
mainwindow.resizable(width=FALSE, height=FALSE)
mainwindow.mainloop()