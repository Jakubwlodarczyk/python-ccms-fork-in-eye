from models.user import User


class Manager(User):
    """
    Class manager
    Parent class: User
    """
    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)
        self.status = 'manager'
