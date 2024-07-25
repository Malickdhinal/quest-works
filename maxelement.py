from functools import reduce
y=[1,2,3,4,5]
x=reduce(lambda a,b:a if a>b else b,y)
print(x)