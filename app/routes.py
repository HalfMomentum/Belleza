from flask import render_template, flash, request, redirect, url_for, session
import auth, json
from app import app,database

@app.route('/')
@app.route('/index')
def index():

    return render_template('index.html',title="Landing")

@app.route('/status/<real>')
def status(real):
    #enter db query to fetch all current booking
    #also add form for other date and time and use data to fetch related details
    if real:
        print 'this can work'
    booked = 2
    left = 3 - booked
    return render_template('status.html',count=booked,available=left,current=real, title='Live')

@app.route('/logout')
def logout():
    session.pop('access_token', None)
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
        em = "Someone"
        database.add_book(em,dt,tm)
        #enter db query to add the form data
        return render_template('index.html',title="Landing")


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
