from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText 
from tkinter.ttk import Combobox,Progressbar
app=Tk()
app.title("registration page")
app.geometry("500x500")
lb1=Label(app,text="First Name : ")
lb1.grid(pady=5,row=0,column=0)
en1=Entry(app)
en1.grid(row=0,column=1)
lb2=Label(app,text="Second Name : ")
lb2.grid(pady=5,row=1,column=0)
en2=Entry(app)
en2.grid(row=1,column=1)
lb3=Label(app,text="Age : ")
lb3.grid(pady=5,row=2,column=0)
s=IntVar()
s.set(1)
sp=Spinbox(app,from_=1,to=50,textvariable=s,width=18)
sp.grid(pady=5,row=2,column=1)
lb4=Label(app,text="Email : ")
lb4.grid(pady=5,row=3,column=0)
en4=Entry(app)
en4.grid(pady=5,row=3,column=1)
lb5=Label(app,text="Place : ")
lb5.grid(pady=5,row=4,column=0)
cm=Combobox(app,width=18)
cm['values']=["Kozhikode","Malapuram","Wayanad","Idukki","Palakkad"]
cm.current(1)
cm.grid(pady=5,row=4,column=1)
lb6=Label(app,text="College : ")
lb6.grid(pady=5,row=5,column=0)
lst=Combobox(app,width=18)
lst['values']=["Peekay cics college","MAMO college","Christian college","JDT college","Sahal college"]
lst.current(1)
lst.grid(pady=5,row=5,column=1)
lb7=Label(app,text="Gender : ")
lb7.grid(pady=5,row=6,column=0)
first=IntVar()
rb1=Radiobutton(app,text="Male",variable=first,value=1)
rb1.grid(pady=5,row=6,column=1)
rb2=Radiobutton(app,text="Female",variable=first,value=2)
rb2.grid(pady=5,row=6,column=2)
lb8=Label(app,text="Language : ")
lb8.grid(pady=5,row=7,column=0)
chb1=Checkbutton(app,text="Hindi")
chb1.grid(pady=5,row=7,column=1)
chb2=Checkbutton(app,text="Malayalam")
chb2.grid(pady=5,row=7,column=2)
chb3=Checkbutton(app,text="English")
chb3.grid(pady=5,row=7,column=3)
lb9=Label(app,text="Phone : ")
lb9.grid(pady=5,row=8,column=0)
en9=Entry(app)
en9.grid(pady=5,row=8,column=1)
pr=Progressbar(app,length=300)
pr['value']=50
pr.grid(row=9,column=1)

def ok():
    messagebox.showinfo("Information","Login Succesful")
btn=Button(app,text="Submit",command=ok)
btn.grid(pady=20,row=10,column=1)



menu1=Menu(app)
filemenu=Menu(menu1,tearoff=False)
menu1.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="New file")
filemenu.add_command(label="New text file")
filemenu.add_command(label="New window")
filemenu.add_separator()
filemenu.add_command(label="Open file")
filemenu.add_command(label="Open folder")
filemenu.add_command(label="Share")
filemenu.add_command(label="Exit",command=app.quit)
editmenu=Menu(menu1,tearoff=False)
menu1.add_cascade(label="Edit",menu=editmenu)
editmenu.add_command(label="Redo")
editmenu.add_command(label="Undo")


app.configure(menu=menu1)

app.mainloop()