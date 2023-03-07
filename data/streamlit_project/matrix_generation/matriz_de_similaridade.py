import pandas as pd
from ast import literal_eval
from comparar import comp

tags = ['budget', 'genres', 'id', 'keywords', 'original_language', 'original_title', 'overview',
        'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue',
        'runtime', 'title', 'vote_average', 'vote_count']

pesos = {'budget': 1, 'genres': 5, 'id': 0, 
         'keywords': 7, 'original_language': 1, 
         'original_title': 0, 'overview': 0,
        'popularity': 2, 'production_companies': 1, 
        'production_countries': 1, 'release_date': 3, 
        'revenue': 2, 'runtime': 1, 'title': 0, 
        'vote_average': 2, 'vote_count': 1}
    
df = pd.read_csv('../data/archive/tmdb_3000_movies.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval,})

filmes = df.values.tolist()

matriz = []

temp = []

t = len(filmes)
for i, filmeA in enumerate(filmes):
    print(f"Processando... {i}/{t}", end = '\r')
    for j in range(i):
        temp.append(None)
    for filmeB in filmes[i+1:]:
        temp.append(round(comp(filmeA, filmeB, tags, pesos), 2))
        #temp.append(f'({filmeA[5]}, {filmeB[5]})') #debugOnly
    matriz.append(temp)
    temp = []

temp = df['original_title']
newDf = pd.DataFrame(data= matriz[:-1], columns=[i for i in temp[1:]], index=[i for i in temp[:-1]])
newDf.to_csv('../data/archive/results/processed_10test.csv')