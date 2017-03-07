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
    students = Model.students_get_all()
    return render_template("show_students_list.html", students=students)


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


@app.route("/add_mentor", methods=['POST', "GET"])
def add_mentor():
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


@app.route("/submissions")
def submissions_list():
    """Shows list of submissions"""
    submissions = Submission.submission_all()
    students = Model.students_get_all()
    return render_template("submission_table.html", submissions=submissions, students=students)


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
        return redirect('/teams')
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
        return redirect('/teams')


@app.route("/remove_student_team")
def remove_student_from_team():
    """ Remove student from a team"""
    students = Model.students_get_all()
    student_id = request.args['student_id']
    student_id = int(student_id)
    print(type(student_id))
    for student in students:
        if student.id == student_id:
            print(student_id)
            Model.remove_student_team(student_id)
    return redirect('/teams')


if __name__ == "__main__":
    app.run(debug=True)
