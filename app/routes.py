from flask import render_template, flash, request, redirect, url_for, session
import auth, json
from urllib2 import urlopen, Request, URLError
from app import app,database


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title="Landing")

@app.route('/status/<real>')
def status(real):
    booked = database.check_book()
    return render_template('status.html',count=booked,current=real, title='Live')

@app.route('/logout')
def logout():
    auth.end_session()
    return redirect(url_for('index'))

@app.route('/book',methods=['GET','POST'])
def booking():
    if request.method == 'GET':
        return render_template('booking.html', title='Book')
    else:
        access_token = session.get('access_token')
        if access_token is None:
            return redirect(url_for('login'))
        dt = request.form['date']
        tm = request.form['time']
        em = session['user']['email']
        database.add_book(em,dt,tm)
        return render_template('index.html',title="Landing")

@app.route('/myBook')
def myBooking():
    access_token = session.get('access_token')
    if access_token is None:
        flash('login to view your bookings')
        return redirect(url_for('login'))
    entries = database.show_book()
    return render_template('myBookings.html', title="History", entries=entries)

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        callback=url_for('authorized', _external=True)
        return auth.google.authorize(callback=callback)
    else:
        access_token = session.get('access_token')
        if access_token is None:
            return render_template('login.html',title='Login')
        return redirect(url_for('index'))


def main():
    app.run()


if __name__ == '__main__':
    main()
