import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import mpld3
import networkx as nx


from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from matrix_generation.matriz_de_similaridade import generate_matrix
    
tags = ['budget', 'genres', 'id', 'keywords', 'original_language', 'original_title', 'overview',
        'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue',
        'runtime', 'title', 'vote_average', 'vote_count']

pesos = {'budget': 0, 'genres': 1, 'id': 0, 'keywords': 1, 'original_language': 0, 'original_title': 0, 'overview': 0,
        'popularity': 0, 'production_companies': 0, 'production_countries': 0, 'release_date': 0, 'revenue': 0,
        'runtime': 0, 'title': 0, 'vote_average': 0, 'vote_count': 0}


st.markdown(
    """
    # Criação do grafo

    Introduzir e falar que finalmente irão montar o grafo.

    """
)
df = pd.read_csv('data/archive/tmdb_3000_movies.csv')

selected_movies = st.multiselect("Selecione filmes para comparar: ", df['title'])
movies = df[df['title'].isin(selected_movies)].values.tolist()

if len(movies) > 1:
    lista_matriz = generate_matrix(movies, tags, pesos)
    st.write(pd.DataFrame(lista_matriz))
    graph_data = pd.DataFrame(lista_matriz)

    G = nx.Graph()

    G.add_nodes_from(graph_data.index.to_list())

    for i, column in enumerate(graph_data.columns):
        value_list = graph_data[column].values.tolist()
        i_corrector = 0
        for j, item in enumerate(value_list):
            i_corrector += 1
            if item == item:        # Checa se o valor não é NaN
                G.add_edge(j, i + i_corrector, weight=item)
            else: break             # Caso seja NaN, quer dizer que chegou ao fim dos valores válidos e podemos pular para a próxima

    fig, ax = plt.subplots()

    pos=nx.shell_layout(G)
    node_names = dict(zip(range(len(selected_movies)), selected_movies))
    nx.draw(G, pos=pos, labels=node_names, with_labels=True, font_weight='bold', font_size=16)

    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, label_pos=0.4)

    fig_html = mpld3.fig_to_html(fig)

    components.html(fig_html, height=800)
