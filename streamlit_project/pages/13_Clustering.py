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

def get_graph() -> Graph:
    G = nx.read_gpickle(f'grafo.pickle')
    return G

df = pd.read_csv(f'streamlit_project/data/archive/tmdb_3000_discreto.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval, 'cast': literal_eval, 'director': literal_eval})
G = get_graph()
nodes_and_index = G.nodes.data('name')


mdl = models.word2vec.Word2Vec.load('n2v_model.w2v')

emb_df = (
    pd.DataFrame(
        [mdl.wv.get_vector(str(n)) for n in G.nodes()],
        index = nodes_and_index
    )
)

st.markdown(
    """

    # Clustering

    Nesta página, podemos ver a aplicação do algoritmo de clustering. Foi utilizado o Node2Vec para gerar embeddings do grafo e então, utilizado o Spectral Clustering para gerarmos os labels de cada filme.

    """
)

X = emb_df.values

ks = range(1, G.number_of_nodes())

NUM_CLUSTERS = st.selectbox('Número de clusters: ', ks, index=round(sqrt(G.number_of_nodes()/2)))

clustering = SpectralClustering(
    n_clusters=NUM_CLUSTERS,
    assign_labels='cluster_qr',
    random_state=128
).fit(X)

clustered_movies = pd.DataFrame(
    clustering.labels_,
    index=nodes_and_index
)

st.write(clustered_movies.rename(columns = {0: 'Cluster'}))

pca = PCA(n_components=2, random_state=7)
pca_mdl = pca.fit_transform(emb_df)

emb_df_PCA = (
    pd.DataFrame(
        pca_mdl,
        columns=['x', 'y'],
        index= emb_df.index
        )
    )
emb_df_PCA.reset_index(inplace=True, level=1)
emb_df_PCA.rename(columns={'level_1': 'Title'}, inplace=True)

fig = ply.scatter(emb_df_PCA, x='x', y='y', color=clustering.labels_.astype(str), hover_name='Title', title="Representação em 2 dimensões")
fig.update_layout(height= 1500)
fig.update_xaxes(showgrid=False, zeroline=False, showticklabels=False,)
fig.update_yaxes(showgrid=False, zeroline=False, showticklabels=False,)
        
st.plotly_chart(fig)

