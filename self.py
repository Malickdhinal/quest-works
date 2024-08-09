class Laptop:
    processor="intel"
    def boot(self,name):
        print("booting",name)
hp=Laptop()
print(hp.processor)
hp.boot("I5")
lenovo=Laptop()
lenovo.boot("")