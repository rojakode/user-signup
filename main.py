from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route("/valid_input", methods=['POST'])
def valid_input():
    username = request.form['Username']
    password1 = request.form['password1']
    password2 = request.form['password2']
    email = request.form['email']

    username_error = ''
    password1_error = ''
    password2_error = ''
    email_error = ''

    error_check = False
    
    if username == '':
        username_error = 'Invalid Username'
        error_check = True
    elif (len(username) <3) or (len(username) >20):
        username_error = 'Username must be greater than 3 characters but less than 20 characters'
        error_check = True
    elif " " in username:
        username_error = 'Username should not contain spaces'
        error_check = True
    
    if password1 == '':
        password1_error = 'Invalid Password'
        error_check = True
    elif (len(password1) <3) or (len(password1) >20):
        password1_error = 'Password must be greater than 3 characters but less than 20 characters'
        error_check = True
    elif " " in password1:
        password1_error = 'Password should not contain spaces'
        error_check = True
    
    if password2 != password1:
        password1_error = 'Password Must Match'
        password2_error = 'Password Must Match'
        error_check = True

    if email != '':
        if email.count('@') != 1:
            email_error = 'Email Address can have only @'
            error_check = True
        elif email.count('.') != 1:
            email_error = 'Email Address can have only one .'
            error_check = True
        elif " " in email:
            email_error = 'Email Address should not contain spaces'
            error_check = True
        elif (len(email) <3) or (len(email) >20):
            email_error = 'Email Address must be greater than 3 characters but less than 20 characters'
            error_check = True
    if username == '' and password1 == '' and password2 == '' and email == '':
        username_error = 'Username Required'
        password1_error = 'Enter Password'
        password2_error = 'Enter Password'
        error_check = True

    if error_check == True:
        return render_template('index.html', username_error = username_error, password1_error = password1_error, password2_error = password2_error, email_error = email_error, username = username, email = email)
    else:
        return render_template('welcome.html', username = username)

app.run(debug = True)