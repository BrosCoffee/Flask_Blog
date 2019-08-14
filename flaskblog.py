from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd0c948886a8a19047c3255db3670afe4'

posts = [
    {
        'author': 'Raymond Yang',
        'title': 'Blog post #1',
        'content': 'My first blog post.',
        'date_posted': 'Aug. 14th 2019'
    },
    {
        'author': 'Meliza Anzures',
        'title': 'Blog post #2',
        'content': 'I am the princess.',
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

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title = "Ray's blog - Register", form = form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = "Ray's blog - Login", form = form)

if __name__ == '__main__':
    app.run(debug=True)

'''
Debug mode ON: whenever the codes changed, the contents changed accordingly.
'''
