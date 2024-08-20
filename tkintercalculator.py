from tkinter import *
app=Tk()
app.title("Calculator")
app.geometry("220x250")
# -----xxxxxxxxxxxxxxxxxxxxx------------
equation=""
def show(value):
    global equation
    if len(equation)==0:
        if value=="0" or value in "+-*/":
            display.config(text=value)
        else:
            equation+=value
            display.config(text=equation)
    elif equation[-1] in "+-*/" and value in "+-*/":
        temp=equation[:-1]
        temp+=value
        equation=temp
        display.config(text=equation)
    else:    
        equation+=value
        display.config(text=equation)
def clear(value):
    global equation
    equation=""
    display.config(text=equation)
def backspace(value):
    global equation
    temp=equation[:-1]
    equation=temp
    display.config(text=equation)
def operation():
    global equation
    result=""
    result=str(eval(equation))
    equation=result
    display.config(text=equation)
# ----------------xxxxxxxxxxxxxxxxxxxxxxxxxxxxx------------------------------
frame=Frame(app,bg="black")
frame.place(relwidth=1,relheight=1)
display=Label(app,width=24,bd=3,bg="black",fg="white",justify="center",relief="ridge",anchor="e")
display.place(x=10,y=10)
bksp=Button(app,command=lambda:backspace("bksp"),text="Bksp",width=8,bd=3,bg="#154c8c",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
bksp.place(x=110,y=40)
ce=Button(app,command=lambda:clear("cl"),text="CE",width=8,bd=3,bg="#A31111",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
ce.place(x=10,y=40)
seven=Button(app,command=lambda:show("7"),text="7",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
seven.place(x=10,y=80)
eight=Button(app,command=lambda:show("8"),text="8",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
eight.place(x=60,y=80)
nine=Button(app,command=lambda:show("9"),text="9",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
nine.place(x=110,y=80)
divide=Button(app,command=lambda:show("/"),text="/",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
divide.place(x=160,y=80)
four=Button(app,command=lambda:show("4"),text="4",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
four.place(x=10,y=120)
five=Button(app,command=lambda:show("5"),text="5",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
five.place(x=60,y=120)
six=Button(app,command=lambda:show("6"),text="6",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
six.place(x=110,y=120)
multiply=Button(app,command=lambda:show("*"),text="X",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
multiply.place(x=160,y=120)
one=Button(app,command=lambda:show("1"),text="1",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
one.place(x=10,y=160)
two=Button(app,command=lambda:show("2"),text="2",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
two.place(x=60,y=160)
three=Button(app,command=lambda:show("3"),text="3",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
three.place(x=110,y=160)
minus=Button(app,command=lambda:show("-"),text="-",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
minus.place(x=160,y=160)
zero=Button(app,command=lambda:show("0"),text="0",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
zero.place(x=110,y=200)
equal=Button(app,command=lambda:operation(),text="=",width=8,bd=3,bg="#10880B",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
equal.place(x=10,y=200)
plus=Button(app,command=lambda:show("+"),text="+",width=2,bd=3,bg="black",fg="#C0C0C0",activeforeground="black",activebackground="#C0C0C0",highlightcolor="purple",justify="center",relief="ridge")
plus.place(x=160,y=200)















app.mainloop()