num1=int(input("enter sterting no"))
num2=int(input("enter limit"))
x=1
for i in range(num1,num2):
    for j in range(2,i):
        if i%j==0:
            x=0
            break
        else:
            x=1
    if x==1:
        print(i)

# num1 = int(input("Enter starting number: "))
# num2 = int(input("Enter limit: "))
# x = 1
# for i in range(num1, num2):
#       # Reset x for each i
#     for j in range(2, i):
#         if i % j == 0:
#             x = 0  # If i is divisible by any j, set x to 1
#             break 
#         else:
#             x=1 # No need to check further
#     if x == 1 :  # Check if x is still 0 after checking all j
#         print(i)

            