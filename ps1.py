# Class Department
class Department:
    # Initialize the empty lists for department details
    def __init__(self):
        self.__name=[]
        self.__maxEmployee=[]
        self.__manager=[]
        self.__employee=[[]]
    # Add the Employee to the employee list
    def addEmployee(self,name,employee):
        self.__employee[self.__name.index(name)].append(employee)
    # Remove the Employee from employee list
    def removeEmployee(self,name,employee):
        if  employee in self.__employee[self.__name.index(name)]:
            self.__employee[self.__name.index(name)].remove(employee)
    # Add the department to the department list
    def addDepartment(self,name,maxEmployee,manager):
        if name in self.__name:
            return print("Name already taken")
        self.__name.append(name)
        self.__maxEmployee.append(maxEmployee)
        self.__manager.append(manager)
        self.__employee.append([])
    # Modify the Department details
    def Modify(self,name,maxEmployee,manager):
        self.__maxEmployee[self.__name.index(name)]=maxEmployee
        self.__manager[self.__name.index(name)]=manager
    # Show department details
    def showDepartment(self,name):
        if name in self.__name:
            print("The department name is: {}, max employee is: {}, manager is: {}, the employees are: {} ".format(name,self.__maxEmployee[self.__name.index(name)],self.__manager[self.__name.index(name)],self.__employee[self.__name.index(name)]))
        else:
            print("Department not present")
    # Set the name of the department with 0 size and  no manager
    def setname(self,name):
        self.addDepartment(name, 0,"None")
    # Get the names of the departments
    def getname(self):
        return self.__name
    # set the manager for department name given
    def setManager(self,name,manager):
        self.__manager[self.__name.index(name)]=manager
    # get the manager names
    def getManager(self):
        return self.__manager
    #set max employee
    def setmaxEmployee(self,name,maxEmployee):
        self.__maxEmployee[self.__name.index(name)]=maxEmployee
    # get maxm employee for the department given
    def getmaxEmployee(self,name):
        if name in self.__name:
            return self.__maxEmployee[self.__name.index(name)]
    # get the employees for the department name given
    def getEmployee(self,name):
        if name in self.__name:
            return self.__employee[self.__name.index(name)]
        
# Class manager
class Manager:
    # Initailize the empty lists for managers
    def __init__(self):
        self.__name=[]
        self.__position=[]
        self.__department=[[]]
    # add manager to the list
    def addManager(self,name,position):
        if name in self.__name:
            return print("Name already taken")
        self.__name.append(name)
        self.__position.append(position)
        self.__department.append("None")
    # Assign department to the manager name given
    def AssignDepartment(self,name,department):
        if self.__position[self.__name.index(name)]== "Project_Manager":
            if self.__department[self.__name.index(name)]== "None":
                self.__department[self.__name.index(name)]=department
            else:
                print("Department already assigned")
        else:
            self.__department[self.__name.index(name)]=department
    # get the deapartment assigned to the manager
    def DepartmentAssigned(self,name):
        print(self.__department[self.__name.index(name)])
    # Show the details of the manager given
    def showManager(self,name):
        if name in self.__name:
            print("Manager name is {}, Position: {}, Department {}".format(name,self.__position[self.__name.index(name)],self.__department[self.__name.index(name)]))
        else:
            print("Manager not present")
    # set the name of manager with position as None 
    def setname(self,name):
        self.addManager(name, "None")
    # get the names of managers
    def getname(self):
        return self.__name
    # Set the department for the name given
    def setDepartment(self,name,Department):
        self.__department[self.__name.index(name)].append(Department)
    # Get all the departments assigned to managers
    def getDepartment(self):
        return self.__department

#Class Employees
class Employee:
    # Initailize the empty lists for employees
    def __init__(self):
        self.__name=[]
        self.__empId=[]
        self.__designation=[]
        self.__experience=[]
        self.__department=[]
    # Add employee to the lsits if name is not already assigned and the Emp Id is not already entered
    def addEmployee(self,name,empId,designation,experience,department="None"):
        if name in self.__name:
            return print("Name already taken")
        if empId in self.__empId:
            return print("EmpId already taken")
        self.__name.append(name)
        self.__empId.append(empId)
        self.__designation.append(designation)
        self.__experience.append(experience)
        self.__department.append(department)
        
    # Join th employee to the department mentioned
    def join(self,department,name):
        self.__department[self.__name.index(name)]=department
    # Leave the department for the employee and make it none
    def leave(self,department,name):
        self.__department[self.__name.index(name)]="None"
    # Show the details for the employee
    def showEmployees(self,name):
        if name in self.__name:
            print("employe name: {}, Emp ID: {}, Designation: {}, Experience: {}, Department: {}".format(name,self.__empId[self.__name.index(name)],self.__designation[self.__name.index(name)],self.__experience[self.__name.index(name)],self.__department[self.__name.index(name)]))
        else:
            print("Employee not present")
    # set the name of employee with position as None 
    def setname(self,name):
        self.addEmployee(name,"None","None","None","None")
    # get the names of employees
    def getname(self):
        return self.__name
    # set the designation for employee name given
    def setDesignation(self,name,designation):
        self.__designation[self.__name.index(name)]=designation
    # get the designations
    def getDesignation(self):
        return self.__designation

# Main program 
if __name__ == "__main__":

    # Initailize instances of class department, employee and Manager
    dept=Department()
    emp=Employee()
    mgr=Manager()
    
    # Take the file from user and open it
    file_name=input("Enter filename")
    file=open(file_name,'r+')
    
    # For each line in the input file
    for line in file:
        l=line.split()
        
        # Check the first element of the line and go to that case
        if l[0] == "ADDE":
            emp.addEmployee(l[1],l[2],l[3],l[4])
        if l[0] == "ADDM":
            mgr.addManager(l[1], l[2])
        if l[0] == "ADDD":
            #if the manager name does not exits then return error
            if not l[3] in mgr.getname():
                print("Manager does not exixts")
                continue
            # else add the department and assign the dept to manager
            dept.addDepartment(l[1], l[2], l[3])
            mgr.AssignDepartment(l[3], l[1])
        if l[0] == "JOIN":
            # If department does not exists then return error
            if not l[1] in dept.getname():
                print("Department does not exists")
                continue
            # else add the employee to department if the max limit of dept not reached
            numE=len(dept.getEmployee(l[1]))
            MaxE=len(dept.getmaxEmployee(l[1]))
            if(numE<MaxE):
                emp.join(l[1], l[2])
                dept.addEmployee(l[1],l[2])
            else:
                print("Maximum limit of department reached")
        if l[0] == "LEAVE":
            #remove the employee from dept and department name from employee data
            emp.leave(l[1],l[2])
            dept.removeEmployee(l[1],l[2])
        if l[0] == "MODIFY":
            # If department does not exists then give error
            if not l[1] in dept.getname():
                print("Department does not exixts")
                continue 
            # Else Modify the department data
            if l[3] in mgr.getname():
                dept.setmaxEmployee(l[1], l[2])
            else:    
                dept.Modify(l[1], l[2], l[3])
        if l[0] == "SHOWE":
            # Show the employee data
            emp.showEmployees(l[1])
        if l[0] == "SHOWM":
            # show the manager data
            mgr.showManager(l[1])
        if l[0] == "SHOWD":
            # Show the department data
            dept.showDepartment(l[1])
    #close the file
    file.close()

