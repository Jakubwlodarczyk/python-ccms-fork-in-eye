from user import User


class Manager(User):
    """
    Class manager
    parent class: User
    """

    manager_list = []

    def __init__(self, name, surname, email, password, status, manager_id):
        User.__init__(self, name, surname, email, password)
        self.status = status
        self.manager_id = manager_id

    def __str__(self):
        return "{} {} {} {} {}".format(self.name, self.surname, self.email, self.status, self.manager_id)

