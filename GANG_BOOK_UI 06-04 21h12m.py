from tkinter import*
import tkinter.messagebox


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
    label2.place(x=5, y=155)
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
        tkinter.messagebox.showinfo("ERROR","해당 도서는 등록 불가능 합니다 !")
    def ERROR_3():   # 예외처리 3
        tkinter.messagebox.showinfo("ERROR","중복 확인 후 도서 등록이 가능합니다 !")
    def ERROR_4():   # 예외처리 4
        tkinter.messagebox.showinfo("ERROR","현재 도서는 이미 등록되어 있는 도서입니다. !")
    def ERROR_5():   # 예외처리 5
        tkinter.messagebox.showinfo("ERROR","해당 부분은 숫자로만 입력이 가능합니다 !")
    def ERROR_6():   # 예외처리 6
        tkinter.messagebox.showinfo("ERROR","해당 정보는 필수정보 입니다. 다시 작성해주세요 !")

    # 사진 미리 보기 창
    # 예외처리 (사진을 등록하지 않았을 때) => 메세지 창 띄우기
    BTN_EDIT('IMAGE_PREVIEW', '사진\n미리보기','orange','15','10',30,80)

    BTN_EDIT('BTN_BOOK_ISBN', 'ISBN', 'orange','8','1', 170, 80)
    BLANK('BTN_BOOK_ISBN',250,80,0.5,0.05)

    # 중복확인시 이벤트 추가함
    OVERLAP_CHECK = Button(window, text='중복확인', bg='orange', width='7', height='1',
                           command = ERROR_1)
    OVERLAP_CHECK.place(x=620, y = 80)    

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
    def ERROR_7():     # 예외처리 7
        tkinter.messagebox.showinfo("ERROR","해당 ISBN으로 수정이 가능합니다 !")
    def ERROR_8():     # 예외처리 8
        tkinter.messagebox.showinfo("ERROR","해당 ISBN으로는 수정하실 수 없습니다 !")
    def ERROR_9():     # 예외처리 9
        tkinter.messagebox.showinfo("ERROR","변경사항을 적용 하여야지 등록/수정이 가능합니다 !")
    def ERROR_10():     # 예외처리 10
        tkinter.messagebox.showinfo("ERROR","해당 부분은 숫자로만 입력이 가능합니다 !")



    BTN_EDIT('IMAGE_PREVIEW', '사진\n미리보기','orange','15','10',30,80)

    BTN_EDIT('BTN_BOOK_ISBN', 'ISBN', 'orange','8','1', 170, 80)
    BLANK('BTN_BOOK_ISBN',250,80,0.5,0.05)

    # 중복확인시 이벤트 발생 추가
    OVERLAP_CHECK = Button(window, text='중복확인', bg='orange', width='7', height='1',
                           command = ERROR_7)
    OVERLAP_CHECK.place(x=620, y = 80)
    
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

    BTN_CANCEL = Button(window, text='취소', bg='gray', width='7', height='1',command=window.destroy )
    BTN_CANCEL.place(x=400, y = 420)
    
