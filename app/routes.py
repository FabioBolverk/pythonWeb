from app import app
from flask import render_template

@app.route('/CURRICULO')
def home():
    return render_template('index.html')


@app.route('/')
def curriculogit ():
    return render_template('HELLO WOLRD')