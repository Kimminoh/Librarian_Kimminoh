from tkinter import*
import tkinter.messagebox
import pandas as pd
from tabulate import tabulate
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import *
from tkinter.simpledialog import *
from datetime import datetime, timedelta
import csv
import pandas as pd
from tkinter import *
from PIL import Image,ImageTk
import math


#from USER2_UI import USER_2
#from USER4_UI import USER_4
from USER_UI import USER_3
from USER3_UI import USER_1

# RENT_NUM 초기화 안되게 고정
rent_df = pd.read_csv("csv/rent.csv",encoding = "utf-8")
rent_df = rent_df.set_index(rent_df['RENT_NUM'])

try:
   num = max(rent_df.index.tolist()) + 1
   
except:
   num=1




# 2번째 화면
def BOOK_MANAGEMENT():
    #공통부분 ↓---------------------------------------------------------------------
    window = Tk()
    window.title("도서관리")
    window.geometry("700x500")
    label1 = Label(window, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)
    window.resizable(width=FALSE, height=FALSE)


    #공통부분 ↑---------------------------------------------------------------------
    # ㉮
    BTN_REG_EDIT = Button(window, text='도서\n등록/수정', bg='gray', width='18',
                          height='8', command = BOOK_MANAGEMENT_FIRST)
    # ㉯
    BTN_SEARCH_RENT = Button(window, text='도서\n조회/대출', bg='gray', width='18',
                          height='8', command = BOOK_LOOKUP)
    # ㉰
    BTN_DELETE = Button(window, text='도서삭제', bg='gray', width='18',
                          height='8', command = BOOK_DELETE)    

    # 뒤로가기 버튼 생성  
    BTN_CANCEL = Button(window, text='뒤로가기', bg='gray'
    , width='8', height='2',command=window.destroy)    

    # 위젯들 위치 설정
    label1.pack()
    BTN_REG_EDIT.pack()
    BTN_SEARCH_RENT.pack()
    BTN_DELETE.pack()
    BTN_CANCEL.pack()
    BTN_REG_EDIT.place(x=100,y=170)
    BTN_SEARCH_RENT.place(x=300,y=170)
    BTN_DELETE.place(x=500,y=170)
    BTN_CANCEL.place(x=5,y=25)


# ㉮의 화면
# 도서 등록/수정 화면
def BOOK_MANAGEMENT_FIRST():
    #공통부분 ↓-----------------------------------------------------------------------
    window = Tk()
    window.title("도서 등록/수정")
    window.geometry("700x500")
    window.resizable(width=FALSE, height=FALSE)
    label1 = Label(window, text = '도서 등록/수정', bg = 'gray',width = 700, height = 5)

    #공통부분 ↑-----------------------------------------------------------------------  

    # Treeview 목록 더블클릭 시 이벤트 발생
    def click_item(event):
        selected=BOOK_SELECT_BOX.focus()
        BOOK_EDIT(int(selected))  # 수정하기 창 실행
        
    # 도서 신규등록 버튼
    BTN_NEW_REG = Button(window, text='도서 신규 등록', bg='gray', width='15', height='2',
                         command = BOOK_NEW_REG)
    # 뒤로가기 버튼
    BTN_CANCEL = Button(window, text='뒤로가기', bg='gray',
     width='8', height='2',command=window.destroy)
    

    
    # 안내 레이블
    label2 = Label(window, text='수정할 도서 검색하기 :',fg='black' ,
                   font=('맑은 고딕',10), width=20,height=1)
    label3 = Label(window, text='도서명 혹은 저자로 검색해주세요 ↓',fg='black' ,
                   font=('맑은 고딕',10), width=30,height=1) 

    # 도서 검색창 생성
    # 엔트리값 가져오기 위해 변수 선언
    BOOK_SEARCH_LABEL = Entry(window)
    BOOK_SEARCH_LABEL.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)
#==========도서명과 저자로 검색하기 / 구현 완료 ====================================================
    def search():
        csv_pull1=pd.read_csv("csv/book.csv", encoding="utf-8")
        csv_pull1 = csv_pull1.set_index("BOOK_ISBN")
                
        for ISBN in csv_pull1.index.tolist():
            book_name = BOOK_SEARCH_LABEL.get()
            
            search1 = csv_pull1["BOOK_TITLE"].str.contains(book_name) # 제목 필터링
            search2 = csv_pull1["BOOK_AUTHOR"].str.contains(book_name) #저자 필터링
            # 제목 + 저자로 필터링
            csv_2_1 = csv_pull1.loc[search1 | search2,["BOOK_TITLE","BOOK_AUTHOR","BOOK_PUBLIC"]]

            # Treeview 기존 목록 삭제
            for item in BOOK_SELECT_BOX.get_children(): 
                BOOK_SELECT_BOX.delete(item)
                
            # 제목과 저자로 필터링한 목록 출력
            for ISBN in csv_2_1.index.tolist():
                book_title = csv_2_1.loc[ISBN, "BOOK_TITLE"]
                book_author = csv_2_1.loc[ISBN, "BOOK_AUTHOR"]
                book_publish = csv_2_1.loc[ISBN, "BOOK_PUBLIC"]
                
                book_add = (ISBN, book_title, book_author, book_publish)
                BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])



#====================================================================================================
    # 검색 버튼 
    BOOK_SEARCH_BTN = Button(window, text = '검색', fg='black' ,bg='gray', command = search) 
    BOOK_SEARCH_BTN.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)


    
    # 등록되어 있는 도서 리스트
    csv_pull = pd.read_csv("csv/book.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")

    # Treeview를 사용해서 도서 목록 나열
    
    BOOK_SELECT_BOX = ttk.Treeview(window, columns=(1,2,3,4), height = 13,show="headings")
    BOOK_SELECT_BTN = Button(window, text = '선택하기', fg='black', bg = 'gray')
    BOOK_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)
    BOOK_SELECT_BTN.bind('<Button-1>',click_item)
    

    # Treeview의 필드명
    BOOK_SELECT_BOX.heading(1, text='ISBN')
    BOOK_SELECT_BOX.heading(2, text='도서명')
    BOOK_SELECT_BOX.heading(3, text='저자')
    BOOK_SELECT_BOX.heading(4, text='출판사')
    # Treeview의 기본 너비 
    BOOK_SELECT_BOX.column(1, width='100')
    BOOK_SELECT_BOX.column(2, width='150')
    BOOK_SELECT_BOX.column(3, width='110')
    BOOK_SELECT_BOX.column(4, width='140')

    # 목록 출력할 데이터 
    # 데이터 프레임 출력 
    for ISBN in csv_pull.index.tolist():
        book_title = csv_pull.loc[ISBN, "BOOK_TITLE"]
        book_author = csv_pull.loc[ISBN, "BOOK_AUTHOR"]
        book_publish = csv_pull.loc[ISBN, "BOOK_PUBLIC"]
        
        book_add = (ISBN, book_title, book_author, book_publish)
        BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])

    # Treview 목록 더블클릭시 이벤트 발생
    BOOK_SELECT_BOX.bind('<Double-Button-1>', click_item)
    BOOK_SELECT_BOX.place(x=90, y=200)
    label1.pack()
    label2.place(x=15, y=155)
    label3.place(x=177, y=125)
    BTN_CANCEL.place(x=5,y=25)
    BTN_NEW_REG.place(x=5,y=90)


    #2022/06/18 새로고침 기능 구현 추가
    def refresh():
        # treeview 지우기
        for item in BOOK_SELECT_BOX.get_children():
            BOOK_SELECT_BOX.delete(item)
        # csv 파일 불러오기 
        csv_pull = pd.read_csv("csv/book.csv",encoding = "utf-8")
        csv_pull = csv_pull.set_index("BOOK_ISBN")

        for ISBN in csv_pull.index.tolist():
            book_title = csv_pull.loc[ISBN, "BOOK_TITLE"]
            book_author = csv_pull.loc[ISBN, "BOOK_AUTHOR"]
            book_publish = csv_pull.loc[ISBN, "BOOK_PUBLIC"]
            
            book_add = (ISBN, book_title, book_author, book_publish)
            BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])

    #새로고침 버튼 추가
    REFRESH_BTN = Button(window, text = '새로고침', fg='black' ,bg='gray', command = refresh) 
    REFRESH_BTN.place(relx=0.86,rely=0.5,relwidth=0.1,relheight = 0.07)
        






    
    

