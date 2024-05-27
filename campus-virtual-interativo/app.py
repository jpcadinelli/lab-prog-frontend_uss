from flask import Flask, render_template
from mocks import eventosMocks, instalacoesMocks, clubesMocks, servicosMocks

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html', eventosMocks=eventosMocks)

@app.route('/evento/<int:id>')
def evento(id:int):
    for eventoMocks in eventosMocks:
        if id == eventoMocks.id:
            return render_template('evento.html', eventoMocks=eventoMocks)
    return render_template('erro.html', mensagem='404 Evento não encontrado.')

@app.route('/instalacoes')
def instalacoes():
    return render_template('instalacoes.html', instalacoesMocks=instalacoesMocks)

@app.route('/instalacao/<int:id>')
def instalacao(id:int):
    for instalacaoMocks in instalacoesMocks:
        if id == instalacaoMocks.id:
            return render_template('instalacao.html', instalacaoMocks=instalacaoMocks)
    return render_template('erro.html', mensagem='404 Instalação não encontrado.')

@app.route('/clubes')
def clubes():
    return render_template('clubes.html', clubesMocks=clubesMocks)

@app.route('/clube/<int:id>')
def clube(id:int):
    for clubeMocks in clubesMocks:
        if id == clubeMocks.id:
            return render_template('clube.html', clubeMocks=clubeMocks)
    return render_template('erro.html', mensagem='404 Clube não encontrado.')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html', servicosMocks=servicosMocks)

@app.route('/servico/<int:id>')
def servico(id:int):
    for servicoMocks in servicosMocks:
        if id == servicoMocks.id:
            return render_template('servico.html', servicoMocks=servicoMocks)
    return render_template('erro.html', mensagem='404 Serviço não encontrado.')

@app.route('/acesso')
def acesso():
    return render_template('acesso.html')