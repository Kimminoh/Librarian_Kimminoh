from tkinter import*
import tkinter.messagebox
import pandas as pd
from tabulate import tabulate
import tkinter as tk
import tkinter.ttk as ttk



# 2번째 화면
def BOOK_MANAGEMENT():
    #공통부분 ↓---------------------------------------------------------------------
    window = Tk()
    window.title("도서관리")
    window.geometry("700x500")
    label1 = Label(window, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)
    window.configure(background = 'sky blue')

    #공통부분 ↑---------------------------------------------------------------------
    # ㉮
    BTN_REG_EDIT = Button(window, text='도서\n등록/수정', bg='orange', width='18',
                          height='8', command = BOOK_MANAGEMENT_FIRST)
    # ㉯
    BTN_SEARCH_RENT = Button(window, text='도서\n조회/대출', bg='orange', width='18',
                          height='8', command = BOOK_LOOKUP)
    # ㉰
    BTN_DELETE = Button(window, text='도서삭제', bg='orange', width='18',
                          height='8', command = BOOK_DELETE)    

      
    BTN_CANCEL = Button(window, text='뒤로가기', bg='orange'
    , width='8', height='2',command=window.destroy)    


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
    label1 = Label(window, text = '도서 등록/수정', bg = 'gray',width = 700, height = 5)
    window.configure(background = 'sky blue')
    #공통부분 ↑-----------------------------------------------------------------------  
    
    BTN_NEW_REG = Button(window, text='도서 신규 등록', bg='orange', width='15', height='2',
                         command = BOOK_NEW_REG)
    BTN_CANCEL = Button(window, text='뒤로가기', bg='orange',
     width='8', height='2',command=window.destroy)
    
    '''#  도서명과 저자로 검색하기 / 이거 아직 구현 안 됨
    def search ():        
        for ISBN in csv_pull.index.tolist():
            BOOK_SEARCH_LABEL = "파이썬"
            search1 = csv_pull["BOOK_TITLE"].str.contains(BOOK_SEARCH_LABEL)
            search2 = csv_pull["BOOK_AUTHOR"].str.contains(BOOK_SEARCH_LABEL)

            search_Book1 = csv_pull.loc[search1 | search2,["BOOK_TITLE"]]
            search_Book2 = csv_pull.loc[search1 | search2,["BOOK_AUTHOR"]]
            search_Book3 = csv_pull.loc[search1 | search2,["BOOK_PUBLIC"]]
            book_add = (ISBN, search_Book1,search_Book2,search_Book3)
            BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0]) '''
    
    
    label2 = Label(window, text='수정할 도서 검색하기 :',fg='black' ,
                   font=('맑은 고딕',10), width=20,height=1)
    
    label3 = Label(window, text='도서명 혹은 저자로 검색해주세요 ↓',fg='black' ,
                   font=('맑은 고딕',10), width=30,height=1) 

    BOOK_SEARCH_LABEL = Entry(window)
    BOOK_SEARCH_LABEL.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)
    
    
    BOOK_SEARCH_BTN = Button(window, text = '검색', fg='white' ,bg='black') # command=search
    BOOK_SEARCH_BTN.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)

    
    # 등록되어 있는 도서 리스트
    csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")

    BOOK_SELECT_BOX = ttk.Treeview(window, columns=(1,2,3,4), height = 13,show="headings")
    
    
    BOOK_SELECT_BTN = Button(window, text = '선택하기', fg='white', bg = 'black',command=BOOK_EDIT)
    BOOK_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)

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
    #스크롤바 (안생기는데 왜 안생기는지 모르겠음)
    scroll = ttk.Scrollbar(window, orient="vertical", command=BOOK_SELECT_BOX.yview)
    scroll.pack(side='right', fill='y')
    BOOK_SELECT_BOX.configure(yscrollcommand=scroll.set)

    # 목록 출력할 데이터 
    # 데이터 프레임 출력
    
    for ISBN in csv_pull.index.tolist():
        book_title = csv_pull.loc[ISBN, "BOOK_TITLE"]
        book_author = csv_pull.loc[ISBN, "BOOK_AUTHOR"]
        book_publish = csv_pull.loc[ISBN, "BOOK_PUBLIC"]
        
        book_add = (ISBN, book_title, book_author, book_publish)
        BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])

    def click_item(event):
        BOOK_EDIT()

    BOOK_SELECT_BOX.bind('<Double-Button-1>', click_item)
    BOOK_SELECT_BOX.place(x=90, y=200)
    label1.pack()
    label2.place(x=15, y=155)
    label3.place(x=177, y=125)
    BTN_CANCEL.place(x=5,y=25)
    BTN_NEW_REG.place(x=5,y=90)
    
    
