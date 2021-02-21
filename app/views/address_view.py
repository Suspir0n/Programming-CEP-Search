from flask import current_app, jsonify, request
from ..models.address_model import AddressModel
from ..schemas.address_schemas import AddressSchema, address_schemas, address_schema 


def get_all():
    data = AddressModel.query.all()
    if data:
        result = address_schemas.dump(data)
        return jsonify({'message': 'successfully fetched', 'data': result}), 200

    return jsonify({'message': f'address dont exist', 'data': {}}), 404


def get_one(uid):
    data = AddressModel.query.get(uid)
    if data:
        result = address_schema.dump(data)
        return jsonify({'message': 'successfully fetched', 'data': result}), 201

    return jsonify({'message': f'address dont exist', 'data': {}}), 404


def delete(uid):
    data = AddressModel.query.get(uid)
    if not data:
        return jsonify({'message': f'address dont exist', 'data': {}}), 404
    if data:
        try:
            current_app.db.session.delete(data)
            current_app.db.session.commit()
            result = address_schema.dump(data)
            return jsonify({'message': 'successfully deleted', 'data': result}), 200
        except Exception as error:
            return jsonify({'message': 'unable to delete', 'data': {}}), 500



def update():
    address = gut_fields(uid)
    if not address['update']:
        return jsonify({'message': f"address don't exist", 'data': {}}), 404
    if address['update']:
        try:
            current_app.db.session.commit()
            result = address_schema.dump(address['update'])
            return jsonify({'message': 'successfully updated', 'data': result}), 201
        except Exception as error:
            return jsonify({'message': 'unable to update', 'data': {}}), 500


def post():
    address = gut_fields()
    try:
        current_app.db.session.add(address['post'])
        current_app.db.session.commit()
        result = address_schema.dump(address['post'])
        return jsonify({'message': 'successfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500
    

def gut_fields(uid=''):
    cep = request.json['cep']
    logradouro = request.json['logradouro']
    complemento = request.json['complemento']
    bairro = request.json['bairro']
    localidade = request.json['localidade']
    uf = request.json['uf']
    ibge = request.json['ibge']
    ddd = request.json['ddd']
    siafi = request.json['siafi']
    _address_post = AddressModel(cep, logradouro, complemento, bairro, localidade, uf, ibge, ddd, siafi)
    _address_update = passed_data_fields_model(uid, cep, logradouro, complemento, bairro, localidade, uf, ibge, ddd, siafi)
    data = {'post': _address_post, 'update': _address_update}
    return data


def passed_data_fields_model(uid, cep, logradouro, complemento, bairro, localidade, uf, ibge, ddd, siafi):
    _address = AddressModel.query.get(uid)
    if not _address:
        return jsonify({'message': "address don't exist", 'data': {}}), 404
    _address.cep = cep
    _address.logradouro = logradouro
    _address.complemento = complemento
    _address.bairro = bairro
    _address.localidade = localidade
    _address.uf = uf
    _address.ibge = ibge
    _address.ddd = ddd
    _address.siafi = siafi
    return _address