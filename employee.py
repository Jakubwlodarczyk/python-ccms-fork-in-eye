from user import *


class Employee(User):
    """
    Class Employee
    Parent class: User
    """

    employees_list = []

    def __init__(self, *args, **kwargs):
        super(Employee, self).__init__(*args, **kwargs)

    def __str__(self):
        return "{} {}, email: {}".format(self.name, self.surname, self.email)
