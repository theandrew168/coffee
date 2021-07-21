import os

from flask import Flask, render_template
import waitress


app = Flask(__name__, root_path='.')

@app.route('/')
def index():
    return 'Hello world from flask!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    port = os.getenv('PORT') or '5000'
    addr = '127.0.0.1:{}'.format(port)
    print('listening on {}'.format(addr))
    waitress.serve(app, listen=addr, url_scheme='https')
