from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Teste'

@app.route('/contato')
def contato():
    nome = 'maria'
    email = "maria@gmail.com"
    return render_template('contato.html', nome = nome, email = email)

@app.route('/perfil', defaults = {'nome': 'fulano'})
@app.route('/perfil/<usuario>')
def perfil(usuario):
    usuario = "fulano"
    return render_template('perfil.html', usuario = usuario)


@app.route('/semestre/<int:x>')
def semestre(x):
    y = x + 1
    return render_template('semestre.html', x=x, y=y)

@app.route('/soma/<int:n1>/<int:n2>')
def soma (n1, n2):
    return str(n1+n2)

@app.route('/exemplo')
def exemplo():
    return render_template('exemplo.html')

@app.route('/exemplo2')
def exemplo2():
    return render_template('exemplo2.html')

if __name__ == "__main__":
    app.run()
