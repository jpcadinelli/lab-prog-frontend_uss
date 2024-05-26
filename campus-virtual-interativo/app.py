from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/eventos')
def eventos():
    return render_template('eventos.html')

@app.route('/instalacoes')
def instalacoes():
    return render_template('instalacoes.html')

@app.route('/clubes')
def clubes():
    return render_template('clubes.html')