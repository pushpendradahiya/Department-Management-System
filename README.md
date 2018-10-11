# Department-Management-System
A small assignment on a department management system

In this system, the three entities are Department, Employee and Manager.

The DMS is able to handle many department which can be joined by many employee(upto max value given for each department) and handled by a single manager.

Basic Features:
  Employee can join  a department and later also leave from the department.
  Each department must be assigned a manager.
  Ability to modify any detail of the department.
  Employee has the following attribute and functions
		Name : String Unique
		EmpId : String Unique
		Designation : String Trainee Engineer, Software Engineer and System Analyst 
		Experience year : integer 1,2,3,4,5
		Department joined : department name
		addEmployee : to add the employee details
		join(department) : function to join a department
		leave(department) : function to leave from a department already taken
		showEmployee : Display all details of the employee

  Manager has the following attribute and functions
		name : String Unique
		position : String Project Manager, Delivery Manager
		addManager : to add the manager details
		departmentAssigned : list of department
		showManager : Display all details of the manager

  Department has the following attribute and function
		name : String Unique
		maxEmployee : maximum number of employee that can join
		manager : Manager assigned
		empJoined : list of employee joined the department
		addDepartment : to add the department details
		Modify(max-emp, manager) : function to modify the max employee limit and the manager of the department
		showDepartment : Display everything of department
