num1=(input("enter name:"))
num2=int(input("enter age:"))
num3=int(input("enter mark:"))
class Marks:
    def __init__(self,name,age,mark):
        # self.a=name
        # self.b=age
        self.c=mark
    def operation(self):
        if self.c>40:
            print("true")
        else:
            print("false")

ab=Marks(num1,num2,num3)
ab.operation()

    