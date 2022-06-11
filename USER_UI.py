import pandas as pd
from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from PIL import Image,ImageTk
import tkinter.messagebox

def USER_3():
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

    def create_entry(entry_name,font,width,x,y):                             # 엔트리 배치 함수
        entry_name = Entry(mainwindow, font=font,width=width)
        entry_name.place(x=x, y = y)
        return entry_name



    def user_reg():
        
        def inuser_csv():
            
            df_user = pd.read_csv('csv/USER.csv', encoding='utf-8')
            df_user = df_user.set_index(df_user['USER_PHONE'])
            def ERROR_2():   # 예외처리 2
                tkinter.messagebox.showinfo("정보","등록이 완료 되었습니다.")
            def ERROR_6():   # 예외처리 6
                tkinter.messagebox.showerror("ERROR","해당 정보는 필수정보 입니다. 다시 작성해주세요 !")


            a = phone_entry.get()
            b = name_entry.get()
            c= birth_entry.get()
            d = mail_entry.get()
            e = image_entry.get('1.0','end')
            

            if a.strip()=="" or b.strip()==""or c.strip()=="" or d.strip()=="" or e.strip()=="":               
                ERROR_6()
                return 0
            else:
                new_user = { "USER_PHONE": phone_entry.get(),                     # -(하이픈) 포함
                        "USER_NAME": name_entry.get(),                         # 영문일 시 공백포함
                        "USER_BIRTH": birth_entry.get(),                       # YYYYMMDD 
                        "USER_SEX": var.get(),                                # TRUE : 남자, FALSE : 여자
                        "USER_MAIL": mail_entry.get(),
                        "USER_REG" : True,
                        "USER_IMAGE": image_entry.get('1.0','end'),                     # 기본값 None(흰 배경)
                        "USER_RENT_CNT": 0 }                                 # +1, -1 하는 방식
                df_user = df_user.append(new_user, ignore_index=True)           # 데이터프레임을 추가하고 행 인덱스를 재배열
                df_user = df_user.set_index(df_user['USER_PHONE'])               # USER_PHONE을 인덱스로 사용

                df_user.to_csv('csv/USER.csv', index=False, encoding='utf-8')
                ERROR_2()
                mainwindow.destroy()
        
        photo = PhotoImage(master=mainwindow)
        sub_label = Label(mainwindow, text ="회원 등록",font=("맑은 고딕",9),bg='gray',height=3)
        image_label = Label(mainwindow,image=photo,width=120, height=150)

        mainwindow.configure(background = 'sky blue')
        
        var = StringVar(mainwindow)
        
        def phonenum_check():
            df_user = pd.read_csv("csv/USER.csv",encoding='utf-8')
            df_user = df_user.set_index(df_user['USER_PHONE'])
            
            a = phone_entry.get()
            phone_number = df_user.index.tolist()

            if  str(a) not in phone_number:
                phone_check['state'] = 'disabled'
                phone_entry['state'] = 'disabled'
                reg_button['state']='normal'

        def find_image_name():
            file_name=askopenfilename(parent=mainwindow,filetype=(("PNG파일", "*.png"),("모든 파일","*.*")))

            photo = Image.open(file_name)
            photo2 = photo.resize((120, 150))
            photo3 = ImageTk.PhotoImage(photo2,master=mainwindow)
            image_label.configure(image=photo3, width=120, height=150)
            image_label.image=photo3
            image_entry.insert(1.0,file_name)
            
        # 위젯 배치
        sub_label.pack(fill=X)
        image_label.pack()
        image_label.place(x=30,y=80)
        name_button = create_button('name_button','orange','이름',9,170,80)
        name_entry = create_entry('name_entry',("맑은 고딕",12),35,250,80)
        birth_button = create_button('birth_button','orange','생년월일',9,170,120)
        birth_entry = create_entry('birth_entry',("맑은 고딕",12),35,250,120)
        sex_button = create_button('sex_button','orange','성별',9,170,160)
        male_rbutton = create_rbutton('male_rbutton',("맑은 고딕",10),'sky blue','남',var,'남자',250,160)
        female_rbutton = create_rbutton('female_rbutton',("맑은 고딕",10),'sky blue','여',var,'여자',300,160)
        phone_button = create_button('phone_button','orange','전화번호',9,170,200)
        phone_entry = create_entry('phone_entry',("맑은 고딕",12),35,250,200)
        phone_check = Button(mainwindow,text='중복확인',bg='gray',width=9,command=phonenum_check)
        phone_check.place(x=580,y=200)                      
        mail_button = create_button('mail_button','orange','이메일 주소',9,170,240)
        mail_entry = create_entry('mail_entry',("맑은 고딕",12),35,250,240)
        image_find = Button(mainwindow,text='찾아보기',bg='gray',width=9,command=find_image_name) #,command=image_search
        image_find.place(x=580,y=280)
        image_button = create_button('image_button','orange','사진',9,170,280)
        image_entry = Text(mainwindow, font=("맑은 고딕",12),width=35,height=4)
        image_entry.place(x=250, y = 280)
        reg_button = Button(mainwindow,text='등록',bg='gray',width=9,command=inuser_csv)
        reg_button.place(x=200,y=400)
        reg_button['state']='disabled'
        cancel_button = Button(mainwindow,bg='gray',text='취소',width=9,command=mainwindow.destroy)
            
        cancel_button.place(x=400,y=400)
        



    mainwindow = Tk()
    user_reg()
    mainwindow.title("회원 등록")
    mainwindow.geometry("700x500")
    mainwindow.resizable(width=FALSE, height=FALSE)
    mainwindow.mainloop()
