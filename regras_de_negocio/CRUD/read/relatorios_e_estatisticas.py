from requisitos_funcionais.app.models import Itens, Solicitacoes, Doador, Status_Itens, Status_Solicitacoes
from requisitos_funcionais.app import db
from sqlalchemy import func

def total_doacoes_realizadas():
    return db.session.query(func.count(Itens.id))\
        .filter(Itens.status == Status_Itens.ENTREGUE.value).scalar()

def lista_itens_entregues():
    itens = Itens.query.filter_by(status=Status_Itens.ENTREGUE.value).all()
    return [{
        "id": item.id,
        "nome_do_item": item.nome_do_item,
        "id_doador": item.ID_doador
    } for item in itens]

def total_beneficiarios_atendidos():
    return db.session.query(Solicitacoes.ID_beneficiario)\
        .filter(Solicitacoes.status == Status_Solicitacoes.ATENDIDA.value)\
        .distinct().count()

def total_solicitacoes_atendidas():
    return db.session.query(func.count(Solicitacoes.id))\
        .filter(Solicitacoes.status == Status_Solicitacoes.ATENDIDA.value).scalar()