# ㉮-1 신규 도서 추가     
def BOOK_NEW_REG():
    #공통부분 ↓-----------------------------------------------------------------------
    window = Tk()
    window.title("도서 신규등록")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 신규 등록', bg = 'gray', width = 700, height = 3)
    window.configure(background = 'sky blue')    
    #공통부분 ↑-----------------------------------------------------------------------  
    label1.pack() # 창 제목 레이블
    
    def BTN_EDIT(a, b, c, d,e, f,g):
        a = Button(window, text=b, bg=c, width=d, height=e)
        a.place(x=f, y = g)    
        
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

        if MSB == 'yes':
            a = SEARCH_BOOK_ISBN.get()
            b = SEARCH_BOOK_TITLE.get()
            c = SEARCH_BOOK_AUTHOR.get()
            d = SEARCH_BOOK_PUBLIC.get()
            e = SEARCH_BOOK_PRICE.get()
            f = SEARCH_BOOK_LINK.get()
            g = SEARCH_IMAGE_FIND.get()
            h = SEARCH_BOOK_DESCRIPTION.get()
            #i = SEARCH_BOOK_RENTAL

            #하나라도 입력하지 않았을 때
            if a.strip()=="" or b.strip()=="" or c.strip()=="" or d.strip()=="" or e.strip()=="" \
               or f.strip()=="" or g.strip()=="" or h.strip()=="":
                ERROR_6()
                return 0

            # 중복확인 안했을 때 
            if not OVERLAP_CHECK['state'] == 'disabled' :
                ERROR_3()

            # 가격이 정수가 아닐 때
            if not e.isdigit():
                ERROR_4()
                
            else:
                csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
                csv_pull = csv_pull.set_index("BOOK_ISBN")
                csv_pull.loc[a, 'BOOK_TITLE']= b
                csv_pull.loc[a, 'BOOK_AUTHOR']= c  
                csv_pull.loc[a, 'BOOK_PUBLIC']= d 
                csv_pull.loc[a, 'BOOK_PRICE']= int(e)
                csv_pull.loc[a, 'BOOK_LINK']= f
                csv_pull.loc[a, 'BOOK_IMAGE']= g
                csv_pull.loc[a, 'BOOK_DESCRIPTION']= h
                #csv_pull.loc[a, 'BOOK_RENTAL']= "FALSE"
                #csv 저장하기 
                csv_pull.to_csv("csv/book_1.csv", index = True)

                print(tabulate(csv_pull, headers='keys', tablefmt='psql',numalign='left',stralign='left'))
                window.destroy()



            
    def ISBN_OVERLAP():
        csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
        csv_pull = csv_pull.set_index("BOOK_ISBN")
        
        a = SEARCH_BOOK_ISBN.get()
        ISBN_OVERLAP = csv_pull.index.tolist()
        if  a in ISBN_OVERLAP:
            ERROR_2()
            
        elif not a.isdigit():
            ERROR_5()
                
        else :
            ERROR_1()
            # 중복 확인 완료시 버튼 비활성화 
            OVERLAP_CHECK['state'] = 'disabled'
            SEARCH_BOOK_ISBN['state'] = 'disabled'




    # 사진 미리 보기 창
    # 예외처리 (사진을 등록하지 않았을 때) => 메세지 창 띄우기

    IMAGE_label = Label(window, text="사진\n미리보기",bg="orange",width='15',height='10')
    IMAGE_label.place(x=30,y=80)


    BTN_BOOK_ISBN = Button(window, text='ISBN', bg='orange', width='8', height='1')
    BTN_BOOK_ISBN.place(x=170, y = 80)
    SEARCH_BOOK_ISBN = Entry(window)
    SEARCH_BOOK_ISBN.place(x= 250, y= 80,relwidth=0.5,relheight=0.05)

    # 중복확인시 이벤트 추가함
    OVERLAP_CHECK = Button(window, text='중복확인', bg='orange', width='7', height='1',
                           command = ISBN_OVERLAP)
    OVERLAP_CHECK.place(x=620, y = 80)    

    BTN_BOOK_TITLE = Button(window, text='도서명', bg='orange', width='8', height='1')
    BTN_BOOK_TITLE.place(x=170, y = 120)
    SEARCH_BOOK_TITLE = Entry(window)
    SEARCH_BOOK_TITLE.place(x= 250, y= 120,relwidth=0.5,relheight=0.05)

    BTN_BOOK_AUTHOR = Button(window, text='저자', bg='orange', width='8', height='1')
    BTN_BOOK_AUTHOR.place(x=170, y = 160)
    SEARCH_BOOK_AUTHOR = Entry(window)
    SEARCH_BOOK_AUTHOR.place(x= 250, y= 160,relwidth=0.5,relheight=0.05)

    BTN_BOOK_PUBLIC = Button(window, text='출판사', bg='orange', width='8', height='1')
    BTN_BOOK_PUBLIC.place(x=170, y = 200)
    SEARCH_BOOK_PUBLIC = Entry(window)
    SEARCH_BOOK_PUBLIC.place(x= 250, y= 200,relwidth=0.5,relheight=0.05)

    BTN_BOOK_PRICE = Button(window, text='가격', bg='orange', width='8', height='1')
    BTN_BOOK_PRICE.place(x=170, y = 240)
    SEARCH_BOOK_PRICE = Entry(window)
    SEARCH_BOOK_PRICE.place(x= 250, y= 240,relwidth=0.5,relheight=0.05)

    BTN_BOOK_LINK = Button(window, text='URL', bg='orange', width='8', height='1') 
    BTN_BOOK_LINK.place(x=170, y = 280)
    SEARCH_BOOK_LINK = Entry(window)
    SEARCH_BOOK_LINK.place(x= 250, y= 280,relwidth=0.5,relheight=0.05)
    
    BTN_BOOK_DESCRIPTION = Button(window, text='도서 설명', bg='orange', width='8', height='1')
    BTN_BOOK_DESCRIPTION.place(x=170, y = 320)
    SEARCH_BOOK_DESCRIPTION = Entry(window)
    SEARCH_BOOK_DESCRIPTION.place(x= 250, y= 320,relwidth=0.5,relheight=0.05)

    BTN_IMAGE_FIND = Button(window, text='사진 찾기', bg='orange', width='8', height='1')
    BTN_IMAGE_FIND.place(x=170, y = 360)
    SEARCH_IMAGE_FIND = Entry(window)
    SEARCH_IMAGE_FIND.place(x= 250, y= 360,relwidth=0.5,relheight=0.05)
    
    BTN_EDIT('BTN_FIND', '찾아 보기', 'gray', '8', '1', 620, 360)
    
    BTN_OK = Button(window, text='확인', bg='gray',width='7', height='1', command = REG)
    BTN_OK.place(x=300, y = 420)

    BTN_CANCEL = Button(window, text='취소', bg='gray', width='7', height='1',
                        command=window.destroy )
    BTN_CANCEL.place(x=400, y = 420)