# 도서 대출하기 버튼 누를 시 생성되는 회원 선택 창 -강민-(2022-06-04 21:11)--------
def bookrent_selectuser():
     def rentbutton():
     rentMsgBox = tkinter.messagebox.askyesno(" ",'"불멸의 이순신"을 대출하시겠습니까? 반납 예정일: 2022-03-11')
          # '불멸의 이순신' 부분을 BOOK_TITLE, '2022-03-11' 부분을 RENT_RDATE로 format
          # if rentMsgBox == 'yes':  (확인버튼 누를 시)
          # today_D = datetime.now().date() # datetime 모듈이용하여 현재 날짜 저장
          # return_D = today_D+timedelta(weeks=2) # timedelta 함수 이용 2주뒤 날짜 저장
          # sbn = book_df[book_df['BOOK_ISBN'] = isbn] # 도서테이블에서 도서 ISBN 값이 담긴 isbn 변수로 값 저장
          # rent_phone = user_df[user_df['USER_PHONE'] = u_phone] # 회원테이블에서 회원 전화번호값이 담긴 u_phone 변수로 값 저장

          # new_rent = { "RENT_NUM": num,
          #              "RENT_DATE": today_D,
          #              "RENT_RDATE": return_D,
          #              "RENT_RYN": False,
          #              "BOOK_ISBN": 9788970504473# 숫자대신 (rent_isbn) 변수가 들어가야함,
          #              "USER_PHONE": '010-4923-5942'# '숫자'대신 (rent_phone)변수가 들어가야함}
          # rent_df.loc[len(rent_df)] = new_rent
          # book_df.replace('BOOK_RENTAL':num,True) # book 데이터프레임에서 BOOK_RENTAL의 num 번째를 True로 변경
          # user_df.replace('USER_RENT_CNT':num,rent_cnt+1) # (임의)rent_cnt는 user테이블에서 대여권수가 담긴 변수
          # num += 1
     rent1 = Tk()
     rent1.title("도서 대출하기")
     rent1.geometry("700x500")

     rent1label = Label(rent1, text = '도서 대출하기', bg = 'gray', width = 700, height = 4)
     rent1.configure(background = 'sky blue')
     rent1label.pack()

     rent1booklabel = Label(rent1, text = '대출할 도서', bg='orange')
     rent1booklabel.place(relx=0.05,rely=0.2,relwidth=0.15,relheight=0.07)

     booknamelabel = Label(rent1, text = '불멸의 이순신', bg = 'gray') # 텍스트는 선택한 도서 이름
     booknamelabel.place(relx=0.25,rely=0.2,relwidth=0.6,relheight=0.07)

     searchuserlabel = Label(rent1, text = '회원정보 입력', bg = 'orange')
     searchuserlabel.place(relx = 0.05,rely=0.3,relwidth=0.15,relheight=0.07)

     searchuserentry = Entry(rent1)
     searchuserentry.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)
     searchuserbutton = Button(rent1, text = "검색")
     searchuserbutton.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)

     userselectlistbox = Listbox(rent1, width=70, height = 8)
     userselectlistbox.place(relx=0.05,rely=0.4,relwidth=0.8,relheight = 0.5)
     userselectlistbox.insert(0,"윤도운 : 010-1234-5678")
     userselectlistbox.insert(1,"김민오 : 010-1234-5678")
     userselectlistbox.insert(2,"남강민 : 010-1234-5678")
     userselectbutton = Button(rent1, text = '선택하기',command = rentbutton)
     userselectbutton.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)

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

    # 새로 추가한 부분 2022-06-04 15:12 -강민-
    def returnbook():
          returnMsgBox = tkinter.messagebox.askyesno(" ",'"불멸의 이순신"을 반납하시겠습니까? 반납 예정일: 2022-03-11')
          # '불멸의 이순신' 부분을 Book_TITLE, '2022-03-11' 부분을 RENT_RDATE로 format
          # if returnMsgBox == 'yes': # 확인버튼 누를 시
          # idx = rent_df[rent_df['RENT_NUM'] == num].index # RENT_NUM 속성에서 num번째 값을 인덱스로 저장
          # rent_df.drop(idx,inplace=True) # num # 인덱스로 저장한 idx를 참고하여 drop(), 해당 행 삭제
          # book_df.replace('BOOK_RENTAL':num,False) # book 데이터프레임에서 BOOK_RENTAL의 num 번째를 False로 변경
          # user_df.replace('USER_RENT_CNT':num,rent_cnt-1) # (임의)rent_cnt는 user테이블에서 대여권수가 담긴 변수
  
  


    BTN_CANCEL = Button(window, text='뒤로가기', bg='orange',
     width='8', height='2',command=window.destroy)
    BTN_CANCEL.place(x=5,y=25)
    
    BTN_SEARCH = Label(window, text='도서 검색', bg='orange', width='10', height='2')         
    BTN_SEARCH.place(x=30,y=95)
    
    BLANK_SEARCH = Entry(window)
    BLANK_SEARCH.place(x= 150, y= 100,relwidth=0.6,relheight=0.06)

    BOOK_SELECT_BOX = Listbox(window, width=70, height = 8, highlightcolor = 'blue') # 선택시 파란색으로 표시
    BOOK_SELECT_BOX.place(relx=0.04,rely=0.3,relwidth=0.8,relheight = 0.3)
    BOOK_SELECT_BOX.insert(0,"도서명 : 불멸의 이순신 / 저자 : 윤도운")
    BOOK_SELECT_BOX.insert(1,"도서명 : 동물농장 / 저자 : 조지 오웰")
    BOOK_SELECT_BOX.insert(2,"도서명 : 1984 / 저자 : 조지 오웰")

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


    # # 새로 추가한 부분 2022-06-04 15:12 -강민-
    # if (해당 도서 대출여부가 N일경우) :
    #    rentbutton = Button(window, text='대출하기', bg= 'gray', width='10', height='2',command=bookrent_selectuser)
    #    rentbutton.place(x=560, y = 430)

    # else :
    #        returnbutton = Button(window, text='반납하기', bg= 'gray', width='10', height='2',command=returnbook)
    #        returnbutton.place(x=560, y = 430)

    BLANK('example', 120, 380, 0.08, 0.05)
    BLANK('example', 210, 380, 0.08, 0.05)
    BLANK('example', 300, 380, 0.08, 0.05)
    BLANK('example', 390, 380, 0.08, 0.05)
    BLANK('example', 480, 380, 0.08, 0.05)
    BLANK('example', 570, 380, 0.08, 0.05)

    
    
    
    


# ㉰의 화면----------------------------------------------------
def BOOK_DELETE():
    #공통부분 ↓-----------------------------------------------------------------------
    window = Tk()
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
        tkinter.messagebox.askquestion("삭제 완료"," (책 이름)을 삭제되었습니다 !")
    def DLT_ERROR():
        tkinter.messagebox.askquestion("삭제 실패"," 해당 도서를 반납하고 삭제해주세요 !")
    
    BOOK_SEARCH_LABEL = Entry(window)
    BOOK_SEARCH_LABEL.insert(END, "도서명 혹은 저자를 입력하세요")
    BOOK_SEARCH_LABEL.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)

    BOOK_SEARCH_BTN = Button(window, text = '검색', fg='white' ,bg='black')
    BOOK_SEARCH_BTN.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)

    BOOK_SELECT_BOX = Listbox(window, width=70, height = 8, highlightcolor = 'blue') # 선택시 파란색으로 표시
    BOOK_SELECT_BOX.place(relx=0.25,rely=0.4,relwidth=0.6,relheight = 0.5)
    BOOK_SELECT_BOX.insert(0,"도서명 : 불멸의 이순신 / 저자 : 윤도운")
    BOOK_SELECT_BOX.insert(1,"도서명 : 동물농장 / 저자 : 조지 오웰")
    BOOK_SELECT_BOX.insert(2,"도서명 : 1984 / 저자 : 조지 오웰")
    BOOK_SELECT_BTN = Button(window, text = '선택하기', fg='white', bg = 'black', command = DLT_ASK)
    BOOK_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)

    BTN_CANCEL.pack()
    BTN_CANCEL.place(x=5,y=25)
    label1.pack()
    label2.pack()
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
