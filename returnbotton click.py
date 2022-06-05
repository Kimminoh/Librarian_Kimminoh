from tkinter import*
from tkinter import messagebox

def returnbook():
    returnMsgBox = messagebox.askyesno(" ",'"불멸의 이순신"을 반납하시겠습니까? 반납 예정일: 2022-03-11')
          # '불멸의 이순신' 부분을 Book_TITLE, '2022-03-11' 부분을 RENT_RDATE로 format
          # if returnMsgBox == 'yes':  (확인버튼 누를 시)
          # idx = rent_df[rent_df['RENT_NUM'] == num].index # RENT_NUM 속성에서 num번째 값을 인덱스로 저장
          # rent_df.drop(idx,inplace=True) # num # 인덱스로 저장한 idx를 참고하여 drop(), 해당 행 삭제
          # book_df.replace('BOOK_RENTAL':num,False) # book 데이터프레임에서 BOOK_RENTAL의 num 번째를 False로 변경
          # user_df.replace('USER_RENT_CNT':num,rent_cnt-1) # (임의)rent_cnt는 user테이블에서 대여권수가 담긴 변수
          
