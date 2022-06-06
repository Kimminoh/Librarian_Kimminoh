import pandas as pd
from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from PIL import Image,ImageTk


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
    
    '''
    def image_search():
        filename = askopenfilename(parent = mainwindow, filetypes =(("JPG 파일","*.jpg"),("GIF 파일","*.GIF"),("모든 파일","*.*")))
        
        
        photo1 = PhotoImage(file = filename)
        image_label.image=photo1
        image_label.configure(image=photo1)
        '''
    

    def inuser_csv():
        df_user = pd.read_csv('csv/USER1.csv', encoding='CP949')
        df_user = df_user.set_index(df_user['USER_PHONE'])

        new_user = { "USER_PHONE": phone_entry.get(),                     # -(하이픈) 포함
                    "USER_NAME": name_entry.get(),                         # 영문일 시 공백포함
                    "USER_BIRTH": birth_entry.get(),                       # YYYYMMDD 
                    "USER_SEX": bool(var),                                # TRUE : 남자, FALSE : 여자
                    "USER_MAIL": mail_entry.get(),
                    "USER_IMAGE": image_entry.get(),                     # 기본값 None(흰 배경)
                    "USER_REG": phone_entry.get(),                          # TRUE : 등록, FALSE : 탈퇴
                    "USER_RENT_CNT": 0 }                                 # +1, -1 하는 방식
        df_user = df_user.append(new_user, ignore_index=True)           # 데이터프레임을 추가하고 행 인덱스를 재배열
        df_user = df_user.set_index(df_user['USER_PHONE'])               # USER_PHONE을 인덱스로 사용

        df_user.to_csv('csv/USER1.csv', index=False, encoding='CP949')
    
    photo = PhotoImage()
    #photo = Image.open(filename)
   # resize_image = photo.resize((120, 200))
    #photo1 = ImageTk.PhotoImage(resize_image,master=mainwindow)
    sub_label = Label(mainwindow, text ="회원 등록",font=("맑은 고딕",9),bg='gray',height=3)
    image_label = Label(mainwindow,image=photo,width=120, height=200)
    #image_label.configure(photo1)
    #state_label = Label(mainwindow, text ="등록 상태",bg='gray')
    mainwindow.configure(background = 'sky blue')
    
    var = BooleanVar()
    
    # 위젯 배치
    sub_label.pack(fill=X)
    image_label.pack()
    image_label.place(x=30,y=80)
    #create_label(image_label,30,80)
    #state_label.place(x=60,y=250)
    name_button = create_button('name_button','orange','이름',9,170,80)
    name_entry = create_entry('name_entry',("맑은 고딕",12),35,250,80)
    birth_button = create_button('birth_button','orange','생년월일',9,170,120)
    birth_entry = create_entry('birth_entry',("맑은 고딕",12),35,250,120)
    sex_button = create_button('sex_button','orange','성별',9,170,160)
    male_rbutton = create_rbutton('male_rbutton',("맑은 고딕",10),'sky blue','남',var,True,250,160)
    female_rbutton = create_rbutton('male_rbutton',("맑은 고딕",10),'sky blue','여',var,False,300,160)
    phone_button = create_button('phone_button','orange','전화번호',9,170,200)
    phone_entry = create_entry('phone_entry',("맑은 고딕",12),35,250,200)
    phone_check = create_button('phone_check','gray','중복확인',9,580,200)                          # 중복확인 버튼 미구현
    mail_button = create_button('mail_button','orange','이메일 주소',9,170,240)
    mail_entry = create_entry('mail_entry',("맑은 고딕",12),35,250,240)
    image_find = Button(mainwindow,text='찾아보기',bg='gray',width=9) #,command=image_search
    image_find.place(x=580,y=280)
    image_button = create_button('image_button','orange','사진',9,170,280)
    image_entry = create_entry('image_entry',("맑은 고딕",12),35,250,280)
    reg_button = Button(mainwindow,text='등록',bg='gray',width=9,command=inuser_csv)
    reg_button.place(x=150,y=400)
    ok_button = create_button('mail_button','gray','확인',9,300,400)
    cancel_button = create_button('mail_button','gray','취소',9,450,400)



mainwindow = Tk()
user_reg()
mainwindow.title("회원 등록")
mainwindow.geometry("700x500")
mainwindow.resizable(width=FALSE, height=FALSE)
mainwindow.mainloop()