# ㉮-1 신규 도서 추가     
def BOOK_NEW_REG():
    #공통부분 ↓-----------------------------------------------------------------------
    window = Tk()
    window.title("도서 신규등록")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 신규 등록', bg = 'gray', width = 700, height = 3)
    window.resizable(width=FALSE, height=FALSE)
    #공통부분 ↑-----------------------------------------------------------------------  
    label1.pack() # 창 제목 레이블

    # 위젯 간편화 함수 1
    def BTN_EDIT(a, b, c, d,e, f,g):
        a = Button(window, text=b, bg=c, width=d, height=e)
        a.place(x=f, y = g)    
    # 위젯 간편화 함수 2    
    def BLANK(a,b,c,d,e):
        a = Entry(window)
        a.place(x= b, y= c,relwidth=d,relheight=e)

    # 중복확인시 이벤트 발생
    def ERROR_1():   # 예외처리 1
        tkinter.messagebox.showinfo("ERROR","해당 도서는 등록 가능 합니다 !")
    def ERROR_2():   # 예외처리 2
        tkinter.messagebox.showerror("ERROR","해당 도서는 등록 불가능 합니다 !")
    def ERROR_3():   # 예외처리 3
        tkinter.messagebox.showerror("ERROR","중복 확인 후 도서 등록이 가능합니다 !")
    def ERROR_4():   # 예외처리 4
        tkinter.messagebox.showerror("ERROR","가격은 정수로만 입력 가능합니다 !")
    def ERROR_5():   # 예외처리 5
        tkinter.messagebox.showerror("ERROR","해당 정보는 숫자로만 입력이 가능합니다 !")
    def ERROR_6():   # 예외처리 6
        tkinter.messagebox.showerror("ERROR","해당 정보는 필수정보 입니다. 다시 작성해주세요 !")

    def REG():  # 확인 버튼 눌렀을 시
        MSB = tkinter.messagebox.askquestion ('신규 도서 등록','도서를 등록 하시겠습니까?')
        if MSB == 'yes':        # 메세지 박스 yes 클릭 시
            a = SEARCH_BOOK_ISBN.get()    # 각 엔트리 박스에 해당하는 정보 가져오기
            b = SEARCH_BOOK_TITLE.get()
            c = SEARCH_BOOK_AUTHOR.get()
            d = SEARCH_BOOK_PUBLIC.get()
            e = SEARCH_BOOK_PRICE.get()
            f = SEARCH_BOOK_LINK.get()
            g = SEARCH_IMAGE_FIND.get()
            h = SEARCH_BOOK_DESCRIPTION.get()
            
            #하나라도 입력하지 않았을 때
            if a.strip()=="" or b.strip()=="" or c.strip()=="" or d.strip()=="" or e.strip()=="" \
               or f.strip()=="" or g.strip()=="" or h.strip()=="":
                ERROR_6()
                return 0

            # 중복확인 안했을 때 
            elif not OVERLAP_CHECK['state'] == 'disabled' :
                ERROR_3()

            # 가격이 정수가 아닐 때
            elif not e.isdigit():
                ERROR_4()
                
            else: # 값 다 입력했을 때 
                csv_pull = pd.read_csv("csv/book.csv",encoding = "utf-8")
                csv_pull = csv_pull.set_index("BOOK_ISBN")
                csv_pull.loc[a, 'BOOK_TITLE']= b
                csv_pull.loc[a, 'BOOK_AUTHOR']= c  
                csv_pull.loc[a, 'BOOK_PUBLIC']= d 
                csv_pull.loc[a, 'BOOK_PRICE']= int(e)
                csv_pull.loc[a, 'BOOK_LINK']= f
                csv_pull.loc[a, 'BOOK_IMAGE']= g
                csv_pull.loc[a, 'BOOK_DESCRIPTION']= h
                csv_pull.loc[a, 'BOOK_RENTAL']= "False"
                #csv 저장하기 
                csv_pull.to_csv("csv/book.csv", index = True)
                tkinter.messagebox.showinfo("SUCCES","도서 등록이 완료 되었습니다 !!")
                # 확인용 tabulate
                window.destroy()

    # 중복확인 함수       
    def ISBN_OVERLAP():
        csv_pull = pd.read_csv("csv/book.csv",encoding = "utf-8")
        csv_pull = csv_pull.set_index("BOOK_ISBN")
        
        a = SEARCH_BOOK_ISBN.get()  # ISBN의 정보 가져오기
        ISBN_OVERLAP = csv_pull.index.tolist()  # 인덱스를 리스트로 추출
        if  int(a) in ISBN_OVERLAP: # 중복일 시
            ERROR_2()
            
        elif not a.isdigit(): # 정수가 아닐 시
            ERROR_5()
                
        else :
            ERROR_1()
            # 중복 확인 완료시 버튼 비활성화 
            OVERLAP_CHECK['state'] = 'disabled'
            SEARCH_BOOK_ISBN['state'] = 'disabled'
            
    # 사진 가져오기
    photo=PhotoImage(master=window)
    IMAGE_label = Label(window,image=photo,text="사진\n미리보기",bg="white",width='120',height='150')
    IMAGE_label.place(x=30,y=80)


    # 위젯 
    BTN_BOOK_ISBN = Button(window, text='ISBN', bg='gray', width='8', height='1')
    BTN_BOOK_ISBN.place(x=170, y = 80)
    SEARCH_BOOK_ISBN = Entry(window)
    SEARCH_BOOK_ISBN.place(x= 250, y= 80,relwidth=0.5,relheight=0.05)

    # 중복확인시 이벤트 추가함
    OVERLAP_CHECK = Button(window, text='중복확인', bg='gray', width='7', height='1',
                           command = ISBN_OVERLAP)
    OVERLAP_CHECK.place(x=620, y = 80)    
    # 위젯
    BTN_BOOK_TITLE = Button(window, text='도서명', bg='gray', width='8', height='1') 
    BTN_BOOK_TITLE.place(x=170, y = 120)
    SEARCH_BOOK_TITLE = Entry(window)
    SEARCH_BOOK_TITLE.place(x= 250, y= 120,relwidth=0.5,relheight=0.05)
    # 위젯
    BTN_BOOK_AUTHOR = Button(window, text='저자', bg='gray', width='8', height='1')
    BTN_BOOK_AUTHOR.place(x=170, y = 160)
    SEARCH_BOOK_AUTHOR = Entry(window)
    SEARCH_BOOK_AUTHOR.place(x= 250, y= 160,relwidth=0.5,relheight=0.05)
    # 위젯
    BTN_BOOK_PUBLIC = Button(window, text='출판사', bg='gray', width='8', height='1')
    BTN_BOOK_PUBLIC.place(x=170, y = 200)
    SEARCH_BOOK_PUBLIC = Entry(window)
    SEARCH_BOOK_PUBLIC.place(x= 250, y= 200,relwidth=0.5,relheight=0.05)
    # 위젯
    BTN_BOOK_PRICE = Button(window, text='가격', bg='gray', width='8', height='1')
    BTN_BOOK_PRICE.place(x=170, y = 240)
    SEARCH_BOOK_PRICE = Entry(window)
    SEARCH_BOOK_PRICE.place(x= 250, y= 240,relwidth=0.5,relheight=0.05)
    # 위젯
    BTN_BOOK_LINK = Button(window, text='URL', bg='gray', width='8', height='1') 
    BTN_BOOK_LINK.place(x=170, y = 280)
    SEARCH_BOOK_LINK = Entry(window)
    SEARCH_BOOK_LINK.place(x= 250, y= 280,relwidth=0.5,relheight=0.05)
    # 위젯    
    BTN_BOOK_DESCRIPTION = Button(window, text='도서 설명', bg='gray', width='8', height='1')
    BTN_BOOK_DESCRIPTION.place(x=170, y = 320)
    SEARCH_BOOK_DESCRIPTION = Entry(window)
    SEARCH_BOOK_DESCRIPTION.place(x= 250, y= 320,relwidth=0.5,relheight=0.05)
    # 위젯
    BTN_IMAGE_FIND = Button(window, text='사진 찾기', bg='gray', width='8', height='1')
    BTN_IMAGE_FIND.place(x=170, y = 360)
    SEARCH_IMAGE_FIND = Entry(window)
    SEARCH_IMAGE_FIND.place(x= 250, y= 360,relwidth=0.5,relheight=0.05)

    # 안내창
    explain = Label(window, text = '※사진은 필수 정보 입니다. 반드시 입력해 주세요 !!',
                width = '45', height = 1)
    explain.place(relx=0.34, rely=0.78)
    explain.configure(font=("Courier", 8, "italic"))

    


    # 사진 찾는 함수 
    def find_image_name():
        file_name=askopenfilename(parent=window,filetype=(("PNG파일", "*.png"),("모든 파일","*.*")))

        photo1=Image.open(file_name)
        photo2=photo1.resize((120,150))
        photo3=ImageTk.PhotoImage(photo2,master=window)
        IMAGE_label.configure(image=photo3,width=120,height=150)
        IMAGE_label.image=photo3

        SEARCH_IMAGE_FIND.delete(0,"end")
        SEARCH_IMAGE_FIND.insert(0,file_name)
        SEARCH_IMAGE_FIND['state'] = 'disabled'
        BTN_FIND['state'] = 'disabled'
        
    # 위젯
    BTN_FIND=Button(window, text="찾아보기",bg='gray',width='8',height='1',command=find_image_name)
    BTN_FIND.place(x=620,y=360)
    BTN_OK = Button(window, text='확인', bg='gray',width='7', height='1', command = REG)
    BTN_OK.place(x=300, y = 420)
    BTN_CANCEL = Button(window, text='취소', bg='gray', width='7', height='1',
                        command=window.destroy )
    BTN_CANCEL.place(x=400, y = 420)


