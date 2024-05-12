class Palestra:
    def __init__(self, id, nome, descricao, dia, mes, palestrantes):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.dia = dia
        self.mes = mes
        self.palestrantes = palestrantes

class Palestrante:
    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao