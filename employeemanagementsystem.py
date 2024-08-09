maindata={}
class Employee: 
    def add(self,name,id,salary,job):
        data={}
        data['name'] = name
        data['id'] = id
        data['salary'] = salary
        data['job'] = job
        maindata[id]=data   
    def display(self,id):
        if id in maindata:
            for x,y in maindata[id].items():
                print(x,":",y)
        else:
            print("not found")
    def update(self,id):
        if id in maindata:
            echoose=int(input("Enter what you want to update:\n1.Name\n2.Id\n3.Salary\n4.Job\n"))
            newdata=input("Enter the new data=")
            if echoose==1:
                maindata[id]["name"]=newdata
            elif echoose==2:
                temp={}
                temp=maindata[id]
                del maindata[id]
                temp["id"]=newdata
                maindata[newdata]=temp
            elif echoose==3:
                maindata[id]["salary"]=newdata
            elif echoose==4:
                maindata[id]["job"]=newdata    
            else:
                print("invalid choice")
        else:
            print("this id is not found")    
    def delete(self,id):
        if id in maindata:
            del maindata[id]
        else:
            print("id not found")
details=Employee()
while 1:
    print("Employee management\n1.Look up an employee\n2.Add a new employee\n3.Change an existing employees details\n4.Delete an employee\n5.Quit\nEnter your choice")
    option=int(input(""))
    if option==1:
        about=input("enter the id of the employee to look:")
        details.display(about)        
    elif option==2:   
        ename=input("enter the name:")
        eid=input("enter the id")
        esalary=input("enter the salary")
        ejob=input("enter the job")
        details.add(ename,eid,esalary,ejob)
    elif option==3:
        upid=input("enter id of person to be updated:")   
        details.update(upid)
    elif option==4:
        delid=input("Enter the id of the person=\n")
        details.delete(delid)
    elif option==5:
        print("EXITED")
        break
    else:
        print("invalid option")
       

    
    

        
        
        
        

        

