import pandas as pd
from .comparar import comp

def generate_matrix(filmes, tags, pesos):
    matriz = []
    temp = []

    t = len(filmes)

    for i, filmeA in enumerate(filmes):
        print(f"Processando... {i}/{t}", end = '\r')
        for filmeB in filmes[i+1:]:
            temp.append(round(comp(filmeA, filmeB, tags, pesos), 2))
        matriz.append(temp)
        temp = []
    return matriz

"""
if __name__ == '__main__':
    df = pd.read_csv('../../../data/archive/10test.csv')
    filmes = df.values.tolist()
        
    tags = ['budget', 'genres', 'id', 'keywords', 'original_language', 'original_title', 'overview',
            'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue',
            'runtime', 'title', 'vote_average', 'vote_count']

    pesos = {'budget': 3, 'genres': 8, 'id': 0, 'keywords': 2, 'original_language': 1, 'original_title': 0, 'overview': 0,
            'popularity': 3, 'production_companies': 1, 'production_countries': 1, 'release_date': 2, 'revenue': 4,
            'runtime': 3, 'title': 0, 'vote_average': 7, 'vote_count': 6}

    print(generate_matrix(filmes, tags, pesos))
"""