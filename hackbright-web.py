from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    #Hey dictionary, here is a key (github) give me its value.  If you 
    #don't have this key, give me jhacks
    github = request.args.get('github','jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                        first=first,
                        last=last,
                        github=github)
    return html 


@app.route("/student_search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/new_student", methods=['POST'])
def add_student():
    """Show form for creating a new student."""

    return render_template("conf.html",
                        first_name=first-name,
                        last_name=last-name,
                        github="github")



@app.route("/homepage")
def homepage():

    return render_template('homepage.html')


@app.route("/user-page")
def user_page():

    

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