# ㉮-2번째 창 / 도서 수정하기
# 도서 목록중 하나 선택해서 도서 수정하기 
def BOOK_EDIT():
    #공통부분 ↓-----------------------------------------------------------------------
    window = Tk()
    window.title("도서 수정하기")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 수정하기', bg = 'gray', width = 700, height = 3)
    window.configure(background = 'sky blue')    
    #공통부분 ↑-----------------------------------------------------------------------
    label1.pack() # 창 제목 레이블
    # 함수안의 함수 => 버튼 형식 생성
    def BTN_EDIT(a, b, c, d,e, f,g):
        a = Button(window, text=b, bg=c, width=d, height=e)
        a.place(x=f, y = g)    

    def BLANK(a,b,c,d,e):
        a = Entry(window)
        a.place(x= b, y= c,relwidth=d,relheight=e)
    
    # 리스트 박스 목록 더블클릭시 창 띄우기 아직 구현 X
    # 선택하기 눌러야 함
    # 예외처리 이벤트
    def ERROR_7():     # 예외처리 7 #수정 불가인데 에러메세지?
        tkinter.messagebox.showerror("ERROR","해당 ISBN으로 수정이 가능합니다 !")
    def ERROR_8():     # 예외처리 8
        tkinter.messagebox.showerror("ERROR","해당 ISBN으로는 수정하실 수 없습니다 !")
    def ERROR_9():     # 예외처리 9
        tkinter.messagebox.showerror("ERROR","변경사항을 적용 하여야지 등록/수정이 가능합니다 !")
    def ERROR_10():     # 예외처리 10
        tkinter.messagebox.showerror("ERROR","해당 부분은 숫자로만 입력이 가능합니다 !")

    #def APPLY():
        
    csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")
    

    IMAGE_label = Label(window, text="사진\n미리보기",bg="orange",width='15',height='10')
    IMAGE_label.place(x=30,y=80)

    BTN_BOOK_ISBN = Button(window, text='ISBN', bg='orange', width='8', height='1')
    BTN_BOOK_ISBN.place(x=170, y = 80)
    SEARCH_BOOK_ISBN = Entry(window)
    SEARCH_BOOK_ISBN.place(x= 250, y= 80,relwidth=0.5,relheight=0.05)

    # 중복확인시 이벤트 발생 추가
    OVERLAP_CHECK = Button(window, text='중복확인', bg='orange', width='7', height='1',
                           command = ERROR_7)
    OVERLAP_CHECK.place(x=620, y = 80)
    
    BTN_BOOK_TITLE = Button(window, text='도서명', bg='orange', width='8', height='1')
    BTN_BOOK_TITLE.place(x=170, y = 120)
    SEARCH_BOOK_TITLE = Entry(window)
    SEARCH_BOOK_TITLE.place(x= 250, y= 120,relwidth=0.5,relheight=0.05)
    #SEARCH_BOOK_TITLE.insert("","end",text="",value=book_add,iid=book_add[0])
    

    BTN_BOOK_AUTHOR = Button(window, text='저자', bg='orange', width='8', height='1')
    BTN_BOOK_AUTHOR.place(x=170, y = 160)
    SEARCH_BOOK_AUTHOR = Entry(window)
    SEARCH_BOOK_AUTHOR.place(x= 250, y= 160,relwidth=0.5,relheight=0.05)

    BTN_BOOK_PUBLIC = Button(window, text='출판사', bg='orange', width='8', height='1')
    BTN_BOOK_PUBLIC.place(x=170, y = 200)
    SEARCH_BOOK_PUBLIC = Entry(window)
    SEARCH_BOOK_PUBLIC.place(x= 250, y= 200,relwidth=0.5,relheight=0.05)

    BTN_BOOK_PRICE = Button(window, text='가격', bg='orange', width='8', height='1')
    BTN_BOOK_PRICE.place(x=170, y = 240)
    SEARCH_BOOK_PRICE = Entry(window)
    SEARCH_BOOK_PRICE.place(x= 250, y= 240,relwidth=0.5,relheight=0.05)

    BTN_BOOK_LINK = Button(window, text='URL', bg='orange', width='8', height='1') 
    BTN_BOOK_LINK.place(x=170, y = 280)
    SEARCH_BOOK_LINK = Entry(window)
    SEARCH_BOOK_LINK.place(x= 250, y= 280,relwidth=0.5,relheight=0.05)
    
    BTN_BOOK_DESCRIPTION = Button(window, text='도서 설명', bg='orange', width='8', height='1')
    BTN_BOOK_DESCRIPTION.place(x=170, y = 320)
    SEARCH_BOOK_DESCRIPTION = Entry(window)
    SEARCH_BOOK_DESCRIPTION.place(x= 250, y= 320,relwidth=0.5,relheight=0.05)

    BTN_IMAGE_FIND = Button(window, text='사진 찾기', bg='orange', width='8', height='1')
    BTN_IMAGE_FIND.place(x=170, y = 360)
    SEARCH_IMAGE_FIND = Entry(window)
    SEARCH_IMAGE_FIND.place(x= 250, y= 360,relwidth=0.5,relheight=0.05)
    
    BTN_EDIT('BTN_FIND', '찾아 보기', 'gray', '8', '1', 620, 360)




    # 적용 버튼 누를 시 수정!
    BTN_APPLY = Button(window, text='적용', bg = 'gray', width='7', height='1')
    
    BTN_OK = Button(window, text='확인', bg='gray',width='7', height='1')
    BTN_OK.place(x=300, y = 420)

    BTN_CANCEL = Button(window, text='취소', bg='gray', width='7', height='1',command=window.destroy )
    BTN_CANCEL.place(x=400, y = 420)
    


