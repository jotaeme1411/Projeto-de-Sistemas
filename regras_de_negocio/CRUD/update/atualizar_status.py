from requisitos_funcionais.app.models import Solicitacoes, Status_Solicitacoes, Itens, Status_Itens
from requisitos_funcionais.app import db

def atualizar_status_item(item_id: int, novo_status: Status_Itens):
    item = Itens.query.get(item_id)
    if not item:
        raise ValueError("Item não encontrado.")

    item.status = novo_status
    db.session.commit()
    return item

def atualizar_status_solicitacao(solicitacao_id: int, novo_status: Status_Solicitacoes):
    solicitacao = Solicitacoes.query.get(solicitacao_id)
    if not solicitacao:
        raise ValueError("Solicitação não encontrada.")

    solicitacao.status = novo_status
    db.session.commit()
    return solicitacao