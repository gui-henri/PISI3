from matplotlib import pyplot as plt
import mpld3
import streamlit as st
import pandas as pd
from ast import literal_eval
import json
from collections import Counter
import networkx as nx 
import streamlit.components.v1 as components
import plotly.express as ply

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from matrix_generation.matriz_de_similaridade import generate_matrix

def plotar_grafo(df, lista_matriz, layout):
        
    cut_value = 0.4
    
    G = nx.Graph()
    for i, node in enumerate(df['title']):
        G.add_node(i, name=f'{node}')
    
    for i, column in enumerate(lista_matriz):
        for j, item in enumerate(column):
            if item != None and item > cut_value and i != j:
                G.add_edge(i, j, weight=item)

    fig, ax = plt.subplots()

    layouts = {
        "Shell": nx.shell_layout(G),
        "Random": nx.random_layout(G),
        "Spiral": nx.spiral_layout(G),
        "Spring": nx.spring_layout(G)
    }
    pos=layouts[layout]

    film_names = df['title']
    node_names = dict(zip(range(len(df['title'])), film_names))
    nx.draw(G, pos=pos, labels=node_names, with_labels=True, edge_color= 'b', font_weight='bold', font_size=16)

    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, label_pos=0.4, font_weight='bold', )
    
    html = mpld3.fig_to_html(fig)
    components.html(html, height=500)



filehandle = open(f'data/filtros/genres.txt', 'r')
genres = json.load(filehandle)
filehandle.close()

filehandle = open(f'data/filtros/keywords.txt', 'r')
keywords = json.load(filehandle)
filehandle.close()

filehandle = open(f'data/filtros/production_countries.txt', 'r')
production_countries = json.load(filehandle)
filehandle.close()

filehandle = open(f'data/filtros/production_companies.txt', 'r')
production_companies = json.load(filehandle)
filehandle.close()

filehandle = open(f'data/filtros/director.txt', 'r')
director = json.load(filehandle)
filehandle.close()

filehandle = open(f'data/filtros/cast.txt', 'r')
cast = json.load(filehandle)
filehandle.close()


df = pd.read_csv(f'data/archive/tmdb_3000_discreto.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval, 'cast': literal_eval, 'director': literal_eval})


tagFiltro = ['genres', 'keywords', 'production_countries', 'production_companies', 'director', 'cast']


radio = st.radio('Escolha uma opção', tagFiltro)

select = st.selectbox('Escolha uma opção', eval(radio))

new_df = df[df[radio].apply(lambda x: select in x)]
new_df.reset_index(drop=True)


# Criar grafos de gêneros, keywords, production_countries e companies, diretores e cast

pg = 0
pk = 0
pc = 0
pco = 0
pdc = 0
pcast = 0


radio = st.radio('Escolha uma opção', tagFiltro, key='1')
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

pesos = {'index': 0, 'movie_id': 0, 'title': 0, 'genres': pg, 'keywords': pk, 'budget': 0, 'revenue': 0, 'popularity': 0,
         'vote_average': 0, 'vote_count': 0, 'runtime': 0, 'release_date': 0, 'original_language': 0,
         'production_countries': pc, 'production_companies': pco, 'director':pdc, 'cast': pcast}

pesos[radio] = 1
possibilities = ["Shell", "Spiral", "Random", "Spring"]

st.write(new_df)

lista_matriz = generate_matrix(new_df.values.tolist(), pesos, 1, "A")


matrix_to_show = pd.DataFrame(lista_matriz, columns=(x := new_df['title']), index=x)



cl1, cl2 = st.columns(2)

with cl1:
    call = st.button('Gerar grafo')
    layout = st.selectbox("Selecionar formato do grafo", possibilities, index=3)
with cl2:
    call_heat = st.button('Gerar heatmap')



if call_heat:
    heatMap = ply.imshow(matrix_to_show, aspect='auto')
    heatMap.update_layout(title='Matriz de similaridade', height= 800)
    st.plotly_chart(heatMap, use_container_width=True)




if call:
        components.html(plotar_grafo(new_df, lista_matriz, layout), height=500)



def createdf(data, tag):
    tmp = []
    lista = data[tag].values.tolist()

    for i in lista:

        tmp = tmp + i

    tmp = Counter(tmp)
    dici = {tag: [i for i in tmp], 'count': [i for i in tmp.values()]}

    return pd.DataFrame(dici).sort_values(by='count', ascending=False)

def create_graph():
    pass

df_genres = createdf(new_df, 'genres')
G = nx.Graph()
for i, node in enumerate(new_df['title'].values.tolist()):
    G.add_node(i, name=f'{node}')

for i, column in enumerate(lista_matriz):
    for j, item in enumerate(column):
        if item != None and item > 0.4 and i != j:
            G.add_edge(i, j, weight=item)

st.write(f'Número de arestas: {G.number_of_edges()}')
st.write(f'Número de nós: {G.number_of_nodes()}')
st.write(f'Média de graus dos nós: {sum(dict(G.degree()).values()) / float(len(G))}')

#st.subheader('Centralidade de grau')
#st.write('Representa a centralidade de grau de cada nó. A centralidade de grau de um nó é calculada dividindo o grau de um nó pelo grau máximo possível.')
#st.write(nx.degree_centrality(G))

st.subheader('Densidade')
st.write('Representa o quão denso é o grafo. O valor é 0 para grafos sem conexões e 1 para um grafo completo.')
st.write(nx.density(G)) 

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
    


