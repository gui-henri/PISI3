import pandas as pd
from ast import literal_eval
import plotly.express as plt
from collections import Counter
import json
from comparar import budget, genres, id, keywords, original_language, original_title, overview, popularity, production_companies, production_countries, release_date, revenue, runtime, title, vote_average, vote_count

def distComp(filmes, tag):
    tags = {'budget': 0, 'genres': 1, 'id': 2, 'keywords': 3, 'original_language': 4, 'original_title': 5, 'overview': 6,
        'popularity': 7, 'production_companies': 8, 'production_countries': 9, 'release_date': 10, 'revenue': 11,
        'runtime': 12, 'title': 13, 'vote_average': 14, 'vote_count': 15}
    
    lista = []
    index = tags[tag]
    f = eval(tag)
    
    for i, filmeA in enumerate(filmes):
        for filmeB in filmes[i+1:]:
            lista.append(f(filmeA[index], filmeB[index]))
        
    return lista


df = pd.read_csv(r'C:\Users\Lombardi\Documents\GitHub\PISI3\data\archive\tmdb_3000_movies.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval,})
movies = df.values.tolist()

targets = ['budget', 'genres', 'id', 'keywords', 'original_title', 'overview', 'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'title', 'vote_average', 'vote_count']

for target in targets:
    data = distComp(movies, target)
    tmp = Counter(data)

    s = sorted(tmp.items())

    with open(f"../distData/{target}.txt", "w+") as filehandle:
        json.dump(s, filehandle)
    filehandle.close()