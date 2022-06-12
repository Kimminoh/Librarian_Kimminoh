import USER2_UI
import USER4_UI
import pandas as pd
from PIL import Image,ImageTk
import csv
from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import *
def USER_1():
    def create_button(button_name,color,text,width,x,y):                   # 버튼 배치 함수
        button_name = Button(mainwindow,bg=color,text=text,width=width)
        button_name.place(x=x, y = y)
        return button_name

    def create_label(label_name,x,y):                                       # 라벨 배치 함수
        label_name.place(x=x, y = y)

    def create_entry(entry_name,text,font,width,x,y):                             # 엔트리 배치 함수
        entry_name = Entry(mainwindow,font=font,width=width)
        entry_name.insert(0,text)
        entry_name.place(x=x, y = y)
        return entry_name


    def user_search():
        sub_label = Label(mainwindow, text ="회원 검색",font=("맑은 고딕",9),bg='gray',height=3)
        user_list = Listbox(mainwindow,width=65,height=10,font=("맑은 고딕",12))

        keyword_entry = create_entry('keyword_entry','이름 혹은 전화번호를 입력하세요.',("맑은 고딕",12),40,120,80)
        treeview = ttk.Treeview(mainwindow,column=['이름','전화번호','생년월일','성별','도서대여권수'],displaycolumns=['이름','전화번호','생년월일','성별','도서대여권수'])
        
        phone=None
        
        csv_list = []
        f = open('csv/user.csv','r',encoding='utf-8')
        reader = csv.reader(f)

        def user_search ():   
            df_user = pd.read_csv('csv/user.csv', encoding='utf-8')
            df_user = df_user.set_index(df_user['USER_PHONE'])
            
            for phone in df_user.index.tolist():
                keyword = keyword_entry.get()
                
                search1 = df_user["USER_NAME"].str.contains(keyword)
                search2 = df_user['USER_PHONE'].str.contains(keyword)

                result = df_user.loc[search1 | search2]
                
                for item in treeview.get_children():
                    treeview.delete(item)

                for phone in result.index.tolist():
                    user_name = result.loc[phone, "USER_NAME"]
                    user_birth = result.loc[phone, "USER_BIRTH"]
                    user_sex = result.loc[phone, "USER_SEX"]
                    user_rent_cnt = result.loc[phone, "USER_RENT_CNT"]
                    
                    result_info = (user_name, phone, user_birth, user_sex,user_rent_cnt)
                    treeview.insert('','end',values=result_info,iid=phone)

        
        def button_item():
            chioce_info = treeview.focus()
            getvalue = treeview.item(chioce_info).get('values')
            phone=getvalue[1]
            USER2_UI.user_2(phone)

        def click_item(event):
            chioce_info = treeview.focus()
            getvalue = treeview.item(chioce_info).get('values')
            phone=getvalue[1]
            USER2_UI.user_2(phone)
        
        def click_item2(event):
            chioce_info = treeview.focus()
            getvalue = treeview.item(chioce_info).get('values')
            phone=getvalue[1]
            USER4_UI.user_2(phone)
            

        def button_item2():
            chioce_info = treeview.focus()
            getvalue = treeview.item(chioce_info).get('values')
            phone=getvalue[1]
            USER4_UI.user_2(phone)


        for row in reader:
            csv_list.append(row)
        f.close()  
        
        for a,b,c,d,e,f,g,h in csv_list[1:]:
            treeview.insert('','end',values=[b,a,c,d,h],iid=a)
        

        #csv_list[a]

        search_button = Button(mainwindow,bg='gray',text='검색',width=9,command=user_search)
        search_button.place(x=560, y = 80)
        update_button = Button(mainwindow,bg='gray',text='수정',width=9,command=button_item)
        update_button.place(x=560, y = 120)
        info_button = Button(mainwindow,bg='gray',text='상세정보',width=9,command=button_item2)
        info_button.place(x=560, y = 160)
        


        treeview.column("이름",width=70,anchor="center",stretch=True)
        treeview.heading("이름",text="이름",anchor="center")
        treeview.column("전화번호",width=150,anchor="center",stretch=True)
        treeview.heading("전화번호",text="전화번호",anchor="center")
        treeview.column("성별",width=50,anchor="center",stretch=True)
        treeview.heading("성별",text="성별",anchor="center")
        treeview.column("생년월일",width=100,anchor="center",stretch=True)
        treeview.heading("생년월일",text="생년월일",anchor="center")
        treeview.column("도서대여권수",width=150,anchor="center",stretch=True)
        treeview.heading("도서대여권수",text="도서대여권수",anchor="center")
        treeview["show"] = "headings"

        treeview.bind('<Double-Button-1>',click_item2)
        treeview.place(x=50,y=220)
        sub_label.pack(fill=X)

    mainwindow = Tk()
    global a
    a = mainwindow
    mainwindow.title("회원 검색/수정/탈퇴")
    mainwindow.geometry("700x500")
    user_search()
    mainwindow.resizable(width=FALSE, height=FALSE)
    mainwindow.mainloop()
def exit_search():
    a.destroy()
