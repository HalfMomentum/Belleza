import os
from app import app
from flask import render_template, session
from flask_mail import Mail, Message
from threading import Thread

app.config.update(dict(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_DEFAULT_SENDER = 'madhavmalpani123@gmail.com',
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'your@mail.com',
    MAIL_PASSWORD = 'yourpassword',
))

mail = Mail()
mail.init_app(app)

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def sendmail(entry):
    try:
        msg = Message("Belleza | Hello", recipients=[entry['email']])
        msg.body = render_template('mailing/mail.txt',entry=entry)
        mail.send(msg)
    except Exception, e:
        print e
