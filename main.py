import alunos
import database
from alunos import processar_cadastro
from database import listar_alunos
from database import criar_banco

criar_banco()

print("------ SISTEMA DE NOTAS ------")
print("")

while True:
    opcao = input("Digite '1' se você quer adicionar um aluno, '2' se quiser visualizar a lista e '3' se quiser sair")

    if opcao == "1":
        nome = input("Informe o nome do aluno: ")
        n1 = float(input("Informe a primeira nota do aluno: "))
        n2 = float(input("Informe a segunda nota do aluno: "))

        processar_cadastro(nome, n1, n2)
        print(f"Aluno cadastrado!")

    elif opcao == "2":
        listagem_alunos = listar_alunos()
        if not listagem_alunos:
            print("Ainda não há alunos cadastrados!")
        else:
            print("------ LISTAGEM DE ALUNOS ------")
            print("")
            for aluno in listagem_alunos:
                print(f"Nome: {aluno[0]} | Matrícula: {aluno[1]} | N1: {aluno[2]} | N2: {aluno[3]} | Média: {aluno[4]} | Status: {aluno[5]}")
    
    elif opcao == "3":
        break

    else:
        print("Opção inválida! Digite '1' se você quer adicionar um aluno, '2' se quiser visualizar a lista e '3' se quiser sair")