from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/page1')
def page1():
    return "Если вы это читаете, вы что-то знаете :)"

if __name__ == '__main__':
    app.run(debug=True)

