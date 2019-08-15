from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Raymond Yang',
        'title': 'Blog post #3',
        'content': 'Coding every day!',
        'date_posted': 'Aug. 15th 2019'
    },
    {
        'author': 'Meliza Anzures',
        'title': 'Blog post #2',
        'content': 'I am the princess.',
        'date_posted': 'Aug. 14th 2019'
    },
{
        'author': 'Raymond Yang',
        'title': 'Blog post #1',
        'content': 'My first blog post.',
        'date_posted': 'Aug. 14th 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', title = "Ray's blog - About")

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'{form.username.data}, your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title = "Ray's blog - Register", form = form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'raymondcyang0219@gmail.com' and form.password.data == 'Passw@rd':
            flash(f'You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title = "Ray's blog - Login", form = form)