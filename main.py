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

    url = "/"

    if (username.strip() == ""):
        error = "Please enter your name."
        url += "?blank_error1=" + error
        return redirect("/?blank_error1=" + error)

    if (password.strip() == ""):
        error = "Please enter your password."
        return redirect("/?blank_error2=" + error)

    if (pass_check.strip() == ""):
        error = "Please enter your password verification."
        return redirect("/?blank_error3=" + error)
    
    if (len(username) < 3) or (len(username) > 20) or (" " in username):
        error = "Please enter a valid username. Within the range of 3 to 20 characters and contains no spaces"
        return redirect("/?error=" + error) 

    if (len(password) < 3) or (len(password) > 20) or (" " in password):
        error = "Please enter a valid password Within the range of 3 to 20 characters and contains no spaces"
        return redirect("/?error=" + error) 

    if (password != pass_check):
        error = "Make sure your password and password verification are the same."
        return redirect("/?error=" + error) 

    if (email != ""):
        if (len(email) < 3) or (len(email) > 20) or (" " in email) or ("@" not in email) or ("." not in email):
            error = "Be sure to enter a valid email."
            return redirect("/?error=" + error) 
        

    return render_template('success.html', name=username)


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    encoded_blank1 = request.args.get("blank_error1")
    encoded_blank2 = request.args.get("blank_error2")
    encoded_blank3 = request.args.get("blank_error3")
    return render_template("form.html", blank_error1=encoded_blank1, blank_error2=encoded_blank2, blank_error3=encoded_blank3, error=encoded_error)

app.run()