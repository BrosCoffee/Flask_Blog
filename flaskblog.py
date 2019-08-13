from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Home Page</h1> '

@app.route('/about')
def about():
    return '<h1>About Page</h1> '

if __name__ == '__main__':
    app.run(debug=True)

'''
Debug mode ON: whenever the codes changed, the contents changed accordingly.
'''
