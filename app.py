from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Teste'

@app.route('/contato')
def contato():
    nome = 'maria'
    email = "maria@gmail.com"
    return render_template('contato.html', nome = nome, email = email)

@app.route('/perfil', defaults = {'usuario': 'fulano'})
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

@app.route('/dados')
def dados():
    return render_template('dados.html')

@app.route("/recebedados", methods = ['POST'])
def recebedados():
    nome = request.form['nome']
    telefone = request.form['telefone']
    estado = request.form['estado']
    # Para aparecer mais de uma opção na tela do usuário.
    #Existe a opção get e a post. 
    escolaridade = request.form.getlist('esc')
    return f"{nome} - {telefone} - {estado} - {escolaridade}"


if __name__ == "__main__":
    app.run()
