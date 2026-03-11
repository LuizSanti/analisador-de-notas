# 📊 Analisador de Notas

Sistema desktop para cadastro e acompanhamento de notas de alunos, com interface gráfica e persistência em banco de dados local.

---

## 🖥️ Funcionalidades

- Cadastro de alunos com nome, matrícula e duas notas
- Cálculo automático de média e status (Aprovado/Reprovado)
- Relatório com listagem de todos os alunos cadastrados
- Dados persistidos em banco de dados SQLite

---

## 📁 Estrutura do Projeto

```
analisador-de-notas/
├── interface.py   # Interface gráfica (tkinter)
├── alunos.py      # Lógica de negócio (média e status)
├── database.py    # Conexão e operações com o banco de dados
├── alunos.db      # Banco de dados gerado automaticamente (não versionado)
└── .gitignore
```

---

## ▶️ Como executar

**Pré-requisito:** Python 3 instalado.

As bibliotecas utilizadas (`tkinter` e `sqlite3`) já fazem parte da biblioteca padrão do Python — nenhuma instalação adicional é necessária.

```bash
python interface.py
```

O arquivo `alunos.db` será criado automaticamente na primeira execução.

---

## 🛠️ Tecnologias

- Python 3
- Tkinter — interface gráfica
- SQLite3 — banco de dados local

---

## 👥 Autores

Projeto desenvolvido por Luiz Gabriel e Vinicius Nascimento.