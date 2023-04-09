# O propósito deste script é gerar o grafo completo que será utilizado para as comparações e salvá-lo localmente

from ast import literal_eval
import pandas as pd
import networkx as nx
from node2vec import Node2Vec as n2v

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from matrix_generation.matriz_de_similaridade import generate_matrix

# ler o arquivo
def generate(cut_value, pesos):

    df = pd.read_csv('streamlit_project/data/archive/5k_movies_bin.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval, 'cast': literal_eval, 'director': literal_eval})

    maxPesos = sum(pesos.values())
    movies = df.values.tolist()

    lista_matriz = generate_matrix(movies, pesos, maxPesos, 'A')

    G = nx.Graph()
    for i, node in enumerate([i[2] for i in movies]):
        G.add_node(i, name=f'{node}')

    for i, column in enumerate(lista_matriz):
            for j, item in enumerate(column):
                if item != None and item > cut_value and i != j:
                    G.add_edge(i, j, weight=item)
    
    nx.write_gpickle(G, 'grafo.pickle')
    return G

if __name__ == "__main__":
     pesos = {'index': 0, 'movie_id': 0, 'title': 0, 'genres': 1, 'keywords': 1, 'budget': 0, 'revenue': 0, 'popularity': 0,
                'vote_average': 0, 'vote_count': 0, 'runtime': 1, 'release_date': 1, 'original_language': 0,
                'production_countries': 0, 'production_companies': 0, 'director': 1, 'cast': 1}
     cut_value = 0.4
     G = nx.gpickle.read_gpickle('grafo_old.pickle')
     WINDOW = 1
     MIN_COUNT = 1
     BATCH_WORDS = 1
     DIMENSIONS = 100
     print('Processando node2vec...')
     g_emb = n2v(G, p=1, q=0.5, dimensions=DIMENSIONS, seed=128, weight_key='weight', walk_length=5, num_walks=100, workers=3, temp_folder='temp_folder/')
     print('Treinando modelo node2vec...')
     mdl = g_emb.fit(
        vector_size=DIMENSIONS,
        window=WINDOW,
        min_count=MIN_COUNT,
        batch_words=BATCH_WORDS,
    )
     print('Salvando modelo node2vec...')
     mdl.save('n2v_model_2.w2v')
     print('Execução concluída!')

