from flask import Flask, render_template, request, redirect, url_for, session, abort
import os
from models.model import Model
from models.student import Student
from models.attendance import Attendance
from models.submission import Submission
from models.assignments import Assignments
import datetime


app = Flask(__name__)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html', user_id=session['user_id'], user_status=session['user_status'], user=session['user'])


@app.route('/login', methods=['POST'])
def user_check():
    username = request.form['username']
    password = request.form['password']
    status = request.form['status']
    person = Model.find_user(username, password, status)
    if not person:
        return render_template('error_login.html')
    session['logged_in'] = True
    session['user_id'] = person.id
    session['user_status'] = person.status
    session['user'] = person.name + ' ' + person.surname
    return home()


@app.route("/logout")
def logout():
    session['logged_in'] = False
    session['user_id'] = None
    session['user_status'] = None
    session['user'] = None
    return home()


@app.route("/students", methods=['GET', 'POST'])
def students_list():
    """ Shows list of students """
    if request.method == "POST":
        student_id = request.form['student_id']
        card = request.form['select-card']
        team = request.form['select-team']
        Model.update_students_team(student_id, team, card)
        return redirect(url_for('students_list'))
    else:
        teams = Model.create_teams_list()
        students = Model.students_get_all()
        cards = ['green', 'yellow', 'red']
        return render_template("show_students_list.html", students=students, teams=teams, cards=cards, user_id=session['user_id'], user_status=session['user_status'], user=session['user'])


@app.route("/students-attendance", methods=['GET', 'POST'])
def students_attendance():
    students_bad = Model.students_get_all()
    attendances = Attendance.create_objects_list_from_database()
    students = Student.student_presence(attendances, students_bad)
    counted_days = Student.count_days()  # Student.counted_days
    Student.current_score(students)

    if request.method == "GET":
        return render_template("student_show_attendence.html", students=students, attendances=attendances,
                               counted_days=counted_days, user_id=session['user_id'], user_status=session['user_status'], user=session['user'])
    else:
        values = [] # students presence
        for index, student in enumerate(students):
            option = request.form[str(index + 1)]
            values.append(option)
        student_ids = []
        for student in students:
            student_ids.append(student.id)
        Model.create_attendance(values, request.form['choose-date'], student_ids)
        return redirect(url_for("students_attendance"))


@app.route("/check_attendance", methods=['GET', 'POST'])
def check_attendance():
    students_bad = Model.students_get_all()
    attendances = Attendance.create_objects_list_from_database()
    students = Student.student_presence(attendances, students_bad)
    current_date = str(datetime.date.today())
    return render_template("attendance.html", students=students, current_date = current_date)


@app.route("/edit_student/<student_id>", methods=['GET', 'POST'])
def edit_student(student_id):
    """ Edits student with selected id in the database
    If the method was GET it shows edit student form.
    If the method was POST it should update student data in database.
    """
    if request.method == 'GET':
        student = Model.get_student_by_id(student_id)
        old_name = student.name
        old_surname = student.surname
        old_email = student.email
        return render_template('edit_person_data.html', old_name=old_name, old_surname=old_surname, old_email=old_email)
    elif request.method == 'POST':
        student = Model.get_student_by_id(student_id)
        new_name = request.form['new_fname']
        new_surname = request.form['new_lname']
        new_email = request.form['new_email']
        Model.update_student_data(student_id, new_name, new_surname, new_email)
    return redirect(url_for('students_list'))


@app.route("/remove_student/<student_id>")
def remove_student(student_id):
    """ Removes student with selected id from the database """
    Model.delete_student(student_id)
    return redirect(url_for('students_list'))


@app.route("/mentors")
def mentors_list():
    """ Shows list of mentors """
    mentors = Model.mentors_get_all()
    return render_template("show_mentors_list.html", mentors=mentors)


@app.route("/submissions", methods=['POST', "GET"])
def submissions_list():
    """Shows list of submissions"""
    options = Model.submission_list_distinct()
    submissions = Submission.submission_all()
    students = Model.students_get_all()
    for student in students:
        print(student.name)
    if request.method == "GET":
        return render_template("submission_table.html", submissions=submissions, options=options, students=students)
    if request.method == "POST":
        option = request.form["select-submission"]
        select_option = "--select--"
        return render_template("submission_table.html", submissions=submissions, option=option,
                               options=options, select_option=select_option, students=students)


@app.route("/add_mentor", methods=['POST', "GET"])
def add_mentor():
    """Shows list of submissions"""
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        name = request.form['fname']
        surname = request.form['lname']
        email = request.form['email']
        Model.add_new_mentor(name, surname, email)
        return redirect(url_for('mentors_list'))


