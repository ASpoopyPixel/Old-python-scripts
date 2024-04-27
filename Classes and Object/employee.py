#Employee class to create an employee object.

class Employee:
    #initializes the data attributes with getName, id, department, and job
    def __init__(self, getName, getID, getDepart, getJobTitle):
        self.__name = getName
        self.__id = getID
        self.__department = getDepart
        self.__jobTitle = getJobTitle

    #The set_ functions are used to set values to the object.
    def set_name(self, getName):
        self.__name = getName
    
    def set_id(self, getID):
        self.__id = getID
    
    def set_department(self, getDepart):
        self.__department = getDepart
    
    def set_job_title(self, getJobTitle):
        self.__jobTitle = getJobTitle

    #get_ functions are used to retrieve specific values of the object.
    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
        
    def get_department(self):
        return self.__department
    
    def get_job_title(self):
        return self.__jobTitle

    #returns the entire employee's ID if the object is called in a print statement.
    def __str__(self):
        return f'''Employee: {self.__name}
ID: {self.__id}
Department: {self.__department}
Job Title: {self.__jobTitle}'''
