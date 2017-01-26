import os

class Ui:
    '''
    Handles user interface.
    '''
    @staticmethod
    def print_table(table, title_list):
        '''
        Displays table with data.
        Args:
            table: list of lists - table to display created in Common.py.
            title_list: list containing table headers.
        '''
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
        print('{}:'.format(title))
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
    def print_error_message(message):
        """
        Displays an error message.
        Args:
            message(str): error message to be displayed.
        """

        print(message)

    @staticmethod
    def print_staff_list(people_list, title):
        """
        :param people_list: list of object of people
        :param title: (string) name of printing heading
        :return: print full list with heading and staff members
        """
        os.system("clear")
        print(title)
        for person in people_list:
            print(person.id,
                  person.name,
                  person.surname,
                  person.email,
                  person.status)

    @staticmethod
    def print_submissions_list(submission_list, title):
        """
        :param submission_list: (list) list of submissions
        :param title: (string) heading of list
        :return: print full list of heading and submissions
        """
        os.system("clear")
        print(title)
        idx = 1
        for sub in submission_list:
            print(idx,
                  sub.start_date,
                  sub.end_date,
                  sub.submission_name,
                  sub.grade,
                  sub.github_link,
                  sub.id)
            idx += 1

    @staticmethod
    def print_data_list(title):
        '''
        Handles printing atributte names.
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
