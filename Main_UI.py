from email.mime import image
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# 도서관리 UI
def book_manager():
    window_book_manager=Tk()
    window_book_manager.title("도서관리")
    window_book_manager.geometry("700x500")
    label1 = Label(window_book_manager, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)
    window_book_manager.configure(background = 'sky blue')

    book_reg_edit_btn=Button(window_book_manager,text="도서 등록/수정", bg='orange', width='18',
                          height='8',command=book_reg_edit)
    book_search_lend_btn=Button(window_book_manager,text="도서 조회/대출", bg='orange', width='18',
                          height='8',command=book_search__lend)
    book_delete_btn=Button(window_book_manager,text="도서 삭제", bg='orange', width='18',
                          height='8',command=book_delete)

    label1.pack()
    book_reg_edit_btn.pack()
    book_search_lend_btn.pack()
    book_delete_btn.pack()

    book_reg_edit_btn.place(x=100,y=170)
    book_search_lend_btn.place(x=300,y=170)
    book_delete_btn.place(x=500,y=170)

    
    window_book_manager.mainloop()

# 도서 등록/수정 UI

def book_reg_edit():
    window_book_reg_edit_main=Tk()
    window_book_reg_edit_main.title("도서 등록/수정")
    window_book_reg_edit_main.geometry("700x500")
    label1 = Label(window_book_reg_edit_main, text = '도서 등록/수정', bg = 'gray', width = 700, height = 5)
    window_book_reg_edit_main.configure(background = 'sky blue')

    #도서 신규등록 버튼 
    book_new_reg_btn = Button(window_book_reg_edit_main,text="도서 신규등록", bg='orange', width='15', height='2',command=book_new_reg)
    book_new_reg_btn.pack()
    book_new_reg_btn.place(x=105,y=105)

    label2 = Label(window_book_reg_edit_main, text='수정할 도서 검색하기',fg='black' ,font=("궁서체",10), width=20,height=1)
    label2.pack()
    label2.place(x=5,y=205)

    window_book_reg_edit_main.mainloop()



# window_book_reg_edit_main 윈도우에 도서명 혹은 저자를 입력하는 칸을 만들기
    

# window_book_reg_edit_main 윈도우에 BOOK 데이터베이스에서 도서명과 저자명을 보여주는 리스트 만들기





# 선택하기 버튼 과 해당 목록을 더블클릭 시, 도서 수정하기로 연결
def book_edit():
    window_book_edit=Tk()

    #loc속성으로 수정하는 코드 작성
    
    



    window_book_edit.mainloop()



# 도서 신규등록 버튼 눌렀을 때 나오는 UI
def book_new_reg():
    window_book_new_reg=Tk()

    # 정보 입력하는 창, 값을 input_정보 변수에 담음 (현재 디폴트 : 문자열)
    input_isbn= Entry(window_book_new_reg)
    input_bookname=Entry(window_book_new_reg)
    input_publish=Entry(window_book_new_reg)
    input_author=Entry(window_book_new_reg)
    input_price=Entry(window_book_new_reg)
    input_url=Entry(window_book_new_reg)
    input_description=Entry(window_book_new_reg)

    input_isbn.pack()
    input_bookname.pack()
    input_publish.pack()
    input_author.pack()
    input_price.pack()
    input_url.pack()
    input_description.pack()
    
    photo=PhotoImage()
    plabel=Label(window_book_new_reg,image=photo)
    plabel.pack()

    image_btn=Button(window_book_new_reg, text="사진찾기",command=open_button)
    image_btn.pack()


#함수 안에 함수 선언(오픈 버튼 누를 시)
def open_button():
    filename=filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
        ('png files', '*.png'), ('jpg files', '*.jpg'), ('all files', '*.*')))
    photo=PhotoImage(file=filename)
    

    label_reg=Label(window,text=window.filename)
    label_reg.pack()


        

    
    #메인 루프는 어떻게 할 것인가?


#----------------------------------------------------------------------


def book_search__lend():
    window_book_search_lend_main=Tk()




    window_book_search_lend_main.mainloop()


def book_delete():
    window_book_delete_main=Tk()



    window_book_delete_main.mainloop()




#------------------------------------------------------------------------

# 회원관리 UI
def user_manager():
    window_user_manager=Tk()

    user_reg_btn=Button(window_user_manager,text="회원등록",command=user_reg)
    user_search_edit_quit_btn=Button(window_user_manager,text="회원검색/수정/탈퇴",command=user_search_edit_quit)
    user_reg_btn.pack()
    user_search_edit_quit_btn.pack()




    window_user_manager.mainloop()


def user_reg():
    window_user_reg=Tk()



    window_user_reg.mainloop()

def user_search_edit_quit():
    window_user_search_edit_quit=Tk()




    window_user_search_edit_quit.mainloop()




# 메인 UI
window = Tk()
window.title("도서관리 프로그램")
window.geometry("700x500")

label1 = Label(window, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)
window.configure(background = 'sky blue')

book_manager_btn=Button(window,text="도서관리",fg="black", bg="orange", width='20',
                  height='10',command=book_manager)
user_manager_btn=Button(window,text="회원관리",fg="black", bg="orange", width='20',
                    height='10',command=user_manager)

label1.pack()
book_manager_btn.pack()
book_manager_btn.place(x=150,y=150)

user_manager_btn.pack()
user_manager_btn.place(x=450,y=150)





window.mainloop()

