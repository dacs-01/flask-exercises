# This file creates a function that is utilized to get the current date and time
# Code inspired from Stack Overflow https://stackoverflow.com/questions/65548490/how-to-get-current-date-time-in-python-flask

from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', timeday=timeday)

@app.route("/time/")
def timeday():
    currently = datetime.now() # variable that holds the current date and time
    dt_string = currently.strftime("%A, %B %d %Y %H:%M:%S") # string that formats the currently variable into the desired output
    return dt_string # returns the string

if __name__ == '__main__':
    app.run(debug=True)
