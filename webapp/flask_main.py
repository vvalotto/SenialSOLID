from flask import Flask, make_response
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/usuario/<nombre>')
def usuario(nombre):
    return '<h1>Hola, %s!!</h1>' %nombre

if __name__ == '__main__':
    manager.run()