import datetime
from flask import Flask, render_template, request, redirect, url_for, session as log_in
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


from models.team import *
from models.assignments import *
from models.model import *
from models.submission import *
from models.student import *
from models.attendance import *


@app.route('/')
def home():
    """
    Handles redirecting for home page based on whenever user is logged or not.
    """
    if not log_in.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html', user_id=log_in['user_id'], user_status=log_in['user_status'],
                               user=log_in['user'])


@app.route('/login', methods=['POST'])
def user_check():
    """
    Checks for user in database based on given username and password.
    """
    username = request.form['username']
    password = request.form['password']
    status = request.form['status']
    person = Model.find_user(username, password, status)
    if not person:
        return render_template('error_login.html')
    log_in['logged_in'] = True
    log_in['user_id'] = person.id
    log_in['user_status'] = person.status
    log_in['user'] = person.name + ' ' + person.surname
    return home()


@app.route("/logout")
def logout():
    """
    Drops the session.
    """
    log_in['logged_in'] = False
    log_in['user_id'] = None
    log_in['user_status'] = None
    log_in['user'] = None
    return home()


@app.route("/students", methods=['GET', 'POST'])
def students_list():
    """ Shows list of students """
    if request.method == "POST":
        student_id = request.form['student_id']
        card = request.form['select-card']
        team = request.form['select-team']
        Student.edit_student_team_card(student_id, team, card)
        return redirect(url_for('students_list'))
    else:
        teams = Team.get_all()
        students = Student.get_all()
        cards = ['green', 'yellow', 'red']
        return render_template("show_students_list.html", students=students, teams=teams, cards=cards,
                               user_id=log_in['user_id'], user_status=log_in['user_status'], user=log_in['user'])


@app.route("/students-attendance", methods=['GET', 'POST'])
def students_attendance():
    """ Check attendance of students :
        if method is get - shows students attendance
        if method is post - check students attendance
    """
    students = Student.get_all()
    attendances = Attendance.get_all()
    counted_days = Student.count_days()

    if request.method == "GET":
        return render_template("student_show_attendence.html", students=students, attendances=attendances,
                               counted_days=counted_days, user_id=log_in['user_id'], user_status=log_in['user_status'],
                               user=log_in['user'])
    else:
        index = 0
        for student in students:
            index += 1
            status = request.form[str(index)]
            date = request.form['choose-date']
            student_id = request.form['student_id'+str(index)]
            Student.add_student_attendance(date, status, student_id)
        return redirect(url_for("students_attendance"))


@app.route("/check_attendance", methods=['GET', 'POST'])
def check_attendance():
    students = Student.get_all()
    current_date = str(datetime.date.today())
    return render_template("attendance.html", students=students, current_date=current_date)


@app.route("/edit_student/<student_id>", methods=['POST'])
def edit_student(student_id):
    """ Edits student with selected id in the database
    If the method was GET it shows edit student form.
    If the method was POST it should update student data in database.
    """
    new_name = request.form['new_fname']
    new_surname = request.form['new_lname']
    new_email = request.form['new_email']
    Student.edit_student(student_id, new_name, new_surname, new_email)
    return redirect(url_for('students_list'))

@app.route("/remove_student/<student_id>")
def remove_student(student_id):
    """ Removes student with selected id from the database """
    Student.remove_student(student_id)
    return redirect(url_for('students_list'))


@app.route("/mentors")
def mentors_list():
    """ Shows list of mentors """
    mentors = Mentor.get_all()
    return render_template("show_mentors_list.html", mentors=mentors, user_id=log_in['user_id'],
                           user_status=log_in['user_status'], user=log_in['user'])


@app.route("/submissions", methods=['POST', "GET"])
def submissions_list():
    """Shows list of submissions"""
    submissions = db.session.query(Submission).all()
    options = Submission.get_sub_distinct()

    students = Student.get_all()
    if request.method == "GET":
        return render_template("submission_table.html", submissions=submissions, options=[option.name for option in options] , students=students,
                               user_id=log_in['user_id'], user_status=log_in['user_status'], user=log_in['user'])

    if request.method == "POST":
        option = request.form["select-submission"]
        select_option = "--select--"
        return render_template("submission_table.html", submissions=submissions, option=option,
                               options=[option.name for option in options], select_option=select_option, students=students,
                               user_id=log_in['user_id'], user_status=log_in['user_status'], user=log_in['user'])


@app.route("/add_mentor", methods=['POST'])
def add_mentor():
    """Shows list of submissions"""
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        name = request.form['fname']
        surname = request.form['lname']
        email = request.form['email']
        Mentor.add_mentor(name, surname, email)
        return redirect(url_for('mentors_list'))


@app.route("/edit_mentor/<mentor_id>", methods=['GET', 'POST'])
def edit_mentor(mentor_id):
    """ Edits mentor with selected id in the database
    If the method was GET it shows edit mentor form.
    If the method was POST it should update mentor data in database.
    """
    new_name = request.form['new_fname']
    new_surname = request.form['new_lname']
    new_email = request.form['new_email']
    Mentor.edit_mentor(mentor_id, new_name, new_surname, new_email)
    return redirect(url_for('mentors_list'))


@app.route("/remove_mentor/<mentor_id>")
def remove_mentor(mentor_id):
    """ Removes student with selected id from the database """
    Mentor.remove_mentor(mentor_id)
    return redirect(url_for('mentors_list'))


@app.route("/teams")
def teams_list():
    """ Shows list of teams"""
    teams = Team.get_all()
    students = Student.get_all()
    return render_template("teams.html", teams=teams, students=students, user_id=log_in['user_id'],
                           user_status=log_in['user_status'], user=log_in['user'])


