a=[]
v=[]
for i in range(5):
    b=int(input("enter the nos:"))
    a.append(b)
# a=set(a)
# print(a)
for i in a:
    if i not in v:
        v.append(i)
print(v)    



        


