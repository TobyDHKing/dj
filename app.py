from flask import Flask,render_template,request,session,redirect, url_for
#from flask.ext.session import Session
from werkzeug.wrappers import CommonRequestDescriptorsMixin, Request
from forms import LoginForm
from flask.cli import with_appcontext
import sqlite3
import db
import user
users = {

}
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

@app.route('/set/')
def set():
    session['username'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')

@app.route('/book')
def get_book():
    
    if  'userinfo' in session:
        djlist = db.db_getDJs()
        for i in djlist:
            print(i)


        return(render_template('book.html', loggedIn = True))
    else:
        return(render_template('book.html',loggedIn = False))

    


@app.route('/')
@app.route('/home')
def get_home():
    if  'userinfo' in session:
        return(render_template('home.html',loggedIn = True))
    else:
        return(render_template('home.html',loggedIn = False))

@app.route('/login', methods = ['GET','POST'])
def get_login():
    if request.method == 'POST':
        if  'userinfo' in session:
            return (redirect(url_for('get_home')))
        username = request.form.get('username')
        password = request.form.get('password')
        print( username, password)
        form = LoginForm(username,password)
        userInfo = db.db_getUser(username = username)

        if form.validateAll() == False:
            print("login error")
            return(render_template('login.html',error="Error, Invalid Username or Password"))
        else:
            if userInfo[3] == 'dj':
                djInfo = db.db_getDJ(userInfo[0])
                userInfo = {
                    "type" : "dj",
                    "username" : username,
                    "id": userInfo[1],
                    "bio": djInfo[2],
                    "genres": djInfo[3],
                }
                session['userinfo'] = userInfo
                #print(session['userinfo'] )
                #users[username] = user.dj(username,userInfo[1],djInfo[2],djInfo[3])
                # make login fuction that deals with sql and create user object relative to user type
            return(redirect(url_for('get_home')))

    return(render_template('login.html',error=""))


if __name__ == '__main__':
    
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['FLASK_DEBUG'] = 1
    app.run(debug=True)


