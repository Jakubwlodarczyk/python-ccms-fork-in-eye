from user import User


class Manager(User):
    """
    Class manager
    parent class: User
    """

    def __init__(self, name, surname, email, password):
        User.__init__(self, name, surname, email, password)

    def view_manager_list(self):
        pass
