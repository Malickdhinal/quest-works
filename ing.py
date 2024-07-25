a=input("enter the string")
b=len(a)
if b>=3:
    if a.endswith("ing"):
        print(a+"ly")
    else:
        print(a+"ing")
else:
    print(a)