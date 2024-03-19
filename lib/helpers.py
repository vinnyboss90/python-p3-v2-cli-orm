from models.department import Department
from models.employee import Employee

def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson

def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)

def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f"Department {name} not found.")

def find_department_by_id():
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f"Department {id_} not found.")

def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print('Error creating department: ', exc)

def update_department():
    id_ = input("Enter the department's id: ")
    # The walrus operator := allows you to assign a value to a variable as part of an expression in loops or conditional statements. It allows you to assign variables and user inputs directly inside the while loop or if condition.  
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print('Error updating department: ', exc)
    else:
        print(f'Department {id_} not found.')
    
def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted.')
    else:
        print(f'Department {id_} not found.')


# You'll implement the employee functions in the lab. Don't forget to reset the databases by running this in the terminal python lib/debug.py. Also, everytime you change the functions, you must execute again the file that calls the functions. Exit the CLI program by typing 0 and run python lib/cli.py in the terminal.
        
def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    # Because the action is just one (printing), use a ternary operator here.
    print(employee) if employee else print(f'Employee {name} not found.')
     
def find_employee_by_id():
    id_ = input("Enter the employee's id ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f"Employee {id_} not found.")

def create_employee():
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    department_id = input("Enter the department's id: ")
    try:
        if department_id := Department.find_by_id(department_id).id:
            employee = Employee.create(name, job_title, department_id)
            print(f'Success: {employee}')
        else:
            print(f'Department {department_id} not found.')
    except Exception as exc:
            print('Error creating employee: ', exc)
    
def update_employee():
    employee_id = input("Enter the employee's id: ") 
    if employee := Employee.find_by_id(employee_id):
        try:
            name = input("Enter the employee's new name: ")
            employee.name = name
            job_title = input("Enter the employee's new job title: ")
            employee.job_title = job_title
            department_id = input("Enter the employee's new department id: ")   
            if department_id := Department.find_by_id(department_id).id:
                employee.department_id = department_id
                employee.update()
                print(f'Success: {employee}')
        except Exception as exc:
            print('Error updating employee: ', exc)
    else:
        print(f'Employee {employee_id} not found.')
    
def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted.')
    else:
        print(f'Employee {id_} not found.')

def list_department_employees():
    department_id = input("Enter the department's id: ")
    department = Department.find_by_id(department_id)
    if department:
        employees = department.employees()
        for employee in employees:
            print(employee.name)
    else:
        print(f'Department not found.')
