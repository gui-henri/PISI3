import streamlit as st
import pandas as pd
import ast

import streamlit as st
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

# crescimento do lucro dos filmes no tempo
# analisar os outliners
# corrigir pela inflação
# correlação entre faturam
# ento e orçamento e tentar achar um valor ótimo/ mais eficiente
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

# Avatar, Indiana Jones

# Orçamento, Faturamento, Popularidade, Tempo de duração, Número de votos, Nota
#df.set_index('original_title', inplace=True)

st.title("Comparar filmes")

def orc_x_fat(films):
    partial_data = [df.loc[film] for film in films]
    data_films = [x[["budget", "revenue"]] for x in partial_data]
    st.bar_chart(data_films)

def popularity(films):
    partial_data = [df.loc[film] for film in films]
    data_films = [x[["popularity"]] for x in partial_data]
    st.bar_chart(data_films)

def duration(films):
    partial_data = [df.loc[film] for film in films]
    data_films = [x[["runtime"]] for x in partial_data]
    st.bar_chart(data_films)

def votes(films):
    partial_data = [df.loc[film] for film in films]
    data_films = [x[["vote_count"]] for x in partial_data]
    st.bar_chart(data_films)

def note(films):
    partial_data = [df.loc[film] for film in films]
    data_films = [x[["vote_average"]] for x in partial_data]
    st.bar_chart(data_films)
    
def orc_x_fat(films):

    partial_data = [df.loc[film] for film in films]
    lista = [[f["title"], f["budget"], f["revenue"]] for f in partial_data]
    to_stream = pd.DataFrame(lista, columns=("title", "budget", "revenue"))    
    
    plt.rcParams.update({"font.size": 14, "font.weight": "bold"})
    fig, ax = plt.subplots(figsize=(12, 8),)
    sns.set_style("whitegrid")
    to_stream.plot.barh(x="title", figsize=(12, 8), width=0.9, ax=ax)
    plt.title("Orçamento x Faturamento", fontsize=24, fontweight="bold")
    plt.legend(loc="lower right")
    for patch in ax.patches:
        w, h = patch.get_width(), patch.get_height()
        y = patch.get_y()
        ax.text(w + -0.1, h / 2 + y, f"{w:.3f}", va="center")

    st.pyplot(fig)


def execute_comparason(comparason):
    comparason(selected_movies)

lista = {
    "Orçamento x Faturamento": orc_x_fat,
    "Popularidade": popularity,
    "Tempo de duração": duration,
    "Quantidade de votos": votes,
    "Nota IMDB": note
}

selected_movies = st.multiselect("Selecione filmes para comparar: ", df['title'])
chosen_comparason = st.selectbox("Selecione o parâmetro", ["Orçamento x Faturamento", "Popularidade", "Tempo de duração", "Quantidade de votos", "Nota IMDB"])

execute_comparason(lista[chosen_comparason])