class Evento:
    def __init__(self, id, nome, descricao, palestrante, local, urlMapa, imagem, dia, mes):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.palestrante = palestrante
        self.local = local
        self.urlMapa = urlMapa
        self.imagem = imagem
        self.dia = dia
        self.mes = mes

class Instalacao:
    def __init__(self, id, nome, descricao, local, urlMapa, imagem, horarioFuncionamento, disponibilidade, contato):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.local = local
        self.urlMapa = urlMapa
        self.imagem = imagem
        self.horarioFuncionamento = horarioFuncionamento
        self.disponibilidade = disponibilidade
        self.contato = contato

class Clube:
    def __init__(self, id, nome, descricao, eventos, noticias, imagem, contato):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.eventos = eventos
        self.noticias = noticias
        self.imagem = imagem
        self.contato = contato