#Bryson Shane
#Project Status: Complete
#Project Description: Program gets data of 3 employees and displays the results. This program uses
#the employee class.

#imports the employee class module
import employee

#Global constant of current employees
TOTAL_EMPLOYEES = 3

def main():
    theEmployees = make_list() #stores the list in employees
    display_list(theEmployees) #passes the employees variable to the display list function showing the results.
    
def make_list():
    #Blank list to store the employees
    employeeList = []
    name, id, department, jobTitle = '', 0, '', '' #initial values for the object.

    #Continues to loop for 3 employees and get the information, creates the object employees and appends it
    #to a list
    for addEmployee in range(TOTAL_EMPLOYEES):
    
        employees = employee.Employee(name,id,department,jobTitle)
        
        name = input('Input Employee\'s Name: ')
        employees.set_name(name)
        try:
            id = int(input('Input Employee\'s ID: '))
        except ValueError:
            print('ID must contain integer values')
        employees.set_id(id)
        department = input('Input Employee\'s Department: ')
        employees.set_department(department)
        jobTitle = input('Input Employee\'s Job Title: ')
        employees.set_job_title(jobTitle)    
        
        employeeList.append(employees)
    
    return employeeList #passes it to the main function and stores it in a list.

def display_list(employeeList):
    for readList in employeeList:
        print()
        print(readList)
        print()
    #void function that displays all the employee's results.

main()
