import pandas as pd
import csv
from tabulate import tabulate
from tkinter import *
from tkinter import ttk
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

    keyword_entry = create_entry('keyword_entry','이름 혹은 전화번호를 입력하세요.',("맑은 고딕",12),40,120,80)
    search_button = create_button('search_button','gray','검색',9,560,80)
    update_button = create_button('update_button','gray','수정',9,560,120)
    info_button = create_button('info_button','gray','상세 정보',9,560,160)
    treeview = ttk.Treeview(mainwindow,column=['이름','전화번호','성별','도서대여권수'],displaycolumns=['이름','전화번호','성별','도서대여권수'])
    csv_list = []
    f = open('csv/USER1.csv','r')
    reader = csv.reader(f)
    for row in reader:
        csv_list.append(row)
    f.close()
    
    for a,b,c,d,e,f,g,h in csv_list:
        treeview.insert('','end',values=[b,a,d,h])
    #yscrollbar = Scrollbar(mainwindow,orient='vertical',command=user_list.yview)
    #yscrollbar.pack()
    #yscrollbar.place(x=640, y=220)
    treeview.column("이름",width=70,anchor="center",stretch=True)
    treeview.heading("이름",text="이름",anchor="center")
    treeview.column("전화번호",width=150,anchor="center",stretch=True)
    treeview.heading("전화번호",text="전화번호",anchor="center")
    treeview.column("성별",width=50,anchor="center",stretch=True)
    treeview.heading("성별",text="성별",anchor="center")
    treeview.column("도서대여권수",width=150,anchor="center",stretch=True)
    treeview.heading("도서대여권수",text="도서대여권수",anchor="center")
    treeview["show"] = "headings"

    #user_list.config(yscrollcommand=yscrollbar.set)
    #treeview.xview()
    treeview.place(x=50,y=220)
    sub_label.pack(fill=X)

mainwindow = Tk()
mainwindow.title("회원 검색/수정/탈퇴")
mainwindow.geometry("700x500")
user_search()
mainwindow.resizable(width=FALSE, height=FALSE)
mainwindow.mainloop()