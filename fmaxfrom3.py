a=int(input("enter the first no:"))
b=int(input("enter the second no:"))
c=int(input("enter the third no:"))
l=[a,b,c]
from functools import reduce
# def greater(y):
x=reduce(lambda a,b:a if a>b else b,l)
print(x)
# greater(l)