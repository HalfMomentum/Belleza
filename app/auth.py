import json
from config import GOOGLE_CLIENT_ID,GOOGLE_CLIENT_SECRET, REDIRECT_URI, SECRET_KEY, ADMIN
from flask import session, redirect, url_for
from urllib2 import urlopen, Request, URLError
from app import app
from flask_oauth import OAuth

oauth = OAuth()

google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key=GOOGLE_CLIENT_ID,
                          consumer_secret=GOOGLE_CLIENT_SECRET)

@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    set_session()
    return redirect(url_for('index'))

@google.tokengetter
def get_access_token():
    return session.get('access_token')

def set_session():
    access_token = get_access_token()
    access_token = access_token[0]
    headers = {'Authorization': 'OAuth '+access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)
    res = urlopen(req)
    session['user'] = json.loads(res.read())

def end_session():
    if session:
        session.clear()

def isadmin(usr,psw):
    return usr==ADMIN['username'] and psw==ADMIN['password']
