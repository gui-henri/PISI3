# O propósito deste script é gerar o grafo completo que será utilizado para as comparações e salvá-lo localmente

from ast import literal_eval
import pandas as pd
import networkx as nx

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from matrix_generation.matriz_de_similaridade import generate_matrix

# ler o arquivo
def generate(cut_value, pesos):

    df = pd.read_csv('streamlit_project/data/archive/tmdb_3000_ranges.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval, 'cast': literal_eval, 'director': literal_eval})

    maxPesos = sum(pesos.values())
    movies = df.values.tolist()

    lista_matriz = generate_matrix(movies, pesos, maxPesos, 'B')

    G = nx.Graph()
    for i, node in enumerate([i[2] for i in movies]):
        G.add_node(i, name=f'{node}')

    for i, column in enumerate(lista_matriz):
            for j, item in enumerate(column):
                if item != None and item > cut_value and i != j:
                    G.add_edge(i, j, weight=item)
    
    nx.write_gpickle(G, 'grafo_generos.pickle')

if __name__ == "__main__":
     pesos = {'index': 0, 'movie_id': 0, 'title': 0, 'genres': 1, 'keywords': 0, 'budget': 0, 'revenue': 0, 'popularity': 0,
                'vote_average': 0, 'vote_count': 0, 'runtime': 0, 'release_date': 0, 'original_language': 0,
                'production_countries': 0, 'production_companies': 0, 'director': 0, 'cast': 0}
     cut_value = 0.4
     generate(cut_value, pesos)