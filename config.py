import os
from app import app

DATABASE = os.path.join(app.root_path, 'belleza.db')
GOOGLE_CLIENT_ID = '716230243314-k9j5b63dook0mvsehusfondeo9q5rp89.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'XNPhyKJjmbKIa1iSihhzNWcU'
REDIRECT_URI = '/googlelogin'
SECRET_KEY = 'ufoyRofNuej25JEAR/wrdTUQLejwyiggEupicE'
ADMIN = {'username':'admin',
         'password':'admin'}

MAIL_SERVER = 'smtp.gmail.com',
MAIL_PORT = 587,
MAIL_USE_TLS = True,
MAIL_USE_SSL = False,
MAIL_USERNAME = 'my_username@gmail.com',
MAIL_PASSWORD = 'my_password'
