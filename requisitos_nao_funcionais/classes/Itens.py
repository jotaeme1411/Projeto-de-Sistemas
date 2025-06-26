from enums.enum_itens import Status_Itens

class Itens:
    def __init__(self, ID:int, nome_do_item:str, quantidade:int, status:Status_Itens, ID_doador:int):
        self.ID = ID
        self.nome_do_item = nome_do_item
        self.quantidade = quantidade
        self.status = status
        self.ID_doador = ID_doador

