count=int(input("enter the no:of words"))
li=[]
if count>0:
    for i in range(0,count):
        a=input("enter the elements")
        l=li.append(a)

y=list(map(lambda z:z.upper(),li))
print(y)
