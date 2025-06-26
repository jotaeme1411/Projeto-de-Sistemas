from requisitos_funcionais.app.models import Itens

def listar_itens():
    return Itens.query.all()