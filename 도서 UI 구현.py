from tkinter import*


def func_exit():
    window.quit()
    #window.destroy()

# 2번째 화면
def BOOK_MANAGEMENT():
    #공통부분 ↓---------------------------------------------------------------------
    window = Tk()
    window.title("도서관리")
    window.geometry("700x500")
    label1 = Label(window, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)
    window.configure(background = 'sky blue')
    #공통부분 ↑---------------------------------------------------------------------
    
    BTN_REG_EDIT = Button(window, text='도서\n등록/수정', bg='orange', width='18',
                          height='8', command = BOOK_MANAGEMENT_FIRST)
    BTN_SEARCH_RENT = Button(window, text='도서\n조회/대출', bg='orange', width='18',
                          height='8')
    BTN_DELETE = Button(window, text='도서삭제', bg='orange', width='18',
                          height='8')

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

# 도서 등록/수정 화면
def BOOK_MANAGEMENT_FIRST():
    #공통부분 ↓
    window = Tk()
    window.title("도서 등록/수정")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 등록/수정', bg = 'gray',width = 700, height = 5)
    window.configure(background = 'sky blue')
    #공통부분 ↑


    BTN_CANCEL = Button(window, text='뒤로가기', bg='orange'
    , width='8', height='2',command=window.destroy)
    BTN_NEW_REG = Button(window, text='도서 신규 등록'
    , bg='orange', width='15', height='2')

    label2 = Label(window, text='수정할 도서 검색하기 :',fg='black' ,
                   font=('맑은 고딕',10), width=20,height=1) 

    USER_SEARCH_LABEL = Entry(window)
    USER_SEARCH_LABEL.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)
    USER_SEARCH_LABEL.insert(END, "도서명 혹은 저자를 입력하세요")
    
    USER_SEARCH_BTN = Button(window, text = '검색', fg='white' ,bg='black')
    USER_SEARCH_BTN.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)

    USER_SELECT_BOX = Listbox(window, width=70, height = 8)
    USER_SELECT_BOX.place(relx=0.05,rely=0.4,relwidth=0.8,relheight = 0.5)
    USER_SELECT_BOX.insert(0,"윤도운 : 010-1234-5678")
    USER_SELECT_BOX.insert(1,"김민오 : 010-1234-5678")
    USER_SELECT_BOX.insert(2,"남강민 : 010-1234-5678")
    USER_SELECT_BTN = Button(window, text = '선택하기', fg='white', bg = 'black')
    USER_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)
    
    
    label1.pack()

    label2.pack()
    label2.place(x=5, y=155)
    
    BTN_CANCEL.pack()
    BTN_CANCEL.place(x=5,y=25)

    BTN_NEW_REG.pack()
    BTN_NEW_REG.place(x=5,y=90)
    
    
    



    
# 첫번째 화면(메인화면)
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
                    height='10', command=quit)

label1.pack()


BTN_BOOK.pack()
BTN_BOOK.place(x=150,y=150)

BTN_MEMBER.pack()
BTN_MEMBER.place(x=450,y=150)

window.mainloop()
