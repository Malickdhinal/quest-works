num1=int(input("enter radius:"))

class Circle:
    def __init__(self,len):
        self.a=len
        
    def operation(self):
        self.c=3.14*self.a*self.a
    def display(self):
        print("area of circle =",self.c)
ab=Circle(num1)
ab.operation()
ab.display()
    