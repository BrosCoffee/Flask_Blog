# Origin
&nbsp; The project is using Python and the [Flask framework](https://flask.palletsprojects.com/en/1.1.x/) to create a personal blog.

### Details
> * flaskblog.py: 
>> * `@app.route('/')`
>> * `app = Flask(__name__)`
>> * `@app.route('/')`<br>`def home():`
>> * `if __name__ == '__main__':`<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`app.run(debug=True)`
> * home.html
>> * `from flask import Flask, render_template`
>> * `{% ... %}` for python syntax
>> * `{{ ... }}` for variables

##### Learning resource: Corey Schafer https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g
###### (Last updated date: Aug. 14th 2019) 