import streamlit as st
import pandas as pd
import ast

df = pd.read_csv('data/archive/all/tmdb_5000_movies.csv')

st.title("Pré-Processamento")

st.write("Nesta seção, estão descritas todas as etapas realizadas na fase de pré-processamento dos dados. Todos os modelos e análises realizados nas outras páginas passaram pelos processos descritos.")

st.markdown("#### Gêneros de filmes")

st.write("A coluna de gêneros é populada por uma série de objetos JSON. Para facilitar as analises, extrairemos apenas o nome de cada uma e guardaremos numa lista.")
st.write(
    """
    ```
    def json_to_list(item):
        item_list = [x["name"] for x in ast.literal_eval(item)]
        return item_list

    df['genres'] = df['genres'].apply(json_to_list)
    df["genres"].head()
    ```
    """
)

def json_to_list(item):
    item_list = [x["name"] for x in ast.literal_eval(item)]
    return item_list

df["genres"] = df["genres"].apply(json_to_list)
st.write(df["genres"].head())
st.write("Formatar os gêneros em lista facilita a manipulação dos dados com o python, já que este não tem suporte nativo ao JSON como o JavaScript.")

st.markdown("#### Palavras-chave do enredo")
st.write("De forma similar aos gêneros de um filme, várias outras colunas estão representadas no formato JSON. Utilizaremos a mesma função que usamos para converter os gêneros para uma lista, mas agora nas palavras-chave, na lista de empresas que produziram o filme, nos países onde o filme foi produzido e nas línguas faladas.")
st.markdown(
    """
    ```
    df['keywords'] = df['keywords'].apply(json_to_list)
    df['production_companies'] = df['production_companies'].apply(json_to_list)
    df['production_countries'] = df['production_countries'].apply(json_to_list)
    df['spoken_languages'] = df['spoken_languages'].apply(json_to_list)
    df[["keywords", "production_companies", "production_countries", "spoken_languages"]].head()
    ```
    """
)
df['keywords'] = df['keywords'].apply(json_to_list)
df['production_companies'] = df['production_companies'].apply(json_to_list)
df['production_countries'] = df['production_countries'].apply(json_to_list)
df['spoken_languages'] = df['spoken_languages'].apply(json_to_list)
st.write(df[["keywords", "production_companies", "production_countries", "spoken_languages"]].head())

st.markdown("#### Adição da coluna dos atores")
st.write("As colunas com informações a respeito dos atores e da produção está em um arquivo separado. Para facilitar o uso, combinaremos os dois dataframes.")


st.markdown(
    """
    ```
    dfc = pd.read_csv('data/archive/tmdb_5000_credits.csv')

    df["cast"] = dfc["cast"]
    df["crew"] = dfc["crew"]
    df.head()
    ```
    """
)

dfc = pd.read_csv('data/archive/tmdb_5000_credits.csv')

df["cast"] = dfc["cast"]
df["crew"] = dfc["crew"]
st.write(df.head())
st.write("Ao contrário de outras colunas, os atores e a produção acabam se favorecendo por permanecerem no formato JSON, pois cada item contém informações relevantes que serão de mais fácil manipulação caso estejam no formato de dicionário.")
