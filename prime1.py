num1=int(input("enter sterting no"))
num2=int(input("enter limit"))
for i in range(num1,num2):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
            



            



