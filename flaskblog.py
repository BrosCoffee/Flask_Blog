from flask import Flask, render_template

app = Flask(__name__)

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
def home():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

'''
Debug mode ON: whenever the codes changed, the contents changed accordingly.
'''
