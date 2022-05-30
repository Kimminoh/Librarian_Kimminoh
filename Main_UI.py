from tkinter import *

# 도서관리 UI
def book_manager():
    window_book_manager=Tk()
    
    book_reg_edit_btn=Button(window_book_manager,text="도서 등록/수정",command=book_reg_edit)
    book_search_lend_btn=Button(window_book_manager,text="도서 조회/대출",command=book_search__lend)
    book_delete_btn=Button(window_book_manager,text="도서 삭제",command=book_delete)

    book_reg_edit_btn.pack()
    book_search_lend_btn.pack()
    book_delete_btn.pack()
    
    window_book_manager.mainloop()

# 도서 등록/수정 UI

def book_reg_edit():
    window_book_reg_edit_main=Tk()

    #도서 신규등록 버튼 
    book_new_reg_btn = Button(window_book_reg_edit_main,text="도서 신규등록",command=book_new_reg)
    book_new_reg_btn.pack()

    


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
window=Tk()

book_manager_btn=Button(window,text="도서관리",command=book_manager)
user_manager_btn=Button(window,text="회원관리",command=user_manager)

book_manager_btn.pack()
user_manager_btn.pack()






window.mainloop()
