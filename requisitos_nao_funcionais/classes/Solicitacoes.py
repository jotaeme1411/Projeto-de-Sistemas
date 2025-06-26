from enums.enum_solicitacoes import Status_Solicitacoes

class Solicitacoes:
    def __init__(self, ID:int, desc_necessidade:str, status:Status_Solicitacoes, ID_beneficiario:int):
        self.ID = ID
        self.desc_necessidade = desc_necessidade
        self.status = status
        self.ID_beneficiario = ID_beneficiario

        