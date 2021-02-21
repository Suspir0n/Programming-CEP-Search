from flask import jsonify
from ..views.address_view import gut_fields
import requests
import json
import re

all_data = list()


def validation_cep(cep_expected, issave):
    cep_regex_generation = re.compile(r'^\d{8}$') 
    got = cep_regex_generation.findall(cep_expected)
    if got[0] == cep_expected:
        result = ordering_from_api(cep_expected, issave)
        return result
    return {'message': 'This CEP is invalid'}


def ordering_from_api(cep, issave):
    try:
        link = f'https://viacep.com.br/ws/{cep}/json'
        my_data = requests.get(link)
        if my_data.status_code == 400:
            return {'message': 'CEP with invalid format'}
        my_json = my_data.content.decode('utf8').replace("'", '"')
        got = json.loads(my_data.content)
        if issave == 'sim':
            requests.post('http://127.0.0.1:5000/address', json=got)
        return got['logradouro']
    except:
        return {'message': 'error querying the CEP api'}
        
    