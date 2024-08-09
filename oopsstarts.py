# class Laptop:
#     color="grey"
#     processor="intel"
# hp=Laptop()
# lenovo=Laptop()
# print(hp.grey)
# print(lenovo.color)
# print(hp.processor)
# print(lenovo.processor)
# class Human:
#     eyes=2
#     legs=2
# alaka=Human()
# print(alaka.eyes)
# keerthana=Human()
# print(keerthana.eyes)
# # del alaka.eyes
# # print(alaka.eyes)
# alaka.eyes=3
# print(alaka.eyes)
# a=int(input("enter the no"))
# def mult(x):
#     for i in range(11):
#         if i<11:
#             print(x,"X",i,"=",i*x)
#             i+=1
# mult(a)
# letters=input("enter the string:\n")
# def vowl(let):
#     sra=["a","e","i","o","u","A","E","I","O","U"]
#     count=0
#     for i in let:
#         if i in sra:
#             count+=1
#     print(count)
# vowl(letters)
letters=input("enter the string:\n")
class Work:
    def vowl(self,let):
        sra=["a","e","i","o","u","A","E","I","O","U"]
        count=0
        for i in let:
            if i in sra:
                count+=1
        print(count)
    vowl(letters)
wr=Work()
wr.vowl(letters)