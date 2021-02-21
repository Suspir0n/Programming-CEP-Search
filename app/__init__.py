from flask import Flask, render_template, request
from .views import validation_cep
import requests
import json


def create_app():
    app = Flask(__name__)
    return app

_app = create_app()

@_app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@_app.route('/search_cep', methods=['GET'])
def response(data):
    if data != str(data):
        data = 'Este CEP não existe ou é invalido'
    return render_template('response.html', data=data)


@_app.route('/search_cep', methods=['POST'])
def search_cep():
    cep_expected = str(request.form['cep'])
    got = validation_cep(cep_expected)
    return response(got)




