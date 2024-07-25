z=[]
s=[]
d=[]
for i in range(2):
    for j in range(2):
        a=int(input("enter the ""noS"))
        
        if len(s)<2:
            s.append(a)
        else:
            d.append(a)
z=s,d
print(z)
