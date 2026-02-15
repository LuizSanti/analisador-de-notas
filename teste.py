print("------- Analisador de notas (-------")
print(" ")

lista_alunos = []

while True:
    nome = input("Informe o nome do aluno (para encerrar digite 'sair'): ")
    if nome.lower() == 'sair':
        break
    matricula = int(input("Informe a matrícula do aluno: "))
    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input("Informe a segunda nota: "))

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "n1": n1,
        "n2": n2
    }
    lista_alunos.append(aluno)
    print("Aluno cadastrado com sucesso!")

    print("------- Registro de notas (-------")
    print(" ")

    for aluno in lista_alunos:
        print(f"Aluno: {aluno['nome']} | {aluno['matricula']} | {aluno['n1']} | {aluno['n2']}")