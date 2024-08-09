class Student:
    school="mems"
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
        print("id",self.id,"\nname",self.name,"\nage",self.age)

obj1=Student(1,"sara",10)
obj2=Student(2,"jose",20)
# print(getattr(obj2,"school"))
setattr(obj1,'kevin',30)
# print(obj1."kevin")






# class Myclass:
#     x=10
#     y=20
# obj1=Myclass()
# obj2=Myclass()
# # print(obj2.x)
# # setattr(obj1,"z",100)
# # print(obj1.z)
# # print(getattr(obj1,'y'))
# # print(hasattr(obj1,'x'))
# # print(hasattr(obj1,'h'))
# delattr(obj1,'x')
# print(obj1.x)