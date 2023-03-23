import streamlit as st

# crescimento do lucro dos filmes no tempo
# analisar os outliners
# corrigir pela inflação
# correlação entre faturam
# ento e orçamento e tentar achar um valor ótimo/ mais eficiente
# tentar prever o crescimento da industria
# crescimento do orçamento no tempo
# crescimento do faturamento no tempo

st.title("Painel de Administração do MoviePicker")
st.write("O Painel de Administração do MoviePicker é uma ferramenta criada para auxiliar na análise dos dados do sistema e fornecer insights que podem ser usados para tomada de decisão.")
st.markdown(
    """
    **👈 Selecione uma guia** para ver cada ferramenta ou análise.
    #### Páginas
    - Introdução: Nossa página principal. Apertar nela o trará de volta para cá!
    - Pré-processamento: Aqui estão documentadas as etapas necessárias para tratar o dataset.
    - Dataset: Descrição detalhada das mais diversas informações a respeito do dataset e suas variáveis.
    - Visualizar filme: Busque as principais informações a respeito de um filme.
    - Comparador de filmes: Compare diretamente as principais métricas de vários filmes.
    - Visão global: Observe a relaçao de lucro e investimento de todos os filmes.
    - Mais em breve :D

    #### Mais informações?

    - Visite nosso [Github](https://github.com/gui-henri/PISI3)
    - Visualize o [Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

    """
)
st.sidebar.success("Selecione acima a página que gostaria de visitar")


# Avatar, Indiana Jones

# Orçamento, Faturamento, Popularidade, Tempo de duração, Número de votos, Nota
#df.set_index('original_title', inplace=True)

