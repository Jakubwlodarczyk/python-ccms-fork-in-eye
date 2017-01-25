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

    def user_password_check(login, password, users_list):
        '''
        Args:
        email(login) from inputs.
        password from inputs.
        Checks if given user exists.
        Checks if password for given user is correct.
        '''
        for objects_list in all_users:
            for person in objects_list:
                for data in person:
                    if data[2] == email and data[3] == password:
                        return True
                    else:
                        return False
