import sqlite3

conn = sqlite3.connect('alunos.db')

conn.execute('''CREATE TABLE IF NOT EXISTS alunos
             (matricula INTEGER PRIMARY KEY AUTOINCREMENT,
             nome TEXT,
             n1 FLOAT,
             n2 FLOAT,
             media FLOAT,
             status TEXT);''')
conn.commit()

while True:
    opcao = input("Digite '1' para adicionar novo aluno, '2' para visualizar a lista de alunos ou '3' para sair: ")
    if opcao == "1":
        while True:
            nome = input("Informe o nome do aluno: ")
            n1 = float(input("Informe a primeira nota do aluno: "))
            n2 = float(input("Informe a segunda nota do aluno: "))

            media = (n1 + n2)/2

            if media >= 7:
                status = "Aprovado" 
            else:
                status = "Reprovado"

            conn.execute("INSERT INTO alunos (nome, n1, n2, media, status) VALUES (?, ?, ?, ?, ?)", 
                (nome, n1, n2, media, status)
            )
            conn.commit()

            print("Aluno cadastrado!")
            final = input("Deseja cadastrar outro aluno? (Responda 'sim' ou 'não'): ")
            if final.lower() == 'não':
                break   


    elif opcao == "2":
        lista_alunos = conn.execute("SELECT nome, matricula, n1, n2, media, status from alunos")
        print("------- Lista de Alunos ------")
        print(" ")
        for aluno in lista_alunos:
            print(" ")
            print(f"Aluno: {aluno [0]} | Matrícula: {aluno[1]} | N1: {aluno[2]} | N2: {aluno[3]} | Média: {aluno[4]} | Status: {aluno[5]}")
    elif opcao == "3":
        break