from menu import *
from ui import *
from assignments import *
from student import *


class MentorMenu(Menu):

    @staticmethod
    def choose_option():
        """

        """

        while True:
            title = 'Mentor menu'
            list_options = ['Check the list of students', 'Add an assignment',
                            'Grade an assignment submitted by students', 'Check attendance of students',
                            'Add a student to a class', 'Remove a student from class', "Edit student's data"]
            Ui.print_menu(title, list_options, 'Log out')
            chose_option = Ui.get_inputs(["Please enter a number: "], "")

            if chose_option[0] == '1':
                # print list of students
                print(Ui.print_staff_list(Student.student_list, "List of students"))

            elif chose_option[0] == '2':
                # add an assignment
                add_an_assignment_input = Ui.get_inputs(['start_date: ', 'end_date: ', 'assignment_name: '],
                                                        "Please provide the assignment: ")
                Assignments.assignments_list.append(add_an_assignment_input)
            elif chose_option[0] == '3':
                # grade submission
                pass
            elif chose_option[0] == '4':
                # check attendance of students
                pass
            elif chose_option[0] == '5':
                # add a student to a class
                add_student_input = Ui.get_inputs(['name: ', 'surname: ', 'email: ', 'password: '],
                                                  "Please provide the students details: ")
                Student.student_list.append(add_student_input)
            elif chose_option[0] == '6':
                # remove student from class

                # print student list -> ask for input ->remove

                pass
            elif chose_option[0] == '7':
                # edit student's data

                # print student list - ask for input - edit
                pass
            elif chose_option[0] == '0':
                # exit
                pass
            else:
                raise ValueError('Wrong input')


MentorMenu.choose_option()
