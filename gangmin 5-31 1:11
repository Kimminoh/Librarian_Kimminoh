from tkinter import*

#def func_exit():
#    window.quit()
#    window.destroy()
  
# 검색 누를시 command
# def search():

    
# 1번째 화면
rent = Tk()
rent.title("도서 조회/대출")
rent.geometry("700x500")

rentlabel1 = Label(rent, text = '도서 조회/대출', bg = 'gray', width = 700, height = 4)
rent.configure(background = 'sky blue')
rentlabel1.pack()

#메인메뉴 누르면 메인메뉴로 넘어감

#
sbatext = '도서명 혹은 저자를 입력하세요'
sbaentry = Entry(rent,textvariable=sbatext) # Entry() 는 입력창 명령어
sbaentry.place(relx=0.1,rely=0.2,relwidth=0.7,relheight=0.05)
# relx는 x좌표 배치 비율, rely는 y좌표 배치 비율, relwidht는 위젯의 너비 비율, relheight는 위젯의 높이 비율

sbabutton = Button(rent, text = "검색")
sbabutton.place(relx=0.82,rely=0.2,relwidth=0.1,relheight = 0.05)

selectlistbox = Listbox(rent, width=70, height = 8)
selectlistbox.place(relx=0.1,rely=0.28,relwidth=0.7,relheight = 0.26)
selectlistbox.insert(0,"도서명 : 불멸의 이순신 저자 : 윤도운")
selectlistbox.insert(1,"도서명 : 파이썬 저자 : 김민오")
selectlistbox.insert(2,"도서명 : C++ 저자 : 남강민")
selectbutton = Button(rent, text = '선택하기')
selectbutton.place(relx=0.82,rely=0.28,relwidth=0.1,relheight=0.05)

infobutton = Button(rent, text = '도서 상세 정보')
infobutton.place(relx=0.03,rely=0.55,relwidth=0.2,relheight=0.05)

rent.mainloop()
