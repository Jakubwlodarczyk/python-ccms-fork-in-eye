from ui import Ui

class Common:


    @staticmethod
    def get_table_from_file(file_name):
        """
        Reads csv file and returns it as a list of lists.
        Lines are rows columns are separated by ";"

        Args:
            file_name (str): name of file to read

        Returns:
            List of lists read from a file.
        """
        with open(file_name, "r") as file:
            lines = file.readlines()
        table = [element.replace("\n", "").split(",") for element in lines]
        return table

    # write a @table into a file
    #
    # @file_name: string
    # @table: list of lists of strings
    @staticmethod
    def write_table_to_file(file_name, table):
        """
        Writes list of lists into a csv file.

        Args:
            file_name (str): name of file to write to
            table: list of lists to write to a file

        Returns:
            None
        """
        with open(file_name, "w") as file:
            for record in table:
                row = ','.join(record)
                file.write(row + "\n")
    @staticmethod
    def error_integer_handling(chosen_option, value_of_possible_options):
        """

        :param chosen_option: user's input.
        :param value_of_possible_options: how many options users could take? Don't count 0 - exit
        :return: True or False. Will be useful to control while loop in other part of program. If True, continue program.
        """
        try:
            int(chosen_option)
            if int(chosen_option) < 0 or int(chosen_option) > value_of_possible_options:
                raise ValueError
        except TypeError:
            print("Wrong input.")
            m = Ui.get_inputs([""], "")
            return False
        except ValueError:
            print("It must be integer between 1 and " + str(value_of_possible_options))
            m = Ui.get_inputs([""], "")
            return False
        return True

    @staticmethod
    def check_date(max_day, user_day):
        """
        :param max_day: int (e.g. 30)
        :param user_day: str (e.g. 32)
        :return: True (if
        """

        try:
            if int(user_day) > max_day:
                raise ValueError
            return True
        except ValueError:
            return False








