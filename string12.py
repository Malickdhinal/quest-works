a1=str(input("enter the first string"))
a2=str(input("enter the second string"))
n1=len(a1)
n2=len(a2)
b1=a1[0]+a1[n1//2]+a1[n1-1]+a2[0]+a2[n2//2]+a2[n2-1]

print(b1)