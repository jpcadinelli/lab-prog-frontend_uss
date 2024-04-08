from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/pagina2")
def pag2():
    return render_template("pagina2.html")