import streamlit as st
import pandas as pd
import ast

# crescimento do lucro dos filmes no tempo
# analisar os outliners
# corrigir pela inflação
# correlação entre faturamento e orçamento e tentar achar um valor ótimo/ mais eficiente
# tentar prever o crescimento da industria
# crescimento do orçamento no tempo
# crescimento do faturamento no tempo

st.title("TMDB Dataset")
st.write("A tabela a seguir é uma pequena visualização, mostrando o formato dos dados extraidos.")

df = pd.read_csv('../archive/TMDB_5000_movies.csv')

st.write(df.head())

st.title("Visualização de filmes")
filme = st.selectbox(
    "Selecione um filme: ",
    df['original_title']
)
if filme:
    df.set_index('original_title', inplace=True)
    filme_info = df.loc[filme]

    st.header(filme_info['title'])
    st.subheader(filme_info['tagline'])
    st.write(filme_info['overview'])
    generos_list = [x["name"] for x in ast.literal_eval(filme_info["genres"])]
    generos_formated_to_print = [f"{x}, " for x in generos_list]
    generos_formated_to_print[-1] = generos_formated_to_print[-1].replace(", ", "")
    st.header("Gêneros:")
    st.write(*generos_formated_to_print)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.subheader("Orçamento")
        st.markdown(f"{filme_info['budget']:,}")
    with c2:
        st.subheader("Faturamento")
        st.markdown(f"{filme_info['revenue']:,}")
    with c3:
        st.subheader("Data de lançamento")
        st.write(filme_info['release_date'])
    
    c4, c5, c6, c7 = st.columns(4)

    with c4:
        st.write(f"Tempo de duração: {int(filme_info['runtime'])} minutos")
    with c5:
        st.write(f"Popularidade: {filme_info['popularity']}")
    with c6:
        st.write(f"Nota no IMDB: {filme_info['vote_average']}")
    with c7:
        st.write(f"Número de votos: {filme_info['vote_count']}")
else:
    st.write("Por favor, selecione um filme")