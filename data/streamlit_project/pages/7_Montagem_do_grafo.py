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

st.markdown(
    """

    # Grafo de relacionamento entre os filmes

    O principal diferencial desta página é o uso de grafos para facilitar a visualização da similaridade entre filmes. Iniciaremos explicando passo a passo o processo de montagem do grafo e depois forneceremos as ferramentas de visualização que surgiram a partir dele.

    ## Criação do grafo

    A primeira etapa na concepção do grafo foi decidir de que forma ele seria representado. Optamos por representar cada filme como um vértice, e para cada atributo em comum entre dois filmes, haverá uma conexão. Alguns atributos são compostos por listas, então a medida para a conexão será um valor entre 0 e 1, sendo 0 listas sem nenhum item em comum e 1 listas com os mesmos valores. Para filmes com múltiplas conexões, adicionaremos pesos as arestas.

    Após estruturarmos como seria o grafo, nossa primeira ação foi a de pré-processar os pesos das arestas, e por consequência, os atributos das arestas. Graças a isso, o ato de remontar o grafo inteiro caso algum erro ocorra se torna menos custoso.

    Com os pesos processados, utilizamos a biblioteca NetworkX para montar o grafo. Ela é compatível com as bibliotecas de machine learning que usaremos futuramente e também vem com dezenas de funções built-in que podemos utilizar para analisar o grafo.

    ## Ferramentas para visualização do grafo

    Podemos utilizar os dados de nosso dataset diretamente para obter uma visualização do grafo em tempo real. Podemos adicionar os filmes que desejamos, filtrar por atributo e também filtrar por peso da conexão.

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

    gen_b = st.checkbox("Gêneros")
    pop_b = st.checkbox("Popularidade")
    pdc_b = st.checkbox("Produtoras")
    o_b = st.checkbox("Orçamento")
    pc_b = st.checkbox("Palavras-chave")

    gen = 0
    if gen_b == True:
        gen = 1

    pop = 0
    if pop_b == True:
        pop = 1
    
    pdc = 0
    if pdc_b == True:
        pdc = 1
    
    o = 0
    if o_b == True:
        o = 1

    pc = 0
    if pc_b == True:
        pc = 1

    pesos = {'budget': o, 'genres': gen, 'id': 0, 'keywords': pc, 'original_language': 0, 'original_title': 0, 'overview': 0,
        'popularity': pop, 'production_companies': pdc, 'production_countries': 0, 'release_date': 0, 'revenue': 0,
        'runtime': 0, 'title': 0, 'vote_average': 0, 'vote_count': 0}

    lista_matriz = generate_matrix(movies, tags, pesos)
    
    G = nx.Graph()
    for i, node in enumerate([i[5] for i in movies]):
        G.add_node(i, name=f'{node}')

    #newDf = pd.DataFrame(data= lista_matriz, columns=[i for i in movies], index=[i for i in movies])
    #print(newDf)
        
    for i, column in enumerate(lista_matriz):
        for j, item in enumerate(column):
            if item != None and item >= cut_value and i != j:
                G.add_edge(i, j, weight=item)

    fig, ax = plt.subplots()

    layouts = {
        "Shell": nx.shell_layout(G),
        "Random": nx.random_layout(G),
        "Spiral": nx.spiral_layout(G),
        "Spring": nx.spring_layout(G)
    }
    pos=layouts[layout]


    node_names = dict(zip(range(len(selected_movies)), [i[13] for i in movies]))
    nx.draw(G, pos=pos, labels=node_names, with_labels=True, edge_color= 'b', font_weight='bold', font_size=16)

    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, label_pos=0.4, font_weight='bold', )

    fig_html = mpld3.fig_to_html(fig)

    components.html(fig_html, height=500)

    st.write(f"Similaridade máxima: {gen + pop + pdc + o + pc}")

    st.write(pd.DataFrame(lista_matriz))