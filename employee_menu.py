from ui import Ui
import sys
import os
from student import Student

class EmployeeMenu:

    @staticmethod
    def choose_option():
        """
        prints staff menu for kati and miriam
        :return: None
        """

        while True:
            os.system("clear")
            title = 'Employee menu'
            list_options = ['Show list of students']
            Ui.print_menu(title, list_options, 'Exit program')
            chose_option = Ui.get_inputs(["Choose option: "], "")
            my_option = chose_option[0]
            try:
                print(my_option)
                int(my_option)
                if int(my_option) < 0 or int(my_option) > len(list_options):
                    raise ValueError
            except TypeError:
                print("Wrong input.")
                m = Ui.get_inputs([""], "")
                continue
            except ValueError:
                print("It must be integer between 1 and " + str(len(list_options)) + " or 0.")
                m = Ui.get_inputs([""], "")
                continue


            if chose_option[0] == '1':
                os.system("clear")
                print(Ui.print_staff_list(Student.student_list, "List of students:"))
                Ui.get_inputs([""], "")

            elif chose_option[0] == '0':
                sys.exit()

            else:
                raise ValueError('Wrong input')


EmployeeMenu.choose_option()
