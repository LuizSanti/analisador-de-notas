<<<<<<< Updated upstream
def main():

    print("--------- Analisador de Notas ---------")
    print(" ")

    lista_alunos = []
=======
print("--------- Analisador de Notas ---------")
print(" ")
>>>>>>> Stashed changes

    while True:
        nome = input("Informe o nome do aluno (ou 'sair' para encerrar): ")

        if nome.lower() == 'sair':
            break

        matricula = int(input("Informe a matrícula do aluno: "))
        n1 = float(input("Informe a primeira nota: "))
        n2 = float(input("Informe a segunda nota: "))

        media = (n1 + n2) / 2

        aluno = {
            "nome": nome,
            "matricula": matricula,
            "n1": n1,
            "n2": n2,
            "media" : media
        }

        lista_alunos.append(aluno)
        print("Aluno cadastrado com sucesso!")
        final = input("Deseja cadastrar outro aluno?: ")
        if final.lower() != "n":
            print("Cadastro de alunos finalizado!")
            break

    print("--------- Relatório de Notas ---------")
    print(" ")

    for aluno in lista_alunos:   
        status = "Aprovado" if aluno["media"] >= 7 else "Reprovado"
        print(f"Aluno: {aluno['nome']} | {aluno['matricula']} | {aluno['n1']} | {aluno['n2']} | Média: {aluno['media']:.2f} | Status: {status}")

while True:
    main()

    while True:
        resposta = input("Reiniciar programa?: ").lower().strip()

        if resposta in ["s", "sim"]:
            print("Reiniciando o programa...")
            break 

        elif resposta in ["n", "nao", "não"]:
            print("Finalizando o programa. Até mais!")
            exit()

        else:
            print("Resposta inválida.")
