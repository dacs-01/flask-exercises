# This app.py file adds the inputs taken from HTML and implements them as key value pairs
# into a dictionary called registered. 

# Inspired from GeeksForGeeks https://www.geeksforgeeks.org/add-a-keyvalue-pair-to-dictionary-in-python/
# as well as Professor Krevat 

from flask import Flask, request, render_template

app = Flask(__name__)

registered = {} # initialize dictionary

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST']) 
def result(): # This method will define what goes into the registered dictionary
    name = request.form.get('name') # key
    org = request.form.get('organization') # value
    registered[name] = org # add pair to the dictionary
    return render_template('result.html', registered=registered) # return the dictionary in the result page 

if __name__ == "__main__": # debugger
    app.run(debug=True)
