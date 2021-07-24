import os
import waitress
from random import choice
from flask import Flask, request, render_template, redirect


app = Flask(__name__, root_path='.')

@app.route('/', methods = ['GET', 'POST'])
def index():
    current_buyer = None
    potential_buyers = ['Derz', 'Wes']
    if request.method == 'POST':
        if 'random' in request.form.keys():
            current_buyer = choice(potential_buyers)
        else:
            current_buyer = request.form['potential_buyers']
        with open('buyer.txt', 'w') as f:
            f.write(current_buyer)
        return redirect('/')
    else:
        if os.path.isfile('buyer.txt'):
            with open('buyer.txt', 'r') as f:
                current_buyer = f.read()
        else:
            with open('buyer.txt', 'w') as f:
                f.write('None')
    return render_template('index.html', current_buyer=current_buyer, potential_buyers=potential_buyers) 


if __name__ == '__main__':
    port = os.getenv('PORT') or '5000'
    addr = '127.0.0.1:{}'.format(port)
    print('Listening on {}'.format(addr))
    waitress.serve(app, listen=addr)
