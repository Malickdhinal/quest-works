a="ABCDEf"
b="12345678"
save=""
reva=a[::-1]
n=len(b)
m=len(reva)
for i in range(n):
    for j in range(m):     
        save=save+b[i]+reva[i]
        if reva>n:
            save+=b[i]
print(save)