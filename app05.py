# coding: utf-8
from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "admin": "password",
    "guest": "password"
}

@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None

@auth.error_handler
def auth_error():
    return "auth error"


@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()

if __name__ == '__main__':
    app.run(host="localhost",debug=True, port=80, threaded=True) 