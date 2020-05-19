from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('lista.html', titulo='Jogos')


if __name__ == '__main__':
    app.run()
