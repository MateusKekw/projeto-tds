from flask import *
from projeto_tds.functions import *

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