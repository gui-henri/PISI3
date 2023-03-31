import streamlit as st
import pandas as pd
from ast import literal_eval
import json
from collections import Counter

filehandle = open(f'streamlit_project/data/filtros/genres.txt', 'r')
genres = json.load(filehandle)
filehandle.close()

filehandle = open(f'streamlit_project/data/filtros/keywords.txt', 'r')
keywords = json.load(filehandle)
filehandle.close()

filehandle = open(f'streamlit_project/data/filtros/production_countries.txt', 'r')
production_countries = json.load(filehandle)
filehandle.close()

filehandle = open(f'streamlit_project/data/filtros/production_companies.txt', 'r')
production_companies = json.load(filehandle)
filehandle.close()

filehandle = open(f'streamlit_project/data/filtros/director.txt', 'r')
director = json.load(filehandle)
filehandle.close()

filehandle = open(f'streamlit_project/data/filtros/cast.txt', 'r')
cast = json.load(filehandle)
filehandle.close()


df = pd.read_csv(f'streamlit_project/data/archive/tmdb_3000_discreto.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval, 'cast': literal_eval, 'director': literal_eval})

tagCompleta = ['index', 'movie_id', 'title', 'genres', 'keywords', 'budget', 'revenue', 'popularity',
         'vote_average', 'vote_count', 'runtime', 'release_date', 'original_language',
         'production_countries', 'production_companies', 'director', 'cast']

tagFiltro = ['genres', 'keywords', 'production_countries', 'production_companies', 'director', 'cast']


radio = st.radio('Escolha uma opção', tagFiltro)

select = st.selectbox('Escolha uma opção', eval(radio))

new_df = df[df[radio].apply(lambda x: select in x)]
new_df.drop(columns=['Unnamed: 0'], inplace=True)

st.write(new_df)




def createdf(data, tag):
    tmp = []
    lista = data[tag].values.tolist()

    for i in lista:
        tmp = tmp + i

    tmp = Counter(tmp)
    dici = {tag: [i for i in tmp], 'count': [i for i in tmp.values()]}

    return pd.DataFrame(dici).sort_values(by='count', ascending=False)

df_genres = createdf(new_df, 'genres')
df_keywords = createdf(new_df, 'keywords')
df_production_countries = createdf(new_df, 'production_countries')
df_production_companies = createdf(new_df, 'production_companies')
df_director = createdf(new_df, 'director')
df_cast = createdf(new_df, 'cast')
 
    
cl1, cl2, cl3 = st.columns(3)
    
with cl1:
    st.write(df_genres)
    st.write(df_keywords)

with cl2:
    st.write(df_production_countries)
    st.write(df_production_companies)
    
with cl3:  
    st.write(df_director)
    st.write(df_cast)
    


