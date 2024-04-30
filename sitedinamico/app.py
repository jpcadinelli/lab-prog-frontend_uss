from flask import Flask, render_template
from curso import Curso

app = Flask(__name__)

eng_software = Curso(1, "Engenharia de Software", "Bacharelado", "Presencial", 4)
eng_civil = Curso(2, "Engenharia Civil", "Bacharelado", "Presencial", 5)
eng_eletrica = Curso(3, "Engenharia Elétrica", "Bacharelado", "Presencial", 5)
psicologia = Curso(4, "Psicologia", "Bacharelado", "Presencial", 4)
gestao_venda = Curso(5, "Gestão de Vendas", "Tecnólogo", "Digital", 2)
curso_catalogo = [eng_software, eng_civil, eng_eletrica, gestao_venda, psicologia]

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/curso-catalogo")
def catalogo_curso():
    return render_template("catalogo-curso.html", 
                           cursos = curso_catalogo)

@app.route("/curso/<int:id>")
def curso(id:int):
    for curso_do_catalogo in curso_catalogo:
        if curso_do_catalogo.id == id:
            return render_template("curso.html", curso = curso_do_catalogo)
    return "<h1>Ops! Curso não encontrado!</h1>"
