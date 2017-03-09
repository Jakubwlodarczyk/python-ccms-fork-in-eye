import sqlite3


class Assignments:
    """
    Class Assignments
    handle assignments objects (assignment list)
    """
    assignments_list = []

    def __init__(self, start_date, end_date, assignment_name, link):
        self.start_date = str(start_date)
        self.end_date = str(end_date)
        self.assignment_name = str(assignment_name)
        self.link = link

    @classmethod
    def assignments_all(cls):
        """
        Creates abjects based on data from database.
        :param file_path:
        :return:
        """
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        name_q = "SELECT start_date, end_date, name, link  FROM assignments;"
        name_db = c.execute(name_q)
        conn.commit()

        assignments_list = []

        for row in name_db:
            start_date = row[0]
            end_date = row[1]
            name = row[2]
            link = row[3]
            full_name = cls(start_date, end_date, name, link)
            assignments_list.append(full_name)
        conn.close()
        return assignments_list
