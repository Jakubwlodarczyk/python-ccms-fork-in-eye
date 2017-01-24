class Ui:
    '''
    Handles user interface.
    '''
    def print_table(self, table, title_list):
        '''
        Displays table with data.
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

    def print_menu(self, title, list_options, exit_message):
        '''
        Handles displaying menu.
        '''
        n = 1
        print('{}:'.format(title))
        for item in list_options:
            print('\t({}) {}'.format(str(n), item))
            n += 1
        print('\t(0) {}'.format(exit_message))

    def get_inputs(self, list_labels, title):
        '''
        Gets list of inputs from the user.
        '''
        print(title)

        input_table = []
        for label in list_labels:
            input_table.append(input(label))
        return input_table
