from flask import _app_ctx_stack
import sqlite3
from app import app

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    print 'database fn called'
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
        top.sqlite_db.row_factory = sqlite3.Row
    return top.sqlite_db

def init_db():
    """Initializes the database."""
    db = __init__.get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def add_book(email,date,time):
    """Add entry in the booking"""
    if check_book <3:
        try:
            db = get_db()
            db.execute('insert into Bookings (customerEmail,bookDate, bookTime) values (?, ?, ?)',
                [email,date,time])
            db.commit()
            return 'Appointment added successfully !!'
        except e:
            return 'Error connecting Database !!'
    return 'No slots available, try a different slot !!'

def check_book():
    """Fetch all current bookings"""
    db = get_db()
    query = 'select count(*) from Bookings where bookDate=Date(now())'
    cnt = db.execute(query)
    return cnt;
