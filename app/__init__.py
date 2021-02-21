from flask import Flask, render_template, request
from .views import validation_cep, address_view
from .settings.connection import connect_db
from .settings.config import config_db, config_ma, secret_key
import requests
import json


def create_app():
    app = Flask(__name__)
    connect_db(app)
    config_db(app)
    config_ma(app)
    secret_key(app)
    return app

_app = create_app()

@_app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@_app.route('/search_cep', methods=['GET'])
def response(data):
    return render_template('response.html', data=data)


@_app.route('/search_cep', methods=['POST'])
def search_cep():
    cep_expected = str(request.form['cep'])
    issave = str(request.form['save'])
    got = validation_cep(cep_expected, issave)
    return response(got)


@_app.route('/address', methods=['GET'])
def get_addresss():
    return address_view.get_all()


@_app.route('/address/<uid>', methods=['GET'])
def get_address(uid):
    return address_view.get_one(uid)


@_app.route('/address', methods=['POST'])
def post_address():
    return address_view.post()


@_app.route('/address/<uid>', methods=['DELETE'])
def delete_adress(uid):
    return address_view.delete(uid)


@_app.route('/address/<uid>', methods=['PUT'])
def update_address(uid):
    return address_view.update(uid)





