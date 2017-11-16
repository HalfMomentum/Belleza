from flask import _app_ctx_stack,g,current_app, flash
import sqlite3
from app import app
from config import DATABASE

"""
need to init_db everytime schema is changed
steps to connect:
$>execute python shell
$>from app import database
$>database.init_db()
"""

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(DATABASE)
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    with app.app_context():
        db = get_db()
        with current_app.open_resource('schema.sql', mode='r') as f:
            db.executescript(f.read())
        db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def add_book(email,date,time):
    """Add entry in the booking"""
    if check_book() < 3:
        try:
            query = 'insert into Bookings (customerEmail,bookDate, bookTime, bookService) values (\'{}\', \'{}\', \'{}\', \'{}\');'.format(email,date,time,'haircut')
            res = query_db(query, one=True)
            flash( 'Appointment added successfully !!')
        except Exception, e:
            print e
            flash('Error connecting Database !!')
    return 'No slots available, try a different slot !!'

def check_book():
    """Fetch all current bookings"""

    query = 'select * from Bookings;'
    cnt = query_db(query)
    for entry in cnt:
        print entry
    query = 'select count(*) as booked from Bookings;'
    cnt = int(query_db(query, one=True)['booked'])
    return cnt;
