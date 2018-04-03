from flask import Flask, request, redirect, render_template
import re
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/signup", methods=['POST'])
def validation():
    user_username = cgi.escape(request.form['username'], quote=True)
    user_password = request.form['password']
    user_password_verify = request.form['verify']
    user_email = request.form['email']
    password_error = False
    username_error = False
    verify_error = False
    email_error = False

    if (not user_password) or (user_password.strip() == ""):
        password_error = True

    if (not user_username) or (user_username.strip() == ""):
        username_error = True

    if (not user_password_verify) or (user_password_verify.strip() == ""):
        verify_error = True

    if (len(user_username) > 20) or (len(user_username) < 3):
        username_error = True
    
    if (len(user_password) > 20) or (len(user_password) < 3):
        password_error = True

    if user_password != user_password_verify:
       verify_error = True

    if (not username_error) and (not password_error) and (not verify_error) and (not email_error):
        return render_template('welcome.html', username=user_username)
    else:
        return render_template('signup.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html')


app.run()