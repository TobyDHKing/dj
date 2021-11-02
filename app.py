from flask import Flask
from flask import render_template
from werkzeug.wrappers import CommonRequestDescriptorsMixin, Request
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask import request
from flask_nav.elements import *
from forms import LoginForm
from flask import current_app, g
from flask.cli import with_appcontext
import sqlite3

app = Flask(__name__)



@app.route('/book')
def get_book():
    return(render_template('book.html'))


@app.route('/')
@app.route('/home')
def get_home():
    return(render_template('home.html'))

@app.route('/login', methods = ['GET','POST'])
def get_login():
    username = request.form.get('username')
    password = request.form.get('password')
    print( username, password)
    form = LoginForm(username,password)
    if request.method == 'POST':
        print('post')
        print(form.validateAll())
    #form = LoginForm(request.form)
    return(render_template('login.html'))

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()



if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['FLASK_DEBUG'] = 1
    app.run(debug=True)


