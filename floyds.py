rows=int(input("enter the no:rows"))
a=1
for i in range(rows):
    for j in range(i+1):
        print(a,end=' ')
        a+=1
    print()