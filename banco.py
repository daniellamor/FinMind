
import sqlite3
from pathlib import Path

# Local onde nosso banco ficará armazenado
BASE = Path(__file__).resolve().parent
BANCO = BASE / "finmind.db"


def criar_banco():
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS movimentacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao TEXT NOT NULL,
                tipo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                valor_centavos INTEGER NOT NULL,
                data TEXT NOT NULL
            )
        """)


def salvar_movimentacao(descricao, tipo, categoria, valor, data):
    with sqlite3.connect(BANCO) as conexao:
        conexao.execute(
            """
            INSERT INTO movimentacoes
            (descricao, tipo, categoria, valor_centavos, data)
            VALUES (?, ?, ?, ?, ?)
            """,
            (descricao, tipo, categoria, valor, data)
        )


def listar_movimentacoes():
    with sqlite3.connect(BANCO) as conexao:
        registros = conexao.execute(
            """
            SELECT descricao, tipo, categoria,
                   valor_centavos, data
            FROM movimentacoes
            ORDER BY data DESC, id DESC
            """
        ).fetchall()

    return registros

if __name__ == "__main__":
    criar_banco()
    print("Banco de dados FinMind criado com sucesso!")
