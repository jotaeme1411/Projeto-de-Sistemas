from requisitos_funcionais.app.models import Solicitacoes

def listar_solicitacoes():
    return Solicitacoes.query.all()