from models.user import User


class Employee(User):
    """
    Class Employee
    Parent class: User
    """

    employees_list = []

    def __init__(self, id, name, surname, email, password, status):
        User.__init__(self, id, name, surname, email, password, status)
        self.status = 'employee'
