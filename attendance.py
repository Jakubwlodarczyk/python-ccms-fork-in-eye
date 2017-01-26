from ui import Ui
import os
import datetime
from Common import Common

class Attendance:

    attendances_list = []

    def __init__(self, data, status, id=None):
        self.data = data
        self.status = status
        self.id = id


    @staticmethod
    def check_attendance():
        pass


    @staticmethod
    def set_date():
        """
        :return: date of chosen day as list with strings (e.g. ["2017", "05", "03"]
        """
        date = None
        while True:
            os.system("clear")
            options_list = Ui.get_inputs(["1 - Check attendance for today\n2 - Choose another day\n0 - Go back\n"], "Do \
you want to check attendance for today or set another day? \n")
            if Common.error_integer_handling(options_list[0], 2):
                if options_list[0] == "1":
                    today = datetime.date.today()
                    today = str(today)
                    today_as_list = today.split("-")
                    date = today_as_list
                    return date
                if options_list[0] == "2":
                    while True:
                        os.system("clear")
                        options_list = Ui.get_inputs(
                            ["Year (e.g. 2017): ", "Month (e.g. 01): ", "Day (e.g. 23): "], "Write date you \
want to check attendance: \n")
                        today = datetime.date.today()
                        today = str(today)
                        date = [options_list[0], options_list[1], options_list[2]]
                        if len(options_list[2]) < 2 or len(options_list[2]) > 2:
                            continue
                        if len(options_list[1]) < 2 or len(options_list[2]) > 2:
                            continue
                        if len(options_list[0]) < 4 or len(options_list[2]) > 4:
                            continue
                        if Common.error_integer_handling(options_list[0], 9999) and Common.error_integer_handling(options_list[1], 12) and Common.error_integer_handling(options_list[2], 31):
                            if options_list[1] == "02":
                                if Common.check_date(30, options_list[2]):
                                    print(date)
                                    return date
                                else:
                                    Ui.print_error_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "04":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_error_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "06":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_error_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "09":
                                print("Jestem tutaj 11")
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_error_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "11":
                                if Common.check_date(30, options_list[2]):
                                    return date
                                else:
                                    Ui.print_error_message("Can't accept this date.")
                                    wait = Ui.get_inputs([""], "")
                            if options_list[1] == "01" or options_list[1] == "03" or options_list[1] == "05" or options_list[1] == "07" or options_list[1] == "08" or options_list[1] == "10" or options_list[1] == "12":
                                return date
                        else:
                            Ui.print_error_message("Can't accept this date.")
                            wait = Ui.get_inputs([""], "")
                            continue
            else:
                 continue
            date = [options_list[0], options_list[1], options_list[2]]
            print(date)
            wait = Ui.get_inputs([""], "")
            return date






    # @staticmethod
    # def choose_student():
    #     while True:
    #         os.system("clear")
    #         print("Which student do you want to choose?\n")
    #         for number, student in enumerate(Student.student_list):
    #             print("  {}: {}".format(number + 1, student))
    #         print("  0: Go back\n")
    #
    #         option_list = Ui.get_inputs([""],"")
    #         my_option = option_list[0]
    #         try:
    #             my_option = int(my_option)
    #             if int(my_option) < 0 or int(my_option) > len(Student.student_list):
    #                 raise ValueError
    #         except TypeError:
    #             print("Wrong input.")
    #             m = Ui.get_inputs([""], "")
    #             continue
    #         except ValueError:
    #             print("It must be integer between 1 and " + str(len(Student.student_list)) + " or 0.")
    #             m = Ui.get_inputs([""], "")
    #             continue
    #         Attendance.create_attendace_object_for_student(Student.student_list[my_option - 1])


Attendance.set_date()




