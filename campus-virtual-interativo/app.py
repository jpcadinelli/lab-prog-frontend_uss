from flask import Flask, render_template
from mocks import eventosMocks

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html', eventosMocks=eventosMocks)

@app.route('/instalacoes')
def instalacoes():
    return render_template('instalacoes.html')

@app.route('/clubes')
def clubes():
    return render_template('clubes.html')

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')

@app.route('/acesso')
def acesso():
    return render_template('acesso.html')