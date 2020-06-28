# coding: utf-8
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('hello06.html', title='app06')


@app.route('/test', methods=['GET', 'POST'])
def test():
    try:
        if request.method == 'POST':
            return request.form['test']
        else:
            return request.args.get('test', '')
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(host="localhost",debug=True, port=80, threaded=True) 