# ㉮-2번째 창 / 도서 수정하기
# 도서 목록중 하나 선택해서 도서 수정하기 
def BOOK_EDIT(selected):
    #공통부분 ↓-----------------------------------------------------------------------
    window = Tk()
    window.title("도서 수정하기")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 수정하기', bg = 'gray', width = 700, height = 3)
    #공통부분 ↑-----------------------------------------------------------------------
    label1.pack() # 창 제목 레이블
    # 함수안의 함수 => 버튼 형식 생성
    def BTN_EDIT(a, b, c, d,e, f,g):
        a = Button(window, text=b, bg=c, width=d, height=e)
        a.place(x=f, y = g)    

    def BLANK(a,b,c,d,e):
        a = Entry(window)
        a.place(x= b, y= c,relwidth=d,relheight=e)

    # 예외처리 이벤트
    def ERROR_7():     # 예외처리 7 #수정 불가인데 에러메세지?
        tkinter.messagebox.showeinfo("SUCCESS","해당 ISBN으로 수정이 가능합니다 !")
    def ERROR_8():     # 예외처리 8
        tkinter.messagebox.showerror("ERROR","해당 ISBN으로는 수정하실 수 없습니다 !")
    def ERROR_9():     # 예외처리 9
        tkinter.messagebox.showerror("ERROR","변경사항을 적용 하여야지 등록/수정이 가능합니다 !")
    def ERROR_10():     # 예외처리 10
        tkinter.messagebox.showerror("ERROR","해당 부분은 숫자로만 입력이 가능합니다 !")
        
    # csv파일 불러오기    
    csv_pull = pd.read_csv("csv/book.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")

    # csv파일에서 정보 가져오기

    #사진 가져오기 + 크기 정렬
    IMAGE_label=Label(window,bg="white",width=120,height=150)
    photo = Image.open(csv_pull.loc[selected]["BOOK_IMAGE"])
    photo2 = photo.resize((120, 200))
    photo3 = ImageTk.PhotoImage(photo2,master=window)
    IMAGE_label.configure(image=photo3, width=120, height=150)
    IMAGE_label.image=photo3
    IMAGE_label.place(x=30,y=80)
        
    # 위젯
    BTN_BOOK_ISBN = Button(window, text='ISBN', bg='gray', width='8', height='1')
    BTN_BOOK_ISBN.place(x=170, y = 80)
    SEARCH_BOOK_ISBN = Entry(window)
    SEARCH_BOOK_ISBN.place(x= 250, y= 80,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_ISBN.insert(0,selected)       # ISBN 값 출력              
    # 위젯
    BTN_BOOK_TITLE = Button(window, text='도서명', bg='gray', width='8', height='1')
    BTN_BOOK_TITLE.place(x=170, y = 120)
    SEARCH_BOOK_TITLE = Entry(window)
    SEARCH_BOOK_TITLE.place(x= 250, y= 120,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_TITLE.insert(0,csv_pull.loc[selected]["BOOK_TITLE"])    # 도서명 가져와서 출력
    # 위젯
    BTN_BOOK_AUTHOR = Button(window, text='저자', bg='gray', width='8', height='1')
    BTN_BOOK_AUTHOR.place(x=170, y = 160)
    SEARCH_BOOK_AUTHOR = Entry(window)
    SEARCH_BOOK_AUTHOR.place(x= 250, y= 160,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_AUTHOR.insert(0,csv_pull.loc[selected]["BOOK_AUTHOR"]) # 저자 가저와서 출력
    # 위젯
    BTN_BOOK_PUBLIC = Button(window, text='출판사', bg='gray', width='8', height='1')
    BTN_BOOK_PUBLIC.place(x=170, y = 200)
    SEARCH_BOOK_PUBLIC = Entry(window)
    SEARCH_BOOK_PUBLIC.place(x= 250, y= 200,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_PUBLIC.insert(0,csv_pull.loc[selected]["BOOK_PUBLIC"]) # 출판사 가져와서 출력
    # 위젯
    BTN_BOOK_PRICE = Button(window, text='가격', bg='gray', width='8', height='1')
    BTN_BOOK_PRICE.place(x=170, y = 240)
    SEARCH_BOOK_PRICE = Entry(window)
    SEARCH_BOOK_PRICE.place(x= 250, y= 240,relwidth=0.5,relheight=0.05)
    price = float(csv_pull.loc[selected]["BOOK_PRICE"])
    SEARCH_BOOK_PRICE.insert(0,int(price)) # 가격 가져와서 출력
    # 위젯
    BTN_BOOK_LINK = Button(window, text='URL', bg='gray', width='8', height='1') 
    BTN_BOOK_LINK.place(x=170, y = 280)
    SEARCH_BOOK_LINK = Entry(window)
    SEARCH_BOOK_LINK.place(x= 250, y= 280,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_LINK.insert(0,csv_pull.loc[selected]["BOOK_LINK"]) # 링크 가져와서 출력
    # 위젯
    BTN_BOOK_DESCRIPTION = Button(window, text='도서 설명', bg='gray', width='8', height='1')
    BTN_BOOK_DESCRIPTION.place(x=170, y = 320)
    SEARCH_BOOK_DESCRIPTION = Entry(window)
    SEARCH_BOOK_DESCRIPTION.place(x= 250, y= 320,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_DESCRIPTION.insert(0,csv_pull.loc[selected]["BOOK_DESCRIPTION"]) # 설명 가져와서 출력
    # 위젯
    BTN_IMAGE_FIND = Button(window, text='사진', bg='gray', width='8', height='1')
    BTN_IMAGE_FIND.place(x=170, y = 360)
    #SEARCH_IMAGE_FIND = Entry(window)
    #SEARCH_IMAGE_FIND.place(x= 250, y= 360,relwidth=0.5,relheight=0.05)

    SEARCH_IMAGE_FIND = Text(window, font=("맑은 고딕",12),width=40,height=2)
    SEARCH_IMAGE_FIND.insert('1.0',csv_pull.loc[selected,'BOOK_IMAGE'])
    SEARCH_IMAGE_FIND.place(x=250,y=360)
    SEARCH_IMAGE_FIND.get('1.0','end').replace('\n','')

    SEARCH_IMAGE_FIND.configure(state='disable')
    # 안내창
    explain = Label(window, text = '※사진은 필수 정보 입니다. 반드시 입력해 주세요 !!',
                width = '45', height = 1)
    explain.place(relx=0.34, rely=0.82)
    explain.configure(font=("Courier", 8, "italic"))


    
    
    # 사진 찾아오기 
    def find_image_name():
        file_name=askopenfilename(parent=window,filetype=(("PNG파일", "*.png"),("모든 파일","*.*")))
        SEARCH_IMAGE_FIND.configure(state='normal')
        photo=Image.open(file_name)
        photo2=photo.resize((120,150))
        photo3=ImageTk.PhotoImage(photo2,master=window)
        IMAGE_label.configure(image=photo3,width=120,height=150)
        IMAGE_label.image=photo3
        SEARCH_IMAGE_FIND.delete('1.0',"end")
        SEARCH_IMAGE_FIND.insert('1.0',file_name)
        SEARCH_IMAGE_FIND['state'] = 'disabled'
        BTN_FIND['state'] = 'disabled'
        
    # 위젯
    BTN_FIND=Button(window, text="찾아보기",bg='gray',width='8',height='1',command=find_image_name)
    BTN_FIND.place(x=620,y=360)

    #중복확인 시, 예외처리
    def ERROR_1():   # 예외처리 1
        tkinter.messagebox.showinfo("ERROR","해당 도서는 등록 가능 합니다 !")
    def ERROR_2():   # 예외처리 2
        tkinter.messagebox.showerror("ERROR","해당 도서는 등록 불가능 합니다 !")
    def ERROR_3():   # 예외처리 3
        tkinter.messagebox.showerror("ERROR","중복 확인 후 도서 등록이 가능합니다 !")
    def ERROR_4():   # 예외처리 4
        tkinter.messagebox.showerror("ERROR","가격은 정수로만 입력 가능합니다 !")
    def ERROR_5():   # 예외처리 5
        tkinter.messagebox.showerror("ERROR","해당 정보는 숫자로만 입력이 가능합니다 !")
    def ERROR_6():   # 예외처리 6
        tkinter.messagebox.showerror("ERROR","해당 정보는 필수정보 입니다. 다시 작성해주세요 !")
    
    def APPLY():  # 확인,적용  버튼 눌렀을 시
        MSB = tkinter.messagebox.askquestion ('도서 수정','도서를 수정 하시겠습니까?')
        if MSB == 'yes':
            a = SEARCH_BOOK_ISBN.get()
            b = SEARCH_BOOK_TITLE.get()
            c = SEARCH_BOOK_AUTHOR.get()
            d = SEARCH_BOOK_PUBLIC.get()
            e = SEARCH_BOOK_PRICE.get()
            f = SEARCH_BOOK_LINK.get()
            g = SEARCH_IMAGE_FIND.get('1.0','end').replace('\n','')
            h = SEARCH_BOOK_DESCRIPTION.get()

            #하나라도 입력하지 않았을 때
            if a.strip()=="" or b.strip()=="" or c.strip()=="" or d.strip()=="" or e.strip()=="" \
               or f.strip()=="" or g.strip()=="" or h.strip()=="":
                ERROR_6()
                return 0

            # 중복확인 안했을 때 
            elif not OVERLAP_CHECK['state'] == 'disabled' :
                ERROR_3()

            # 가격이 정수가 아닐 때
            elif not e.isdigit():
                ERROR_4()
                
            else:
                csv_pull = pd.read_csv("csv/book.csv",encoding = "utf-8")
                csv_pull = csv_pull.set_index("BOOK_ISBN")
                csv_pull.loc[selected, 'BOOK_TITLE']= b
                csv_pull.loc[selected, 'BOOK_AUTHOR']= c  
                csv_pull.loc[selected, 'BOOK_PUBLIC']= d 
                csv_pull.loc[selected, 'BOOK_PRICE']= int(e)
                csv_pull.loc[selected, 'BOOK_LINK']= f
                csv_pull.loc[selected, 'BOOK_IMAGE']= g
                csv_pull.loc[selected, 'BOOK_DESCRIPTION']= h
                
                # ISBN 값 수정하는 코드 추가
                csv_pull = csv_pull.reset_index()
                csv_pull.loc[0, 'BOOK_ISBN']= a
                csv_pull = csv_pull.set_index("BOOK_ISBN")
                
                #csv 저장하기   
                csv_pull.to_csv("csv/book.csv", index = True)
                tkinter.messagebox.showinfo("수정 성공","수정이 완료 되었습니다!")
                print(tabulate(csv_pull, headers='keys', tablefmt='psql',numalign='left',stralign='left'))
                window.destroy()

    # 중복확인 함수
    def ISBN_OVERLAP():
        csv_pull = pd.read_csv("csv/book.csv",encoding = "utf-8")
        csv_pull = csv_pull.set_index("BOOK_ISBN")
        
        a = SEARCH_BOOK_ISBN.get()
        # 인덱스 값 리스트로 추출
        ISBN_OVERLAP = csv_pull.index.tolist()
        if  int(a) in ISBN_OVERLAP and  int(a) != selected :
            ERROR_2()
                         
        elif not a.isdigit():  # 정수가 아닐 시 에러
            ERROR_5()
                
        else :
            ERROR_1()
            # 중복 확인 완료시 버튼 비활성화 
            OVERLAP_CHECK['state'] = 'disabled'
            SEARCH_BOOK_ISBN['state'] = 'disabled'

    # 중복확인시 이벤트 발생 추가
    OVERLAP_CHECK = Button(window, text='중복확인', bg='gray', width='7', height='1',
                           command = ISBN_OVERLAP)
    OVERLAP_CHECK.place(x=620, y = 80)

    # 적용 버튼 누를 시 수정!
    BTN_APPLY = Button(window, text='적용', bg = 'gray', width='7', height='1',command=APPLY)
    BTN_APPLY.place(x=300, y = 450)
   
    BTN_CANCEL = Button(window, text='취소', bg='gray', width='7', height='1',command=window.destroy )
    BTN_CANCEL.place(x=400, y = 450)
    



# ㉯의 화면----------------------------------------------------
def BOOK_LOOKUP():
    window = Tk()
    window.title('도서 조회/대출')
    window.geometry("700x500")
    label1 = Label(window, text = '도서 조회/대출', bg ='gray', width = 700, height = 5)


    label1.pack()
    # 위젯 간편화 함수
    def BTN_EDIT(a, b, c, d,e, f,g):
        a = Button(window, text=b, bg=c, width=d, height=e)
        a.place(x=f, y = g)    

    def BLANK(a,b,c,d,e) :
        a = Entry(window)
        a.place(x= b, y= c,relwidth=d,relheight=e)
    # 위젯
    BTN_CANCEL = Button(window, text='뒤로가기', bg='gray',
     width='8', height='2',command=window.destroy)
    BTN_CANCEL.place(x=5,y=25)

    BLANK_SEARCH = Entry(window)
    BLANK_SEARCH.place(relx=0.11,rely=0.2,relwidth=0.7,relheight=0.05)

    # csv 파일 가져오기
    csv_pull = pd.read_csv("csv/book.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")

    csv_pull_rent = pd.read_csv("csv/rent.csv",encoding = "utf-8")

    csv_pull1 = pd.read_csv("csv/book.csv",encoding = "utf-8")
    csv_pull1 = csv_pull1.set_index("BOOK_ISBN")
    # 도서를 조회하기 위해 검색 시 도서명과 저자로 검색 가능
    def search1 ():
                
        for ISBN in csv_pull1.index.tolist():
            book_name = BLANK_SEARCH.get()
            
            search1 = csv_pull1["BOOK_TITLE"].str.contains(book_name) # 제목 필터링
            search2 = csv_pull1["BOOK_AUTHOR"].str.contains(book_name) #저자 필터링
            # 제목 + 저자로 필터링
            csv_2 = csv_pull1.loc[search1 | search2,["BOOK_TITLE","BOOK_AUTHOR","BOOK_PUBLIC"]]

            # Treeview 기존 목록 삭제
            for item in BOOK_SELECT_BOX.get_children(): 
                BOOK_SELECT_BOX.delete(item)
                
            # 제목과 저자로 필터링한 목록 출력
            for ISBN in csv_2.index.tolist():
                book_title = csv_2.loc[ISBN, "BOOK_TITLE"]
                book_author = csv_2.loc[ISBN, "BOOK_AUTHOR"]
                book_publish = csv_2.loc[ISBN, "BOOK_PUBLIC"]
                
                book_add = (ISBN, book_title, book_author, book_publish)
                BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])
                
    BTN_SEARCH = Button(window, text='도서 검색', bg='gray',command=search1)         
    BTN_SEARCH.place(relx=0.001,rely=0.2,relwidth = 0.1,relheight=0.05)

# Treeview---------------------------------------------------------------------
    # 도서 목록 창 (Treeview)
    BOOK_SELECT_BOX = ttk.Treeview(window, columns=(1,2,3,4), height = 6,show="headings")

    # 필드명
    BOOK_SELECT_BOX.heading(1, text='ISBN')
    BOOK_SELECT_BOX.heading(2, text='도서명')
    BOOK_SELECT_BOX.heading(3, text='저자')
    BOOK_SELECT_BOX.heading(4, text='출판사')
    # 기본 너비 
    BOOK_SELECT_BOX.column(1, width='170')
    BOOK_SELECT_BOX.column(2, width='130')
    BOOK_SELECT_BOX.column(3, width='120')
    BOOK_SELECT_BOX.column(4, width='80')


    # 목록 출력할 데이터 
    # 데이터 프레임 출력
    for ISBN in csv_pull.index.tolist():
        book_title = csv_pull.loc[ISBN, "BOOK_TITLE"]
        book_author = csv_pull.loc[ISBN, "BOOK_AUTHOR"]
        book_publish = csv_pull.loc[ISBN, "BOOK_PUBLIC"]
        
        book_add = (ISBN, book_title, book_author, book_publish)
        BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])

    def click_item(event):
        selected=BOOK_SELECT_BOX.focus()
        book_information()


    # 더블 클릭시 이벤트 발생 
    BOOK_SELECT_BOX.bind('<Double-Button-1>', click_item)

    BOOK_SELECT_BOX.place(relx=0.01,rely=0.28,relwidth=0.8,relheight = 0.4)

    
#=============================반납, 대출 버튼 이벤트 =======================================
# 도서 상세 정보
    def book_information():

        select_book = int(BOOK_SELECT_BOX.focus())
        #select_book_ISBN = BOOK_SELECT_BOX.item(select_book).get('values')
        
        window = Tk()
        window.title("도서 상세정보")
        window.geometry("700x500")
        label1 = Label(window, text = '도서 상세정보', bg = 'gray', width = 700, height = 3)
    
        label1.pack()

        IMAGE_label=Label(window,bg="white",width=120,height=150)
        photo = Image.open(csv_pull.loc[select_book]["BOOK_IMAGE"])
        photo2 = photo.resize((120, 200))
        window.resizable(width=FALSE, height=FALSE)
        photo3 = ImageTk.PhotoImage(photo2,master=window)
        IMAGE_label.configure(image=photo3, width=120, height=150)
        IMAGE_label.image=photo3
        IMAGE_label.place(x=30,y=80)


        
        BTN_BOOK_ISBN = Button(window, text='ISBN', bg='gray', width='8', height='1')
        BTN_BOOK_ISBN.place(x=180, y = 80)
        SEARCH_BOOK_ISBN = Entry(window)
        SEARCH_BOOK_ISBN.place(x= 260, y= 80,relwidth=0.5,relheight=0.05)
        SEARCH_BOOK_ISBN.insert(0,select_book)

        BTN_BOOK_TITLE = Button(window, text='도서명', bg='gray', width='8', height='1')
        BTN_BOOK_TITLE.place(x=180, y = 120)
        SEARCH_BOOK_TITLE = Entry(window)
        SEARCH_BOOK_TITLE.place(x= 260, y= 120,relwidth=0.5,relheight=0.05)
        SEARCH_BOOK_TITLE.insert(0,csv_pull.loc[select_book]["BOOK_TITLE"])
        
        
        BTN_BOOK_AUTHOR = Button(window, text='저자', bg='gray', width='8', height='1')
        BTN_BOOK_AUTHOR.place(x=180, y = 160)
        SEARCH_BOOK_AUTHOR = Entry(window)
        SEARCH_BOOK_AUTHOR.place(x= 260, y= 160,relwidth=0.5,relheight=0.05)
        SEARCH_BOOK_AUTHOR.insert(0,csv_pull.loc[select_book]["BOOK_AUTHOR"])
        BTN_BOOK_PUBLIC = Button(window, text='출판사', bg='gray', width='8', height='1')
        BTN_BOOK_PUBLIC.place(x=180, y = 200)
        SEARCH_BOOK_PUBLIC = Entry(window)
        SEARCH_BOOK_PUBLIC.place(x= 260, y= 200,relwidth=0.5,relheight=0.05)
        SEARCH_BOOK_PUBLIC.insert(0,csv_pull.loc[select_book]["BOOK_PUBLIC"])
        BTN_BOOK_PRICE = Button(window, text='가격', bg='gray', width='8', height='1')
        BTN_BOOK_PRICE.place(x=180, y = 240)
        SEARCH_BOOK_PRICE = Entry(window)
        SEARCH_BOOK_PRICE.place(x= 260, y= 240,relwidth=0.5,relheight=0.05)
        price=float(csv_pull.loc[select_book]["BOOK_PRICE"])
        SEARCH_BOOK_PRICE.insert(0,int(price))
        BTN_BOOK_LINK = Button(window, text='URL', bg='gray', width='8', height='1') 
        BTN_BOOK_LINK.place(x=180, y = 280)
        SEARCH_BOOK_LINK = Entry(window)
        SEARCH_BOOK_LINK.place(x= 260, y= 280,relwidth=0.5,relheight=0.05)
        SEARCH_BOOK_LINK.insert(0,csv_pull.loc[select_book]["BOOK_LINK"])
        
        BTN_BOOK_DESCRIPTION = Button(window, text='도서 설명', bg='gray', width='8', height='1')
        BTN_BOOK_DESCRIPTION.place(x=180, y = 320)
        SEARCH_BOOK_DESCRIPTION = Entry(window)
        SEARCH_BOOK_DESCRIPTION.place(x= 260, y= 320,relwidth=0.5,relheight=0.05)
        SEARCH_BOOK_DESCRIPTION.insert(0,csv_pull.loc[select_book]["BOOK_DESCRIPTION"])
        BTN_IMAGE_FIND = Button(window, text='사진', bg='gray', width='8', height='1')
        BTN_IMAGE_FIND.place(x=180, y = 360)

        SEARCH_IMAGE_FIND = Text(window, font=("맑은 고딕",12),width=40,height=2)
        SEARCH_IMAGE_FIND.insert('1.0',csv_pull.loc[select_book,'BOOK_IMAGE'])
        SEARCH_IMAGE_FIND.place(x=260,y=360)
        SEARCH_IMAGE_FIND.get('1.0','end').replace('\n','')
        
        # rent.csv파일에서 ISBN 기준으로 테이터 추출
        # 대여날짜 불러오기 위해서
        RENT_ISBN_PULL = csv_pull_rent[csv_pull_rent['BOOK_ISBN'] == int(select_book)]
        RENT_ISBN_PULL = RENT_ISBN_PULL.set_index("BOOK_ISBN")
        
        
        if RENT_ISBN_PULL.empty == False :
            DATE_PULL = RENT_ISBN_PULL.loc[int(select_book)]["RENT_DATE"]
            RDATE_PULL = RENT_ISBN_PULL.loc[int(select_book)]["RENT_RDATE"]
            RENTAL_CHECK = csv_pull.loc[int(select_book)]["BOOK_RENTAL"]
            RENTAL_USER = RENT_ISBN_PULL.loc[int(select_book)]["USER_PHONE"]
            
            
            if RENTAL_CHECK == True:
                IFM_PULL = ('대여일 :\n{}\n\n반납예정일 :\n{}\n\n대여자 전화번호 :\n{}'.format(DATE_PULL,RDATE_PULL,RENTAL_USER))
                IFM_PULL2 = ('대출 불가')
                font_color = 'red'
            else:
                IFM_PULL = ('대출 가능')
                IFM_PULL2 = ('대출 가능')
                font_color = 'blue'
        else :
            IFM_PULL = ('')
            IFM_PULL2 = ('대출 가능')
            font_color = 'blue'

        

        # 대출, 여부 확인    
        RENT_NOTICE = Label(window, text = IFM_PULL2, width = '12',
                            justify=LEFT,height = 2)
        RENT_NOTICE.place(relx=0.05, rely=0.5)
        RENT_NOTICE.configure(font=("강조", 10), fg=font_color)
        # 대여일, 반납일 확
        RENT_IFM = Label(window, text = IFM_PULL,width = '20', justify=LEFT,height = 8)
        RENT_IFM.place(relx=0.02, rely=0.65)
        RENT_IFM.configure(font=("Impact", 10))
        

        BTN_CANCEL = Button(window, text='확인', bg='gray', width='7', height='1',command=window.destroy )
        BTN_CANCEL.place(relx=0.5, rely = 0.9)

    def bookrent_selectuser():
        
      select_book = int(BOOK_SELECT_BOX.focus())
      
      rent_df = pd.read_csv("csv/rent.csv",encoding = "utf-8")
      
      a = rent_df['BOOK_ISBN'].tolist() 
      
      if select_book not in a:
        rent1 = Tk()
        rent1.title("도서 대출하기")
        rent1.geometry("700x500")
        
        def click_item(event):
            window = Tk()
        
        df_user = pd.read_csv('csv/user.csv', encoding="utf-8")
        df_user = df_user.set_index(df_user['USER_PHONE'])
        USER_SELECT_BOX = ttk.Treeview(rent1, columns=(1,2,3,4),show="headings")

         # 필드명
        USER_SELECT_BOX.heading(1, text='전화번호')
        USER_SELECT_BOX.heading(2, text='이름')
        USER_SELECT_BOX.heading(3, text='생년월일')
        USER_SELECT_BOX.heading(4, text='성별')
        # 기본 너비 
        USER_SELECT_BOX.column(1, width='130')
        USER_SELECT_BOX.column(2, width='130')
        USER_SELECT_BOX.column(3, width='120')
        USER_SELECT_BOX.column(4, width='80')
        for phone in df_user.index.tolist():
            user_name = df_user.loc[phone, "USER_NAME"]
            user_birth = df_user.loc[phone, "USER_BIRTH"]
            user_sex = df_user.loc[phone, "USER_SEX"]
            
            
            user_add = (phone,user_name,user_birth, user_sex)
            USER_SELECT_BOX.insert("","end",text="",value=user_add,iid=phone)

                   
            #result_info = (user_name, phone, user_birth, user_sex)
            #USER_SELECT_BOX.insert('','end',values=result_info,iid=phone)
           
        
        
        
        def event_book_rent():
            global num
            rent_df = pd.read_csv("csv/rent.csv",encoding = "utf-8")
            rent_df = rent_df.set_index(rent_df['RENT_NUM'])
            #number = rent_df['RENT_NUM'].tolist() 
            
            number = rent_df['RENT_NUM'].tolist()
            if num in number:
                num = max(rent_df.index.tolist()) + 1
            
            for i in range(1,len(rent_df)+1):
                  if i not in number and num > i:
                     num = i
            if len(rent_df) == 0:
                num = 1
            book_df = pd.read_csv("csv/book.csv",encoding = "utf-8")
            book_df = book_df.set_index(book_df['BOOK_ISBN'])

            user_df = pd.read_csv("csv/user.csv",encoding = "utf-8")
            user_df = user_df.set_index(user_df['USER_PHONE'])

            
            

            today_D = datetime.now().date() # datetime 모듈이용하여 현재 날짜 저장
            return_D = today_D+timedelta(weeks=2) # timedelta 함수 이용 2주뒤 날짜 저장
            select_user = USER_SELECT_BOX.focus()
            
            new_rent = { "RENT_NUM": num,
                     "RENT_DATE": today_D,
                     "RENT_RDATE": return_D,
                     "RENT_RYN": False,
                     "BOOK_ISBN": select_book,
                     "USER_PHONE": select_user} 
            
            
            book_df.loc[select_book,'BOOK_RENTAL']="True"
            rent_df = rent_df.set_index(rent_df['BOOK_ISBN'])
            rent_df.loc[len(rent_df)+1] = new_rent
            usercnt = user_df.loc[select_user,'USER_RENT_CNT']
            user_df.loc[select_user,'USER_RENT_CNT'] = usercnt+1
            #rent_df = rent_df.set_index(rent_df['RENT_NUM'])
            #rent_df.reset_index(drop=True,inplace=True)
            rent_df = rent_df.sort_values(by = ["RENT_NUM"]) 
            num += 1

                       
            book_df.to_csv("csv/book.csv",index=False)
            user_df.to_csv("csv/user.csv", index = False)
            rent_df.to_csv("csv/rent.csv", index = False)
            tkinter.messagebox.showinfo("도서 대출", "도서 대출 완료")
            rent1.destroy()
            window.destroy()

                
            
        
         
        rent1label = Label(rent1, text = '도서 대출하기', bg = 'gray', width = 700, height = 4)
        rent1label.pack()
 
        rent1booklabel = Label(rent1, text = '대출할 도서', bg='gray')
        rent1booklabel.place(relx=0.05,rely=0.2,relwidth=0.15,relheight=0.07)

        # 책에 맞게 제목 빌려오기
        ABC = csv_pull.loc[int(select_book)]["BOOK_TITLE"]
        booknamelabel = Label(rent1, text = '▶{}◀'.format(ABC), bg = 'gray') 
        booknamelabel.place(relx=0.25,rely=0.2,relwidth=0.6,relheight=0.07)

 
        searchuserlabel = Label(rent1, text = '회원정보 입력', bg = 'gray')
        searchuserlabel.place(relx = 0.05,rely=0.3,relwidth=0.15,relheight=0.07)

        Notice = Label(rent1, text = '※ 대출을 원하시는 회원을 선택하고 선택하기 버튼을 눌러주세요',)
        Notice.place(relx = 0.05,rely=0.8,relwidth=0.5,relheight=0.07)

        
        searchuserentry = Entry(rent1)
        searchuserentry.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)
        def search2 ():        
            for phone in df_user.index.tolist():
                user_name = searchuserentry.get()
                
                search1 = df_user["USER_PHONE"].str.contains(user_name) # 폰번호 필터링
                search2 = df_user["USER_NAME"].str.contains(user_name) # 이름 필터링
                # 제목 + 저자로 필터링
                csv_2 = df_user.loc[search1 | search2,["USER_PHONE","USER_NAME","USER_SEX"]]

            # Treeview 기존 목록 삭제
            for item in USER_SELECT_BOX.get_children(): 
                USER_SELECT_BOX.delete(item)
                
            # 제목과 저자로 필터링한 목록 출력
            for phone in csv_2.index.tolist():
                user_name = df_user.loc[phone, "USER_NAME"]
                user_birth = df_user.loc[phone, "USER_BIRTH"]
                user_sex = df_user.loc[phone, "USER_SEX"]          
            
                user_add = (phone,user_name,user_birth, user_sex)
                USER_SELECT_BOX.insert("","end",text="",value=user_add,iid=phone)
            
        searchuserbutton = Button(rent1, text = "검색",command=search2)
        searchuserbutton.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)
 
        userselectbutton = Button(rent1, text = '선택하기',command = event_book_rent)
        userselectbutton.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)

        #USER_SELECT_BOX.bind('<Double-Button-1>',click_item)
        USER_SELECT_BOX.place(relx=0.05,rely=0.4,relwidth=0.8,relheight = 0.4)
      else:
          tkinter.messagebox.showerror("오류","이미 대출중인 도서입니다.")
    
    def event_book_return():
         book_df = pd.read_csv("csv/book.csv",encoding = "utf-8")
         book_df = book_df.set_index(book_df['BOOK_ISBN'])
         user_df = pd.read_csv("csv/user.csv",encoding = "utf-8")
         user_df = user_df.set_index(user_df['USER_PHONE'])
         rent_df = pd.read_csv("csv/rent.csv",encoding = "utf-8")
         rent_df = rent_df.set_index(rent_df['BOOK_ISBN'])
         select_book = int(BOOK_SELECT_BOX.focus())         
         global num
         b = rent_df['BOOK_ISBN'].tolist()

         if select_book in b:
           returnMsgBox = tkinter.messagebox.askquestion(" ",'해당 도서를 반납하시겠습니까?')
           if returnMsgBox == 'yes':
                select_user = rent_df.loc[select_book,'USER_PHONE']
                usercnt = user_df.loc[select_user,'USER_RENT_CNT']

                user_df.loc[select_user,'USER_RENT_CNT'] = usercnt-1
                book_df.loc[select_book,'BOOK_RENTAL']="False"
                idx = rent_df[rent_df['BOOK_ISBN']==select_book].index
                rent_df.drop(idx,inplace=True) # num # 인덱스로 저장한 idx를 참고하여 drop(), 해당 행 삭제

                rent_df = rent_df.sort_values(by = ["RENT_NUM"])
              
                num -= 1
                book_df.to_csv("csv/book.csv",index=False)
                user_df.to_csv("csv/user.csv", index = False)
                rent_df.to_csv("csv/rent.csv", index = False)
                tkinter.messagebox.showinfo("도서 반납", "도서 반납 완료")
           else:
                 tkinter.messagebox.showinfo("취소"," 도서 반납을 취소합니다.")
         else :
          tkinter.messagebox.showerror("오류","대출 중인 도서가 아닙니다")
         window.destroy()
         


