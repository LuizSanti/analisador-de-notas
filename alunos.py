import database

def calcular_media(n1, n2):
    calculo_media = (n1 + n2) / 2
    return calculo_media

def verificar_status(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

def processar_cadastro(nome, n1, n2):
    m = calcular_media(n1, n2)
    s = verificar_status(m)

    database.cadastrar_aluno(nome, n1, n2, m, s)