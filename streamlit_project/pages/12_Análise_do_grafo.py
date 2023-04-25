import itertools
from math import sqrt
import pandas as pd
from sklearn.cluster import SpectralClustering
from sklearn.decomposition import PCA
import streamlit as st
import networkx as nx
from networkx import Graph
from ast import literal_eval
from node2vec import Node2Vec as n2v
from gensim import models
import plotly.express as ply
import numpy as np

G: Graph = nx.read_gpickle(f'grafo.pickle')

st.header('Análise do grafo')

st.write(f'Número de vértices: {G.number_of_nodes()}')
st.write(f'Número de arestas: {G.number_of_edges()}')
centrality = nx.degree_centrality(G)
list = list(centrality.values())
st.write(f'Grau médio dos vértices: {round(G.number_of_edges()/G.number_of_nodes())}')
st.write(f'Centralidade de grau média: {np.mean(list)}')
st.write(f'Maiores centralidades de grau: ')

centrality_ordenada = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
# pick the values in centrality_ordenada and use them to make a df
names = [G.nodes[centrality_ordenada[i][0]]['name'] for i, node in enumerate(centrality_ordenada[:20])]
names_df = pd.DataFrame(names, columns=['title'])

st.write(names_df)

name = G.nodes[centrality_ordenada[0][0]]['name']
st.write(f'Filme com maior centralidade de grau: {name}')