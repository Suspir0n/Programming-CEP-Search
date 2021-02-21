import uuid
from ..settings.config import db


class AddressModel(db.Model):
    __tablename__ = 'address'
    uid = db.Column(db.String, primary_key=True, default=uuid.uuid4, unique=True)
    cep = db.Column(db.String(10), unique=True, nullable=False)
    logradouro = db.Column(db.String(200), unique=True, nullable=False)
    complemento = db.Column(db.String(200), unique=True, nullable=False)
    bairro = db.Column(db.String(200), unique=True, nullable=False)
    localidade = db.Column(db.String(100), unique=True, nullable=False)
    uf = db.Column(db.String(2), unique=True, nullable=False)
    ibge = db.Column(db.String(50), unique=True, nullable=False)
    ddd = db.Column(db.String(3), unique=True, nullable=False)
    siafi = db.Column(db.String(5), unique=True, nullable=False)
    
    
    def __init__(self, cep, logradouro, complemento, bairro, localidade, uf, ibge, ddd, siafi):
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf
        self.ibge = ibge
        self.ddd = ddd
        self.siafi = siafi