"""Controller"""

import sqlite3
from flask import Flask, render_template, request, session, flash, redirect, url_for, g

# Configuration
DATABASE = 'blog.py'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 's:E\xa8\xb12\xf9\x9b\xe6\xfd\xcb\xd6\xaf\xb8}i1\x1d02\xb1e\x97Z'

app = Flask(__name__)

# Pulls in app configuration by looking for UPPERCASE variables
app.config.from_object(__name__)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('login'))


@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
