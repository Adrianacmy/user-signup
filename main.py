from flask import Flask, request, redirect, render_template
import re
# app = Flask(__name__)
# app.config['DEBUG'] = True


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('base.html', title='Hello, Word')

@app.route('/signup')
def display_signup():
    return render_template('signup.html')


@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    email = request.form['email']

    error_username = ''
    error_password = ''
    error_confirm_password = ''
    error_email = ''

    if not re.match('^[a-zA-Z]\w{2,19}$', username):
        error_username = 'Must start with a letter and contains 3 to 20 characters(letters,underscores, numbers)'
        username = ''
    if not re.match('^[a-zA-Z]\w{2,19}$', password):
        error_password = 'Must start with letter, contains 3 to 20 characters(letters, numbers, underscores)'
        password = ''
    if confirm_password != password:
        error_confirm_password = 'Password do not match'
        confirm_password = ''
    if email:
        if not re.match('^\w+([-+]\w+)*@\w+([-]\w+)*\.\w+([-]\w+)*${2, 19}', email):
            email = ''
            error_email = 'Invalid email'

    if not error_username and not error_password and not error_confirm_password and not error_email:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template(
            'signup.html',
            username = username,
            password = password,
            confirm_password = confirm_password,
            email = email,
            error_username = error_username,
            error_password = error_password,
            error_confirm_password = error_confirm_password,
            error_email = error_email
            )


@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)


app.run()

