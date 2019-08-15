# Origin
&nbsp; The project is using Python and the [Flask framework](https://flask.palletsprojects.com/en/1.1.x/) to create a personal blog.

### Details
> * flaskblog.py: 
>> * `from flask import Flask, render_template`
>> * `@app.route('/')`
>> * `app = Flask(__name__)`
>> * `@app.route('/')`<br>`def home():`
>> * `if __name__ == '__main__':`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`app.run(debug=True)`
> * home.html
>> * `{% ... %}` for python syntax
>> * `{{ ... }}` for variables
> * layout.html
>> * Using bootstrap as the layout model for the website
> * main.css
>> * The main css model

##### Learning resource: [Corey Schafer](https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH)
###### (Last updated date: Aug. 15th 2019) 