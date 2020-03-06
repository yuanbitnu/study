from flask import Flask

app = Flask(__name__)


@app.route('/login')
def hello():
    return '你好'