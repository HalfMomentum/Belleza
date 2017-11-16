import os
from app import app
DATABASE = os.path.join(app.root_path, 'belleza.db')
USERNAME='admin',
PASSWORD='default'
GOOGLE_CLIENT_ID = '716230243314-k9j5b63dook0mvsehusfondeo9q5rp89.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'XNPhyKJjmbKIa1iSihhzNWcU'
REDIRECT_URI = '/googlelogin'
SECRET_KEY = 'ufoyRofNuej25JEAR/wrdTUQLejwyiggEupicE'
app.config['SESSION_TYPE'] = 'filesystem'
