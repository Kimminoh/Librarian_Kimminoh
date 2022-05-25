import pandas as pd
from datetime import datetime, timedelta
from tabulate import tabulate

rent_book=pd.read_csv("RENT.csv",encoding="utf-8")
rent_book = pd.read_csv("Book_df.csv",encoding="utf-8")
rent_user = pd.read_csv('USER.csv', encoding='utf-8')

#isbn이 3334564577인 도서가  선택 되었을 때
#isbn으로 회원정보를 찾는다
isbn=3334564577
c_isbn= rent_book[rent_book[:,"BOOK_ISBN"]==isbn]
phone="010-1212-1212"


rent_book.loc[isbn,"BOOK_RENTAL"]=False 
rent_user.loc[phone,"USER_RENT_CNT"]-=1 
rent_book.loc[num,"RYN"]=True


rent_df.to_csv("RENT.csv",index=True,encoding="utf-8")
