x=int(input("enter first number:"))
y=int(input("enter second number:"))
w=int(input("1.addition\n2.subtraction\n3.multiplication\n4.devision"))
def add(a,b):
    print(a+b)
# add(x,y)
def sub(a,b):
    print(a-b)
# sub(x,y)
def mult(a,b):
    print(a*b)
# mult(x,y)
def div(a,b):
    print(a/b)
# div(x,y)
if w==1:
    add(x,y)
elif w==2:
    sub(x,y)
if w==3:
    mult(x,y)
elif w==4:
    div(x,y)
else:
    print(".....")


