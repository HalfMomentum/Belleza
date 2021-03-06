from flask import _app_ctx_stack,g,current_app, flash, session
import sqlite3
from app import app, emails
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


def close_db():
    """Closes the database on admin request"""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


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


def show_all_book():
    """Show all entries from user's account"""
    try:
        query = 'select date(bookDate) as bookDate, time(bookDate) as bookTime, bookService from Bookings;'
        res = query_db(query)
        return res
    except Exception, e:
        print e
        flash('Error connecting to Database !')


def show_book():
    """Show all entries from user's account"""
    try:
        email = session['user']['email']
        query = 'select date(bookDate) as bookDate, time(bookDate) as bookTime, Service as bookService from Bookings,Services as s where customerEmail=\'{}\' and bookService=s.id;'.format(email)
        res = query_db(query)
        return res
    except Exception, e:
        print e
        flash('Error connecting to Database !')


def add_book(serv,email,date,time):
    """Add entry in the booking"""
    if check_book() < 3:
        try:
            datetime = '{} {}'.format(date,time)
            query = 'insert into Bookings (customerEmail,bookDate, bookService ) values (\'{}\', \'{}\', \'{}\');'.format(email,datetime,serv)
            query_db(query)
            flash( 'Appointment added successfully !!' )
            serv = query_db('select service from Services where id={};'.format(serv),one=True)['service']
            entry = {
                'date' : date,
                'name' : session.get('user')['given_name'],
                'time' : time,
                'email' : email,
                'service' : serv
            }
            emails.sendmail(entry);
            return
        except Exception, e:
            print e
            flash('Error connecting Database !!')
            return
    flash('No slots available, try a different slot !!')
    return


def check_clash(date,time):
    """fetch all booking for particular date-time"""
    datetime = '{} {}'.format(date,time)
    try:
        query = 'select count(*) as booked from Bookings where bookDate between datetime({},\'-15 minutes\') and datetime({},\'+15 minutes\');'.format(datetime,datetime)
        cnt = int(query_db(query, one=True)['booked'])
        return cnt;
    except Exception, e:
        flash('Error connecting Database !!')
        print e


def check_book():
    """Fetch all current bookings"""
    try:
        query = 'select count(*) as booked from Bookings where bookdate between datetime(\'now\',\'-15 minutes\') and datetime(\'now\',\'+15 minutes\');'
        cnt = int(query_db(query, one=True)['booked'])
        return cnt;
    except Exception, e:
        print e
