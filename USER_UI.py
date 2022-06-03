from tkinter import *
from tkinter.simpledialog import *

def create_rbutton(rbutton_name,font,color,text,var,value,x,y):         # 라디오 버튼 배치 함수
    rbutton_name = Radiobutton(mainwindow,font=font,bg=color,text=text,variable=var,value=1)
    rbutton_name.place(x=x, y = y)
    return rbutton_name

def create_button(button_name,color,text,width,x,y):                   # 버튼 배치 함수
    button_name = Button(mainwindow,bg=color,text=text,width=width)
    button_name.place(x=x, y = y)
    return button_name

def create_label(label_name,x,y):                                       # 라벨 배치 함수
    label_name.place(x=x, y = y)

def create_entry(entry_name,font,width,x,y):                             # 엔트리 배치 함수
    entry_name = Entry(mainwindow, font=font,width=width)
    entry_name.place(x=x, y = y)
    return entry_name

def user_reg():

    sub_label = Label(mainwindow, text ="회원 등록",font=("맑은 고딕",9),bg='gray',height=3)
    image_label = Label(mainwindow, text='사진\n미리보기', bg='orange', width=15, height=10)
    state_label = Label(mainwindow, text ="등록 상태",bg='gray')
    mainwindow.configure(background = 'sky blue')
    
    var = IntVar()

    # 위젯 배치
    sub_label.pack(fill=X)
    create_label(image_label,30,80)
    state_label.place(x=60,y=250)
    name_button = create_button('name_button','orange','이름',9,170,80)
    name_entry = create_entry('name_entry',("맑은 고딕",12),35,250,80)
    birth_button = create_button('birth_button','orange','생년월일',9,170,120)
    birth_entry = create_entry('birth_entry',("맑은 고딕",12),35,250,120)
    sex_button = create_button('sex_button','orange','성별',9,170,160)
    male_rbutton = create_rbutton('male_rbutton',("맑은 고딕",10),'sky blue','남',var,1,250,160)
    female_rbutton = create_rbutton('male_rbutton',("맑은 고딕",10),'sky blue','여',var,2,300,160)
    phone_button = create_button('phone_button','orange','전화번호',9,170,200)
    phone_entry = create_entry('phone_entry',("맑은 고딕",12),35,250,200)
    phone_check = create_button('phone_check','gray','중복확인',9,580,200)
    mail_button = create_button('mail_button','orange','이메일 주소',9,170,240)
    mail_entry = create_entry('mail_entry',("맑은 고딕",12),35,250,240)
    image_find = create_button('image_find','gray','찾아보기',9,580,280)
    image_button = create_button('image_button','orange','사진',9,170,280)
    image_entry = create_entry('image_entry',("맑은 고딕",12),35,250,280)
    reg_button = create_button('mail_button','gray','등록',9,150,400)
    ok_button = create_button('mail_button','gray','확인',9,300,400)
    cancel_button = create_button('mail_button','gray','취소',9,450,400)

 

mainwindow = Tk()
user_reg()
mainwindow.title("회원 등록")
mainwindow.geometry("700x500")
mainwindow.resizable(width=FALSE, height=FALSE)
mainwindow.mainloop()
