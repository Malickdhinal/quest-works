num1=int(input("enter first num:"))
num2=int(input("enter second num:"))
class Rectangle:
    def __init__(self,len,bre):
        self.a=len
        self.b=bre
    def operation(self):
        self.c=self.a*self.b
    def display(self):
        print("area of rectangle =",self.c)
ab=Rectangle(num1,num2)
ab.operation()
ab.display()
    