from requisitos_funcionais.app.models import Solicitacoes, Status_Solicitacoes
from requisitos_funcionais.app import db

def criar_solicitacao(desc_necessidade: str, id_beneficiario: int):
    if not desc_necessidade or not id_beneficiario:
        raise ValueError("Descrição da necessidade e ID do beneficiário são obrigatórios.")

    nova_solicitacao = Solicitacoes(
        desc_necessidade=desc_necessidade,
        status=Status_Solicitacoes["PENDENTE"],
        ID_beneficiario=id_beneficiario
    )

    db.session.add(nova_solicitacao)
    db.session.commit()

    return nova_solicitacao