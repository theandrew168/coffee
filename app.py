import os
import waitress
from flask import Flask, request, render_template


app = Flask(__name__, root_path='.')

@app.route('/', methods = ['GET', 'POST'])
def index(buyer='None'):
    if request.method == 'POST':
        buyer = request.form['user_name']
        with open('buyer.txt', 'w') as f:
            f.write(buyer)
    else:
        if os.path.isfile('buyer.txt'):
            with open('buyer.txt', 'r') as f:
                buyer = f.read()
    return render_template('index.html', name=buyer) 


if __name__ == '__main__':
    port = os.getenv('PORT') or '5000'
    addr = '127.0.0.1:{}'.format(port)
    print('Listening on {}'.format(addr))
    waitress.serve(app, listen=addr, url_scheme='https')
