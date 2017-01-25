from user import *


class Employee(User):
    """docs"""

    employees_list = []

    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)

    def __str__(self):
        return "{} {}, email: {}".format(self.name, self.surname, self.email)

    @classmethod
    def update_employees_list(cls):
        cls.employees_list = []
        #cls.employees_list.extend(Mentor.create_mentors_object_list())
        cls.employees_list.extend(Employee.create_staff_list())

    @classmethod
    def create_staff_list(cls):
        staff_object_list = []
        with open ("Regular_employees.csv", "r") as staff_file:
            for line in staff_file:
                line = line.split(",")
                lenght = len(line) -1
                line[lenght] = line[lenght][:-2]
                name = line[0]
                surname = line[1]
                email =line[2]
                password = line[3]
                status = line[4]
                id = line[5]
                employee_name = name + "_" + surname
                employee_name = cls(name, surname, email, password, status, id)
                staff_object_list.append(employee_name)
        return staff_object_list




    @staticmethod
    def show_employees():
        """docs"""
        for employee in Employee.employees_list:
            print(employee)


    def edit_employee_data(self): # ADD employee_id ATTRIBUTE
        """docs"""

        # Here search an employee object with employee_id id


        list_of_employee_atributes = ["name", "surname", "e-mail", "password"]
        for number, attribute in enumerate(list_of_employee_atributes):
            print("  {}: {}".format(number + 1, attribute))
        print("  0: Go back")

        user_input = input("What do you want to change?\n")
        option = user_input

        if option == "1":
            os.system('clear')
           # OBJECT.edit_name_employee()  # REPLACE "OBJECT"
        elif option == '2':
            os.system('clear')
           # OBJECT.edit_surname_employee()  # REPLACE "OBJECT"
        elif option == '3':
            os.system('clear')
           # OBJECT.edit_email_employee()  # REPLACE "OBJECT"
        elif option == '4':
            os.system('clear')
           # OBJECT.edit_password_employee()  # REPLACE "OBJECT"
        elif option == '0':
            os.system('clear')
              # GO BACK method (or nothing)

    @staticmethod
    def remove_employee():
        """"docs"""
        print("Which employee you want to remove?\n\n")
        for number, employee in enumerate(Employee.employees_list):
            print("  {}: {}".format(number + 1, employee))
        print("  0: Go back\n")
        option = int(input("Number: ")) # add error handling
        for number, employee in enumerate(Employee.employees_list):
            if number + 1 == option:
                employee.remove_employee_now()

    def remove_employee_now(self):
        # if self in Mentor.mentors_object_list: #  UNHASH IT LATER
        #     Mentor.mentors_object_list.remove(self)
        if self in Employee.employees_list:
            Employee.employees_list.remove(self)


    def edit_name_employee(self):
        new_name = input("Type a new name for chosen employee: ")
        #self.edit_name(new_name) # UNHASH IT WHEN METHOD CREATED IN USER CLASS

    def edit_surname_employee(self):
        new_surname = input("Type a new surname for chosen employee: ")
        #self.edit_surname(new_surname)# UNHASH IT WHEN METHOD CREATED IN USER CLASS

    def edit_email_employee(self):
        new_email = input("Type a new e-mail for chosen employee: ")
        #self.edit_email(new_email)#  UNHASH IT WHEN METHOD CREATED IN USER CLASS

    def edit_password_employee(self):
        new_password = input("Type a new password for chosen employee: ")
        #self.edit_password(new_password)#  UNHASH IT WHEN METHOD CREATED IN USER CLASS

    






#
#
# ja = Employee("krzysiek", "dzioba", "skidzioba@interia.pl", "maslo", "student", "wegf343")
# ja.create_staff_list()
# Employee.update_employees_list()
# print(Employee.employees_list)
# print(Employee.employees_list[0])
# Employee.show_employees()
