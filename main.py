from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True  




@app.route("/add", methods=['POST'])
def check_form():
    username = request.form['user-id']
    password = request.form["password"]
    pass_check = request.form["pass-check"]
    email = request.form["email"]
    errors = 0

    error1 = ""
    error2 = ""
    error3 = ""
    error4 = ""
    error5 = ""
    error6 = ""
    error7 = ""

    if (username.strip() == ""):
        error1 = "Please enter your name."
        errors += 1

    if (password.strip() == ""):
        error2 = "Please enter your password."
        errors += 1

    if (pass_check.strip() == ""):
        error3 = "Please enter your password verification."
        errors += 1
    
    if (len(username) < 3) or (len(username) > 20) or (" " in username):
        error4 = "Please enter a valid username. Within the range of 3 to 20 characters and contains no spaces"
        errors += 1

    if (len(password) < 3) or (len(password) > 20) or (" " in password):
        error5 = "Please enter a valid password Within the range of 3 to 20 characters and contains no spaces"
        errors += 1

    if (password != pass_check):
        error6 = "Make sure your password and password verification are the same."
        errors += 1

    if (email != ""):
        if (len(email) < 3) or (len(email) > 20) or (" " in email) or ("@" not in email) or ("." not in email):
            error7 = "Be sure to enter a valid email."
            errors += 1

    if (errors > 0):
        return render_template('form.html', name_mem=username, email_mem=email, error1=error1, error2=error2, error3=error3, error4=error4, error5=error5, error6=error6, error7=error7)

    return render_template('success.html', name=username)


@app.route("/")
def index():
    return render_template("form.html")

app.run()