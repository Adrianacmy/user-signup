from flask import Flask, request, redirect, render_template

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

    if not username:
        error_username = 'username error'
        username = ''
    if not password:
        error_password = 'password error'
        password = ''
    if confirm_password != password:
        error_confirm_password = 'confirm_password error'
        confirm_password = ''
    if not email:
        email = ''
        error_email = 'email error'
    
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

