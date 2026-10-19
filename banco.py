import sqlite3

conexao = sqlite3.connect("Sistema_academico.db")

cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matricula TEXT NOT NULL,
    curso TEXT NOT NULL,
    email TEXT NOT NULL)
""")

conexao.commit()
conexao.close()

print("Banco de dados criado com sucesso!")
