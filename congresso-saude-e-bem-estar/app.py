from flask import Flask, render_template
from mocks import palestras, palestrantes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", palestras=palestras, palestrantes=palestrantes)

@app.route("/ministrantes/<int:id>")
def ministrantes(id:int):
    for palestra in palestras:
        if palestra.id == id:
            return render_template("palestrantes.html", palestra=palestra, palestrantes=palestrantes)
    return "<h1>404 Page Not Found.</h1>"