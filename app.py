from flask import Flask,render_template,request,session,redirect, url_for

from forms import LoginForm

import db


#yy-mm-dd

def validateDate(date): #checks if date is possible, then returns bool
    date = date.split("-")
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])

    if year < 1000 or year > 3000 or month == 0 or month > 12:
        return False

    monthLength = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

    if((year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)): # allow for leap years
        monthLength[1] = 29

    return day > 0 and day <= monthLength[month - 1]


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

@app.route('/book') 
def get_book():
    if  'userinfo' in session:
        djs = db.getDJs() # get all djs
        djList = []
        print(djs)
        for i in djs: #generate dj list into array with needed data
            user = db.getUserId(i[1])
            arr = [i[2],i[3],user[1]]
            djList += [arr]

        return(render_template('book.html',loggedIn = True, djList = djList))
    else:
        return(redirect(url_for('get_home',loggedIn = False ))) #dont allow them on the page if not logged in

@app.route('/book/confirm')
def  get_confirm():
    if  'userinfo' in session:
        dj = request.args['dj'] #get the dj from client for them to book

        return(render_template("bookconfirm.html",loggedIn = True , dj = dj))

    else:
        return(redirect(url_for('get_home',loggedIn = False )))

@app.route('/book/confirm/book')
def  get_confirmbook():
    if  'userinfo' in session:
        dj = request.args['dj'] #dj to be booked
        date = request.args['date'] #date that  is booked
        id = session["userinfo"]["id"] #clients id to be inserted in db

        if not validateDate(date): #if date not valid then return home
            return(redirect(url_for('get_home',loggedIn = True )))

        dj = db.getUser(dj)# get user from username
        dj = db.getDJ(dj[0])# get dj from user id

        return(redirect(url_for('get_home',loggedIn = True )))
    else:
        return(redirect(url_for('get_home',loggedIn = False )))

@app.route('/signout')  
def  get_signout():
    if  'userinfo' in session:
        session.pop("userinfo") #remove userinfo from session
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
        
        form = LoginForm(username,password) #create form object
        userInfo = db.getUser(username = username)

        if userInfo: #db function refurn false if failed to retrieve data, checked this here
            correctPass = (userInfo[2] == password) #see if password is the same

        if form.validateAll() == False or not userInfo or not correctPass: #validate form, check if userinfo is valid and check if password is correct.
            return(render_template('login.html',error="Error, Invalid Username or Password")) # error is returned if not logged in and added to webpage
        else:
            if userInfo[3] == 'dj': #store different data on the client for the different users
                djInfo = db.getDJ(userInfo[0])
                userInfo = {
                    "type" : "dj",
                    "username" : username,
                    "id": userInfo[0],
                    "bio": djInfo[2],
                    "genres": djInfo[3],
                }
                session['userinfo'] = userInfo
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
        bookings = []

        if session['userinfo']['type'] == 'dj': #if user is dj show the bookings that book them
            bookings = db.getDJBookings(session['userinfo']['id'])
        elif (session['userinfo']['type'] == 'customer'): #if customer show the bookings they have made
            bookings = db.getCustomerBookings(session['userinfo']['id'])
        else:
            bookings = db.getAllBookings() #else show all of the bookling make
        
        return(render_template('profile.html',user = session['userinfo'],loggedIn = True, bookings = bookings))
    else:
        return(render_template('login.html',error=""))

if __name__ == '__main__':
    
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['FLASK_DEBUG'] = 1
    app.run(debug=True)
