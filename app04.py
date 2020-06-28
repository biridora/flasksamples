# coding: utf-8
from flask import Flask, jsonify

app = Flask(__name__)

#json ascii -> unescape
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def getjson():
  result = {
      "name": "たつのぶ。",
      "age": 23,
      "sex": "男",
  }
  return jsonify(result)

if __name__ == "__main__":
    app.run(host="localhost",debug=True, port=80, threaded=True) 