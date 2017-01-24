from menu import *
from ui import *


class MentorMenu(Menu):

    @staticmethod
    def choose_option():
        title = 'Mentor menu'
        list_options = ['Check the list of students', 'Add an assignment',
                        'Grade an assignment submitted by students', 'Check attendance of students',
                        'Add a student to a class', 'Remove a student from class', "Edit student's data"]
        Ui.print_menu(title, list_options, 'Exit')