#=======================================================================================

    # 검색 버튼
    BOOK_SEARCH_BTN = Button(window, text = '검색', fg='black' ,bg='gray',command=search1)
    BOOK_SEARCH_BTN.place(relx=0.82,rely=0.2,relwidth=0.1,relheight = 0.05)
    # 선택하기 버튼
    BOOK_INF = Button(window, text = '선택하기', fg='black', bg = 'gray',command=book_information)
    BOOK_INF.place(relx=0.82,rely=0.28,relwidth=0.1,relheight=0.05)

    #rent_df = pd.read_csv("csv/rent.csv",encoding = "utf-8")
    #rent_df = csv_pull.set_index("BOOK_ISBN")

    #a = SEARCH_BOOK_ISBN.get()
    #ISBN_OVERLAP = rentdf.index.tolist()
    #if  a in ISBN_OVERLAP:
    #    tkinter.messagebox.
    rent_button=Button(window,text='대출하기',bg='gray',command=bookrent_selectuser)
    rent_button.place(relx=0.82,rely=0.58,relwidth=0.1,relheight=0.1)
    return_button=Button(window,text='반납하기',bg='gray',command=event_book_return)
    return_button.place(relx=0.82,rely=0.68,relwidth=0.1,relheight=0.1)




# ㉰의 화면----------------------------------------------------
def BOOK_DELETE():
    #공통부분 ↓-----------------------------------------------------------------------
    window = tkinter.Tk()
    window.title("도서 삭제")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 삭제', bg = 'gray',width = 700, height = 5)
    window.resizable(width=FALSE, height=FALSE)

    #공통부분 ↑-----------------------------------------------------------------------
    label2 = Label(window, text='삭제할 도서 검색하기 :',fg='black' ,
                   font=('맑은 고딕',10), width=20,height=1)

    BTN_CANCEL = Button(window, text='뒤로가기', bg='gray'
    , width='8', height='2',command=window.destroy)

    # 상황별 메세지 창 
    def DLT_ASK():
        tkinter.messagebox.askquestion("도서 삭제"," (책 이름)을 삭제하시겠습니까?")
    def DLT_DONE():
        tkinter.messagebox.showinfo("삭제 완료"," (책 이름)을 삭제되었습니다 !")
    def DLT_ERROR():
        tkinter.messagebox.showerror("삭제 실패"," 해당 도서를 반납하고 삭제해주세요 !")

    # 클릭 시 이벤트 발생 -> 도서 삭제 즉시 실행
    def click_item(event):
        selected=BOOK_SELECT_BOX.focus()
        DLT_BOOK(int(selected))
        
    # 도서 삭제 구현 
    def DLT_BOOK(selected):
        # book.csv 가져오기 ( 인덱스로 접근해서 삭제 / 포맷팅 ) 
        csv_pull = pd.read_csv("csv/book.csv",encoding = "utf-8")
        # rent.csv 가져오기 ( 대여여부 확인 / 행삭제 접근)
        csv_pull_1 = pd.read_csv("csv/rent.csv",encoding = "utf-8")
        # book.csv 인덱스 설정
        csv_pull = csv_pull.set_index("BOOK_ISBN")
        # 포맷팅
        name = csv_pull.loc[selected]["BOOK_TITLE"]
        
        

        CHECK_ISBN = csv_pull_1['BOOK_ISBN'].tolist() 

        MB = tkinter.messagebox.askquestion("도서 삭제", "{}을 삭제하시겠습니까?".format(name))
        
        if MB == "yes":
            if selected not in CHECK_ISBN:    #도서 정보 가져와야함 / 구현 성공
                csv_pull = csv_pull.drop(selected)
                tkinter.messagebox.showinfo("삭제 완료", " 삭제가 완료 되었습니다 !")
                csv_pull.to_csv("csv/book.csv", index = True, encoding='utf-8')
                
            else:
                tkinter.messagebox.showerror("삭제 오류", " 이미 대출 중인 도서입니다.")

