import pandas as pd
from ast import literal_eval
from collections import Counter
import json

df = pd.read_csv('streamlit_project/data/archive/5k_movies_bin.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval, 'cast': literal_eval, 'director': literal_eval})
movies = df.values.tolist()

def distComp(filmes, tag , fun):
    
    indices  = {'index': 0, 'movie_id':1, 'title':2, 'genres':3, 'keywords':4, 'budget':5, 'revenue':6, 'popularity':7,
             'vote_average':8, 'vote_count':9, 'runtime':10, 'release_date':11, 'original_language':12,
             'production_countries':13, 'production_companies':14, 'cast':15, 'director':16}
    
    lista = []
    func = 'comparar.' + tag
    f = eval(func)
    
    ind = indices[tag]
    
    for i, filmeA in enumerate(filmes):
        for filmeB in filmes[i+1:]:
            lista.append(round(f(filmeA[ind], filmeB[ind], fun), 2))
    
    return lista


tags = ['genres', 'keywords', 'budget', 'revenue', 'popularity',
             'vote_average', 'vote_count', 'runtime', 'release_date', 'original_language',
             'production_countries', 'production_companies', 'director', 'cast']

for tag in tags:
    print(tag, end='\r')
    data = distComp(movies, tag, 'A')
    tmp = Counter(data)
    
    s = sorted(tmp.items())
    
    with open(f'streamlit_project/data/distData/{tag}.txt', 'w+') as filehandle:
        json.dump(s, filehandle)
    filehandle.close()

