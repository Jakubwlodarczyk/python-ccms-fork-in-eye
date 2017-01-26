from employee import *


class Mentor(Employee):

    mentors_list = []

    def __init__(self, *args, **kwargs):
        super(Mentor, self).__init__(*args, **kwargs)

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

