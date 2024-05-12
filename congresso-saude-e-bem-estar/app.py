from flask import Flask, render_template
from mocks.mocks import palestras, palestrantes

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", palestras=palestras, palestrantes=palestrantes)