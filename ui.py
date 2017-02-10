import os


class Ui:
    '''
    Handles user interface.
    '''

    @staticmethod
    def print_table(table, title, title_list):
        '''
        Displays table with data.
        Args:
            table: list of items to print
            title: string containing main table header
            title_list: header
        '''
        os.system("clear")
        print(title)
        len_for_col = []
        for title_iterator in range(len(title_list)):
            len_col = len(title_list[title_iterator])
            for row in table:
                if len(str(row[title_iterator])) > len_col:
                    len_col = len(str(row[title_iterator]))

            len_for_col.append(len_col)

        how_wide = 0
        for name in title_list:
            x = (len_for_col[title_list.index(name)])
            how_wide += (len(("|{: <" + str(x + 2) + "}").format(name)))
        print('-' * how_wide)

        for name in title_list:
            print("|", end="")
            x = (len_for_col[title_list.index(name)])
            print(("{: <" + str(x + 2) + "}").format(name), end="")
        print("|")
        print('-' * how_wide)

        for row in table:
            print("|", end="")
            for element in row:
                x = (len_for_col[row.index(element)])
                print(("{: <" + str(x + 2) + "}|").format(element), end="")
            print()
        print('-' * how_wide)

    @staticmethod
    def print_menu(title, list_options, exit_message):
        '''
        Handles displaying menu.
        Args:
            title (str): menu title
            list_options (list): list of strings - options that will be shown in menu
            exit_message (str): the last option with (0) (example: "Back to main menu")
        '''
        n = 1
        print('{}'.format(title))
        for item in list_options:
            print('\t({}) {}'.format(str(n), item))
            n += 1
        print('\t(0) {}'.format(exit_message))

    @staticmethod
    def get_inputs(list_labels, title):
        '''
        Gets list of inputs from the user.
        Sample call:
            get_inputs(["Name","Surname","email"],"Please provide your personal information")
        Args:
            list_labels: list of strings - labels of inputs
            title: title of the "input section".
        Returns:
            List of data given by the user.
        '''
        print(title)
        input_table = []
        for label in list_labels:
            input_table.append(input(label))
        return input_table

    @staticmethod
    def print_message(message):
        """
        Displays an error message.
        Args:
            message(str): error message to be displayed.
        """
        print(message)

    @staticmethod
    def print_submissions_list(submission_list, title):
        """
        :param submission_list: (list) list of submissions
        :param title: (string) heading of list
        :return: print full list of heading and submissions
        """
        os.system("clear")
        print(title+'\n')
        print("{:>15} {:>15} {:>15} {:>15} {:>15}"
              .format('SEND DATE:', 'NAME:', 'GRADE:', 'GITHUB LINK:', 'STUDENT ID:'))
        for sub in submission_list:
            print("{:>15} {:>15} {:>15} {:>15} {:>15}"
                  .format(sub.send_date, sub.name, sub.grade, sub.github_link, sub.student_id))
        print('\n')

    @staticmethod
    def print_data_list(title):
        '''
        Handles printing attribute names.
        '''
        os.system("clear")
        n = 1
        options = ['Name', 'Surname', 'email']
        print('{}:'.format(title))
        for item in options:
            print('\t({}) {}'.format(str(n), item))
            n += 1

    @staticmethod
    def print_assignments_list(assignments_list, title):
        """
        :param assignments_list: (list) list of assignments
        :param title: (string) heading of list
        :return: print full list of heading and assignments
        """
        os.system("clear")
        print(title)
        idx = 1

        for assign in assignments_list:
            print(idx,
                  assign.start_date,
                  assign.end_date,
                  assign.assignment_name)
            idx += 1

    @classmethod
    def print_student_teams(cls, stu_list):
        """
        :param stu_list: list of student objects
        :return: print students team in a pretty format :D
        """
        os.system('clear')
        team_names = []
        for team in stu_list:
            if team.team in team_names:
                pass
            else:
                team_names.append(team.team)
        for team_name in team_names:
            print(team_name+':')
            for student in stu_list:
                if student.team == team_name:
                    print(student.name, student.surname)
            print('\n')

    @staticmethod
    def print_student_average_grades(student_grades):
        '''
        Displays each students grades.
        '''
        os.system('clear')
        print("STUDENTS' GRADE AVERAGE:\n")
        for key, value in student_grades.items():
            print(key, value[0], value[1], value[2])

    @staticmethod
    def print_full_report_of_students_performance(performance, title):
        """
        :param title: title of table to print
        :param performance: list of students performance data
        :return: prints table with data
        """
        if len(performance) < 2:
            os.system('clear')
            print("There is no submissions in given date time :( \n\n\n")
            Ui.get_inputs([''], 'Enter to go back')
            os.system('clear')
        else:
            os.system('clear')
            print(title, '\n')
            for row in performance:
                print("{:>15} {:>15} {:>15} {:>15} {:>15}".format(row[0], row[1], row[2], row[3], row[4]))
            print('\n')
            Ui.get_inputs([''],'Enter to go back')
            os.system('clear')

    @staticmethod
    def create_person_table_to_print(object_list):
        '''
        Creates table to put into printing function for person.
        '''

        table =[]
        for person in object_list:
            person_attributes = list(map(str, [person.id, person.name, person.surname, person.email, person.status]))
            table.append(person_attributes)

        return table

    @staticmethod
    def create_student_table_to_print(object_list):
        '''
        Creates table to put into printing function for student
        '''

        table = []
        for student in object_list:
            student_attributes = [student.id, student.name, student.surname, student.email, student.status, student.team, student.card]
            table.append(student_attributes)
        return table

    @staticmethod
    def create_submission_table_to_print(object_list):
        '''
        Creates table to put into printing function for submission
        '''
        table = []
        for submission in object_list:
            sub = [submission.name, submission.grade]
            table.append(sub)
        return table
