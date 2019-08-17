## Origin
&nbsp; The project is using Python and the [Flask framework](https://flask.palletsprojects.com/en/1.1.x/) 
to create a personal blog. The main focus is to understand the HTTP protocol, the interaction between the website and its database,
 and the deployment of the application. Thus, I simply implemented the Bootstrap as the front-end framework. 

## Details
### run.py:
* type `python run.py` in the terminal to initiate the website
* `if __name__ == '__main__':`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`app.run(debug=True)`
### flaskblog/ :
#### __init__.py: 
> * call the `app = Flask(__name__)`
> * database `db = SQLAlchemy(app)`
> * bcrypt `bcrypt = Bcrypt(app)`
> * login manager `login_manager = LoginManager(app)`
> * then call routes.py
#### routes.py:
> * manage all the routes (website pages)
> ##### forms.py:
> * import FlaskForm, fields, and validators
> * Two objects: "RegisterForm" and "LoginForm"
> ##### models.py:
> * import db and write into the database
> * two objects: "User" and "Post"
#### templates/ :
> ##### home.html
> * `{% ... %}` for python syntax
> * `{{ ... }}` for variables
> * layout.html
> * Using bootstrap as the layout model for the website
> ##### post.html
> * Bootstrap [Modal](https://getbootstrap.com/docs/4.0/components/modal/#live-demo): search for "Live demo"
> * etc.
#### static/ :
> ##### main.css
> * The main css model

##### Learning resource: [Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
###### (Last updated date: Aug. 16th 2019) 