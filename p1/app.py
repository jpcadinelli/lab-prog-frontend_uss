from flask import Flask, render_template
from produto import Produto
from comentario import Comentario

hamburguer = Produto(1, "Hamburguer", "img/hamburguer.jpg", "O nosso hamburguer é feito só com ingredientes altamente selecionados, possibilitando fazer essa gloriosa obra de arte saborosa!", "R$ 49,99", ["Pão Brioche Max", "Blend de 180g de Picanha", "Queijo Qualho", "Bacon Defumado", "Alface Americana", "Tomate Italiano", "Molho Especial"])
comentario1Hamburguer = Comentario(1, "José Orelha", "Despois que comi este hamburguer, nunca mais comi em casa como ele todo dia!", 1)
comentario2Hamburguer = Comentario(2, "Maria da Silva", "Que hamburguer incrível! To anciosa pra comer de novo!", 1)

picanha = Produto(2, "Picanha", "img/picanha.jpg", "Nossa Picanha é Argentina e feita na brasa pra deixar todos os carnívoros muito bem servidos!", "R$ 159,99", ["Picanha", "Sal", "Alecrim"])
comentario1Picanha = Comentario(3, "João das Couves", "Essa picanha é muito bem servida, Recomendo!", 2)
comentario2Picanha = Comentario(4, "Ana dos Santos", "Tão bom que ganhou do churrasco do meu pai!", 2)

macarrao = Produto(3, "Macarrão", "img/macarrao.jpg", "Nosso cargo chefe! Macarrão de respeito de uma legítma cantina italiana!", "R$ 89,99", ["Macarrão", "Tomate cereja", "Molho de tomate", "Alho", "Azeite"])
comentario1Macarrao = Comentario(5, "Ivan", "Que macarrão bom!", 3)
comentario2Macarrao = Comentario(6, "Augusta", "To vindo todo dia comer esse macarrão gostoso!", 3)

cardapio = [hamburguer, picanha, macarrao]
comentarios = [comentario1Hamburguer, comentario2Hamburguer, comentario1Picanha, comentario2Picanha, comentario1Macarrao, comentario2Macarrao]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", cardapio = cardapio)

@app.route("/produto/<int:id>")
def produto(id:int):
    for produto in cardapio:
        if produto.id == id:
            return render_template("produto.html", produto = produto, comentarios = comentarios)
    return "<h1>404 Page Not Found.</h1>"