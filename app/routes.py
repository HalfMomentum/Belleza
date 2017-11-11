from flask import render_template, flash, request, redirect, url_for, session
import auth, json
from app import app,database


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',title="Landing")

@app.route('/status/<real>')
def status(real=True):
    return render_template('status.html',count=2,current=real, title='Live')

@app.route('/logout')
def logout():
    return redirect(url_for('index'))

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html',title='Login')
    else:
        db = database.get_db()
        Name = request.form['name']
        Email = request.form['email']
        if len(Name)>0 and len(Email)>0:
            db.execute('insert into Users (name, email) values (?, ?)',
                       [Name,Email])
            db.commit()
            flash('New User registered successfully')
            return redirect(url_for("index"))
        flash('Wrong Credentials')
        return redirect(url_for('login'))


def main():
    app.run()


if __name__ == '__main__':
    main()
