from flask import *
import mysql.connector


# Funções primordiais para o funcionamento do sistema
# (por enquanto)

def connect_init(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

def cadastro(connect, username, email, senha, idade):
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Usuario (username, email, senha, idade) VALUES (%s, %s, %s, %i)", (username, email, senha, idade))
    connect.commit() 
    cursor.close()

def bolões(connect, chave, IdPartida, hora):
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Boloes (chave, IdPartida, hora) VALUES (%s, %i, %s)", (chave, IdPartida, hora))
    connect.commit() 
    cursor.close()

def partidas(connect, hora, data, local, IdTime):
    cursor = connect.cursor()
    cursor.execute("INSERT INTO Partidas (hora, data, local, IdTime) VALUES (%s, %s, %s, %i)", (hora, data, local, IdTime))
