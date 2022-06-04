from tkinter import *
from tkinter import messagebox
def rentbutton():
    rentMsgBox = messagebox.askyesno(" ",'"불멸의 이순신"을 대출하시겠습니까? 반납 예정일: 2022-03-11')
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

