import pandas as pd
from tkinter import *
import tkinter.ttk as ttk
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
            
            df_user = pd.read_csv('csv/user.csv', encoding='utf-8')
            df_user = df_user.set_index(df_user['USER_PHONE'])
            def ERROR_2():   # 예외처리 2
                tkinter.messagebox.showinfo("정보","등록이 완료 되었습니다.")
            def ERROR_6():   # 예외처리 6
                tkinter.messagebox.showerror("ERROR","해당 정보는 필수정보 입니다. 다시 작성해주세요 !")


            input_phone = phone_entry.get()
            input_name = name_entry.get()
            yy = yearcombo.get()
            mm = monthcombo.get()
            dd = daycombo.get() 
            input_birth = yy + mm + dd
            input_mail = mail_entry.get()
            input_image = image_entry.get('1.0','end')

            if input_phone.strip()=="" or input_name.strip()==""or input_birth.strip()=="" or input_mail.strip()=="" or input_image.strip()==""\
                or yy.strip()==""or mm.strip()==""or dd.strip()=="":
                ERROR_6()
                return 0
            else:
                new_user = { "USER_PHONE": input_phone,                     # -(하이픈) 포함
                        "USER_NAME": input_name,                         # 영문일 시 공백포함
                        "USER_BIRTH": input_birth,                                      # YYYYMMDD 
                        "USER_SEX": var.get(),                                # TRUE : 남자, FALSE : 여자
                        "USER_MAIL": input_mail,
                        "USER_REG" : True,
                        "USER_IMAGE": image_entry.get('1.0','end'),          # 기본값 None(흰 배경)
                        "USER_RENT_CNT": 0 }                                 # +1, -1 하는 방식
                df_user = df_user.append(new_user, ignore_index=True)           # 데이터프레임을 추가하고 행 인덱스를 재배열
                df_user = df_user.set_index(df_user['USER_PHONE'])               # USER_PHONE을 인덱스로 사용

                df_user.to_csv('csv/user.csv', index=False, encoding='utf-8')
                ERROR_2()
                mainwindow.destroy()
        
        photo = PhotoImage(master=mainwindow)
        sub_label = Label(mainwindow, text ="회원 등록",font=("맑은 고딕",9),bg='gray',height=3)
        image_label = Label(mainwindow,image=photo,width=120, height=150)

        mainwindow.configure(background = 'sky blue')
        
        var = StringVar(mainwindow)
        
        def phonenum_check():
            def check_pass():   # 예외처리 4
                tkinter.messagebox.showinfo("정보","사용 가능한 전화번호입니다.")
            def check_nonpass():   # 예외처리 5
                tkinter.messagebox.showerror("ERROR","이미 등록된 전화번호입니다.")           

            df_user = pd.read_csv("csv/user.csv",encoding='utf-8')
            df_user = df_user.set_index(df_user['USER_PHONE'])
            
            a = phone_entry.get()
            phone_number = df_user.index.tolist()

            if  str(a) not in phone_number:
                check_pass()
                phone_check['state'] = 'disabled'
                phone_entry['state'] = 'disabled'
                reg_button['state'] = 'normal'
            else:
                check_nonpass()

        def find_image_name():
            file_name=askopenfilename(parent=mainwindow,filetype=(("PNG파일", "*.png"),("모든 파일","*.*")))

            photo = Image.open(file_name)
            photo2 = photo.resize((120, 150))
            photo3 = ImageTk.PhotoImage(photo2,master=mainwindow)
            image_label.configure(image=photo3, width=120, height=150)
            image_label.image=photo3
            image_entry.delete(1.0,"end")
            image_entry.insert(1.0,file_name)
        
        year = []
        month = []
        day = []

        for i in range(1900,2023):
            year.append(str(i))
        for j in range(1,13):
            if (j < 10):
                j = '0' + str(j)
            month.append(j)
        for k in range(1,32):
            if (k < 10):
                k = '0' + str(k)
            day.append(k)

        yearcombo = ttk.Combobox(mainwindow,width=6,height=5,values=year,state="readonly")
        monthcombo = ttk.Combobox(mainwindow,width=4,height=5,values=month,state="readonly")
        daycombo = ttk.Combobox(mainwindow,width=4,height=5,values=day,state="readonly")
        yearcombo.set("")
        monthcombo.set("")
        daycombo.set("")
        yearcombo.pack()
        monthcombo.pack()
        daycombo.pack()
        yearcombo.place(x=250,y=120)
        monthcombo.place(x=350,y=120)
        daycombo.place(x=450,y=120)



        # 위젯 배치
        sub_label.pack(fill=X)
        image_label.pack()
        image_label.place(x=30,y=80)
        name_button = create_button('name_button','orange','이름',9,170,80)
        name_entry = create_entry('name_entry',("맑은 고딕",12),35,250,80)
        birth_button = create_button('birth_button','orange','생년월일',9,170,120)
        #birth_entry = create_entry('birth_entry',("맑은 고딕",12),35,250,120)
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