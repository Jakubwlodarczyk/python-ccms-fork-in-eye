from user import User


class Manager(User):
    """
    Class manager
    parent class: User
    """

    manager_list = []

    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

