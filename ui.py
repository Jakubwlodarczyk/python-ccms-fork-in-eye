import os


class Ui:
    '''
    Handles user interface.
    '''

    @staticmethod
    def print_table(object_list, title):
        '''
        Displays table with data.
        Args:
            object_list: list of objects to unpack into table.
            title: string containing main table header.
        '''
        os.system("clear")
        print(title)
        title_list = ['ID', 'Name', 'Surname', 'Email', 'Status']
        table = []
        for obj in object_list:
            obj_atrr = [obj.id, obj.name, obj.surname, obj.email, obj.status]
            table.append(obj_atrr)

        len_for_col = []
        for title_iterator in range(len(title_list)):
            len_col = len(title_list[title_iterator])
            for row in table:
                if len(row[title_iterator]) > len_col:
                    len_col = len(row[title_iterator])

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
    def print_student_table(object_list, title):
        '''
        Displays table with data.
        Args:
            object_list: list of objects to unpack into table.
            title: string containing main table header.
        '''
        os.system("clear")
        print(title)
        title_list = ['ID', 'Name', 'Surname', 'Email', 'Status', 'Team', 'Card']
        table = []
        for obj in object_list:
            obj_atrr = [obj.id, obj.name, obj.surname, obj.email, obj.status, obj.team, obj.card]
            table.append(obj_atrr)

        len_for_col = []
        for title_iterator in range(len(title_list)):
            len_col = len(title_list[title_iterator])
            for row in table:
                if len(row[title_iterator]) > len_col:
                    len_col = len(row[title_iterator])

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
            input_table.append(input(label ))
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
        idx = 1
        for sub in submission_list:
            print(idx,
                  sub.send_date,
                  sub.submission_name,
                  sub.grade,
                  sub.github_link,
                  sub.id)
            idx += 1
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

    @classmethod
    def print_submissions(cls, submission_list):
        '''
        Displays assignments with grades for student.
        '''
        title = 'YOUR SUBMISSIONS'
        title_list = ['Assignment name:', 'Grade:']
        table = []
        for sub in submission_list:
            sub = [sub.submission_name, sub.grade]
            table.append(sub)

        len_for_col = []
        for title_iterator in range(len(title_list)):
            len_col = len(title_list[title_iterator])
            for row in table:
                if len(row[title_iterator]) > len_col:
                    len_col = len(row[title_iterator])

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

    def print_student_average_grades(student_grades):
        '''
        Displays each students grades.
        '''
        os.system('clear')
        print("STUDENTS' GRADE AVERAGE:\n")
        print(student_grades)
        for key, value in student_grades:
            print(key, value)
