from requisitos_funcionais.app.models import Doador

def listar_doadores():
    return Doador.query.all()