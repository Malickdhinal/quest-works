from random import*
while 1:
    name=input("enter your name")
    random_no=randrange(0,10)
    print("hi",name,"welcome to the game")
    for i in range(3):
        guess_no=int(input("guess a number between 0-9"))
        if random_no==guess_no:
            print("your guess is correct")
            break
        else:
            if 2-i==0:
                pass
            else:
                print("wrong guess you have only",2-i,"chance")
    else:
        print("sorry,try again\nthe guessed no by system is",random_no)