# ㉯의 화면----------------------------------------------------
def BOOK_LOOKUP():
    window = Tk()
    window.title('도서 조회/대출')
    window.geometry("700x500")
    label1 = Label(window, text = '도서 조회/대출', bg ='gray', width = 700, height = 5)
    window.configure(background = 'sky blue')

    label1.pack()
    
    def BTN_EDIT(a, b, c, d,e, f,g):
        a = Button(window, text=b, bg=c, width=d, height=e)
        a.place(x=f, y = g)    

    def BLANK(a,b,c,d,e) :
        a = Entry(window)
        a.place(x= b, y= c,relwidth=d,relheight=e)

    BTN_CANCEL = Button(window, text='뒤로가기', bg='orange',
     width='8', height='2',command=window.destroy)
    BTN_CANCEL.place(x=5,y=25)
    
    BTN_SEARCH = Button(window, text='도서 검색', bg='orange', width='10', height='2')         
    BTN_SEARCH.place(x=30,y=95)
    
    BLANK_SEARCH = Entry(window)
    BLANK_SEARCH.place(x= 150, y= 100,relwidth=0.6,relheight=0.06)
# Treeview---------------------------------------------------------------------
    # csv 파일 가져오기
    csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")

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
    #스크롤바 (안생기는데 왜 안생기는지 모르겠음)
    scroll = ttk.Scrollbar(window, orient="vertical", command=BOOK_SELECT_BOX.yview)
    scroll.pack(side='right', fill='y')
    BOOK_SELECT_BOX.configure(yscrollcommand=scroll.set)

    # 목록 출력할 데이터 
    # 데이터 프레임 출력
    
    for ISBN in csv_pull.index.tolist():
        book_title = csv_pull.loc[ISBN, "BOOK_TITLE"]
        book_author = csv_pull.loc[ISBN, "BOOK_AUTHOR"]
        book_publish = csv_pull.loc[ISBN, "BOOK_PUBLIC"]
        
        book_add = (ISBN, book_title, book_author, book_publish)
        BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])

    def click_item(event):
        window = Tk()

    # 더블 클릭시 이벤트 발생 
    BOOK_SELECT_BOX.bind('<Double-Button-1>', click_item)

    BOOK_SELECT_BOX.place(x=90, y=150)
