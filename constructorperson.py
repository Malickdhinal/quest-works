# class Person:
#     def __init__(self,name,age):
#         print("hello,my name is",name,"and i am",age,"years old")
# obj1=Person("akhil",13)

class Person:
    def __init__(self,name,age):
        self.nam=name
        self.ag=age
    def display(self):
        print("hello,my name is",self.nam,"and i am",self.ag,"years old")
        
obj1=Person("akhil",13)
obj1.display()