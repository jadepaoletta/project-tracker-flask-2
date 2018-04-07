"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template, flash

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template('student_info.html', github=github, first=first,
                            last=last)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add", methods=['GET', 'POST'])
def student_add():
    """Add a student."""
    # import pdb; pdb.set_trace()
    # print request.form

    if request.method == 'POST':
        first = request.form.get("first")
        last = request.form.get("last")
        github = request.form.get("github")

        hackbright.make_new_student(first, last, github)

        flash("Successfully added student {} {}".format(first, last))
        return render_template("student_add.html", link=True, github=github)


    return render_template("student_add.html", link=False)

if __name__ == "__main__":
    app.secret_key = 'abc'
    hackbright.connect_to_db(app)
    app.run(debug=True)
