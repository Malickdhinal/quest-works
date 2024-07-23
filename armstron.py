a=int(input("enter a num"))
i=0
b=0
b=a
while a>0:
    a=a//10
    i+=1
d=0
s=0
while b>0:
    d=b%10
    s=s+d**i
    b=b//10
print(s)

    