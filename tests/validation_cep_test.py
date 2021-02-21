import re


def test_happy_way():
    cep_expected = '40353200'
    cep_regex_generation = re.compile(r'^\d{8}$') 
    got = cep_regex_generation.findall(cep_expected)
    assert (got[0] == cep_expected) is True  
    

def test_sad_way():
    invalid_cep_expected = ['999999999', '99999 999', '99999-999', 'abc99ab9']
    cep_regex_generation = re.compile(r'^\d{8}$') 
    for invalid_cep in invalid_cep_expected:
        got = cep_regex_generation.findall(invalid_cep)
        assert (got != []) is False
        
    
