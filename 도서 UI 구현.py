from tkinter import*


# 2번째 화면
def BOOK_MANAGEMENT():
    #공통부분 ↓
    window = Tk()
    window.title("도서관리")
    window.geometry("700x500")
    label1 = Label(window, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)
    window.configure(background = 'sky blue')
    #공통부분 ↑

    # ㉮
    BTN_REG_EDIT = Button(window, text='도서\n등록/수정', bg='orange', width='18',
                          height='8', command = BOOK_MANAGEMENT_FIRST)
    # ㉯
    BTN_SEARCH_RENT = Button(window, text='도서\n조회/대출', bg='orange', width='18',
                          height='8')
    # ㉰
    BTN_DELETE = Button(window, text='도서삭제', bg='orange', width='18',
                          height='8', command = BOOK_DELETE)    

    label1.pack()
    BTN_REG_EDIT.pack()
    BTN_SEARCH_RENT.pack()
    BTN_DELETE.pack()
    
    BTN_REG_EDIT.place(x=100,y=170)
    BTN_SEARCH_RENT.place(x=300,y=170)
    BTN_DELETE.place(x=500,y=170)

# ㉮의 화면
def BOOK_MANAGEMENT_FIRST():
    #공통부분 ↓
    window = Tk()
    window.title("도서 등록/수정")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 등록/수정', bg = 'gray',width = 700, height = 5)
    window.configure(background = 'sky blue')
    #공통부분 ↑

    BTN_CANCEL = Button(window, text='뒤로가기', bg='orange', width='8', height='2')
                        
    BTN_NEW_REG = Button(window, text='도서 신규 등록', bg='orange', width='15', height='2',
                         command = BOOK_NEW_REG)

    label2 = Label(window, text='수정할 도서 검색하기 :',fg='black' ,
                   font=('맑은 고딕',10), width=20,height=1) 

    BOOK_SEARCH_LABEL = Entry(window)
    BOOK_SEARCH_LABEL.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)
    BOOK_SEARCH_LABEL.insert(END, "도서명 혹은 저자를 입력하세요")
    
    BOOK_SEARCH_BTN = Button(window, text = '검색', fg='white' ,bg='black')
    BOOK_SEARCH_BTN.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)

    # 등록되어 있는 도서 리스트
    # 실제 구현시에는 데이터프레임에 있는 데이터 목록을 가져와서 출력해야함
    BOOK_SELECT_BOX = Listbox(window, width=70, height = 8, highlightcolor = 'blue') # 선택시 파란색으로 표시
    BOOK_SELECT_BOX.place(relx=0.05,rely=0.4,relwidth=0.8,relheight = 0.5)
    BOOK_SELECT_BOX.insert(0,"도서명 : 불멸의 이순신 / 저자 : 윤도운")
    BOOK_SELECT_BOX.insert(1,"도서명 : 동물농장 / 저자 : 조지 오웰")
    BOOK_SELECT_BOX.insert(2,"도서명 : 1984 / 저자 : 조지 오웰")
    BOOK_SELECT_BTN = Button(window, text = '선택하기', fg='white', bg = 'black',command=BOOK_EDIT)
    BOOK_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)
    
    
    label1.pack()

    label2.pack()
    label2.place(x=5, y=155)
    
    BTN_CANCEL.pack()
    BTN_CANCEL.place(x=5,y=25)

    BTN_NEW_REG.pack()
    BTN_NEW_REG.place(x=5,y=90)
    
    
