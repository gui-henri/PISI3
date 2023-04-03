import itertools
import pandas as pd
from sklearn.cluster import SpectralClustering
import streamlit as st
import networkx as nx
from networkx import Graph
from ast import literal_eval
from node2vec import Node2Vec as n2v

def get_graph() -> Graph:
    G = nx.read_gpickle(f'grafo_generos.pickle')
    return G

df = pd.read_csv(f'streamlit_project/data/archive/tmdb_3000_discreto.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval, 'cast': literal_eval, 'director': literal_eval})
G = get_graph()
nodes_and_index = G.nodes.data('name')

config_manu = st.checkbox('Configurar parâmetros manualmente?', False)

cut_value = 0.0
WINDOW = 1
MIN_COUNT = 1
BATCH_WORDS = 4
DIMENSIONS = 56

if config_manu:
    c3, c4, c5, c6, c7 = st.columns(5)
    with c3: cut_value = st.slider("Valor mínimo para conexão: ", 0.01, 1.0, step=0.01)
    with c4: WINDOW = st.slider("Janela (distância máxima entre entre nós): ", 1, 25, step=1)
    with c5: MIN_COUNT = st.slider("Valor mínimo (ignora nós com frequência total menor que esta): ", 1, 25, step=1)
    with c6: BATCH_WORDS = st.slider("Tamanho do lote para processamento paralelo: ", 1, 25, step=1)
    with c7: DIMENSIONS = st.slider("Dimensões (número de dimensões usadas para representar cada nó): ", 2, 256, step=8)

@st.cache_resource
def execute_n2v(_G):
    g_emb = n2v(G, dimensions=DIMENSIONS, seed=128, weight_key='weight', walk_length=80, num_walks=10, workers=3, temp_folder='temp_folder/')
    mdl = g_emb.fit(
        vector_size=DIMENSIONS,
        window=WINDOW,
        min_count=MIN_COUNT,
        batch_words=BATCH_WORDS,
    )
    return mdl

mdl = execute_n2v(G)

emb_df = (
    pd.DataFrame(
        [mdl.wv.get_vector(str(n)) for n in G.nodes()],
        index = nodes_and_index
    )
)

st.markdown(
    """

    # Recomendação de filmes

    Nesta página, temos como obter recomendações de filmes com base em um certo critério. Basta selecionar um filme para procurar por uma recomendação, e se quiser, modificar o método de busca.

    """
)

base_film = st.selectbox('Selecione o filme base: ', df['title'])

rec_forms = ['Similaridade de Cosseno', 'Clusters', 'Vizinho mais próximo']
rec_form = ''

st.subheader('Forma de recomendação')
rec_form = st.selectbox('Selecione a forma de recomendação: ', rec_forms)

if rec_form == 'Similaridade de Cosseno':

    base_film_index = ""
    for node in nodes_and_index:
        if base_film == node[1]:
            base_film_index = node[0]
    similars = mdl.wv.most_similar(str(base_film_index), topn=10)
    similars_list = [int(item[0]) for item in similars]
    df_closest = emb_df.loc[similars_list]

    st.write(df_closest)

if rec_form == 'Vizinhos mais próximos':
    pass