@app.route("/edit_mentor/<mentor_id>", methods=['GET', 'POST'])
def edit_mentor(mentor_id):
    """ Edits mentor with selected id in the database
    If the method was GET it shows edit mentor form.
    If the method was POST it should update mentor data in database.
    """
    if request.method == 'GET':
        mentor = Model.get_mentor_by_id(mentor_id)
        old_name = mentor.name
        old_surname = mentor.surname
        old_email = mentor.email
        return render_template('edit_person_data.html', old_name=old_name, old_surname=old_surname, old_email=old_email)
    elif request.method == 'POST':
        mentor = Model.get_mentor_by_id(mentor_id)
        new_name = request.form['new_fname']
        new_surname = request.form['new_lname']
        new_email = request.form['new_email']
        Model.update_mentor_data(mentor_id, new_name, new_surname, new_email)
        return redirect(url_for('mentors_list'))


@app.route("/remove_mentor/<mentor_id>")
def remove_mentor(mentor_id):
    """ Removes student with selected id from the database """
    Model.delete_mentor(mentor_id)
    return redirect(url_for('mentors_list'))


@app.route("/teams")
def teams_list():
    """ Shows list of teams"""
    teams = Model.create_teams_list()
    students = Model.students_get_all()
    return render_template("teams.html", teams=teams, students=students)


@app.route("/assignments")
def assignments_list():
    """ Shows list of students """
    assignments = Assignments.assignments_all()
    return render_template("show_assignments.html", assignments=assignments)


@app.route("/edit_team_name", methods=['GET', 'POST'])
def edit_team_name():
    """ Edit name of team"""
    if request.method == "POST":
        old_name = request.args['team_name']
        new_name = request.form['name']
        Model.update_team_name(old_name, new_name)
        return redirect(url_for('teams_list'))
    else:
        team_id = request.args['team_id']
        team_name = request.args['team_name']
        return render_template("edit_team_name.html", team_id=team_id, team_name=team_name)


@app.route("/add_student", methods=['POST', "GET"])
def add_student():
    """ Add student to database """
    if request.method == "GET":
        return render_template("add.html", user_id=session['user_id'], user_status=session['user_status'], user=session['user'])
    if request.method == "POST":
        person = []
        person.append([request.form["fname"], request.form["lname"],
                       request.form["email"]])
        Model.save_new_student(person)
        return redirect(url_for('students_list'))


@app.route("/add_team", methods=['GET', 'POST'])
def add_team():
    """ Add new team """
    if request.method == 'GET':
        return render_template("add_new_team.html", user_id=session['user_id'], user_status=session['user_status'], user=session['user'])
    else:
        team_name = request.form['new-team-name']
        Model.add_team(team_name)
        return redirect(url_for('teams_list'))


@app.route("/remove_student_team")
def remove_student_from_team():
    """ Remove student from a team"""
    students = Model.students_get_all()
    student_id = request.args['student_id']
    student_id = int(student_id)
    for student in students:
        if student.id == student_id:
            Model.remove_student_team(student_id)
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
                               user_id=session['user_id'], user_status=session['user_status'], user=session['user'])


@app.route("/submit_assignment", methods=['POST'])
def submit_assignment():
    """ Add submission to submission list"""

    student_example = Student("the_id", "name", "surname", "email", "password", "status", "green", "Miszczowie")
    students = Model.students_get_all()
    name = request.form["submission_name"]
    link = request.form["submission_link"]
    end_date = request.form["submission_end_date"]
    if request.method == 'POST':
        if request.form["select_form"] == "Submit assignment":
            my_submission = Submission(end_date, '0', name, link, student_example.id)
            submission_status = Model.add_submission(my_submission)
            return render_template("submit_assignment_information.html", submission_status=submission_status,
                                   user_id=session['user_id'], user_status=session['user_status'], user=session['user'])
        else:
            my_submission = Submission(end_date, '0', name, link, student_example.id)
            Model.add_submission(my_submission)
            Model.create_submission_list()
            for student in students:
                if student.team == student_example.team:
                    my_submission = Submission(end_date, '0', name, link, student.id)
                    submission_status = Model.add_submission(my_submission)
            return render_template("submit_assignment_information.html", submission_status=submission_status,
                                   user_id=session['user_id'], user_status=session['user_status'], user=session['user'])


@app.route("/update_grade", methods=['POST'])
def update_grade():
    """ Update grade of student submission in database """
    grade = request.form['grade']
    student_id = request.form['student_id']
    Model.update_grades(student_id, grade)
    return redirect(url_for('submissions_list'))


@app.route("/remove_team", methods=["POST"])
def remove_team():
    team_name = request.form['team_name']
    team_id = request.form['team_id']
    Model.delete_team(team_id, team_name)
    return redirect(url_for('teams_list'))


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
