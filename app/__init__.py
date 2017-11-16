from flask import Flask

app = Flask(__name__)

from app import routes

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