#---------------------------------------------------------------------------

    BOOK_SEARCH_BTN = Button(window, text = '검색', fg='white' ,bg='black')
    BOOK_SEARCH_BTN.place(x=600,y=95,relwidth=0.1,relheight = 0.07)

    BOOK_INF = Button(window, text = '선택하기', fg='white', bg = 'black')
    BOOK_INF.place(x=600,y=150,relwidth=0.1,relheight=0.05)

    BTN_EDIT('BTN_IMAGE', '사진', 'gray', '7', '1', 30, 320)
    BTN_EDIT('BTN_ISBN', 'ISBN', 'gray', '7', '1', 120, 320)
    BTN_EDIT('BTN_TITLE', '도서명', 'gray', '7', '1', 210, 320)
    BTN_EDIT('BTN_AUTHOR', '저자', 'gray', '7', '1', 300, 320)
    BTN_EDIT('BTN_PRICE', '가격', 'gray', '7', '1', 390, 320)
    BTN_EDIT('BTN_URL', 'URL', 'gray', '7', '1', 480, 320)
    BTN_EDIT('BTN_RENT', '대출여부', 'gray', '7', '1', 570, 320)

    BLANK('example', 120, 380, 0.08, 0.05)
    BLANK('example', 210, 380, 0.08, 0.05)
    BLANK('example', 300, 380, 0.08, 0.05)
    BLANK('example', 390, 380, 0.08, 0.05)
    BLANK('example', 480, 380, 0.08, 0.05)
    BLANK('example', 570, 380, 0.08, 0.05)

    BTN_EDIT("example", '대출하기\n반납하기','gray','10','2',560,430)
    
    
    


