a=input("enter the string")
c=a[0]
b=len(a)
for i in range(0,b):
    if i==a[0]:
        continue
    elif i==c:
        x=a.replace(c,"&")
        print(c)
        print(x)



         

