import random
import string
from ui import *


class Common:

    @classmethod
    def write_table_to_file(cls, file_name, obj_list):  # for persons
        """
        Writes list of lists into a csv file.

        Args:
            file_name (str): name of file to write to
            table: list of lists to write to a file

        Returns:
            None
        """
        with open(file_name, "w") as f:
            for index, obj in enumerate(obj_list):
                obj_atrr = [str(obj.name), str(obj.surname), str(obj.email), str(obj.password), str(obj.status),
                            str(obj.id)]

                if index < len(obj_list) - 1:
                    f.write(','.join(obj_atrr) + '\n')
                else:
                    f.write(','.join(obj_atrr))


    @classmethod
    def write_students_to_file(cls, file_name, obj_list):
        """
        Writes list of lists into a csv file.

        Args:
            obj_list: list students objects
            file_name (str): name of file to write to
        Returns:
            None
        """
        with open(file_name, "w") as f:
            for index, obj in enumerate(obj_list):
                obj_atrr = [obj.name, obj.surname, obj.email, obj.password, obj.status, obj.id, obj.team, obj.card]

                if index < len(obj_list) - 1:
                    f.write(','.join(obj_atrr) + '\n')
                else:
                    f.write(','.join(obj_atrr))


    @classmethod
    def write_assignment_to_file(cls, file_name, obj_list):
        """
      Writes list of lists into a csv file.
        Args:
            obj_list: list of assignment objects
            file_name (str): name of file to write to
        Returns:
                None"""
        with open(file_name, "w") as f:
            for index, obj in enumerate(obj_list):
                obj_atrr = [str(obj.start_date), str(obj.end_date), str(obj.assignment_name)]

                if index < len(obj_list) - 1:
                    f.write(','.join(obj_atrr) + '\n')
                else:
                    f.write(','.join(obj_atrr))

    @classmethod
    def write_attendance_to_file(cls, file_name, obj_list):
        """
      Writes list of lists into a csv file.
        Args:
            file_name (str): name of file to write to
            obj_list: list of lists to write to a file
        Returns:
                None"""

        with open(file_name, "w") as f:
            for index, obj in enumerate(obj_list):
                obj_atrr = [str(obj.data), str(obj.status), str(obj.id)]
                if index < len(obj_list) - 1:
                    f.write(','.join(obj_atrr) + '\n')
                else:
                    f.write(','.join(obj_atrr))

    @classmethod
    def write_submission_to_file(cls, file_name, obj_list):
        """
      Writes list of lists into a csv file.
        Args:
            obj_list
            file_name (str): name of file to write to
            table: list of lists to write to a file
        Returns:
                None"""

        with open(file_name, "w") as f:
            for index, obj in enumerate(obj_list):
                obj_atrr = [str(obj.send_date), str(obj.submission_name), str(obj.grade), str(obj.github_link),
                            str(obj.id)]
                if index < len(obj_list) - 1:
                    f.write(','.join(obj_atrr) + '\n')
                else:
                    f.write(','.join(obj_atrr))

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
            print("It must be integer between 1 and " + str(value_of_possible_options) + " or 0. Press enter to try again.")
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

    @staticmethod
    def generate_random_id(table):
        """
        Generates random and unique string. Used for id/key generation.
        """
        characters = [['!', '@', '#', '$', '%', '^', '&', '*'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
        characters.append(list(string.ascii_uppercase))
        characters.append(list(string.ascii_lowercase))
        generated = ''
        is_unique = False
        id_table = []
        for element in table:
            id_table.append(element)

        while not is_unique:
            is_unique = True
            for i in range(2):
                generated += str(characters[0][random.randint(0, len(characters[0])-1)])
                generated += str(characters[1][random.randint(0, len(characters[1])-1)])
                generated += str(characters[2][random.randint(0, len(characters[2])-1)])
                generated += str(characters[3][random.randint(0, len(characters[3])-1)])
            if generated in id_table:
                is_unique = False

        return generated
