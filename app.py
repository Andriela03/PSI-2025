from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Teste'

@app.route('/contato')
def contato():
    return 'contato@gmail.com'

if __name__ == "__main__":
    app.run()
