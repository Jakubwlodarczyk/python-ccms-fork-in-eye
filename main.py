from flask import Flask, render_template, request, redirect, url_for
from models.model import Model
from models.student import Student
from models.submission import Submission
from models.assignments import Assignments

app = Flask(__name__)


@app.route("/students")
def students_list():
    """ Shows list of students """
    students = Model.students_get_all()
    return render_template("show_students_list.html", students=students)


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
        update = Model.update_student_data(student_id, new_name, new_surname, new_email)
    return redirect(url_for('students_list'))


@app.route("/remove_student/<student_id>")
def remove_student(student_id):
    """ Removes student with selected id from the database """
    delete = Model.delete_student(student_id)
    return redirect(url_for('students_list'))


@app.route("/mentors")
def mentors_list():
    """ Shows list of mentors """
    mentors = Model.mentors_get_all()
    return render_template("show_mentors_list.html", mentors=mentors)


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
    delete = Model.delete_mentor(mentor_id)
    return redirect(url_for('mentors_list'))


@app.route("/submissions")
def submissions_list():
    """Shows list of submissions"""
    submissions = Submission.submission_all()
    return render_template("submission_table.html", submissions=submissions)


@app.route("/teams")
def teams_list():
    """ Shows list of teams"""

    teams = Student.create_teams_list()
    students = Student.students_all()
    return render_template("teams.html", teams=teams, students=students)


@app.route("/assignments")
def assignments_list():
    """ Shows list of students """
    assignments = Assignments.assignments_all()
    return render_template("show_assignments.html", assignments=assignments)


if __name__ == "__main__":
    app.run(debug=True)
