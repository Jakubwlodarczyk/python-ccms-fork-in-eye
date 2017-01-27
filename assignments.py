from ui import Ui
import os


class Assignments:
    """
    Class Assignments
    handle assignments objects (assignment list)
    """
    assignments_list = []

    def __init__(self, start_date, end_date, assignment_name):
        self.start_date = str(start_date)  # sample date "01.01.2017"
        self.end_date = str(end_date)  # sample date "01.01.2017"
        self.assignment_name = str(assignment_name)  # sample name "OOP_SI_exercise"

    def __str__(self):
        return '{} {} {}'.format(self.start_date, self.end_date, self.assignment_name)

    @staticmethod
    def view_assignment_list():
        """
        method prints the list or error_message if list is empty
        """

        if len(Assignments.assignments_list) == 0:
            Ui.print_error_message("Assignment list is empty")
        else:
            Ui.print_assignments_list(Assignments.assignments_list, "Assignments List:")

    @classmethod
    def add_an_assignment(cls):
        """
        method adds assignments to assignment_list, and update this list
        """
        os.system('clear')
        data = Ui.get_inputs(['start_date (dd-mm-yyyy): ', 'end_date (dd-mm-yyyy): ', 'assignment_name: '],
                             "Please provide the assignment: \n")

        new_assignment = cls(data[0], data[1], data[2])
        Assignments.assignments_list.append(new_assignment)


    @classmethod
    def create_assignments_list(cls, file_path):
        """
        reads the file with data, and creates the list of objects
        :param file_path: the path to file
        :return: (list) list of objects of assignments
        """
        assignments_list = []
        with open(file_path, "r") as f:
            my_lines = f.readlines()
            for index, line in enumerate(my_lines):
                line = line.split(",")
                length = len(line) - 1
                if index + 1 == len(my_lines):
                    pass
                else:
                    line[length] = line[length][:-1]
                if line[2][-1] == '\n':
                    line[2] = line[2][:-1]
                start_date = line[0]
                end_date = line[1]
                assignment_name = line[2]
                full_assignment_name = cls(start_date, end_date, assignment_name)
                assignments_list.append(full_assignment_name)
        return assignments_list
