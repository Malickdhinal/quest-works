b=[]
d=[]
z=[]
for i in range(4):
    a=input("list1")
    b.append(a)
for j in range(4):
    c=input("list2")
    d.append(c)
for i in b:
    for j in d:
        if i==j:
            z.append(i)
print(z)