from tkinter import *
#추가 주석 : 수정 테스트!


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
    
    # 값 입력하는 UI만들기

    
    window_book_new_reg.mainloop()



def book_search__lend():
    window_book_search_lend_main=Tk()




    window_book_search_lend_main.mainloop()


def book_delete():
    window_book_delete_main=Tk()



    window_book_delete_main.mainloop()
