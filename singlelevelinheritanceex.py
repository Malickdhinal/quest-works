# class A:
#     fruit="apple"
#     def normal(self):
#         print("normal method")
# class B(A):
#     pass
# obj=B()
# print(obj.fruit)
# obj.normal()
# class Student:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#         print("constructor method")
#     def display(self):
#         print("name is",self.n,"and age is",self.a)
# class Second(Student):
#     def normal(self):
#         print("normal method")
# obj=Second("akhil",19)
# obj.normal()
# obj.display()

# class A:
#     def __init__(self,name,age):
#         print("constructor method",name,age)
# class B(A):
#     def __init__(self,name,age):
#         print("second class method")            
#         super().__init__(name,age)
#         A.__init__(self,name,age)
# obj=B("ammu",78)

# class A:
#     def first(self):
#         print("first class method")
# class B(A):
#     def second(self):
#         print("second class method")
# class C(B):
#     def third(self):
#         print("third class method")        
# class D(C):
#     def fourth(self):
#         print("fourth class method")
# obj=D()
# obj.fourth()
# obj.third()
# obj.second()
# obj.first()

# class Parent1:
#     def first(self):
#         print("first class method")
# class Parent2:
#     def second(self):
#         print("second class method")    
# class Child(Parent1,Parent2):
#     def third(self):
#         print("third class method")
# obj=Child()

# class Person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#     def display(self):
#         print(self.n,self.a)
# class Student(Person):
#     def __init__(self,name,age,studentid):
#         self.st=studentid
#         self.n=name
#         self.a=age
#         print(name,age,studentid)
# obj=Student("akhil",78,67)
# obj.display()

# class Shape:
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,len,bre):
#         self.l=len
#         self.b=bre
#         self.a=self.l*self.b
#     def display(self):
#         print(self.a)
# obj=Rectangle(5,4)
# obj.display()

# class Employee:
#     def __init__(self,name,salary):
#         self.n=name
#         self.s=salary
#     def display(self):
#         print(self.n,self.s)
# class Manager(Employee):
#     def __init__(self,name,salary,department):
#         super().__init__(name,salary)
#         self.d=department
#         print(self.d)
# obj=Manager("akhil",100000,"bsc")
# obj.display()



# class Animal:
#     def move(self):
#         print("animal")
# class Bird(Animal):
#     def fly(self):
#         print("bird")
# obj=Bird()
# obj.fly()
# obj.move()

# class Book:
#     def __init__(self,name,author):
#         self.n=name
#         self.a=author
#     def display1(self):
#         print(self.n,self.a)
# class Ebook(Book):
#     def __init__(self,name,author,size):
#         super().__init__(name,author)
#         self.s=size
#     def display(self):
#         super().display1()
#         print(self.s)
# obj=Ebook("mal","hal",12)
# obj.display1()
# obj.display()

# class Person:
#     def __init__(self,name,age):
#         self.n=name
#         self.a=age
#     def display1(self):
#         print(self.n,self.a)
# class Employee(Person):
#     def __init__(self,name,age,id):
#         super().__init__(name,age)
#         self.i=id
#     def display2(self):
#         super().display1()
#         print(self.i)
# class Manager(Employee):
#     def __init__(self,name,age,id,dept):
#         super().__init__(name,age,id)
#         self.d=dept
#     def display3(self):
#         super().display2()
#         print(self.d)
# obj=Manager("mal",12,123,"bsc")
# obj.display3()
# # obj.display1()

# class Vehicle:
#     def __init__(self,make,model,year):
#         self.m=make
#         self.mo=model
#         self.y=year
#     def display1(self):
#         print(self.m,self.mo,self.y)
# class Car(Vehicle):
#     def __init__(self,make,model,year,ndoor):
#         super().__init__(make,model,year)
#         self.n=ndoor
#     def display2(self):
#         super().display1()
#         print(self.n)
# class Electriccar(Car):
#     def __init__(self,make,model,year,ndoor,battery):
#         super().__init__(make,model,year,ndoor)
#         self.b=battery
#     def display3(self):
#         super().display2()
#         print(self.b)
# obj=Electriccar("mal",12,123,"bsc",123)
# obj.display3()
# # obj.display1()


