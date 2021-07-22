import os

from flask import Flask, request, render_template
import waitress


app = Flask(__name__, root_path='.')


@app.route('/', methods = ['GET', 'POST'])
def index(buyer='None'):
    if request.method == 'POST':
        buyer = request.form['user_name']

    return render_template('index.html', name=buyer) 


if __name__ == '__main__':
    port = os.getenv('PORT') or '5000'
    addr = '127.0.0.1:{}'.format(port)
    print('Listening on {}'.format(addr))
    waitress.serve(app, listen=addr, url_scheme='https')
