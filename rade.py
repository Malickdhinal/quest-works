a=int(input("enter the percentae"))

if a<=30:
    print("D")
elif a>=31 or a<=40:
    print("c")    
elif a>=41 or a<=50:
    print("c+")  
elif a>=51 or a<=60:
    print("b")  
elif a>=61 or a<=70:
    print("b+") 
elif a>=71 or a<=80:
    print("a")  
elif a>=81 or a<=90:
    print("a+")  
elif a>=91 or a<=100:
    print("o") 
else:
    print("invalid output")
