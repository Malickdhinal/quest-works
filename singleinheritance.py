class A:
    fruit="apple"
    def normal(self):
        print("normal method")
class B(A):
    animal="lion"
    def hello(self):
        print("welcome")
obj1=B()
print(obj1.animal)
obj1.hello()
obj1.normal()
print(obj1.fruit)