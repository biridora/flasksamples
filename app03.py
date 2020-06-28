# coding: utf-8
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    name = "humanX"
    return render_template('hello03.html', title='app03', name=name)

if __name__ == "__main__":
    app.run(host="localhost",debug=True, port=80, threaded=True)  