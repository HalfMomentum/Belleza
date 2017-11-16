from flask import _app_ctx_stack,g,current_app, flash, session
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
    db = get_db()
    cur = db.execute(query, args)
    rv = cur.fetchall()
    cur.close()
    db.commit()
    return (rv[0] if rv else None) if one else rv

def show_book():
    """Show all entries from user's account"""
    try:
        email = session['user']['email']
        query = 'select date(bookDate) as bookDate, time(bookDate) as bookTime, bookService from Bookings where customerEmail=\'{}\';'.format(email)
        res = query_db(query)
        return res
    except Exception, e:
        print e
        flash('Error connecting to Database !')

def add_book(email,date,time):
    """Add entry in the booking"""
    if check_book() < 3:
        try:
            datetime = '{} {}'.format(date,time)
            query = 'insert into Bookings (customerEmail,bookDate, bookService) values (\'{}\', \'{}\', \'{}\');'.format(email,datetime,'haircut')
            query_db(query)
            flash( 'Appointment added successfully !!' )
            check_book()
            return()
        except Exception, e:
            print e
            flash('Error connecting Database !!')
    flash('No slots available, try a different slot !!')
    return()

def check_clash(date,time):
    """fetch all booking for particular date-time"""
    datetime = '{} {}'.format(date,time)
    try:
        query = 'select count(*) as booked from Bookings where bookDate between datetime({},\'-30 minutes\') and datetime({},\'+1 hours\');'.format(datetime,datetime)

        cnt = int(query_db(query, one=True)['booked'])
        print '---------{}-'.fromat(cnt)
        return cnt;

    except Exception, e:
        flash('Error connecting Database !!')
        print e

def check_book():
    """Fetch all current bookings"""
    try:
        query = 'select count(*) as booked from Bookings where bookdate between datetime(\'now\',\'-30 minutes\') and datetime(\'now\',\'+1 hours\');'

        cnt = int(query_db(query, one=True)['booked'])
        print 'xxx-{}--'.format(cnt)
        return cnt;
    except Exception, e:
        print e
