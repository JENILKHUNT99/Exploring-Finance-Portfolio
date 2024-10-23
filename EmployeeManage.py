class Employees:

    class Employee:
        def __init__(self,eid,name,designation,salary,x):
            self.eid=eid
            self.name=name
            self.designation=designation
            self.salary=salary
            self.x=x

    employeesDetails=[]
    
    def addEmployee(self,eid,name,designation,salary,x):
        self.employeesDetails.append(self.Employee(eid,name,designation,salary,x))
    
    def allEmployeeSalaryTotal(self):
        totalSalary=0
        for i in self.employeesDetails:
            totalSalary+=i.salary
        return totalSalary
    
    def totalEmployee(self):
        return len(self.employeesDetails)
    
    def printAllEmployeeDatails(self):
        # print("Eid  Name  designation   salary   Details")
        for i in self.employeesDetails:
            print(i.eid,i.name,i.designation,i.salary,i.x)

    def copyEmployee(self,e2):
        for i in e2.employeesDetails:
            self.addEmployee(i.eid,i.name,i.designation,i.salary,i.x)

    
    def employeeManagement(self):
        choice=None
        while choice !="4":
            print()
            choice=input("(1)Add Employee \n(2)Remove Employee \n(3)Increment All Employee Salary \n(4)Increment Salary Particular Employee \n(5)View All Employee Details \n(6)View Particular Employee Details \n(7)Exit \n")

            if (choice in ["2","3","4","5","6"]) and (not self.employeesDetails):
                print("Employee List Is Empty")
                continue
            
            if choice=="1":
                eid=int(input("Enter Employee ID : "))
                # name,designation,salary,x
                name=input("Enter Name Of Employee : ")
                designation=input("Enter Designation Of Employee : ")
                salary=int(input("Enter Salary Of Employee : "))
                x=input("Enter Other Description Of Employee : ")
                self.addEmployee(eid,name,designation,salary,x)
                print("Employee Sucessfuly Added")

            elif choice=="2":
                eid=int(input("Enter Employee ID : "))
                for i in self.employeesDetails:
                    if i.eid==eid:
                        self.employeesDetails.remove(i)
                        print("Employee Successfuly Removed...")
                        break
                else:
                    print("This Employee ID Not Found...")
            elif choice=="3":
                incrementSalary=int(input("Enter Increment Salary Value : "))
                for i in self.employeesDetails:
                    i.salary+=incrementSalary
                else:
                    print("For All Employee Salary Incremented")
            elif choice=="4":
                eid=int(input("Enter Employee ID : "))
                incrementSalary=int(input("Enter Increment Salary Value : "))
                for i in self.employeesDetails:
                    if i.eid==eid:
                        i.salary+=incrementSalary
                        print("Employee's Successfuly Salary Incremented...")
                        
                else:
                    print("This Employee ID Not Found...")
            elif choice=="5":
                self.printAllEmployeeDatails()
            elif choice=="6":
                eid=int(input("Enter Employee ID : "))
                for i in self.employeesDetails:
                    if i.eid==eid:
                        print(i.eid,i.name,i.designation,i.salary,i.x)
                        break
                        
                else:
                    print("This Employee ID Not Found...")
            elif choice=="7":
                break
            else:
                print("Invalid Option")
            

# ee=Employees().employeeManagement()