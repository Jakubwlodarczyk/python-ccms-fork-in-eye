import random
import string

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
