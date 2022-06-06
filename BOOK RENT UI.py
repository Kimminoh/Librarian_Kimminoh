from tkinter import *

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
userselectbutton = Button(rent1, text = '선택하기')
userselectbutton.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)

rent1.mainloop()