from employee import Employee


class Mentor(Employee):

    mentors_list = []

    def __init__(self, *args, **kwargs):
        super(Mentor, self).__init__(*args, **kwargs)

    def __str__(self):
        return "{} {}, email: {}".format(self.name, self.surname, self.email)

    @classmethod
    def create_staff_list(cls):
        staff_object_list = []
        with open("Mentor.csv", "r") as staff_file:
            for line in staff_file:
                line = line.split(",")
                lenght = len(line)-1
                line[lenght] = line[lenght][:-2]
                name = line[0]
                surname = line[1]
                email = line[2]
                password = line[3]
                status = line[4]
                id = line[5]
                mentor_name = name + "_" + surname
                mentor_name = cls(name, surname, email, password, status, id)
                mentors_object_list.append(mentor_name)
        return mentors_object_list
