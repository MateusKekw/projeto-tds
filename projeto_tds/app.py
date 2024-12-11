from flask import *
from projeto_tds.functions import *

import projeto_tds.brasileirao as brasileirao

connect = connect_init
app = Flask(__name__)

# definição de rotas
# Nome seguido de - // ingual o arquivo.html

@app.route("/")
def index ():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/recuperação-de-conta")
def forgot_senha():
    return render_template('forgotsenha.html')

@app.route("/user-cadastro")
def userCadastro():
    return render_template('user.html')

@app.route("/liga-mata")
def ligaMata():
    return render_template('Lmata_mata.html')

@app.route("/liga-principal")
def ligaMain():
    return render_template('ligaMain.html')

@app.route("/liga-classica")
def ligaClassica():
    return render_template('Lclassica.html')

@app.route("/api/brasileirao")
def get_brasileirao():
    return brasileirao.baixarbrasileirao()