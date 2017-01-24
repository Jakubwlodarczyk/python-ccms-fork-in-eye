from Ui import *
from Common import *
import sys

class ManagerMenu(Menu):

    def handle_menu():
        options = ["View mentors list", "Edit mentors' data", "Fire mentor", "View students list"]
        while True:
            ui.print_menu("What you want to do?", options, "Log out")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == '1':
                # view mentors list
                pass
            elif option == '2':
                # edit mentors data
                pass
            elif option == '3':
                # fire mentors
                pass
            elif option == '4':
                # view students list
                pass
            elif option == '0':
                #common.write_table_to_file('Mentors.csv')
                sys.exit()
            else:
                ui.print_error_message('There is no such option.')

