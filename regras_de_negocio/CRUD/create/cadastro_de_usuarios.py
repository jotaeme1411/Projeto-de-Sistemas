from requisitos_funcionais.app import db
from requisitos_funcionais.app.models import Doador

def criar_doador(nome:str, contato:str, endereco:str):
    if not nome or not contato or not endereco:
        raise ValueError("Todos os campos são obrigatórios.")

    novo_doador = Doador(nome=nome, contato=contato, endereco=endereco)
    db.session.add(novo_doador)
    db.session.commit()

    return novo_doador