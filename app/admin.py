from flask import render_template, flash, request, redirect, url_for, session
from app import app,database as db,auth

@app.route('/admin')
def admin():
    if not session.get('admin'):
        flash('Only admin allowed')
        return redirect(url_for('adminlogin'))
    entries = db.show_all_book()
    return render_template('myBookings.html', title="Manager", entries=entries)

@app.route('/admin/login', methods=['GET','POST'])
def adminlogin():
    if request.method == 'GET':
        return render_template('admin_login.html',title='Admin')
    else:
        un = request.form['username']
        pw = request.form['password']
        if auth.isadmin(un,pw):
            session['admin'] = True
            return redirect(url_for('admin'))
        else:
            flash('Incorrect Credentials')
            return redirect(url_for('adminlogin'))
