# This app.py file uses a try except block to make sure the user inputs an integer.
# If the user enters something other than an integer, it will be entered as invalid.

# This file was inspired from Stack Overflow https://stackoverflow.com/questions/5424716/how-to-check-if-string-input-is-a-number
# https://stackoverflow.com/questions/59285033/how-to-with-request-args-get-in-flask and Professor Krevat
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.get('/result')
def result():
    try:
        input = int(request.args.get('integer'))
    except ValueError:
        input = 'invalid'
    return render_template('result.html', input=input)
