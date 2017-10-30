from flask import render_template, flash, request, redirect, url_for, session
import auth, json
from app import app,database

@app.route('/')
def home():
    db = database.get_db()
    cur = db.execute('select name,email from Users')
    users = cur.fetchall()
    return render_template('home.html', users=users)

@app.route('/home')
def index():
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))

    access_token = access_token[0]
    from urllib2 import Request, urlopen, URLError

    headers = {'Authorization': 'OAuth '+access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)
    try:
        res = urlopen(req)
    except URLError, e:
        if e.code == 401:
            # Unauthorized - bad token
            session.pop('access_token', None)
            return redirect(url_for('login'))
        return render_template(
            'index.html',
            msg = json.loads(res.read()),
            title='Detail',
        )

    msg = json.loads(res.read())
    print(msg['id'])
    return render_template(
        'index.html',
        msg = msg,
        title='Detail',
    )


@app.route('/add', methods=['POST'])
def add_user():
    db = database.get_db()
    db.execute('insert into Users (name, email) values (?, ?)',
               [request.form['name'], request.form['email']])
    db.commit()
    flash('New User registered successfully')
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    return redirect(url_for('home'))

@app.route('/login')
def login():
    callback=url_for('authorized', _external=True)
    return auth.google.authorize(callback=callback)


def main():
    app.run()


if __name__ == '__main__':
    main()
