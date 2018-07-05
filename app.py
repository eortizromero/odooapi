# -*- encoding: utf-8 -*-

from flask import Flask, render_template, redirect, request
from api import get_database
http = Flask(__name__)


@http.route('/')
def webclient():
    context = {'connected': False}
    if not context['connected']:
        return redirect('/connect', 303)
    return render_template('index.html', context=context)


@http.route('/connect', methods=['POST', 'GET'])
def odoo():
    context = {}
    return render_template('connect.html', context=context)


@http.route('/check_connect', methods=['GET', 'POST'])
def check_connect():
    if request.method == 'POST':
        host = request.form.get('host', None)
        password = request.form.get('password', None)
        port = request.form.get('port', None)
        host = 'http://' + host + (':' + port if port else 80)
        db = get_database(host)
        context = {
            'title_block': 'Select Your Database',
            'db': db
        }
        return render_template('load_database.html', context=context)
    else:
        # TODO: Check if connection is current setter

        return redirect('/connect', 303)

if __name__ == '__main__':
    http.run(debug=True)
