from flask import Flask, render_template

app = Flask(__name__)

# simples classe para exemplo
class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/')
def hello():
    jogo1 = Jogo('Super Mario', 'Acao', 'SNES')
    jogo2 = Jogo('Pokemon Gold', 'RPG', 'GBA')
    jogo3 = Jogo('Mortal Kombat', 'Luta', 'SNES')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)


if __name__ == '__main__':
    app.run()
