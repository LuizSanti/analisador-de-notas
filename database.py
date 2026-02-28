import sqlite3

def criar_banco():
    conn = sqlite3.connect('alunos.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS alunos
             (matricula INTEGER PRIMARY KEY AUTOINCREMENT,
             nome TEXT,
             n1 FLOAT,
             n2 FLOAT,
             media FLOAT,
             status TEXT);''')
    conn.commit()
    conn.close()

def cadastrar_aluno(nome, n1, n2, media, status):
    conn = sqlite3.connect('alunos.db')
    conn.execute("INSERT INTO alunos (nome, n1, n2, media, status) VALUES (?, ?, ?, ?, ?)", 
        (nome, n1, n2, media, status)
    )
    conn.commit()
    conn.close()   

def listar_alunos():
    conn = sqlite3.connect('alunos.db')
    lista_alunos = conn.execute("SELECT nome, matricula, n1, n2, media, status from alunos")
    dados = lista_alunos.fetchall()
    conn.close()
    return dados