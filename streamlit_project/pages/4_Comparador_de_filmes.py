import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('data/archive/tmdb_5000_movies.csv')
df.set_index('original_title', inplace=True)

st.title("Comparar filmes")

def popularity(films):
    if len(films) == 0:
        return "Nada para ver aqui"

    partial_data = [df.loc[film] for film in films]
    data_films = [x[["popularity"]] for x in partial_data]
    st.plotly_chart(px.bar(data_films, x="popularity", labels={"popularity":"Nota", "index": "Titulo"}))

def duration(films):
    if len(films) == 0:
        return "Nada para ver aqui"

    partial_data = [df.loc[film] for film in films]
    data_films = [x[["runtime"]] for x in partial_data]
    st.plotly_chart(px.bar(data_films, x="runtime", labels={"runtime":"Duração minutos", "index": "Titulo"}))

def votes(films):
    if len(films) == 0:
        return "Nada para ver aqui"

    partial_data = [df.loc[film] for film in films]
    data_films = [x[["vote_count"]] for x in partial_data]
    st.plotly_chart(px.bar(data_films, x="vote_count", labels={"vote_count":"Votos", "index": "Titulo"}))

def note(films):
    if len(films) == 0:
        return "Nada para ver aqui"

    partial_data = [df.loc[film] for film in films]
    data_films = [x[["vote_average"]] for x in partial_data]
    st.plotly_chart(px.bar(data_films, x="vote_average", labels={"vote_average":"Nota", "index": "Titulo"}))
    
def orc_x_fat(films):

    if len(films) == 0:
        return "Nada para ver aqui"

    partial_data = [df.loc[film] for film in films]
    lista = [[f["title"], f["budget"], f["revenue"]] for f in partial_data]
    to_stream = pd.DataFrame(lista, columns=("Títulos", "Orçamento", "Faturamento"))    
    st.plotly_chart(px.bar(data_frame=to_stream, x=["Orçamento", "Faturamento"], y="Títulos", barmode='group', labels={"value":"US$"}))

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