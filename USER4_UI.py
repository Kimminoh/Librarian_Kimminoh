import pandas as pd
from tkinter import *
from tkinter.simpledialog import *
from PIL import Image,ImageTk
from tkinter.filedialog import *
import tkinter.messagebox



def user_2(phone1):
    phone = phone1
    def create_rbutton(rbutton_name,font,text,var,value,x,y):         # 라디오 버튼 배치 함수
        rbutton_name = Radiobutton(mainwindow,font=font,text=text,variable=var,value=value)
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
        df_user = pd.read_csv('csv/user.csv', encoding='utf-8')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        sub_label = Label(mainwindow, text ="회원 상세 정보",font=("맑은 고딕",9),bg='gray',height=3)
        image_label = Label(mainwindow,width=120, height=150)
        
        def ERROR_4():   # 예외처리 4
            tkinter.messagebox.showinfo("정보","탈퇴가 완료되었습니다.")
        def ERROR_5():   # 예외처리 5
            tkinter.messagebox.showinfo("정보","복구가 완료되었습니다.")

        state_label = Label(mainwindow, text ="등록 상태",bg='gray')
        if bool(df_user.loc[phone,'USER_REG']) == True:
            state_label.config(text='등록 상태')
        elif bool(df_user.loc[phone,'USER_REG']) == False:
            state_label.config(text='탈퇴 상태')
        
        
        var = BooleanVar()

        # 위젯 배치
        sub_label.pack(fill=X)
        create_label(image_label,30,80)
        state_label.place(x=60,y=250)
        name_button = create_button('name_button','gray','이름',9,170,80)
        name_entry = create_entry('name_entry',df_user.loc[phone,'USER_NAME'],("맑은 고딕",12),35,250,80)
        birth_button = create_button('birth_button','gray','생년월일',9,170,120)
        birth_entry = create_entry('birth_entry',df_user.loc[phone,'USER_BIRTH'],("맑은 고딕",12),35,250,120)
        sex_button = create_button('sex_button','gray','성별',9,170,160)
        male_rbutton = create_rbutton('male_rbutton',("맑은 고딕",10),'남',var,'남자',250,160)
        female_rbutton = create_rbutton('male_rbutton',("맑은 고딕",10),'여',var,'여자',300,160)
        
        if df_user.loc[phone,'USER_SEX'] == '남자':
            male_rbutton.select()
            female_rbutton.deselect()
        elif df_user.loc[phone,'USER_SEX'] == '여자':
            male_rbutton.deselect()
            female_rbutton.select()

        def state_change():
            if bool(df_user.loc[phone,'USER_REG']) == True:
               if df_user.loc[phone,'USER_RENT_CNT'] == 0: 
                df_user.loc[phone,'USER_REG'] = False
                ERROR_4()
               else :
                   tkinter.messagebox.showerror("오류","도서를 대여중인 회원은 탈퇴가 불가능합니다,")
            else:
                df_user.loc[phone,'USER_REG'] = True
                ERROR_5()
            df_user.to_csv('csv/user.csv', index=False, encoding='utf-8')
            mainwindow.destroy()

        phone_button = create_button('phone_button','gray','전화번호',9,170,200)
        phone_entry = create_entry('phone_entry',phone,("맑은 고딕",12),35,250,200)
        mail_button = create_button('mail_button','gray','이메일 주소',9,170,240)
        mail_entry = create_entry('mail_entry',df_user.loc[phone,'USER_MAIL'],("맑은 고딕",12),35,250,240)
        image_find = create_button('image_find','gray','찾아보기',9,580,280)
        image_button = create_button('image_button','gray','사진',9,170,280)
        image_entry = Text(mainwindow, font=("맑은 고딕",12),width=35,height=4)
        image_entry.insert(1.0,df_user.loc[phone,'USER_IMAGE'])
        image_entry.place(x=250,y=280)

        image1=image_entry.get('1.0','end').replace('\n','')
        photo = Image.open(image1)
        photo2 = photo.resize((120, 150))
        photo3 = ImageTk.PhotoImage(photo2,master=mainwindow)
        image_label.configure(image=photo3, width=120, height=150)
        image_label.image=photo3

        reg_button = Button(mainwindow,bg='gray',width=9,command=state_change)
        
        if df_user.loc[phone,'USER_REG'] == True:
            reg_button.config(text='탈퇴')
        elif df_user.loc[phone,'USER_REG'] == False:
            reg_button.config(text='복구')

        
        ok_button = Button(mainwindow,bg='gray',text='확인',width=9,command=mainwindow.destroy)
        
        
        reg_button.place(x=200,y=400)
        ok_button.place(x=400,y=400)
        
        name_entry['state'] = 'disabled'
        birth_entry['state'] = 'disabled'
        male_rbutton['state'] = 'disabled'
        female_rbutton['state'] = 'disabled'
        phone_entry['state'] = 'disabled'
        phone_entry['state'] = 'disabled'
        mail_entry['state'] = 'disabled'
        image_entry['state'] = 'disabled'
        image_find.destroy()
        

    mainwindow = Tk()
    user_update()
    mainwindow.title("회원 수정")
    mainwindow.geometry("700x500")
    mainwindow.resizable(width=FALSE, height=FALSE)
    mainwindow.mainloop()
