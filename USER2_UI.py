import pandas as pd
import USER3_UI
import USER_UI
import csv
from tkinter import *
from tkinter.simpledialog import *
from PIL import Image,ImageTk
from tkinter.filedialog import *
import tkinter.messagebox
import tkinter.ttk as ttk



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
        df_user = pd.read_csv('csv/user.csv', encoding='utf-8')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        
        def find_image_name():
            file_name=askopenfilename(parent=mainwindow,filetype=(("PNG파일", "*.png"),("모든 파일","*.*")))
            
            photo = Image.open(file_name)
            photo2 = photo.resize((120, 150))
            photo3 = ImageTk.PhotoImage(photo2,master=mainwindow)
            image_label.configure(image=photo3, width=120, height=150)
            image_label.image=photo3
            image_entry.delete(1.0,"end")
            image_entry.insert(1.0,file_name)
            image_entry['state'] = 'disabled'
            image_find['state'] = 'disabled'
        
        var = StringVar(mainwindow)

        def update_csv():
            df_user = pd.read_csv('csv/user.csv', encoding='utf-8')
            df_user = df_user.set_index(df_user['USER_PHONE'])
                                                                        # 등록되어있는 회원들의 정보를 불러와서 출력
            phone_number = phone_entry1.get() + '-' + phone_entry2.get() + '-' + phone_entry3.get()
            input_phone = phone_number
            input_name = name_entry.get()
            yy = yearcombo.get()
            mm = monthcombo.get()
            dd = daycombo.get() 
            input_birth = yy + mm + dd
            input_mail = mail_entry.get()
            input_image = image_entry.get('1.0','end')

            if phone_entry1.get().strip()=="" or input_name.strip()==""or input_birth.strip()=="" or input_mail.strip()=="" or input_image.strip()==""\
                or yy.strip()==""or mm.strip()==""or dd.strip()==""or var.get().strip()==""\
                or phone_entry1.get().strip()=="" or phone_entry2.get().strip()=="" or phone_entry3.get().strip()=="":
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

                df_user.to_csv('csv/user.csv', index=False, encoding='utf-8')   # 수정된 회원 정보 저장
                ok_notice()
                mainwindow.destroy()
                USER3_UI.exit_search()
                USER3_UI.USER_1()         
                
       
        def phonenum_check():
                
            def check_pass():   # 예외처리 4
                tkinter.messagebox.showinfo("정보","사용 가능한 전화번호입니다.")
            def check_nonpass():   # 예외처리 5
                tkinter.messagebox.showerror("ERROR","이미 등록된 전화번호입니다.")           
            def check_error1():   # 예외처리 5
                tkinter.messagebox.showerror("ERROR","전화번호를 잘못입력하셨습니다.")           

    

            df_user = pd.read_csv("csv/user.csv",encoding='utf-8')
            df_user = df_user.set_index(df_user['USER_PHONE'])
            n1 = phone_entry1.get()
            n2 = phone_entry2.get()
            n3 = phone_entry3.get()
            phone_number = phone_entry1.get() + '-' + phone_entry2.get() + '-' + phone_entry3.get()
            a = phone_number
            phone_number = df_user.index.tolist()
            
            if (len(n1) ==3 and len(n2) ==4 and len(n3) ==4):
                try:
                    int(n1)
                    int(n2)
                    int(n3)
                except:
                    check_error1()
                else:            
                    if ((0 <= int(n1) <=999) and (0 <= int(n2) <=9999) and (0 <= int(n3) <=9999)):
                        if  str(a) not in phone_number:
                            check_pass()
                            phone_check['state'] = 'disabled'
                            phone_entry1['state'] = 'disabled'
                            phone_entry2['state'] = 'disabled'
                            phone_entry3['state'] = 'disabled'
                            reg_button['state'] = 'normal'
                        else:
                            check_nonpass()
                    else:
                        check_error1()
            else:
                check_error1()

        sub_label = Label(mainwindow, text ="회원정보 수정",font=("맑은 고딕",9),bg='gray',height=3)
        image_label = Label(mainwindow, bg='orange', width=15, height=10)
        

        state_label = Label(mainwindow,bg='orange')
        if df_user.loc[phone,'USER_REG'] == True:
            state_label.config(text='등록 상태')
        elif df_user.loc[phone,'USER_REG'] == False:
            state_label.config(text='탈퇴 상태')
        mainwindow.configure(background = 'sky blue')
        
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

        df_user = pd.read_csv('csv/user.csv', encoding='utf-8')
        df_user = df_user.set_index(df_user['USER_PHONE'])
        USER_CHOICE = phone
        birth = str(df_user.loc[USER_CHOICE,'USER_BIRTH'])
        
        yearcombo = ttk.Combobox(mainwindow,width=6,height=5,values=year,state="readonly")
        monthcombo = ttk.Combobox(mainwindow,width=4,height=5,values=month,state="readonly")
        daycombo = ttk.Combobox(mainwindow,width=4,height=5,values=day,state="readonly")
        yearcombo.set(birth[0:4])
        monthcombo.set(birth[4:6])
        daycombo.set(birth[6:8])
        yearcombo.pack()
        monthcombo.pack()
        daycombo.pack()
        yearcombo.place(x=250,y=120)
        monthcombo.place(x=350,y=120)
        daycombo.place(x=450,y=120)

        

        # 위젯 배치
        sub_label.pack(fill=X)
        create_label(image_label,30,80)
        state_label.place(x=60,y=250)
        name_button = create_button('name_button','orange','이름',9,170,80)
        name_entry = create_entry('name_entry',df_user.loc[phone,'USER_NAME'],("맑은 고딕",12),35,250,80)
        birth_button = create_button('birth_button','orange','생년월일',9,170,120)
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
        phone_entry1 = create_entry('phone_entry1',phone[0:3],("맑은 고딕",12),10,250,200)
        phone_entry2 = create_entry('phone_entry2',phone[4:8],("맑은 고딕",12),10,360,200)
        phone_entry3 = create_entry('phone_entry3',phone[9:13],("맑은 고딕",12),10,470,200)
        phone_check = Button(mainwindow,text='중복확인',bg='gray',width=9,command=phonenum_check)
        phone_check.place(x=580,y=200)                      
        if df_user.loc[USER_CHOICE,"USER_RENT_CNT"] != 0:
            phone_entry1['state'] = 'disabled'
            phone_entry2['state'] = 'disabled'
            phone_entry3['state'] = 'disabled'
            phone_check['state'] = 'disabled'           

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
