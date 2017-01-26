from employee import *


class Mentor(Employee):
    '''
    Class Mentor
    Parent class: User
    '''
    mentors_list = []

    def __init__(self, *args, **kwargs):
        super(Mentor, self).__init__(*args, **kwargs)
        self.status = 'mentor'

    def __str__(self):
        return "{} {}".format(self.name, self.surname)
