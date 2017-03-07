from flask import Flask, render_template, request, redirect, url_for
from models.model import Model
from models.submission import Submission
from models.assignments import Assignments

app = Flask(__name__)


@app.route("/students")
def students_list():
    """ Shows list of students """
    students = Model.students_get_all()
    return render_template("show_students_list.html", students=students)


@app.route("/mentors")
def mentors_list():
    """ Shows list of mentors """
    mentors = Model.mentors_get_all()
    return render_template("show_mentors_list.html", mentors=mentors)


@app.route("/submissions")
def submissions_list():
    """Shows list of submissions"""
    submissions = Submission.submission_all()
    return render_template("submission_table.html", submissions=submissions)


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

if __name__ == "__main__":
    app.run(debug=True)
