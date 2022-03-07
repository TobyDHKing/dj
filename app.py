from flask import Flask,render_template,request,session,redirect, url_for
#from flask.ext.session import Session
from werkzeug.wrappers import CommonRequestDescriptorsMixin, Request
from forms import LoginForm
from flask.cli import with_appcontext
import sqlite3
import db
import user


def create_app():
    app = Flask(__name__)

    db.init_app(app)

    return app

app = create_app()

app.config.update(
    TESTING=True,
    SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
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
    djs = db.db_getDJs()
    djList = []
    print(djs)
    for i in djs:
        
        user = db.db_getUserId(i[1])

        arr = [i[2],i[3],user[1]]
        djList += [arr]
        print(i)
    print(djList)
    return(render_template('book.html', djList = djList))

@app.route('/book/confirm')
def  get_confirm():
    if  'userinfo' in session:
        dj = request.args['dj']

        return(render_template("bookconfirm.html",loggedIn = True , dj = dj))

    else:
        return(redirect(url_for('get_home',loggedIn = False )))


@app.route('/signout')  
def  get_signout():
    if  'userinfo' in session:
        session.pop("userinfo")
        return(redirect(url_for('get_home',loggedIn = False)))



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
        if userInfo:
            correctPass = (userInfo[2] == password)
        print(userInfo)
        if form.validateAll() == False or not userInfo or not correctPass:
            print("login error")
            return(render_template('login.html',error="Error, Invalid Username or Password"))
        else:
            if userInfo[3] == 'dj':
                djInfo = db.db_getDJ(userInfo[0])
                userInfo = {
                    "type" : "dj",
                    "username" : username,
                    "id": userInfo[0],
                    "bio": djInfo[2],
                    "genres": djInfo[3],
                }
                session['userinfo'] = userInfo
                #print(session['userinfo'] )
                #users[username] = user.dj(username,userInfo[1],djInfo[2],djInfo[3])
            else:
                userInfo = {
                    "type" : userInfo[3],
                    "username" : username,
                    "id": userInfo[0],
                }
                session['userinfo'] = userInfo
            return(redirect(url_for('get_home')))

    return(render_template('login.html',error=""))

@app.route('/profile')
def get_profile():
    if  'userinfo' in session:
        if session['userinfo']['type'] == 'dj':
            bookings = db.db_getDJBookings(session['userinfo']['id'])
            print("here buddy")
            print(session['userinfo']['id'])
            print(bookings)
        elif (session['userinfo']['type'] == 'customer'):
            bookings = db.db_getCustomerBookings(session['userinfo']['id'])
        else:
            bookings = db.getAllBookings()
        
        if not bookings :
            bookings = []

        return(render_template('profile.html',user = session['userinfo'],loggedIn = True, bookings = bookings))

    else:
        return(render_template('login.html',error=""))

if __name__ == '__main__':
    
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['FLASK_DEBUG'] = 1
    app.run(debug=True)


