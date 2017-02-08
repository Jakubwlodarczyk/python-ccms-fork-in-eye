from user import User


class Manager(User):
    """
    Class manager
    Parent class: User
    """
    manager_list = []

    def __init__(self, *args, **kwargs):
        super(Manager, self).__init__(*args, **kwargs)
        self.status = 'manager'

    def __str__(self):
        return "{} {}".format(self.name, self.surname)



    @classmethod
    def view_full_students_statistics(cls):
        pass

    @classmethod
    def view_full_mentors_statistics(cls):
        pass
