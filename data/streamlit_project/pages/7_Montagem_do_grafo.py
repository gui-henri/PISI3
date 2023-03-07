import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import mpld3
import networkx as nx
from ast import literal_eval

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from matrix_generation.matriz_de_similaridade import generate_matrix
    
tags = ['budget', 'genres', 'id', 'keywords', 'original_language', 'original_title', 'overview',
        'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue',
        'runtime', 'title', 'vote_average', 'vote_count']

pesos = {'budget': 0, 'genres': 1, 'id': 0, 'keywords': 0, 'original_language': 0, 'original_title': 0, 'overview': 0,
        'popularity': 0, 'production_companies': 0, 'production_countries': 0, 'release_date': 0, 'revenue': 0,
        'runtime': 0, 'title': 0, 'vote_average': 0, 'vote_count': 0}


st.markdown(
    """
    # Grafo de relacionamento entre os filmes

    O principal diferencial desta página é o uso de grafos para facilitar a visualização da similaridade entre filmes. Iniciaremos explicando passo a passo o processo de montagem do grafo e depois forneceremos as ferramentas de visualização que surgiram a partir dele.

    ## Criação do grafo

    A primeira etapa na concepção do grafo foi decidir de que forma ele seria representado. Optamos por representar cada filme como um vértice, e para cada atributo em comum entre dois filmes, haverá uma conexão. Alguns atributos são compostos por listas, então a medida para a conexão será um valor entre 0 e 1, sendo 0 listas sem nenhum item em comum e 1 listas com os mesmos valores. 

    """
)
df = pd.read_csv('data/archive/tmdb_3000_movies.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval,})


selected_movies = st.multiselect("Selecione filmes para comparar: ", df['title'])
movies = df[df['title'].isin(selected_movies)].values.tolist()

if len(movies) > 1:

    c1, c2 = st.columns(2)
    cut_value = 0.0
    layout = ""

    with c1:
        cut_value = st.slider("Valor mínimo para conexão: ", 0.0, 1.0, step=0.01)

    with c2:
        possibilities = ["Shell", "Spiral", "Random", "Spring"]
        layout = st.selectbox("Selecionar formato do grafo", possibilities)

    lista_matriz = generate_matrix(movies, tags, pesos)
    graph_data = pd.DataFrame(lista_matriz)

    G = nx.Graph()
    for i, node in enumerate(graph_data.index.to_list()):
        G.add_node(node, name=f'{selected_movies[i]}')

    i_corrector = 0
    for i, column in enumerate(graph_data.columns):
        i_corrector = 0
        value_list = graph_data[column].values.tolist()
        for j, item in enumerate(value_list):
            i_corrector += 1
            if item != None and item >= cut_value:
                G.add_edge(j, i + i_corrector, weight=item)

    fig, ax = plt.subplots()

    layouts = {
        "Shell": nx.shell_layout(G),
        "Random": nx.random_layout(G),
        "Spiral": nx.spiral_layout(G),
        "Spring": nx.spring_layout(G)
    }
    pos=layouts[layout]


    node_names = dict(zip(range(len(selected_movies)), selected_movies))
    nx.draw(G, pos=pos, labels=node_names, with_labels=True, edge_color= 'b', font_weight='bold', font_size=16)

    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, label_pos=0.4, font_weight='bold', )

    fig_html = mpld3.fig_to_html(fig)

    components.html(fig_html, height=500)

    st.write(pd.DataFrame(lista_matriz))