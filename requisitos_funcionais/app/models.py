from requisitos_funcionais.app import db
from sqlalchemy import Enum

from requisitos_nao_funcionais.enums.enum_itens import Status_Itens
from requisitos_nao_funcionais.enums.enum_solicitacoes import Status_Solicitacoes

class Doador(db.Model):
    __tablename__ = 'doadores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    contato = db.Column(db.String(50), nullable=False)
    endereco = db.Column(db.String(250), nullable=False)

class Itens(db.Model):
    __tablename__ = 'itens'
    id = db.Column(db.Integer, primary_key=True)
    nome_do_item = db.Column(db.String(150), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    status = db.Column(Enum(Status_Itens), nullable=False)
    ID_doador = db.Column(db.Integer, db.ForeignKey('doadores.id'), nullable=False)

class Solicitacoes(db.Model):
    __tablename__ = 'solicitacoes'
    id = db.Column(db.Integer, primary_key=True)
    desc_necessidade = db.Column(db.String(250), nullable=False)
    status = db.Column(Enum(Status_Solicitacoes), nullable=False)
    ID_beneficiario = db.Column(db.Integer, db.ForeignKey('doadores.id'), nullable=False)