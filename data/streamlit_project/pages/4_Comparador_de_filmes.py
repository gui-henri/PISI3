import pandas as pd
import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns

df = pd.read_csv('../archive/TMDB_5000_movies.csv')
df.set_index('original_title', inplace=True)

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

    if len(films) == 0:
        return "Nada para ver aqui"

    partial_data = [df.loc[film] for film in films]
    lista = [[f["title"], f["budget"], f["revenue"]] for f in partial_data]
    to_stream = pd.DataFrame(lista, columns=("Títulos", "Orçamento", "Faturamento"))    
    
    plt.rcParams.update({"font.size": 14, "font.weight": "bold"})
    fig, ax = plt.subplots(figsize=(12, 8),)
    sns.set_style("whitegrid")
    to_stream.plot.barh(x="Títulos", figsize=(12, 8), width=0.9, ax=ax)
    plt.title("Orçamento x Faturamento", fontsize=24, fontweight="bold")
    plt.legend(loc="lower right")
    for patch in ax.patches:
        w, h = patch.get_width(), patch.get_height()
        y = patch.get_y()
        ax.text(w + -0.1, h / 2 + y, f"{w:.3f}", va="center")

    st.pyplot(fig)


def execute_comparason(comparason, movies):
    comparason(movies)

lista = {
    "Orçamento x Faturamento": orc_x_fat,
    "Popularidade": popularity,
    "Tempo de duração": duration,
    "Quantidade de votos": votes,
    "Nota IMDB": note
}

selected_movies = st.multiselect("Selecione filmes para comparar: ", df['title'])
chosen_comparason = st.selectbox("Selecione o parâmetro", ["Orçamento x Faturamento", "Popularidade", "Tempo de duração", "Quantidade de votos", "Nota IMDB"])

execute_comparason(lista[chosen_comparason], selected_movies)