from flask import jsonify
import requests
import json
import re

all_data = list()


def validation_cep(cep_expected):
    cep_regex_generation = re.compile(r'^\d{8}$') 
    got = cep_regex_generation.findall(cep_expected)
    if got[0] == cep_expected:
        result = ordering_from_api(cep_expected)
        return result
    return jsonify({'message': 'This CEP is invalid'}), 401


def ordering_from_api(cep):
    try:
        link = f'https://viacep.com.br/ws/{cep}/json'
        my_data = requests.get(link)
        if my_data.status_code == 400:
            return jsonify({'message': 'CEP with invalid format'}), 400
        my_json = my_data.content.decode('utf8').replace("'", '"')
        got = json.loads(my_json)
        all_data.append(got['logradouro'])
        return got['logradouro']
    except:
        return jsonify({'message': 'error querying the CEP api'}), 401
        
    