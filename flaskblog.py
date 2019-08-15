from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd0c948886a8a19047c3255db3670afe4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"User('{self.title}', '{self.date_posted}')"

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
        flash(f'Account created for {form.username.data}', 'success')
        return redirect(url_for('home'))
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

if __name__ == '__main__':
    app.run(debug=True)

'''
Debug mode ON: whenever the codes changed, the contents changed accordingly.
'''