# 도서명과 저자로 검색하기 ======================================================================
    def search ():        
        for ISBN in csv_pull.index.tolist():
            csv_pull_delete = pd.read_csv("csv/book.csv",encoding = "utf-8")
            csv_pull_delete = csv_pull_delete.set_index("BOOK_ISBN")

            book_name = BOOK_SEARCH_LABEL.get()
            
            search1 = csv_pull_delete["BOOK_TITLE"].str.contains(book_name)
            search2 = csv_pull_delete["BOOK_AUTHOR"].str.contains(book_name)

            csv_2_delete = csv_pull_delete.loc[search1 | search2,["BOOK_TITLE","BOOK_AUTHOR","BOOK_PUBLIC"]]

            for item in BOOK_SELECT_BOX.get_children():
                BOOK_SELECT_BOX.delete(item)

            for ISBN in csv_2_delete.index.tolist():
                book_title = csv_2_delete.loc[ISBN, "BOOK_TITLE"]
                book_author = csv_2_delete.loc[ISBN, "BOOK_AUTHOR"]
                book_publish = csv_2_delete.loc[ISBN, "BOOK_PUBLIC"]
                
                book_add = (ISBN, book_title, book_author, book_publish)
                BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])

#==================================================================================================

    # 레이블 1 
    label3 = Label(window, text='도서명 혹은 저자로 검색해주세요 ↓',fg='black' ,
                   font=('맑은 고딕',10), width=30,height=1)         
    # 레이블 2
    BOOK_SEARCH_LABEL = Entry(window)
    BOOK_SEARCH_LABEL.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)
    # 버튼 1
    BOOK_SEARCH_BTN = Button(window, text = '검색', fg='black' ,bg='gray', command = search)
    BOOK_SEARCH_BTN.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)
    # 버튼 2
    BOOK_SELECT_BTN = Button(window, text = '선택하기', fg='black', bg = 'gray')
    BOOK_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)
    BOOK_SELECT_BTN.bind('<Button-1>',click_item)
    # csv 파일 가져오기
    csv_pull = pd.read_csv("csv/book.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")

    # 도서 목록 창 (Treeview)
    BOOK_SELECT_BOX = ttk.Treeview(window, columns=(1,2,3,4), height = 13,show="headings")
    
    # 필드명
    BOOK_SELECT_BOX.heading(1, text='ISBN')
    BOOK_SELECT_BOX.heading(2, text='도서명')
    BOOK_SELECT_BOX.heading(3, text='저자')
    BOOK_SELECT_BOX.heading(4, text='출판사')
    # 기본 너비 
    BOOK_SELECT_BOX.column(1, width='170')
    BOOK_SELECT_BOX.column(2, width='130')
    BOOK_SELECT_BOX.column(3, width='120')
    BOOK_SELECT_BOX.column(4, width='80')


    # 목록 출력할 데이터 
    # 데이터 프레임 출력
    for ISBN in csv_pull.index.tolist():
        book_title = csv_pull.loc[ISBN, "BOOK_TITLE"]
        book_author = csv_pull.loc[ISBN, "BOOK_AUTHOR"]
        book_publish = csv_pull.loc[ISBN, "BOOK_PUBLIC"]
        
        book_add = (ISBN, book_title, book_author, book_publish)
        BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])
        
    # 더블 클릭시 이벤트 발생 
    BOOK_SELECT_BOX.bind('<Double-Button-1>', click_item)

    BOOK_SELECT_BOX.place(x=90, y=200)
    BTN_CANCEL.pack()
    BTN_CANCEL.place(x=5,y=25)
    label1.pack()
    label2.pack()
    label3.place(x=177, y=125)
    label2.place(x=5, y=155)

    def refresh_delete():
    # treeview 지우기
        for item in BOOK_SELECT_BOX.get_children():
            BOOK_SELECT_BOX.delete(item)
    # csv 파일 불러오기 
        csv_pull = pd.read_csv("csv/book.csv",encoding = "utf-8")
        csv_pull = csv_pull.set_index("BOOK_ISBN")

        for ISBN in csv_pull.index.tolist():
            book_title = csv_pull.loc[ISBN, "BOOK_TITLE"]
            book_author = csv_pull.loc[ISBN, "BOOK_AUTHOR"]
            book_publish = csv_pull.loc[ISBN, "BOOK_PUBLIC"]
            
            book_add = (ISBN, book_title, book_author, book_publish)
            BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])

