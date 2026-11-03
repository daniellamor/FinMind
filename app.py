
import streamlit as st

from decimal import Decimal
from banco import criar_banco, salvar_movimentacao, listar_movimentacoes
# Configuração da página
st.set_page_config(
    page_title="FinMind",
    page_icon="💜",
    layout="wide"
)

# Título do aplicativo
st.title("💜 FinMind")
st.caption("Inteligência para o seu dinheiro.")

# Dados fictícios iniciais
transacoes = [
    {"Descrição": "Salário", "Tipo": "Entrada", "Valor": 2500.00},
    {"Descrição": "Mercado", "Tipo": "Saída", "Valor": 350.00},
    {"Descrição": "Transporte", "Tipo": "Saída", "Valor": 150.00}
]

# Cálculo do saldo
entradas = sum(
    t["Valor"] for t in transacoes
    if t["Tipo"] == "Entrada"
)

saidas = sum(
    t["Valor"] for t in transacoes
    if t["Tipo"] == "Saída"
)

saldo = entradas - saidas

def moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# Indicadores financeiros
col1, col2, col3 = st.columns(3)

col1.metric("Entradas", moeda(entradas))
col2.metric("Saídas", moeda(saidas))
col3.metric("Saldo disponível", moeda(saldo))

# Histórico
st.subheader("📋 Movimentações financeiras")
st.dataframe(transacoes, use_container_width=True, hide_index=True)

st.info("Esta primeira versão utiliza apenas dados fictícios.")


# Preparar o banco de dados
criar_banco()

st.divider()
st.subheader("💰 Nova movimentação")

with st.form("form_movimentacao", clear_on_submit=True):

    descricao = st.text_input("Descrição")

    tipo = st.selectbox(
        "Tipo",
        ["Despesa", "Receita"]
    )

    categoria = st.selectbox(
        "Categoria",
        [
            "Alimentação",
            "Transporte",
            "Compras",
            "Moradia",
            "Saúde",
            "Salário",
            "Outros"
        ]
    )

    valor = st.number_input(
        "Valor (R$)",
        min_value=0.0,
        step=0.01,
        format="%.2f"
    )

    data = st.date_input("Data")

    salvar = st.form_submit_button(
        "💾 Salvar movimentação"
    )

if salvar:
    if not descricao.strip() or valor <= 0:
        st.error("Preencha a descrição e um valor maior que zero.")
    else:
        centavos = int(Decimal(str(valor)) * 100)

        salvar_movimentacao(
            descricao.strip(),
            tipo,
            categoria,
            centavos,
            data.isoformat()
        )

        st.success("Movimentação salva com sucesso!")

st.subheader("📋 Movimentações cadastradas")

registros = listar_movimentacoes()

if registros:
    dados = []

    for desc, tipo, cat, centavos, data in registros:
        dados.append({
            "Descrição": desc,
            "Tipo": tipo,
            "Categoria": cat,
            "Valor (R$)": f"{centavos / 100:.2f}",
            "Data": data
        })

    st.dataframe(dados, hide_index=True)
else:
    st.info("Nenhuma movimentação cadastrada ainda.")
