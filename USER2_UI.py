import pandas as pd
from tabulate import tabulate
from tkinter import *
from tkinter.simpledialog import *

def user_2(phone1):
    phone = phone1
    def create_rbutton(rbutton_name,font,color,text,var,value,x,y):         # 라디오 버튼 배치 함수
        rbutton_name = Radiobutton(mainwindow,font=font,bg=color,text=text,variable=var,value=value)
        rbutton_name.place(x=x, y = y)
        return rbutton_name

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

    def user_update():
        df_user = pd.read_csv('csv/USER1.csv', encoding='CP949')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        def update_csv():
            df_user = pd.read_csv('csv/USER1.csv', encoding='CP949')
            df_user = df_user.set_index(df_user['USER_PHONE'])
                                                                        # 등록되어있는 회원들의 정보를 불러와서 출력
            USER_CHOICE = phone                               # 사용자가 선택한 회원의 전화번호(기본키)를 기준으로 정보 검색
            df_user.loc[USER_CHOICE,'USER_PHONE'] = phone_entry.get()
            df_user.loc[USER_CHOICE,'USER_NAME'] = name_entry.get()
            df_user.loc[USER_CHOICE,'USER_BIRTH'] = birth_entry.get()
            df_user.loc[USER_CHOICE,'USER_SEX'] = ' '#sex_button.get()
            df_user.loc[USER_CHOICE,'USER_MAIL'] = mail_entry.get()
            df_user.loc[USER_CHOICE,'USER_IMAGE'] = image_entry.get()
            df_user.loc[USER_CHOICE,'USER_REG'] = ' '#reg_entry.get()
            df_user.loc[USER_CHOICE,'USER_RENT_CNT'] = 4

            df_user.to_csv('csv/USER1.csv', index=False, encoding='CP949')   # 수정된 회원 정보 저장

            # 탈퇴 시
            #df_user.loc[USER_CHOICE,'USER_REG'] = False
            # 복구 시
            #df_user.loc[USER_CHOICE,'USER_REG'] = True

        sub_label = Label(mainwindow, text ="회원정보 수정",font=("맑은 고딕",9),bg='gray',height=3)
        image_label = Label(mainwindow, text='사진\n미리보기', bg='orange', width=15, height=10)
        state_label = Label(mainwindow, text ="등록 중",bg='orange')
        mainwindow.configure(background = 'sky blue')
        
        var = BooleanVar()

        # 위젯 배치
        sub_label.pack(fill=X)
        create_label(image_label,30,80)
        state_label.place(x=60,y=250)
        name_button = create_button('name_button','orange','이름',9,170,80)
        name_entry = create_entry('name_entry',df_user.loc[phone,'USER_NAME'],("맑은 고딕",12),35,250,80)
        birth_button = create_button('birth_button','orange','생년월일',9,170,120)
        birth_entry = create_entry('birth_entry',df_user.loc[phone,'USER_BIRTH'],("맑은 고딕",12),35,250,120)
        sex_button = create_button('sex_button','orange','성별',9,170,160)
        male_rbutton = create_rbutton('male_rbutton',("맑은 고딕",10),'sky blue','남',var,'남자',250,160)
        female_rbutton = create_rbutton('male_rbutton',("맑은 고딕",10),'sky blue','여',var,'여자',300,160)
        
        if df_user.loc[phone,'USER_SEX'] == '남자':
            male_rbutton.select()
            female_rbutton.deselect()
        elif df_user.loc[phone,'USER_SEX'] == '여자':
            male_rbutton.deselect()
            female_rbutton.select()
        phone_button = create_button('phone_button','orange','전화번호',9,170,200)
        phone_entry = create_entry('phone_entry',phone,("맑은 고딕",12),35,250,200)
        phone_check = create_button('phone_check','gray','중복확인',9,580,200)                          # 중복확인 버튼 미구현
        mail_button = create_button('mail_button','orange','이메일 주소',9,170,240)
        mail_entry = create_entry('mail_entry',df_user.loc[phone,'USER_MAIL'],("맑은 고딕",12),35,250,240)
        image_find = create_button('image_find','gray','찾아보기',9,580,280)
        image_button = create_button('image_button','orange','사진',9,170,280)
        image_entry = create_entry('image_entry',df_user.loc[phone,'USER_IMAGE'],("맑은 고딕",12),35,250,280)
        reg_button = Button(mainwindow,text='수정',bg='gray',width=9,command=update_csv)
        reg_button.place(x=150,y=400)
        ok_button = create_button('mail_button','gray','확인',9,300,400)
        cancel_button = create_button('mail_button','gray','취소',9,450,400)

    mainwindow = Tk()
    user_update()
    mainwindow.title("회원 수정")
    mainwindow.geometry("700x500")
    mainwindow.resizable(width=FALSE, height=FALSE)
    mainwindow.mainloop()