# ㉮-1 신규 도서 추가     
def BOOK_NEW_REG():
    window = Tk()
    window.title("도서 신규등록")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 신규 등록', bg = 'gray', width = 700, height = 3)
    window.configure(background = 'sky blue')    

    label1.pack() # 창 제목 레이블
    
    def BTN_EDIT(a, b, c, d,e, f,g):
        a = Button(window, text=b, bg=c, width=d, height=e)
        a.pack()
        a.place(x=f, y = g)    

    def BLANK(a,b,c,d,e):
        a = Entry(window)
        a.place(x= b, y= c,relwidth=d,relheight=e)

    # 사진 미리 보기 창
    IMAGE_PREVIEW = Button(window, text='사진\n미리보기', bg='orange', width='15', height='10')
    IMAGE_PREVIEW.pack()
    IMAGE_PREVIEW.place(x=30, y = 80)
    
    BTN_BOOK_ISBN = Button(window, text='ISBN', bg='orange', width='8', height='1')
    BTN_BOOK_ISBN.pack()
    BTN_BOOK_ISBN.place(x=170, y = 80)
    SEARCH_BOOK_ISBN = Entry(window)
    SEARCH_BOOK_ISBN.place(x= 250, y= 80,relwidth=0.5,relheight=0.05)

    # 예외처리 (사진을 등록하지 않았을 때) => 메세지 창 띄우기
    BTN_EDIT('IMAGE_PREVIEW', '사진\n미리보기','orange','15','10',30,80)

    BTN_EDIT('BTN_BOOK_ISBN', 'ISBN', 'orange','8','1', 170, 80)
    BLANK('BTN_BOOK_ISBN',250,80,0.5,0.05)

    # 중복확인시 이벤트 발생 추가해야함 (예외처리 4가지)
    # (중복 확인 누르지 않을 때 / ISBN 동일 / 정수 이외의 값 / 정보 다 입력하지 않을 때)
    # => 메세지 창으로 이벤트 발생 시키기 추가 해야 함
    BTN_EDIT('OVERLAP_CHECK', '중복확인', 'orange', '7', '1', 620, 80)

    BTN_EDIT('BTN_BOOK_TITLE', '도서명','orange', '8',  '1', 170,120)
    BLANK('SEARCH_BOOK_TITLE', 250,120,0.5,0.05)

    BTN_EDIT('BTN_BOOK_AUTHOR', '저자', 'orange', '8', '1', 170, 160)
    BLANK('SEARCH_BOOK_AUTHOR', 250, 160, 0.5, 0.05)

    BTN_EDIT('BTN_BOOK_PUBLIC', '출판사', 'orange', '8', '1', 170, 200)
    BLANK('SEARCH_BOOK_PUBLIC', 250, 200, 0.5, 0.05)

    BTN_EDIT('BTN_BOOK_PRICE', '가격', 'orange', '8', '1', 170, 240)
    BLANK('SEARCH_BOOK_PRICE', 250, 240, 0.5, 0.05)

    BTN_EDIT('BTN_BOOK_LINK', 'URL', 'orange', '8', '1', 170, 280)
    BLANK('SEARCH_BOOK_LINK', 250, 280, 0.5, 0.05)
    
    BTN_EDIT('BTN_BOOK_DESCRIPTION', '도서 설명', 'orange', '8', '1', 170, 320)
    BLANK('SEARCH_BOOK_DESCRIPTION', 250, 320, 0.5, 0.05)

    BTN_EDIT('BTN_IMAGE_FIND', '사진 찾기', 'orange', '8', '1', 170, 360)
    BLANK('SEARCH_IMAGE_FIND', 250, 360, 0.5, 0.05)
    
    BTN_EDIT('BTN_FIND', '찾아 보기', 'gray', '8', '1', 620, 360)
    
    BTN_EDIT('BTN_OK', '확인', 'gray', '7', '1', 300, 420)

    BTN_EDIT('BTN_CANCEL', '취소', 'gray', '7', '1', 400, 420)


