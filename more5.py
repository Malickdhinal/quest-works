a=[]
for i in range(5):
    b=input("enter the name of fruits")
    a.append(b)
x=[i for i in a if len(i)>5]
print(x)