employee_dict = {101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}}
menu_message = """
----------------------------------------------------------------------------------------------
Welcome to Employee Management System ( EMS)
1. Add Employee
2. View All Employees
3. Search for Employee
4. Exit
----------------------------------------------------------------------------------------------
"""
def add_employee():
    """ Allows you to Add Employee Information  to the Data """
    
    emp_id = int(input("Employee Id : "))
    name = input("Employee Name : ")
    age = int(input("Employee Age : "))
    department = input("Employee Department : ")
    salary = float(input("Employee Salary : "))
    if emp_id in employee_dict.keys():
        DUP_FLAG = True
    else:
        DUP_FLAG = False
    
    while  DUP_FLAG:
        print("This ID is already registered Please Select another one")
        emp_id = int(input("Employee Id : "))
        if emp_id  in employee_dict.keys():
            DUP_FLAG = True
        else:
            DUP_FLAG = False
    employee_dict[emp_id]= {'name': name, 'age': age, 'department': department, 'salary': salary}
    return f"Employee {emp_id} Successfully Added"
def display_employee_list():
    """ This Function Displays the list of all Employees Available"""
    
    i = 25
    str1 = ""
    if len(employee_dict) > 0:
        str1 += "Employee Id".ljust(i)
        str1+= "Employee Name".ljust(i)
        str1 += "Employee Age".ljust(i)
        str1 += "Employee Department".ljust(i)
        str1 +="Employee Salary\n"
        for key, value in employee_dict.items():
            name = value['name']
            dep = value["department"]
            age = value["age"]
            sal = value["salary"]
            str1 += f"{key}".ljust(i)
            str1 += f"{name}".ljust(i)
            str1 += f"{age}".ljust(i)
            str1 += f"{dep}".ljust(i)
            str1 += f"{sal}".ljust(i)
            str1+= "\n"
    else:
        str1 = "No Employees Available"
    return str1

def search_employee():
    """ This Function Allows to Search The Employee Info all over the data"""
    emp_id = int(input("Enter the Employee Id"))
    str1 = ""
    if emp_id in employee_dict.keys():
        str1 += f"""
        Employee Name : {employee_dict[emp_id]['name']}
        Employee Age :{employee_dict[emp_id]['age']}
        Department :{employee_dict[emp_id]['department']} 
        Salary : {employee_dict[emp_id]['salary']}
        """
    else:
        str1 = "Employee Not Found"
    return str1

def prog_exit():
    str1 = "Thank You for Using this System\nCome Back Again!"
    return str1

menu_input = 0
menu_dict = {
    1: add_employee,
    2: display_employee_list,
    3: search_employee
}


while menu_input != 4:
    print(menu_message)
    menu_input = int(input("Please Select your Choice : "))
    if menu_input in menu_dict.keys():
        print(f"{menu_dict[menu_input].__doc__}\n------------------------------------------------------------------------")
        message = menu_dict[menu_input]()
        print(message)
        print("------------------------------------------------------------------------------")
    else:
        message = prog_exit()
        menu_input = 4
        print(message)
    
else:
    message = prog_exit()
    print(message)