a=int(input("enter the number"))
ones=["zero","one","two","three","four","five","six","seven","eight","nine"]
teens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
# hundred=["","hundred","two hundred","three hundred","four hundred","five hundred","six hundred","seven hundred","eight hundred","nine hundred"]
if a<10:
    print(ones[a])
elif a<20:
    print(teens[a-10])
elif a<100:#56
    if a%10==0:
        a//=10
        c=a%10
        print(tens[c-1])
    else:
        b=a%10#b=6
        a//=10#5
        c=a%10#c=5
        print(tens[c-1],ones[b])
elif a<1000:#56
    if a%100==0:
        a//=100
        c=a%10
        print(ones[c]," hundered")
    elif a%10==0:
        a//=10
        b=a%10#b=6
        a//=10#5
        c=a%10#c=5
        print(ones[c]," hundered",tens[b-1])
    elif a%10!=0:#151
        b=a%10#1
        a//=10#15
        if a%10==1:
            d=a%10
            a//=10
            c=a%10
            print(ones[c],"hundered",teens[b])
        else:#151
            
            c=a%10#5
            a//=10#1
            d=a%10
            print(ones[d]," hundered",tens[c-1],ones[b])

    



