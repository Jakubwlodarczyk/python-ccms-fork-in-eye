from user import User
from ui import *

class Employee(User):
    """docs"""
    Employees = []

    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)


    @staticmethod
    def show_employees():
        """docs"""
        print(Employee.Employees)


    def edit_employee_data(self, employee_id):
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
            OBJECT.edit_name()  # REPLACE "OBJECT"
        elif option == '2':
            os.system('clear')
            OBJECT.edit_surname()  # REPLACE "OBJECT"
        elif option == '3':
            os.system('clear')
            OBJECT.edit_email()  # REPLACE "OBJECT"
        elif option == '4':
            os.system('clear')
            OBJECT.edit_password()  # REPLACE "OBJECT"
        elif option == '0':
            os.system('clear')
              # GO BACK method

    def remove_employee(self):
        """"docs"""
        pass

    def edit_name(self):
        pass








ja = Employee("krzysiek", "dzioba", "skidzioba@interia.pl", "maslo")
ja.remove_employee()
