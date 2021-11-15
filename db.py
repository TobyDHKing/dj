import sqlite3
import click
from flask import current_app
from flask.cli import with_appcontext

db = None

def get_db():
    global db
    if not db:
        try:
            db = sqlite3.connect(
                current_app.config['DATABASE'])
        except Error as e:
            print(e)
            print("nooo")
        db.row_factory = sqlite3.Row

    return db


def close_db(e=None):
    global db
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
        print(row['username'])


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)