#새로고침 버튼 추가
    REFRESH_BTN = Button(window, text = '새로고침', fg='black' ,bg='gray', command = refresh_delete) 
    REFRESH_BTN.place(relx=0.86,rely=0.5,relwidth=0.1,relheight = 0.07)
        

def USER_MANAGEMENT():
    #공통부분 ↓---------------------------------------------------------------------
    window = Tk()
    window.title("도서관리")
    window.geometry("700x500")
    label1 = Label(window, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)
    window.resizable(width=FALSE, height=FALSE)

    #공통부분 ↑---------------------------------------------------------------------

    BTN_CANCEL = Button(window, text='뒤로가기', bg='gray'
    , width='8', height='2',command=window.destroy) 
    
    USER_REG = Button(window, text='회원 등록',fg="black", bg="gray", width='20',
                      height='10', command = USER_3)
                                    
    USER_INF = Button(window, text='회원\n검색/수정/탈퇴',fg="black", bg="gray", width='20',
                        height='10', command = USER_1)
    label1.pack()
    USER_REG.place(x=150,y=150)
    USER_INF.place(x=450,y=150)
    BTN_CANCEL.place(x=5,y=25)

    








    


# 첫번째 화면(메인화면)--------------------------------------------------------------------------------

window = Tk()
window.title("도서관리 프로그램")
window.geometry("700x500")
window.resizable(width=FALSE, height=FALSE)

label1 = Label(window, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)

#도서관리 누르면 2번째 창으로 넘어감
BTN_BOOK = Button(window, text='도서관리',fg="black", bg="gray", width='20',
                      height='10', command=BOOK_MANAGEMENT)
                                    
BTN_MEMBER = Button(window, text='회원관리',fg="black", bg="gray", width='20',
                        height='10', command = USER_MANAGEMENT)

label1.pack()


BTN_BOOK.pack()
BTN_BOOK.place(x=150,y=150)

BTN_MEMBER.pack()
BTN_MEMBER.place(x=450,y=150)

window.mainloop()
    
