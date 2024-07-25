a=[]
for i in range(5):
    b=int(input("enter the nos:"))
    a.append(b)
for i in a:
    if i%5==0:
        print("%i is div by 5"%i)