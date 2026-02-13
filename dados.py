print("--------- Analisador de Notas ---------")
print(" ")
# nome_aluno = (input("Informe o nome do aluno: "))
# matricula_aluno = (input("Informe a matrícula do aluno: "))
# n1 = (input("Informe a primeira nota do aluno: "))
# n2 = (input("Informe a segunda nota do aluno: "))

# def info_aluno():
#     print(f"O nome do aluno é {nome_aluno}")
#     print(f"A matrícula do aluno é {matricula_aluno}")

# info_aluno()

lista_alunos = []

while True:
    nome = input("Informe o nome do aluno (ou 'sair' para encerrar): ")
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

print("--------- Relatório de Notas ---------")
print(" ")

for aluno in lista_alunos:
    print(f"Aluno: {aluno['nome']} | {aluno['matricula']} | {aluno['n1']} | {aluno['n2']}")