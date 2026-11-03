# 💜 FinMind — Gestão Financeira Inteligente

**Uma aplicação web para organizar finanças pessoais, acompanhar receitas e despesas e facilitar decisões financeiras.**

O FinMind é um projeto pessoal de desenvolvimento de software criado com o objetivo de unir **Python, banco de dados, automação e análise de dados** em uma solução prática e acessível.

O projeto está em desenvolvimento e será aprimorado gradualmente, com foco em usabilidade, organização financeira e novas funcionalidades inteligentes.

---

## 🚀 Funcionalidades implementadas

- ✅ Interface web interativa desenvolvida com Streamlit.
- ✅ Cadastro de receitas e despesas.
- ✅ Classificação das movimentações por categorias.
- ✅ Armazenamento de informações em banco de dados SQLite.
- ✅ Consulta e visualização das movimentações cadastradas.
- ✅ Registro da descrição, valor, tipo e data de cada movimentação.

## 🛠️ Tecnologias utilizadas

- **Python:** linguagem principal da aplicação.
- **Streamlit:** desenvolvimento da interface web.
- **SQLite:** armazenamento das movimentações financeiras.
- **SQL:** criação, inserção e consulta de dados.
- **Git e GitHub:** versionamento e documentação do projeto.

## 📁 Estrutura do projeto

- `app.py` — interface e funcionalidades visuais.
- `banco.py` — criação do banco e operações com os dados.
- `.gitignore` — configuração de arquivos que não devem ser publicados.
- `README.md` — documentação do projeto.
- `finmind.db` — banco de dados local, não incluído no GitHub.

## 💻 Como executar

**Pré-requisito:** Python instalado no computador.

1. Clone o repositório: `git clone https://github.com/daniellamor/FinMind.git`
2. Acesse a pasta: `cd FinMind`
3. Instale o Streamlit: `py -m pip install streamlit`
4. Inicialize o banco de dados: `py banco.py`
5. Execute a aplicação: `py -m streamlit run app.py`
6. Abra o endereço local informado no terminal, normalmente `http://localhost:8501`.

*Os comandos apresentados são destinados ao Windows.*

## 📈 Próximas funcionalidades

- [ ] Dashboard financeiro totalmente integrado aos dados reais.
- [ ] Gráficos interativos e filtros por período.
- [ ] Controle de cartões de crédito e parcelamentos.
- [ ] Metas de economia e planejamento financeiro.
- [ ] Alertas automáticos sobre gastos.
- [ ] Análises de padrões de consumo.
- [ ] Recursos de inteligência artificial para recomendações financeiras.
- [ ] Autenticação de usuários e publicação segura na internet.

## 🔒 Privacidade

O banco de dados utilizado durante o desenvolvimento é armazenado localmente e não faz parte do repositório.

A versão atual é experimental e deve ser testada com informações fictícias. Recursos adicionais de segurança serão necessários antes de utilizar dados financeiros sensíveis em uma aplicação pública.

## 👩🏻‍💻 Desenvolvimento

Projeto pessoal desenvolvido por **Daniella Morais Justino**, formada em Engenharia da Computação, com interesse em desenvolvimento de software, automação e Ciência de Dados.

O FinMind também faz parte do meu processo de aprimoramento técnico e construção de portfólio profissional.

**GitHub:** [daniellamor](https://github.com/daniellamor)

---

**FinMind — Transformando dados financeiros em decisões mais inteligentes.** 💜