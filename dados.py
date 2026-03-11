import tkinter as tk
from tkinter import messagebox

lista_alunos = []

def cadastrar_aluno():
    nome = entry_nome.get()
    matricula = entry_matricula.get()
    n1 = float(entry_n1.get())
    n2 = float(entry_n2.get())

    media = (n1 + n2) / 2

    aluno = {
        "nome": nome,
        "matricula": matricula,
        "n1": n1,
        "n2": n2,
        "media": media
    }

    lista_alunos.append(aluno)
    messagebox.showinfo("Sucesso", "Aluno cadastrado!")

def mostrar_relatorio():
    relatorio = ""
    for aluno in lista_alunos:
        status = "Aprovado" if aluno["media"] >= 7 else "Reprovado"
        relatorio += f"{aluno['nome']} - Média: {aluno['media']:.2f} - {status}\n"

    messagebox.showinfo("Relatório", relatorio)

# janela pra ver as coisas
janela = tk.Tk()
janela.title("Sistema de Notas")
janela.geometry("400x300")

# campos pra preencher
tk.Label(janela, text="Nome").pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

tk.Label(janela, text="Matrícula").pack()
entry_matricula = tk.Entry(janela)
entry_matricula.pack()

tk.Label(janela, text="Nota 1").pack()
entry_n1 = tk.Entry(janela)
entry_n1.pack()

tk.Label(janela, text="Nota 2").pack()
entry_n2 = tk.Entry(janela)
entry_n2.pack()

# butão
tk.Button(janela, text="Cadastrar", command=cadastrar_aluno).pack(pady=5)
tk.Button(janela, text="Ver Relatório", command=mostrar_relatorio).pack(pady=5)
tk.Button(janela, text="Sair", command=janela.quit).pack(pady=5)

janela.mainloop() 