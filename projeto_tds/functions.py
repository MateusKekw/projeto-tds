from flask import *
import mysql.connector

import projeto_tds.brasileirao as brasileirao

# Funções primordiais para o funcionamento do sistema
# (por enquanto)

def connect_init(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)


def bolões(connect, chave, IdPartida, hora):
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Boloes (chave, IdPartida, hora) VALUES (%s, %i, %s)", (chave, IdPartida, hora))
    connect.commit() 
    cursor.close()