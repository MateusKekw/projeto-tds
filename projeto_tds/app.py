from flask import *
from projeto_tds.functions import *
from werkzeug.security import *
import projeto_tds.brasileirao as brasileirao
import mysql.connector

connect = connect_init
app = Flask(__name__)

# definição de rotas
# Nome seguido de - // ingual o arquivo.html
friendlist = [
        {"username" : "Mateus", "time" : "Corinthians"},
        {"username" : "Milhomem", "time" : "Santos"},
    ]

userList = [
    {"username" : "Rafael", "time" : "Fortaleza"},
    {"username" : "Sarah", "time" : "Flamengo"},
]

mensagemlist = [
    {"username": "Milhomais", "mensagem" : "te convidou para a liga..."},
    {"username": "Bettio", "mensagem" : "quer ser seu amigo"}
]

@app.route("/")
def index ():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/login", methods = ['GET', 'POST'])
def loginPost():
    if request.method == 'POST':
        email = request.method.get(email)
        senha = request.method.get(senha)

        if not email or not senha:
            flash('Todos os campos são obrigatórios!')
            return redirect(url_for('loginPost'))
        
        try:
            conn = connect
            cursor = conn.cursor()
            cursor.execute (
                "SELECT * FROM users WHERE email = %s", (email,)
            )
            user = cursor.fetchone()

            if user and check_password_hash(user['hashSenha'], senha):
                flash('Login realizado com Sucesso!')
                return redirect(url_for('ligaMain'))
            else:
                flash('Email ou Senha incorretos!')
                return redirect(url_for('loginPost'))
        
        except mysql.connector.Error as err:
            flash(f'Erro: {err}')
            return redirect(url_for('loginPost'))
        finally:
            cursor.close()
            conn.close()
    return render_template('login.html')


@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/cadastro", methods = ['GET', 'POST'])
def cadastroPost():
    if request.method == 'POST':
        email = request.form.get(email)
        senha = request.form.get(senha)
        confSenha = request.form.get(confSenha)
        idade = request.form.get(idade)

        if senha != confSenha:
            flash('As senhas não são iguais!')
            return redirect(url_for('cadastroPost'))
    
        if not email or not senha or not confSenha or not idade:
            flash('Todos os campos são obrigatórios!')
            return redirect(url_for('cadastroPost'))
        
        hashSenha = generate_password_hash(senha)
        
        try:
            conn = connect
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (email, hashSenha, idade) VALUES (%s, %s, %s)", (email, hashSenha, idade)
            )
            conn.commit()

            flash('Prossiga com o cadastro')
            return redirect(url_for('userCadastro'))
        
        except mysql.connector.Error as err:
            flash(f'Erro: {err}')
            return redirect(url_for('cadastroPost'))
        
        finally:
            cursor.close()
            conn.close()
    return render_template('cadastro.html')



@app.route("/user-cadastro")
def userCadastro():
    return render_template('user.html')

@app.route("/user-cadastro", methods=['GET','POST'])
def userCadastroPost():
    if request.method == 'POST':
        usuario = request.form.get(usuario)
        time = request.form.get(time)

        if not usuario or not time:
            flash('Todos os campos são obrigatórios!')
            return redirect(url_for('userCadastroPost'))
    
        try:
            conn = connect
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO users (usuario, time) VALUES (%s, %s)", (usuario, time)
            )
            conn.commit()
            flash('Usuário registrado com Sucesso!')
            return redirect(url_for('login'))
                
        except mysql.connector.Error as err:
            flash(f'Erro: {err}')
            return redirect(url_for('userCadastroPost'))
                
        finally:
            cursor.close()
            conn.close()
    return render_template("user.html")
    



@app.route("/recuperação-de-conta")
def forgot_senha():
    return render_template('forgotsenha.html')


@app.route("/liga-mata")
def ligaMata():
    return render_template('Lmata_mata.html')

@app.route("/main")
def ligaMain():
    return render_template('ligaMain.html')

@app.route("/liga-classica")
def ligaClassica():
    return render_template('Lclassica.html')

# isso aqui não faz sentido, pq abriria o link do api do site?
# @app.route("/api/brasileirao")
# def get_brasileirao():
#     return brasileirao.baixarbrasileirao()

@app.route("/amizade")
def amizade():
    return render_template('amizade.html', amizades=friendlist)

@app.route("/nova-amizade")
def newamizade():
    return render_template('addamizade.html', usuarios = userList)

@app.route("/configuracao")
def configurar():
    return render_template('config.html')

@app.route("/regra")
def regras():
    return render_template('regras.html')

@app.route("/fundo")
def fundo():
    return render_template('fundo.html')

@app.route("/mail-box")
def mensagens():
    return render_template('mensagens.html', mensagens = mensagemlist)
