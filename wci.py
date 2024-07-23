v=float(input("enter the wind speed in miles/hour"))
t=float(input("enter the temparature in farenheit"))
if(0<=v<=4):
    print("WCI=",t)
elif(v>=45):
    print("WCI=",1.6*t-55)
else:
    print("WCI=",91.4+(91.4-t)*(0.0203*v-0.304*v*.5-0.474))


