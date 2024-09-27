from tkinter import *
from tkinter import messagebox
import re
login=Tk()
login.title("Login page")
login.geometry("330x360")
# -----xxxxxxxxxxxxxxxxxxxxx------------
def loginm():
    name1=en1.get()
    if name1!="":
        cap=re.search(r"\d",name1)
        if cap==True:
            messagebox.showerror("Error","No digits allowded")
        else:
            pass

    else :
        messagebox.showerror("Error","Fill the name first")
    phno=en2.get()
    if phno!="":
        cap=re.search("\D",phno)
        if cap==True:
            messagebox.showerror("Error"," digits only")
        else:
            pass
            

    else :
        messagebox.showerror("Error","Fill the phno")
    email=en3.get()
    if email!="":
        cap=re.search("@gmail.com$",email)
        if cap:
            pass
        else:
            messagebox.showerror("Error","complete the email")
    else :
        messagebox.showerror("Error","Fill the email column")
    password=en4.get()
    if password!="":
        cap=r"(^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%?&])[A-Za-z\d@$!%*?&]{8,20}$)"
        if cap:
            pass
        else:
            messagebox.showerror("Error","it should contain a capital letter ,small letter,charector,number")
    else :
        messagebox.showerror("Error","Fill the password column")
    repassword=en5.get()
    if repassword!="":
        if repassword!=password:
            messagebox.showerror("error","it should be same as the above password")
    else :
        messagebox.showerror("Error","Fill the repeat password column")
    
    
     



# ----------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxx------------------------------
frame=Frame(login,bg="white")
frame.place(relwidth=1,relheight=1)
l11=Label(login,text="Login Page",width=10,fg="black",bg="white",font=('Times New Roman',15,'bold'))
l11.place(x=110,y=10)
l1=Label(login,text="Name : ",width=7,fg="black",bg="white")
l1.place(x=10,y=80)
en1=Entry(login,width=20)
en1.place(x=150,y=80)
l2=Label(login,text="Phno : ",width=6,fg="black",bg="white")
l2.place(x=10,y=120)
en2=Entry(login,width=20)
en2.place(x=150,y=120)
l3=Label(login,text="Email : ",width=7,fg="black",bg="white")
l3.place(x=10,y=160)
en3=Entry(login,width=20)
en3.place(x=150,y=160)
l4=Label(login,text="Set password : ",width=13,fg="black",bg="white")
l4.place(x=10,y=200)
en4=Entry(login,width=20,show="*")
en4.place(x=150,y=200)
l5=Label(login,text="Confirm password : ",width=17,fg="black",bg="white")
l5.place(x=10,y=240)
en5=Entry(login,width=20,show="*")
en5.place(x=150,y=240)
# b1=Button(login,text="Login",bg="#00C2E6",command=loginm())
btn=Button(login,text="Submit",command=loginm)

btn.place(x=150,y=300)















login.mainloop()