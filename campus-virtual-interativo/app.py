from flask import Flask, render_template, request
from mocks import eventosMocks, instalacoesMocks, clubesMocks, servicosMocks, transportesMocks

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_query = request.form['search']
        filtered_eventos = [evento for evento in eventosMocks if search_query.lower() in evento.nome.lower() or search_query.lower() in evento.descricao.lower()]
        filtered_instalacoes = [instalacao for instalacao in instalacoesMocks if search_query.lower() in instalacao.nome.lower() or search_query.lower() in instalacao.descricao.lower()]
        filtered_clubes = [clube for clube in clubesMocks if search_query.lower() in clube.nome.lower() or search_query.lower() in clube.descricao.lower()]
        filtered_servicos = [servico for servico in servicosMocks if search_query.lower() in servico.nome.lower() or search_query.lower() in servico.descricao.lower()]
        filtered_transportes = [transporte for transporte in transportesMocks if search_query.lower() in transporte.tipo.lower() or search_query.lower() in transporte.descricao.lower()]
        return render_template('index.html', eventosMocks=filtered_eventos, instalacoesMocks=filtered_instalacoes, clubesMocks=filtered_clubes, servicosMocks=filtered_servicos, transportesMocks=filtered_transportes, search_query=search_query)
    return render_template('index.html', eventosMocks=eventosMocks, instalacoesMocks=instalacoesMocks, clubesMocks=clubesMocks, servicosMocks=servicosMocks, transportesMocks=transportesMocks, search_query='')

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

@app.route('/transportes')
def transportes():
    return render_template('transportes.html', transportesMocks=transportesMocks)

@app.route('/transporte/<int:id>')
def transporte(id:int):
    for transporteMocks in transportesMocks:
        if id == transporteMocks.id:
            return render_template('transporte.html', transporteMocks=transporteMocks)
    return render_template('erro.html', mensagem='404 Transporte ou Acesso não encontrado.')