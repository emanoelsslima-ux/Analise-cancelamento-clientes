import streamlit as st
import pandas as pd
import plotly.express as px

# =========================
# Configuração da página
# =========================

st.set_page_config(
    page_title="Análise de Cancelamento de Clientes",
    page_icon="📉",
    layout="wide"
)

# =========================
# Carregar dados
# =========================

tabela = pd.read_csv("data/cancelamentos.csv")

# Remover coluna desnecessária
tabela = tabela.drop(columns="CustomerID")

# Remover valores nulos
tabela = tabela.dropna()

# =========================
# Título
# =========================

st.title("📉 Análise de Cancelamento de Clientes")

st.markdown("""
Dashboard desenvolvido para analisar os principais fatores que influenciam o cancelamento de clientes.
""")

st.divider()

# =========================
# Métricas principais
# =========================

total_clientes = len(tabela)

clientes_cancelaram = tabela["cancelou"].value_counts()[1]

taxa_cancelamento = (
    tabela["cancelou"]
    .value_counts(normalize=True)[1] * 100
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total de clientes",
    f"{total_clientes}"
)

col2.metric(
    "Clientes cancelados",
    f"{clientes_cancelaram}"
)

col3.metric(
    "Taxa de cancelamento",
    f"{taxa_cancelamento:.1f}%"
)

st.divider()

# =========================
# Visualizações
# =========================

st.subheader("📊 Análise visual dos dados")

colunas = tabela.columns

coluna_escolhida = st.selectbox(
    "Selecione uma coluna para análise",
    colunas
)

grafico = px.histogram(
    tabela,
    x=coluna_escolhida,
    color="cancelou",
    barmode="group",
    text_auto=True
)

st.plotly_chart(
    grafico,
    use_container_width=True
)

st.divider()

# =========================
# Insights encontrados
# =========================

st.subheader("🔍 Principais insights")

st.markdown("""
### 📌 Contrato mensal possui maior taxa de cancelamento

Clientes com contrato do tipo **Monthly** apresentaram maior taxa de churn.

**Solução sugerida:**  
Oferecer benefícios para contratos anuais.
""")

st.markdown("""
### 📌 Muitas ligações para o call center aumentam o cancelamento

Clientes com muitas ligações ao suporte possuem maior chance de cancelar.

**Solução sugerida:**  
Criar alertas internos para clientes com mais de 3 ligações.
""")

st.markdown("""
### 📌 Clientes com atraso tendem a cancelar

Clientes com muitos dias de atraso possuem alta probabilidade de churn.

**Solução sugerida:**  
Implementar ações preventivas antes de 15 dias de atraso.
""")

st.divider()

# =========================
# Simulação de filtros
# =========================

st.subheader("🧪 Simulação de redução de cancelamento")

tabela_filtrada = tabela.copy()

# Filtro contrato
tabela_filtrada = tabela_filtrada[
    tabela_filtrada["duracao_contrato"] != "Monthly"
]

# Filtro call center
tabela_filtrada = tabela_filtrada[
    tabela_filtrada["ligacoes_callcenter"] <= 4
]

# Filtro atraso
tabela_filtrada = tabela_filtrada[
    tabela_filtrada["dias_atraso"] <= 20
]

nova_taxa = (
    tabela_filtrada["cancelou"]
    .value_counts(normalize=True)[1] * 100
)

st.success(
    f"Nova taxa de cancelamento após melhorias: {nova_taxa:.1f}%"
)

st.divider()

# =========================
# Sobre o projeto
# =========================

st.subheader("📌 Sobre o projeto")

st.markdown("""
Projeto desenvolvido com:

- Python
- Pandas
- Plotly
- Streamlit
- Análise de Dados

Objetivo:
Identificar padrões de comportamento que levam clientes ao cancelamento e gerar insights estratégicos para retenção.
""")