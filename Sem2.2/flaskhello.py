from flask import Flask, jsonify
import sys

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/page1')
def page1():
    return "Если вы это читаете, вы что-то знаете :)"

@app.route('/page2')
def page2():
    return jsonify(str(sys.__dict__))


if __name__ == '__main__':
    app.run(debug=True)

