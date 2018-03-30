from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/add", methods=['POST'])
def validation():
    user_username = request.form['username']
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
    if :
        
        return 

    # if the passwords don't match
    if :
       
        return 

    # 'escape' the user's input so that if they typed HTML, it doesn't mess up our site
    new_movie_escaped = cgi.escape(new_movie, quote=True)

    # TODO:
    # Create a template called add-confirmation.html inside your /templates directory
    # Use that template to render the confirmation message instead of this temporary message below
    return render_template('add-confirmation.html', added_mov

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('edit.html', watchlist=get_current_watchlist(), error=encoded_error and cgi.escape(encoded_error, quote=True))


app.run()