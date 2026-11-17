import sqlite3

DATABASE = "gestao_comercial.db"

def conectar():
    return sqlite3.connect(DATABASE)

def criar_tabela_produtos():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            preco REAL NOT NULL CHECK(preco >= 0),
            quantidade INTEGER NOT NULL CHECK(quantidade >= 0),
            descricao TEXT
        )
    """)

    conexao.commit()
    conexao.close()
