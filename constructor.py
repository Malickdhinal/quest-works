# class Laptop:
#     def __init__(self,name):
#         print("always executed",name)
#     processor="intel"
#     def boot(self):
#         print("booting")
# hp=Laptop("akhil")
# print(hp.processor)
# hp.boot()
class Addition:
    def __init__(self,num1,num2):
        self.a=num1
        self.b=num2
    
    def operation(self):
        self.c=self.a+self.b
    def display(self):
        print(self.c)
hp=Addition(5,4)
hp.operation()
hp.display()

