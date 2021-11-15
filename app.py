from flask import Flask,render_template,current_app,request
from werkzeug.wrappers import CommonRequestDescriptorsMixin, Request
from forms import LoginForm
from flask.cli import with_appcontext
import sqlite3
import db


def create_app():
    app = Flask(__name__)

    
    db.init_app(app)

    return app
app = create_app()

app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
    DB_NAME="djapp.db",
    DATABASE = "djapp.db",
)

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
        if form.validateAll() == False:
            print("login error")
            return(render_template('login.html',error="Error, Invalid Username or Password"))
        else:
            return(render_template('login.html',error="Success"))
    return(render_template('login.html',error=""))



if __name__ == '__main__':
    
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['FLASK_DEBUG'] = 1
    app.run(debug=True)


