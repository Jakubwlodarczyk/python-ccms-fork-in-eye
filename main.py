from flask import Flask, render_template, request, redirect, url_for
from models.model import Model
from models.student import Student
from models.attendance import Attendance
from models.submission import Submission
from models.assignments import Assignments


app = Flask(__name__)


@app.route("/students")
def students_list():
    """ Shows list of students """
    teams = Model.create_teams_list()
    students = Model.students_get_all()
    return render_template("show_students_list.html", students=students, teams=teams)


@app.route("/students-attendance")
def students_attendance():
    students_bad = Model.students_get_all() #it's from database
    attendances = Attendance.create_objects_list_from_database()
    students = Student.student_presence(attendances, students_bad)
    counted_days = Student.count_days()  #Student.counted_days
    Student.current_score(students)
    return render_template("student_show_attendence.html", students=students, attendances=attendances, counted_days = counted_days)


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
    
    if request.method == "GET":
        return render_template("submission_table.html", submissions=submissions, options=options)
    if request.method == "POST":
        option = request.form["select-submission"]
        select_option = "--select--"
        return render_template("submission_table.html", submissions=submissions, option=option, options=options, select_option=select_option)


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
        return render_template("add.html")
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
        return render_template("add_new_team.html")
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


@app.route("/submit_changes")
def submit_students_changes():
    return "<h2>TROLololololOoOOo !!!!!!</h2>"


@app.route("/submit_assignment/<name>/<link>/<start_date>/<end_date>", methods=['POST'])
def submit_asignment(name, link, start_date, end_date):
    """ Add submission to submission list"""
    if request.method == 'POST':
        submission = request.form["select_submit_assignment"]
        submission2 = request.form["select_submit_assignment_as_a_team"]
        print(submission)
        print(submission2)
        student = Student("the_id", "name", "surname", "email", "password", "status")

        my_submission = Submission(end_date, '0', name, link, student.id)
        submits_from_db = Model.create_submission_list()
        for submit in submits_from_db:
            if submit.name == my_submission.name:
                if submit.student_id == my_submission.student_id:
                    return "<h2>Assignment is already submitted</h2>"



        Model.add_submission(my_submission)
        return render_template("submit_assignment_information.html")





if __name__ == "__main__":
    app.run(debug=True)
