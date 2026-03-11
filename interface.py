import tkinter as tk
from tkinter import messagebox, ttk
import database
import alunos

database.criar_banco()

def cadastrar():
    nome = entry_nome.get().strip()
    matricula_str = entry_matricula.get().strip()
    n1_str = entry_n1.get().strip()
    n2_str = entry_n2.get().strip()

    if not nome:
        messagebox.showerror("Erro", "Informe o nome do aluno.")
        return

    try:
        n1 = float(n1_str)
        n2 = float(n2_str)
    except ValueError:
        messagebox.showerror("Erro", "As notas devem ser números válidos.")
        return

    if not (0 <= n1 <= 10 and 0 <= n2 <= 10):
        messagebox.showerror("Erro", "As notas devem estar entre 0 e 10.")
        return

    alunos.processar_cadastro(nome, n1, n2)
    messagebox.showinfo("Sucesso", f"Aluno '{nome}' cadastrado com sucesso!")

    entry_nome.delete(0, tk.END)
    entry_matricula.delete(0, tk.END)
    entry_n1.delete(0, tk.END)
    entry_n2.delete(0, tk.END)


def mostrar_relatorio():
    lista = database.listar_alunos()

    if not lista:
        messagebox.showinfo("Relatório", "Nenhum aluno cadastrado ainda.")
        return

    janela_rel = tk.Toplevel(janela)
    janela_rel.title("Relatório de Alunos")
    janela_rel.geometry("680x300")

    colunas = ("Nome", "Matrícula", "N1", "N2", "Média", "Status")
    tabela = ttk.Treeview(janela_rel, columns=colunas, show="headings")

    for col in colunas:
        tabela.heading(col, text=col)
        tabela.column(col, width=100, anchor="center")

    for aluno in lista:
        tabela.insert("", tk.END, values=(
            aluno[0], aluno[1],
            f"{aluno[2]:.1f}", f"{aluno[3]:.1f}",
            f"{aluno[4]:.2f}", aluno[5]
        ))

    tabela.pack(fill="both", expand=True, padx=10, pady=10)


janela = tk.Tk()
janela.title("Sistema de Notas")
janela.geometry("350x280")
janela.resizable(False, False)

tk.Label(janela, text="─── Cadastro de Aluno ───", font=("Arial", 11, "bold")).pack(pady=(12, 6))

frame = tk.Frame(janela)
frame.pack(padx=20)

campos = [("Nome:", "entry_nome"), ("Matrícula:", "entry_matricula"),
          ("Nota 1:", "entry_n1"), ("Nota 2:", "entry_n2")]

entries = {}
for i, (label, key) in enumerate(campos):
    tk.Label(frame, text=label, anchor="w", width=10).grid(row=i, column=0, pady=3, sticky="w")
    e = tk.Entry(frame, width=22)
    e.grid(row=i, column=1, pady=3)
    entries[key] = e

entry_nome       = entries["entry_nome"]
entry_matricula  = entries["entry_matricula"]
entry_n1         = entries["entry_n1"]
entry_n2         = entries["entry_n2"]

tk.Button(janela, text="Cadastrar",      width=20, command=cadastrar).pack(pady=(10, 3))
tk.Button(janela, text="Ver Relatório",  width=20, command=mostrar_relatorio).pack(pady=3)
tk.Button(janela, text="Sair",           width=20, command=janela.quit).pack(pady=3)

janela.mainloop()
