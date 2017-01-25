from employee import Employee


class Mentor(Employee):

    mentor_list = []

    def __init__(self, *args, **kwargs):
        super(Mentor, self).__init__(*args, **kwargs)