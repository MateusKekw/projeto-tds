from flask import *
from projeto_tds.functions import *

connect = connect_init
app = Flask(__name__)

# definição de rotas
# Nome seguido de - // ingual o arquivo.html

@app.route("/")
def index ():
    return render_template('index.html')