# ㉰의 화면----------------------------------------------------
def BOOK_DELETE():
    #공통부분 ↓-----------------------------------------------------------------------
    window = tkinter.Tk()
    window.title("도서 삭제")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 삭제', bg = 'gray',width = 700, height = 5)
    window.configure(background = 'sky blue')
    #공통부분 ↑-----------------------------------------------------------------------
    label2 = Label(window, text='삭제할 도서 검색하기 :',fg='black' ,
                   font=('맑은 고딕',10), width=20,height=1)

    BTN_CANCEL = Button(window, text='뒤로가기', bg='orange'
    , width='8', height='2',command=window.destroy)

    def DLT_ASK():
        tkinter.messagebox.askquestion("도서 삭제"," (책 이름)을 삭제하시겠습니까?")
    def DLT_DONE():
        tkinter.messagebox.showinfo("삭제 완료"," (책 이름)을 삭제되었습니다 !")
    def DLT_ERROR():
        tkinter.messagebox.showerror("삭제 실패"," 해당 도서를 반납하고 삭제해주세요 !")

    def DLT_BOOK():
        csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
        csv_pull = csv_pull.set_index("BOOK_ISBN")

        MB = tkinter.messagebox.askquestion("도서 삭제", "을 삭제하시겠습니까?")
        #if MB == "yes":
        #    if BOOK_RENTAL == True :    도서 정보 가져와야함 / 아직 구현 X
        #        messagebox.showerror("삭제 오류", " 이미 대출 중인 도서입니다.")

         #   else:
         #       csv_pull.drop



    # 레이블 1 
    label3 = Label(window, text='도서명 혹은 저자로 검색해주세요 ↓',fg='black' ,
                   font=('맑은 고딕',10), width=30,height=1)         

    # 레이블 2
    BOOK_SEARCH_LABEL = Entry(window)
    BOOK_SEARCH_LABEL.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)

    # 버튼 1
    BOOK_SEARCH_BTN = Button(window, text = '검색', fg='white' ,bg='black')
    BOOK_SEARCH_BTN.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)

    # 버튼 2
    BOOK_SELECT_BTN = Button(window, text = '선택하기', fg='white', bg = 'black', command = DLT_BOOK)
    BOOK_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)

    # csv 파일 가져오기
    csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")

    # 도서 목록 창 (Treeview)
    BOOK_SELECT_BOX = ttk.Treeview(window, columns=(1,2,3,4), height = 13,show="headings")
    
    BOOK_SELECT_BTN = Button(window, text = '선택하기', fg='white', bg = 'black',command=DLT_BOOK)
    BOOK_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)

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
    #스크롤바 (안생기는데 왜 안생기는지 모르겠음)
    scroll = ttk.Scrollbar(window, orient="vertical", command=BOOK_SELECT_BOX.yview)
    scroll.pack(side='right', fill='y')
    BOOK_SELECT_BOX.configure(yscrollcommand=scroll.set)

    # 목록 출력할 데이터 
    # 데이터 프레임 출력
    
    for ISBN in csv_pull.index.tolist():
        book_title = csv_pull.loc[ISBN, "BOOK_TITLE"]
        book_author = csv_pull.loc[ISBN, "BOOK_AUTHOR"]
        book_publish = csv_pull.loc[ISBN, "BOOK_PUBLIC"]
        
        book_add = (ISBN, book_title, book_author, book_publish)
        BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])

    def click_item(event):
        DLT_BOOK()

    # 더블 클릭시 이벤트 발생 
    BOOK_SELECT_BOX.bind('<Double-Button-1>', click_item)

    BOOK_SELECT_BOX.place(x=90, y=200)
    BTN_CANCEL.pack()
    BTN_CANCEL.place(x=5,y=25)
    label1.pack()
    label2.pack()
    label3.place(x=177, y=125)
    label2.place(x=5, y=155)
    
     

   
    


  
# 첫번째 화면(메인화면)------------------------------------------

window = Tk()
window.title("도서관리 프로그램")
window.geometry("700x500")

label1 = Label(window, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)
window.configure(background = 'sky blue')

#도서관리 누르면 2번째 창으로 넘어감
BTN_BOOK = Button(window, text='도서관리',fg="black", bg="orange", width='20',
                      height='10', command=BOOK_MANAGEMENT)
                      
# 우선적으로 해당 파일에서 회원관리 클릭시 프로그램 종료!                  
BTN_MEMBER = Button(window, text='회원관리',fg="black", bg="orange", width='20',
                        height='10')

label1.pack()


BTN_BOOK.pack()
BTN_BOOK.place(x=150,y=150)

BTN_MEMBER.pack()
BTN_MEMBER.place(x=450,y=150)

window.mainloop()
    

