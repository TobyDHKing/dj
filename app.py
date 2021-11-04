from flask import Flask,render_template,current_app, g,request
from werkzeug.wrappers import CommonRequestDescriptorsMixin, Request
from forms import LoginForm
from flask.cli import with_appcontext
import sqlite3
from db import db

def create_app():
    app = Flask(__name__)

    
    db.init_app(app)

    return app
app = create_app()

app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
    DB_NAME="djapp"
)

@app.route('/book')
def get_book():
    return(render_template('book.html'))


@app.route('/')
@app.route('/home')
def get_home():
    get_db()
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


