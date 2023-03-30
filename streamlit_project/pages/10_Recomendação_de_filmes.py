import itertools
import pandas as pd
from sklearn.cluster import SpectralClustering
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import mpld3
import networkx as nx
from networkx.algorithms import community
from ast import literal_eval
from node2vec import Node2Vec as n2v
from sklearn.decomposition import PCA
from sklearn.metrics import pairwise_distances
import numpy as np
import plotly.express as ply
import plotly.graph_objects as go

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from matrix_generation.matriz_de_similaridade import generate_matrix

st.markdown(
    """

    # Recomendação de filmes

    Nesta página, temos como obter recomendações de filmes com base em um certo critério. Basta selecionar um filme para procurar por uma recomendação, e se quiser, modificar o método de busca.

    """
)

rec_forms = ['node2vec', 'Vizinhos mais próximos']
rec_form = ''

st.subheader('Forma de recomendação')
rec_form = st.selectbox('Selecione a forma de recomendação: ', rec_forms)

cut_value = 0.0
WINDOW = 1
MIN_COUNT = 1
BATCH_WORDS = 4
DIMENSIONS = 16

st.subheader('Parâmetros extras: ')
if rec_form == 'node2vec':
    c3, c4, c5, c6, c7 = st.columns(5)
    with c3: cut_value = st.slider("Valor mínimo para conexão: ", 0.01, 1.0, step=0.01)
    with c4: WINDOW = st.slider("Janela (distância máxima entre entre nós): ", 1, 25, step=1)
    with c5: MIN_COUNT = st.slider("Valor mínimo (ignora nós com frequência total menor que esta): ", 1, 25, step=1)
    with c6: BATCH_WORDS = st.slider("Tamanho do lote para processamento paralelo: ", 1, 25, step=1)
    with c7: DIMENSIONS = st.slider("Dimensões (número de dimensões usadas para representar cada nó): ", 2, 256, step=8)

    st.write('TODO: aplicar node2vec no grafo inteiro, selecionar o filme a ser recomendado e efetivamente recomendar o filme')

if rec_form == 'Vizinhos mais próximos':
    pass