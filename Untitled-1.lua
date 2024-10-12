# import mysql.connector
# mydb=mysql.connector.connect(host="localhost",port=3306,user="root",password="")
# crsr=mydb.cursor()
# crsr.execute("create database newdata")
# print("hnfmb")

from tkinter import *
app=Tk()
app.title("Login page")
app.geometry("1000x1000")
lb1=Label(app,text="Registration page",font=('times new roman',15 ,"bold"))
lb1.grid(pady=20,padx=10,row=0,column=1)

d1=Label(app,text="First name:")
d1.grid(pady=3,row=1,column=1)
en1=Entry(app)
en1.grid(pady=3,row=1,column=2)

d2=Label(app,text="Last name:")
d2.grid(pady=3,row=2,column=1)
en2=Entry(app)
en2.grid(pady=3,row=2,column=2)

d3=Label(app,text="Email id:")
d3.grid(pady=3,row=3,column=1)
en3=Entry(app)
en3.grid(pady=3,row=3,column=2)

d4=Label(app,text="Phone no:")
d4.grid(pady=3,row=4,column=1)
en4=Entry(app)
en4.grid(pady=3,row=4,column=2)

d5=Label(app,text="User id:")
d5.grid(pady=3,row=5,column=1)
en5=Entry(app)
en5.grid(pady=3,row=5,column=2)

d6=Label(app,text="Password:")
d6.grid(pady=3,row=6,column=1)
en6=Entry(app)
en6.grid(pady=3,row=6,column=2)

btn=Button(app,text="Submit")
btn.grid(pady=20,row=7,column=2)

d7=Label(app,text="________________________")
d7.grid(pady=3,row=8,column=1)

d8=Label(app,text="To view",font=("times new roman",15,"bold"))
d8.grid(pady=3,row=9,column=1)

d9=Label(app,text="User id:")
d9.grid(pady=3,row=10,column=1)
en9=Entry(app)
en9.grid(pady=3,row=10,column=2)

d10=Label(app,text="Password:")
d10.grid(pady=3,row=11,column=1)
en10=Entry(app)
en10.grid(pady=3,row=11,column=2)

btn1=Button(app,text="Submit")
btn1.grid(pady=20,row=12,column=2)

d11=Label(app,text="First name:")
d11.grid(pady=3,row=10,column=3)
en11=Entry(app)
en11.grid(pady=3,row=10,column=4)

d12=Label(app,text="Last name:")
d12.grid(pady=3,row=11,column=3)
en12=Entry(app)
en12.grid(pady=3,row=11,column=4)

d13=Label(app,text="Email id:")
d13.grid(pady=3,row=12,column=3)
en13=Entry(app)
en13.grid(pady=3,row=12,column=4)

d14=Label(app,text="Phone no:")
d14.grid(pady=3,row=13,column=3)
en14=Entry(app)
en14.grid(pady=3,row=13,column=4)

d15=Label(app,text="User id:")
d15.grid(pady=3,row=14,column=3)
en15=Entry(app)
en15.grid(pady=3,row=14,column=4)

d16=Label(app,text="Password:")
d16.grid(pady=3,row=15,column=3)
en16=Entry(app)
en16.grid(pady=3,row=15,column=4)

app.mainloop()



# crsr.execute("create table login(id int primary key autoincrement,password varchar(50))")
# print("fdg")
# a="insert into login(id,password)values(101,kalllam)"
# crsr.execute(a)
# mydb.commit()