# ㉮-2번째 창 / 도서 수정하기
# 도서 목록중 하나 선택해서 도서 수정하기 
def BOOK_EDIT():
    window = Tk()
    window.title("도서 수정하기")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 수정하기', bg = 'gray', width = 700, height = 3)
    window.configure(background = 'sky blue')    

    label1.pack() # 창 제목 레이블
    
    # 함수안의 함수 => 버튼 형식 생성
    def BTN_EDIT(a, b, c, d,e, f,g):
        a = Button(window, text=b, bg=c, width=d, height=e)
        a.pack()
        a.place(x=f, y = g)    

    def BLANK(a,b,c,d,e):
        a = Entry(window)
        a.place(x= b, y= c,relwidth=d,relheight=e)
    
    # 리스트 박스 목록 더블클릭시 창 띄우기 아직 구현 X
    # 선택하기 눌러야 함
      
    # 예외처리 2개
    # (적용 버튼 누르지 않을 때 / 사진 없을 때)
    BTN_EDIT('IMAGE_PREVIEW', '사진\n미리보기','orange','15','10',30,80)

    BTN_EDIT('BTN_BOOK_ISBN', 'ISBN', 'orange','8','1', 170, 80)
    BLANK('BTN_BOOK_ISBN',250,80,0.5,0.05)

    # 중복확인시 이벤트 발생 추가해야함 (예외처리 4가지)
    # (중복 확인 누르지 않을 때 / ISBN 동일 / 정수 이외의 값 / 정보 다 입력하지 않을 때)
    # => 메세지 창으로 이벤트 발생 시키기 추가 해야 함
    BTN_EDIT('OVERLAP_CHECK', '중복확인', 'orange', '7', '1', 620, 80)

    BTN_EDIT('BTN_BOOK_TITLE', '도서명','orange', '8',  '1', 170,120)
    BLANK('SEARCH_BOOK_TITLE', 250,120,0.5,0.05)

    BTN_EDIT('BTN_BOOK_AUTHOR', '저자', 'orange', '8', '1', 170, 160)
    BLANK('SEARCH_BOOK_AUTHOR', 250, 160, 0.5, 0.05)

    BTN_EDIT('BTN_BOOK_PUBLIC', '출판사', 'orange', '8', '1', 170, 200)
    BLANK('SEARCH_BOOK_PUBLIC', 250, 200, 0.5, 0.05)

    BTN_EDIT('BTN_BOOK_PRICE', '가격', 'orange', '8', '1', 170, 240)
    BLANK('SEARCH_BOOK_PRICE', 250, 240, 0.5, 0.05)

    BTN_EDIT('BTN_BOOK_LINK', 'URL', 'orange', '8', '1', 170, 280)
    BLANK('SEARCH_BOOK_LINK', 250, 280, 0.5, 0.05)
    
    BTN_EDIT('BTN_BOOK_DESCRIPTION', '도서 설명', 'orange', '8', '1', 170, 320)
    BLANK('SEARCH_BOOK_DESCRIPTION', 250, 320, 0.5, 0.05)

    BTN_EDIT('BTN_IMAGE_FIND', '사진 찾기', 'orange', '8', '1', 170, 360)
    BLANK('SEARCH_IMAGE_FIND', 250, 360, 0.5, 0.05)
    
    BTN_EDIT('BTN_FIND', '찾아 보기', 'gray', '8', '1', 620, 360)

    BTN_EDIT('BTN_apply', '적용', 'gray', '7', '1', 200, 420)
    
    BTN_EDIT('BTN_OK', '확인', 'gray', '7', '1', 300, 420)

    BTN_EDIT('BTN_CANCEL', '취소', 'gray', '7', '1', 400, 420)


# ㉰의 화면
def BOOK_DELETE():
    DLT = Tk()
    DLT.title("도서 삭제")
    DLT.geometry("700x500")
    label1 = Label(DLT, text = '도서 삭제', bg = 'gray',width = 700, height = 5)
    DLT.configure(background = 'sky blue')

    label2 = Label(DLT, text='삭제할 도서 검색하기 :',fg='black' ,
                   font=('맑은 고딕',10), width=20,height=1)

    BTN_CANCEL = Button(DLT, text='뒤로가기', bg='orange', width='8', height='2')
    
    BOOK_SEARCH_LABEL = Entry(DLT)
    BOOK_SEARCH_LABEL.insert(END, "도서명 혹은 저자를 입력하세요")
    BOOK_SEARCH_LABEL.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)

    BOOK_SEARCH_BTN = Button(DLT, text = '검색', fg='white' ,bg='black')
    BOOK_SEARCH_BTN.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)

    BOOK_SELECT_BOX = Listbox(DLT, width=70, height = 8, highlightcolor = 'blue') # 선택시 파란색으로 표시
    BOOK_SELECT_BOX.place(relx=0.25,rely=0.4,relwidth=0.6,relheight = 0.5)
    BOOK_SELECT_BOX.insert(0,"도서명 : 불멸의 이순신 / 저자 : 윤도운")
    BOOK_SELECT_BOX.insert(1,"도서명 : 동물농장 / 저자 : 조지 오웰")
    BOOK_SELECT_BOX.insert(2,"도서명 : 1984 / 저자 : 조지 오웰")
    BOOK_SELECT_BTN = Button(DLT, text = '선택하기', fg='white', bg = 'black')
    BOOK_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)

    BTN_CANCEL.pack()
    BTN_CANCEL.place(x=5,y=25)
    label1.pack()
    label2.pack()
    label2.place(x=5, y=155)
    


  
# 1번째 화면
window = Tk()
window.title("도서관리 프로그램")
window.geometry("700x500")

label1 = Label(window, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)
window.configure(background = 'sky blue')

#도서관리 누르면 2번째 창으로 넘어감
BTN_BOOK = Button(window, text='도서관리',fg="black", bg="orange", width='20',
                  height='10', command=BOOK_MANAGEMENT)
BTN_MEMBER = Button(window, text='회원관리',fg="black", bg="orange", width='20',
                    height='10')

label1.pack()


BTN_BOOK.pack()
BTN_BOOK.place(x=150,y=150)

BTN_MEMBER.pack()
BTN_MEMBER.place(x=450,y=150)

window.mainloop()
