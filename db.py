import sqlite3
import click
from flask import current_app
from flask.cli import with_appcontext



def get_db():
    db = None
    if not db:
        try:
            db = sqlite3.connect(
                current_app.config['DATABASE'] )
        except Exception as e:
            print(e)
        #db.row_factory = sqlite3.Row

    return db


def close_db(e=None):
    db = get_db()
    if db is not None:
        db.close()
        db = None


def testdata_db():
    db = get_db()

    with current_app.open_resource('testdata.sql') as f:
        decode = f.read().decode('utf8')
        c = db.cursor()
        c.executescript(decode)
    db.commit()



def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        decode = f.read().decode('utf8')
        c = db.cursor()
        c.executescript(decode)
    db.commit()


@click.command('init-db')
@with_appcontext

def init_db_command():
    #Clear the existing data and create new tables.
    init_db()
    click.echo('Initialized the database.')
    testdata_db()
    db = get_db()
    cur = db.cursor()
    for row in cur.execute('SELECT * FROM users'):
        print(row)

def init_app(app):
    print("this ran")
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

def db_getUser(username):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM users where username = (?)", [username])
    
    try: userInfo = list(cur.fetchone())
    except: return False
    return userInfo

def db_getUserId(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM users where id = (?)", [id])
   
    try: userInfo = list(cur.fetchone())
    except: return False
    return userInfo

def db_getDJ(id):
    db = get_db()
    cur = db.cursor()
    print(id)
    cur.execute("SELECT * FROM djs where user_id = (?)", [id])
    try: DJInfo = list(cur.fetchone())
    except: return False
    return DJInfo

def db_getDJs():
    db = get_db()
    cur = db.cursor()
    djs = cur.execute("SELECT * FROM djs")

    return djs


def db_getCustomerBookings(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM bookings where booker_id = (?)", [id])
    try: bookings = list(cur.fetchall())
    except: return False
    return bookings

def db_getDJBookings(id):
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM bookings where dj_id = (?)", [id])
    try: bookings = list(cur.fetchall()) 
    except: return False
    print(bookings)
    return bookings

def getAllBookings():
    db = get_db()
    cur = db.cursor()
    cur.execute("SELECT * FROM bookings")
    try: bookings = list(cur.fetchall())
    except: return False
    return bookings



