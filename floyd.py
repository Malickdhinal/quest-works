rows=int(input("enter rows"))

for i in range(rows):
    for j in range(rows-1):
        print(" ",end=" ")
    for k in range(i+1):
        print()
    print()