import streamlit as st
import pandas as pd
from ast import literal_eval
import json 
import networkx as nx
import matplotlib.pyplot as plt
from gensim.models import Word2Vec


from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from matrix_generation.matriz_de_similaridade import generate_sim


st.write('Recomendação de filmes baseadas na comparação do alvo ou critérios personalisados.')

df = pd.read_csv('streamlit_project/data/archive/tmdb_3000_discreto.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval, 'cast': literal_eval, 'director': literal_eval})

radio = st.radio('Escolha uma opção', ['Recomendação a partir de filmes', 'Recomendação customizada'])

def custom():

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

    cl1, cl2, cl3 = st.columns(3)

    with cl1:
        sel_genre = st.multiselect('Escolha um gênero', genres)
        sel_keyword = st.multiselect('Escolha uma palavra-chave', keywords)
        sel_director = st.multiselect('Escolha um diretor', director)
    with cl2:
        sel_date = st.multiselect('Escolha o ano de lançamento', range(1916, 2017), max_selections=1)
        sel_cast = st.multiselect('Escolha um ator', cast)
    with cl3:
        sel_production_countries = st.multiselect('Escolha um país de produção', production_countries)
        sel_production_companies = st.multiselect('Escolha uma produtora', production_companies)

    p_genres = 1
    p_keyword = 1
    p_director = 1
    p_date = 1
    p_cast = 1
    p_production_countries = 1
    p_production_companies = 1


    if sel_genre == []:
        p_genres = 0

    if sel_keyword == []:
        p_keyword = 0

    if sel_director == []:
        p_director = 0
    
    if sel_date == []:
        p_date = 0

    if sel_cast == []:
        p_cast = 0

    if sel_production_countries == []:
        p_production_countries = 0

    if sel_production_companies == []:
        p_production_companies = 0

    custom = [0, 0, 0, sel_genre, sel_keyword, 0, 0, 0, 0, 0, 0, sel_date, 0, sel_production_countries, sel_production_companies, sel_director, sel_cast]

    pesos = {'index': 0, 'movie_id': 0, 'title': 0, 'genres': p_genres, 'keywords': p_keyword, 'budget': 0, 'revenue': 0, 'popularity': 0,
                 'vote_average': 0, 'vote_count': 0, 'runtime': 0, 'release_date': p_date, 'original_language': 0,
                 'production_countries': p_production_countries, 'production_companies': p_production_companies, 'director': p_director, 'cast': p_cast}

    
        
    call = st.button('Gerar recomendação')
    
    if call:
        st.write(generate_sim(df, pesos, sum(pesos.values()), 'C', custom))
       
def mk_set(df, tag):
    lista = []
    
    for i in df[tag].tolist():
        lista += i
    
    return list(set(lista))

def media(df, tag):
    x = sum(df[tag])
    
    return x/len(df[tag])
    
    
def filmeBased():
    radio = st.radio('Escolha um método de recomendação', ['Baseado em similaridade', 'Baseado em cluster'])
    sel_filmes = []
    if radio == 'Baseado em similaridade':
        sel_filmes = st.multiselect('Escolha um filme', df['title'], max_selections=3)
    else:
        sel_filmes = st.multiselect('Escolha um filme', df['title'], max_selections=1)
    
    if radio == 'Baseado em similaridade':
        sel_df = df[df['title'].isin(sel_filmes)]   
        st.write(sel_df)
        m_genres = mk_set(sel_df, 'genres')
        m_keywords = mk_set(sel_df, 'keywords')
        m_contries = mk_set(sel_df, 'production_countries')
        m_companies = mk_set(sel_df, 'production_companies')
        m_director = mk_set(sel_df, 'director')
        m_cast = mk_set(sel_df, 'cast')
            
        
        pesos = {'index': 0, 'movie_id': 0, 'title': 0, 'genres': 1, 'keywords': 1, 'budget': 0, 'revenue': 0, 'popularity': 0,
                    'vote_average': 0, 'vote_count': 0, 'runtime': 0, 'release_date': 1, 'original_language': 0,
                    'production_countries': 1, 'production_companies': 1, 'director': 1, 'cast': 1}
        
        s_df = df[~df['title'].isin(sel_filmes)]
        st.write(s_df)
        call = st.button('Gerar recomendação')

        if call:
            m_date = media(sel_df, 'release_date')
            frank = [0, 0, 0, m_genres, m_keywords, 0, 0, 0, 0, 0, 0, m_date, 0, m_contries, m_companies, m_director, m_cast]
            st.write(generate_sim(s_df, pesos, sum(pesos.values()), 'C', frank))
    else:

        df_cluster = pd.read_csv('streamlit_project/data/archive/clustered_movies.csv')
        df_cluster = pd.merge(df, df_cluster, how='inner', left_on='title', right_on='Unnamed: 1')
        df_cluster = df_cluster.drop(['index', 'Unnamed: 0', 'Unnamed: 1'], axis=1)
        df_cluster = df_cluster.rename(columns={'0': 'cluster_id'})

        # get the cluster id of the selected movies
        sel_df = df_cluster[df_cluster['title'].isin(sel_filmes)]
        cluster_id = sel_df['cluster_id'].tolist()

        # get the movies of the same cluster
        s_df = df_cluster[df_cluster['cluster_id'].isin(cluster_id)]
        s_df = s_df[~s_df['title'].isin(sel_filmes)]
        s_df = s_df.drop(['cluster_id'], axis=1)

        m_genres = mk_set(sel_df, 'genres')
        m_keywords = mk_set(sel_df, 'keywords')
        m_contries = mk_set(sel_df, 'production_countries')
        m_companies = mk_set(sel_df, 'production_companies')
        m_director = mk_set(sel_df, 'director')
        m_cast = mk_set(sel_df, 'cast')
            
        
        pesos = {'movie_id': 0, 'title': 0, 'genres': 1, 'keywords': 1, 'budget': 0, 'revenue': 0, 'popularity': 0,
                    'vote_average': 0, 'vote_count': 0, 'runtime': 0, 'release_date': 1, 'original_language': 0,
                    'production_countries': 1, 'production_companies': 1, 'director': 1, 'cast': 1}
        
        call = st.button('Gerar recomendação')

        if call:
            m_date = media(sel_df, 'release_date')
            frank = [0, 0, m_genres, m_keywords, 0, 0, 0, 0, 0, 0, m_date, 0, m_contries, m_companies, m_director, m_cast]
            st.write(generate_sim(s_df, pesos, sum(pesos.values()), 'C', frank))



if radio == 'Recomendação a partir de filmes':
    filmeBased()

else:
    custom()
