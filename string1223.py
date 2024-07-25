str1="P@#yn26at^&i5ve"
lower=0
upper=0
digit=0
special=0
for i in str1:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digit+=1
    else:
        special+=1
print("upper=",upper,"\nlower=",lower,"\ndigit=",digit,"\nspecial=",special)

