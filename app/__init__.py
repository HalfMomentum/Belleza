from flask import Flask

app = Flask(__name__)

from app import routes,admin, emails
from config import SECRET_KEY

app.secret_key = SECRET_KEY
