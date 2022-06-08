import pandas as pd
from tkinter import *
from tkinter.simpledialog import *
from PIL import Image,ImageTk
from tkinter.filedialog import *
import tkinter.messagebox


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

    def ok_notice():   # 예외처리 3
        tkinter.messagebox.showinfo("정보","수정이 완료 되었습니다.")
    def check_pass():   # 예외처리 4
        tkinter.messagebox.showinfo("정보","사용 가능한 전화번호입니다.")
    def check_nonpass():   # 예외처리 5
        tkinter.messagebox.showerror("ERROR","이미 등록된 전화번호입니다.")
    def REG_ERROR():   # 예외처리 6
        tkinter.messagebox.showerror("ERROR","회원 정보는 모두 입력해야 합니다. 다시 작성해주세요 !")
    
    def user_update():
        df_user = pd.read_csv('csv/USER1.csv', encoding='utf-8')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        
        def find_image_name():
            file_name=askopenfilename(parent=mainwindow,filetype=(("PNG파일", "*.png"),("모든 파일","*.*")))

            photo = Image.open(file_name)
            photo2 = photo.resize((120, 150))
            photo3 = ImageTk.PhotoImage(photo2,master=mainwindow)
            image_label.configure(image=photo3, width=120, height=150)
            image_label.image=photo3
            image_entry.insert(1.0,file_name)
            image_entry['state'] = 'disabled'
            image_find['state'] = 'disabled'
        
        var = StringVar(mainwindow)

        def update_csv():
            df_user = pd.read_csv('csv/USER1.csv', encoding='utf-8')
            df_user = df_user.set_index(df_user['USER_PHONE'])
                                                                        # 등록되어있는 회원들의 정보를 불러와서 출력
            input_phone = phone_entry.get()
            input_name = name_entry.get()
            input_birth = birth_entry.get()
            input_mail = mail_entry.get()
            input_image = image_entry.get('1.0','end')

            if input_phone.strip()=="" or input_name.strip()==""or input_birth.strip()=="" or input_mail.strip()=="" or input_image.strip()=="":               
                REG_ERROR()
                return 0
            else:
            
                USER_CHOICE = phone                               # 사용자가 선택한 회원의 전화번호(기본키)를 기준으로 정보 검색
                df_user.loc[USER_CHOICE,'USER_PHONE'] = input_phone
                df_user.loc[USER_CHOICE,'USER_NAME'] = input_name
                df_user.loc[USER_CHOICE,'USER_BIRTH'] = input_birth
                df_user.loc[USER_CHOICE,'USER_SEX'] = var.get()
                df_user.loc[USER_CHOICE,'USER_MAIL'] = input_mail
                df_user.loc[USER_CHOICE,'USER_IMAGE'] = input_image
                df_user.loc[USER_CHOICE,'USER_RENT_CNT'] = 4

                df_user.to_csv('csv/USER1.csv', index=False, encoding='utf-8')   # 수정된 회원 정보 저장
                ok_notice()
                mainwindow.destroy()
       
        def phonenum_check():
                
                df_user = pd.read_csv("csv/USER1.csv",encoding='utf-8')
                df_user = df_user.set_index(df_user['USER_PHONE'])
                
                choice_phone = phone_entry.get()
                phone_number = df_user.index.tolist()
                if choice_phone == phone:
                    check_pass()
                    phone_check['state'] = 'disabled'
                    phone_entry['state'] = 'disabled'
                    reg_button['state']='normal'
                
                elif  str(choice_phone) not in phone_number:
                    check_pass()
                    phone_check['state'] = 'disabled'
                    phone_entry['state'] = 'disabled'
                    reg_button['state']='normal'
                else:
                    check_nonpass()

        sub_label = Label(mainwindow, text ="회원정보 수정",font=("맑은 고딕",9),bg='gray',height=3)
        image_label = Label(mainwindow, bg='orange', width=15, height=10)
        

        state_label = Label(mainwindow,bg='orange')
        if df_user.loc[phone,'USER_REG'] == True:
            state_label.config(text='등록 상태')
        elif df_user.loc[phone,'USER_REG'] == False:
            state_label.config(text='탈퇴 상태')
        mainwindow.configure(background = 'sky blue')
        
        

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
        female_rbutton = create_rbutton('female_rbutton',("맑은 고딕",10),'sky blue','여',var,'여자',300,160)
        
        if df_user.loc[phone,'USER_SEX'] == '남자':
            male_rbutton.select()
            female_rbutton.deselect()
        elif df_user.loc[phone,'USER_SEX'] == '여자':
            male_rbutton.deselect()
            female_rbutton.select()
        phone_button = create_button('phone_button','orange','전화번호',9,170,200)
        phone_entry = create_entry('phone_entry',phone,("맑은 고딕",12),35,250,200)
        phone_check = Button(mainwindow,text='중복확인',bg='gray',width=9,command=phonenum_check)
        phone_check.place(x=580,y=200)                      
        mail_button = create_button('mail_button','orange','이메일 주소',9,170,240)
        mail_entry = create_entry('mail_entry',df_user.loc[phone,'USER_MAIL'],("맑은 고딕",12),35,250,240)
        image_find = Button(mainwindow,text='찾아보기',bg='gray',width=9,command=find_image_name) #,command=image_search
        image_find.place(x=580,y=280)
        image_button = create_button('image_button','orange','사진',9,170,280)
        image_entry = Text(mainwindow, font=("맑은 고딕",12),width=35,height=4)
        image_entry.insert(1.0,df_user.loc[phone,'USER_IMAGE'])
        image_entry.place(x=250,y=280)
        image1=image_entry.get('1.0','end').replace('\n','')
        photo = Image.open(image1)
        photo2 = photo.resize((120, 200))
        photo3 = ImageTk.PhotoImage(photo2,master=mainwindow)
        image_label.configure(image=photo3, width=120, height=150)
        image_label.image=photo3
        reg_button = Button(mainwindow,text='수정',bg='gray',width=9,command=update_csv)
        reg_button.place(x=200,y=400)
        reg_button['state']='disabled'
        cancel_button = Button(mainwindow,bg='gray',text='취소',width=9,command=mainwindow.destroy)
        
        cancel_button.place(x=400,y=400)
        

    mainwindow = Tk()
    user_update()
    mainwindow.title("회원 수정")
    mainwindow.geometry("700x500")
    mainwindow.resizable(width=FALSE, height=FALSE)
    mainwindow.mainloop()
