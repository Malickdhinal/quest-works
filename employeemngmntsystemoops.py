class Employee:
    def __init__(self,emp_id,name,dept,job_title):
        self.emp_id=emp_id
        self.name=name
        self.dept=dept
        self.job_title=job_title
class Employeedatabase:
    def __init__(self):
        self.employees=[]
    def add_employee(self,employee):
        self.employees.append(employee)
    def lookup(self,emp_id):
        for emp in self.employees:
            if emp.emp_id==emp_id:
                return emp
        return None
    def update(self,emp_id):
        employee=self.lookup(emp_id)
        if employee:
            print("Employee found,what would you like to update?\n1.Name\n2Department\n3.Job title")
            choice=input("Enter your choice=")
            if choice=='1':
                new_name=input("Enter new name=")
                employee.name=new_name
                print("name updated").upper()
            elif choice=='2':
                new_dept=input("Enter new department=")
                employee.dept=new_dept
                print("department updated").upper()
            elif choice=='3':
                new_job_title=input("Enter new job title=")
                employee.job_title=new_job_title
                print("job title updated").upper()
            else:
                print("invalid choice").upper()
        else:
            print("employee not found").upper()
    def delete(self,emp_id):
        employee=self.lookup(emp_id)
        if employee:
            confirm=input("Are you sure you want to delete this employee?(yes/no)").lower()
            if confirm=="yes":
                self.employees.remove(employee)
                print("employee deleted successfully").upper()
            else:
                print("employee not found").upper()

employee_db=Employeedatabase()

while 1:
    print("\nEMPLOYEE MANAGEMENT SYSTEM\n__________________________\n1.Look up an employee\n2.Add a new employee\n3.Change an existing employees details\n4.Delete an employee\n5.Quit\nEnter your choice")
    option=int(input(""))
    if option==1:
        emp_id=int(input("Enter the employee id to lookup="))
        employee=employee_db.lookup(emp_id)
        if employee:
            print("Employee id=",employee.emp_id)
            print("Employee name=",employee.name)
            print("Employee department=",employee.dept)
            print("Employee job title=",employee.job_title)
        else:
            print("EMPLOYEES NOT FOUND")
    elif option==2:
        emp_id=int(input("Enter the employee id="))
        name=input("Enter the name of the employee=")
        dept=input("Enter the name of the department=")
        job_title=input("Enter the name of the job=")
        new_employee=Employee(emp_id,name,dept,job_title)
        employee_db.add_employee(new_employee)
    elif option==3:
        emp_id=int(input("Enter employee id to change the details="))
        employee_db.update(emp_id)
    elif option==4:
        emp_id=int(input("Enter employee id to delete="))
        employee_db.delete(emp_id)
    elif option==5:
        print("-----------------------EXITED-------------------------")
        break
    else:
        print("invalid choice ,enter the correct option").upper()
        
        




            
       
        




