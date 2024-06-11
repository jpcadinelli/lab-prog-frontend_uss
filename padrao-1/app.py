from flask import Flask, render_template, request
from mocks import listaMocks

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    if request.method == "POST":
        pesquisa = request.form["pesquisa"]
        resultadoPesquisa = [item for item in listaMocks if pesquisa.lower() in item.nome.lower() or pesquisa.lower() in item.descricao.lower()]
        return render_template("buscar.html", resultadoPesquisa=resultadoPesquisa)
    return render_template("buscar.html", resultadoPesquisa=listaMocks)