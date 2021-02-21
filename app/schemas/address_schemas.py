from ..settings.config import ma


class AddressSchema(ma.Schema):
    class Meta:
        fields = ('uid', 'cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf', 'ibge', 'ddd', 'siafi')
        
address_schema = AddressSchema()
address_schemas = AddressSchema(many=True)