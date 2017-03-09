from models.user import User


class Employee(User):
    """
    Class Employee
    Parent class: User
    """
    def __init__(self, id, name, surname, email, password, status):
        User.__init__(self, id, name, surname, email, password, status)
        self.status = 'employee'
