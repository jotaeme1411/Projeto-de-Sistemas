from requisitos_funcionais.app import db
from requisitos_funcionais.app.models import Itens, Status_Itens

def criar_item(nome_do_item: str, quantidade: int, ID_doador: int = None):
    if not nome_do_item or quantidade <= 0:
        raise ValueError("Nome do item é obrigatório e quantidade deve ser maior que zero.")
    
    novo_item = Itens(
        nome_do_item=nome_do_item, 
        quantidade=quantidade, 
        status=Status_Itens["DISPONIVEL"], 
        ID_doador=ID_doador
    )

    db.session.add(novo_item)
    db.session.commit()

    return novo_item