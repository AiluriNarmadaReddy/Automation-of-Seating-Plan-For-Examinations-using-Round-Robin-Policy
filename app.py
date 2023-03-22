import subprocess
import pandas as pd

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users = {
    'abc': 'def',
    'ghi': 'jkl',
    'mno': 'pqr'
}

@app.route('/')
def index():
    return render_template('login.html')
@app.route('/login', methods=['GET','POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username in users and users[username] == password:
        return redirect(url_for('sheets'))
    else:
        return render_template('login.html', error='Invalid username or password')


@app.route('/sheets', methods=['GET', 'POST'])
def sheets():
    if request.method == 'POST':
        # Get sheet names from form data
        hallticket_sheet = request.form['hallticket']
        hall_sheet = request.form['hall']

        # Call read_excel.py script with sheet names as arguments
        subprocess.call(["python", "read_excel .py", hallticket_sheet, hall_sheet])

        # Call out_sheet.py script with sheet names as arguments
        subprocess.call(["python", "out_sheet.py", hallticket_sheet, hall_sheet])

        return 'Processing complete!'
    else:
        return render_template('sheet.html')



if __name__ == '__main__':
    app.run(debug=True)