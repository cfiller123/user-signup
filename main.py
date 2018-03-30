from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=['POST'])
def validation():
    user_username = cgi.escape(request.form['username'], quote=True)
    user_password = request.form['password']
    user_password_verify = request.form['verify']
    user_email = request.form['email']

    # if the user typed nothing at all, tell them the error
    if (not user_password) or (user_password.strip() == ""):
        password_error = True
        return password_error

    if (not user_username) or (user_username.strip() == ""):
        username_error = True
        return username_error

    if (not user_password_verify) or (user_password_verify.strip() == ""):
        verify_error = True
        return verify_error

    # if the username or password is entered by not valid
    if (len(user_username) > 20) or (len(user_username) < 3):
        username_error = True
        return username_error
    
    if (len(user_password) > 20) or (len(user_password) < 3):
        password_error = True
        return password_error

    # if the passwords don't match
    if user_password != user_password_verify:
       verify_error = True
        return verify_error

    if (not username_error) or (not password_error) or (not verify_error) or (not email_error):
        return render_template('welcome.html', user_username)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html', watchlist=get_current_watchlist(), error=encoded_error and cgi.escape(encoded_error, quote=True))


app.run()