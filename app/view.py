from app import app
from flask import render_template


@app.route('/')
def index():
    data = {'name': 'Vitaly', 'family': 'Gorbunov'}
    return render_template('index.html', n=data)

@app.route('/about')
def about():
    data = {'name': 'Sveta', 'family': 'Gorbunova'}
    return render_template('about.html', n=data)

@app.route('/contacts')
def contacts():
    data = {'name': 'Bogdan', 'family': 'Gorbunov'}
    return render_template('contacts.html', n=data)
