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
        {"username" : "Milhomem", "time" : "Santos"}, # isso aqui tem que pegar do banco de dados joel, calma fi
    ]

userList = [
    {"username" : "Rafael", "time" : "Fortaleza"},
    {"username" : "Arthur", "time" : "Flamengo"},
    {"username" : "Artur", "time" : "VascoDaGama"}, # isso aqui tem que pegar do banco de dados joel, calma fi
]

mensagemlist = [
    {"username": "Milhomais", "mensagem" : "te convidou para a liga..."},
    {"username": "Bettio", "mensagem" : "quer ser seu amigo"} # isso aqui não, isso aqui ta dboa
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


@app.route("/recuperacao-de-conta")
def forgot_senha():
    return render_template('forgotsenha.html')

@app.route("/recuperacao-de-conta", methods=["GET","POST"])
def forgot_senhaPost():
    if request.method == 'POST':
        email = request.form['email']
        new_password = request.form['Password']
        Conf = request.form['Conf']

        conn = connect
        cursor = conn.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users", (email,))
        user = cursor.fetchtone()

        if Conf != new_password:
            flash('As senhas não são iguais!')
            return redirect(url_for('forgot_senhaPost'))
        
        if user:
            senha_hash = generate_password_hash(new_password)
            cursor.execute(
                "UPDATE users SET hashSenha = %s WHERE email = %s", (senha_hash, email)
            )
            conn.commit()
            cursor.close()
            conn.close()
            flash('Senha redefinida com sucesso!', 'sucess')
            
        else:
            flash('Email não encontrado ou senha repetida')
            return redirect(url_for('forgot_senhaPost'))
    return render_template('forgotsenha.html')


@app.route("/liga-mata")
def ligaMata():
    return render_template('Lmata_mata.html')


@app.route("/liga-principal")
def ligaMain():
    return render_template('ligaMain.html')


@app.route("/")
def principal():
    conn = connect
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM times")
    times = cursor.fetchall()
    conn.close()
    return render_template('telaInicial.html', times = times)

@app.route("/", methods=['POST'])
def fazerPalpite():
    dados = request.json
    time_a = dados.get('timeA')
    time_b = dados.get('timeB')
    placar_a = dados.get('placarA')
    placar_b = dados.get('placarB')

    if not all ([time_a, time_b, placar_a, placar_b]):
        return jsonify({'Erro': 'Dados incompletos'}), 400
    
    conn = connect
    cursor = conn.cursor()
    cursor.execute("INSERT INTO boloes (timeA, timeB, placarA, placarB) VALUES (%s, %s, %s, %s)", (time_a, time_b, placar_a, placar_b),)
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'mensagem': 'Palpite salvo com sucesso'})    


@app.route("/main")
def principal():
    return render_template('telaInicial.html')

@app.route("/liga-classica")
def ligaClassica():
    return render_template('Lclassica.html')

# isso aqui não faz sentido, pq abriria o link da API do site?
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

@app.route("/convite-liga")
def convidar():
    return render_template('convidarliga.html', usuarios = userList)
