from ui import Ui
import os
import sqlite3


class Assignments:
    """
    Class Assignments
    handle assignments objects (assignment list)
    """
    assignments_list = []

    def __init__(self, start_date, end_date, assignment_name):
        self.start_date = str(start_date)  # sample date "2017-01-01"
        self.end_date = str(end_date)  # sample date "2017-01-01"
        self.assignment_name = str(assignment_name)  # sample name "OOP_SI_exercise"

    def __str__(self):
        return '{} {} {}'.format(self.start_date, self.end_date, self.assignment_name)

    @classmethod
    def create_objects_list_from_database(cls, table_name):    #  from database
        """
        Creates abjects based on data from database.
        :param file_path:
        :return:
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        name_q = "SELECT start_date, end_date, name  FROM assignements;"
        name_db = c.execute(name_q)
        conn.commit()

        assignments_list = []

        for row in name_db:
            start_date = row[0]
            end_date = row[1]
            name = row[2]

            full_name = cls(start_date, end_date, name)
            assignments_list.append(full_name)
        conn.close()
        return assignments_list

    @staticmethod
    def view_assignment_list():
        """
        method prints the list or error_message if list is empty
        """

        if len(Assignments.assignments_list) == 0:
            Ui.print_message("Assignment list is empty")
        else:
            Ui.print_assignments_list(Assignments.assignments_list, "Assignments List:")

    @classmethod
    def add_an_assignment(cls):
        """
        method adds assignments to assignment_list, and update this list
        """
        os.system('clear')
        while True:
            data = Ui.get_inputs(['Start date\n\tday(1-31): ', '\tmonth(1-12): ', '\tyear(2000+): ',
                                  'End date\n\tday(1-31): ', '\tmonth(1-12): ', '\tyear(2000+): ',
                                  'Assignment name\n\t'], "Please provide the assignment details: \n")
            try:
                start_date_day = int(data[0])
                start_date_month = int(data[1])
                start_date_year = int(data[2])
                end_date_day = int(data[3])
                end_date_month = int(data[4])
                end_date_year = int(data[5])
                name_of_assign = str(data[6])
            except ValueError:
                Ui.print_message("\nDate must be an integer!\n\n")
                break

            if start_date_day > 31 or start_date_day < 1:
                Ui.print_message('\nStart day value is incorrect')
            else:
                if start_date_month > 12 or start_date_month < 1:
                    Ui.print_message('\nStart month value is incorrect')
                else:
                    if start_date_year > 9999 or start_date_year < 2000:
                        Ui.print_message('\nStart year value is incorrect')
                    else:
                        if end_date_day > 31 or end_date_day < 1:
                            Ui.print_message('\nEnd day value is incorrect')
                        else:
                            if end_date_month > 12 or end_date_month < 1:
                                Ui.print_message('\nEnd month value is incorrect')
                            else:
                                if end_date_year > 9999 or end_date_year < 1000:
                                    Ui.print_message('\nEnd year value is incorrect')
                                else:
                                    if len(name_of_assign) <= 1:
                                        Ui.print_message("\nAssignment name have to be longer!")
                                    else:
                                        list_of_names_of_assignments = []
                                        for i in Assignments.assignments_list:
                                            list_of_names_of_assignments.append(i.assignment_name)
                                        if name_of_assign in list_of_names_of_assignments:
                                            Ui.print_message("\nAssignment name already exist, "
                                                             "type another one!")
                                        else:
                                            start_date = '{}-{}-{}'.format(start_date_year,
                                                                           start_date_month,
                                                                           start_date_day)
                                            end_date = '{}-{}-{}'.format(end_date_year,
                                                                         end_date_month,
                                                                         end_date_day)
                                            new_assignment = cls(start_date, end_date, name_of_assign)
                                            Assignments.assignments_list.append(new_assignment)
                                            Ui.print_message("\nAssignment added!\n")
                                            Ui.get_inputs([''], "Click enter to go back")
            break  # it stops the WHILE loop whenever passed information is incorrect, or assignment has been added
