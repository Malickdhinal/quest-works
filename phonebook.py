phonebook={}
while 1:
    
    print("1.add\n2.display all\n3.update\n4.delete\n5.display")
    
    options=int(input("enter the options:"))
    if options==1:
        contact={}
    
        name=input("enter the name")
        countno=int(input("enter how many contacts:"))
        count1=[]
        for i in range(countno):
            phno=int(input("enter the phno:"))
            count1.append(phno)
        countem=int(input("enter how many emails:"))
        count2=[]
        for i in range(countem):
            email=input("enter the emailid:")
            count2.append(email)
        contact["name"]=name
        contact["phno"]=count1
        contact["email"]=count2     
        phonebook[name]=contact  
    elif options==2:
        print(phonebook)
    elif options==3:
        update=input("enter the data to be updated")
        newdata=input("enter the new data")
        if update in contact["name"]:
            contact["name"]=newdata
        elif update in count1:
            contact["phno"]=newdata
        elif update in count2:
            contact["email"]=newdata
        else:
            print("default")
    elif options==4:
        delete=input("enter the data to be deleted")
        phonebook.pop(delete)
    elif options==5:
        dis=input("enter the content to be displyed")
        print(phonebook[dis])
        

      

            
        
            
        
    
    



    