@app.route("/assignments")
def assignments_list():
    """ Shows list of students """
    assignments = Assignments.get_all()
    return render_template("show_assignments.html", assignments=assignments, user_id=log_in['user_id'],
                           user_status=log_in['user_status'], user=log_in['user'])


@app.route("/add_assignment", methods=['POST', "GET"])
def add_assignment():
    """ add assignment to db """
    if request.method == "GET":
        return render_template("add_assignment.html",user_status=log_in['user_status'],
                               user=log_in['user'])

    elif request.method == "POST":
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]
        assignment_name = request.form["assignment_name"]
        assignment_link = request.form['assignment_link']
        Assignments.add_assignment(start_date, end_date, assignment_name, assignment_link)
        return redirect(url_for('assignments_list'))


@app.route("/edit_team_name/<team_id>", methods=['GET', 'POST'])
def edit_team_name(team_id):
    """ Edit name of team"""
    new_name = request.form['name']
    Team.edit_team(team_id, new_name)
    return redirect(url_for('teams_list'))



@app.route("/add_student", methods=['POST', "GET"])
def add_student():
    """ Add student to database """
    if request.method == "GET":
        return render_template("add.html", user_id=log_in['user_id'], user_status=log_in['user_status'],
                               user=log_in['user'])
    elif request.method == "POST":
        name = request.form["fname"]
        surname = request.form["lname"]
        email = request.form["email"]
        Student.add_student(name, surname, email)
        return redirect(url_for('students_list'))


@app.route("/add_team", methods=['GET', 'POST'])
def add_team():
    """ Add new team """
    if request.method == 'GET':
        return render_template("add_new_team.html", user_id=log_in['user_id'], user_status=log_in['user_status'],
                               user=log_in['user'])
    else:
        team_name = request.form['new-team-name']
        Team.add_team(team_name)
        return redirect(url_for('teams_list'))


@app.route("/remove_student_team")
def remove_student_from_team():
    """ Remove student from a team"""
    student_id = request.args['student_id']
    student_id = int(student_id)
    Student.remove_student_team(student_id)
    return redirect(url_for('teams_list'))


@app.route("/submit_form", methods=["POST"])
def submission_form():
    if request.method == 'POST':
        sub_name = request.form["submission_name"]
        sub_link = request.form["submission_link"]
        sub_start_date = request.form["submission_start_date"]
        sub_end_date = request.form["submission_end_date"]

        return render_template("submission_form.html", sub_name=sub_name, sub_link=sub_link,
                               sub_start_date=sub_start_date, sub_end_date=sub_end_date,
                               user_id=log_in['user_id'], user_status=log_in['user_status'], user=log_in['user'])


@app.route("/submit_assignment/<user_id>", methods=['POST'])
def submit_assignment(user_id):
    """ Add submission to submission list"""
    students = Student.get_all()
    name = request.form["submission_name"]
    link = request.form["submission_link"]
    if not link:
        link = None
    end_date = request.form["submission_end_date"]
    if request.method == 'POST':
        if request.form["select_form"] == "Submit assignment":
            my_submission = Submission(end_date, 0, name, link, user_id)
            submission_status = Submission.add_submission(my_submission.send_date, my_submission.grade,
            my_submission.name, my_submission.github_link, my_submission.student_id)

            return render_template("submit_assignment_information.html", submission_status=submission_status,
                                   user_id=log_in['user_id'], user_status=log_in['user_status'], user=log_in['user'])
        else:
            same_team = []
            student_searched = Student.get_by_id(user_id)  # student with needed id
            for student in students:
                if student.team == student_searched.team:
                    same_team.append(student)

            for same_team_student in same_team:
                for student in students:
                    if student.team == same_team_student.team:

                        my_submission = Submission(end_date, 0, name, link, student.id)
                        submission_status = Submission.add_submission(my_submission.send_date, my_submission.grade,
                        my_submission.name, my_submission.github_link, my_submission.student_id)
                return render_template("submit_assignment_information.html", submission_status=submission_status,
                                       user_id=log_in['user_id'], user_status=log_in['user_status'],
                                       user=log_in['user'])


@app.route("/update_grade", methods=['POST'])
def update_grade():
    """ Update grade of student submission in database """
    grade = request.form['grade']
    student_id = request.form['student_id']
    submission_name = request.form["submission_name"]
    Submission.upgrade_grade(grade, student_id, submission_name)

    return redirect(url_for('submissions_list'))


@app.route("/remove_team/<team_id>")
def remove_team(team_id):
    """
    Removes whole team with members
    """
    Team.remove_team(team_id)
    return redirect(url_for('teams_list'))


@app.route("/students_grades", methods=['GET', 'POST'])
def show_students_grades():
    """ Shows students grades """
    if request.method == "GET":
        students = Student.get_all()
        grades = Student.get_average()
        return render_template("show_grades.html", students=students, grades=grades, user_id=log_in['user_id'],
                               user_status=log_in['user_status'], user=log_in['user'])
    elif request.method == 'POST':
        start = request.form['start_date']
        end = request.form['end_date']
        student_id = request.form['student_id']
        performance = Student.get_performance(student_id, start, end)
        if performance:
            return render_template("get_performance.html", performance=performance, user_id=log_in['user_id'],
                                   user_status=log_in['user_status'], user=log_in['user'])
        return redirect(url_for('show_students_grades'))

@app.route("/grades", methods=["GET"])
def show_all_grades():
    """
    Shows all grades for individual student.
    """
    submissions = Submission.get_all()
    return render_template("grades.html", submissions=submissions, user_id=log_in['user_id'],
                           user_status=log_in['user_status'], user=log_in['user'])



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
