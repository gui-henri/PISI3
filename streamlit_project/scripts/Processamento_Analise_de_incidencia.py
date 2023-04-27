import pandas as pd
from ast import literal_eval
from collections import Counter
import json

df = pd.read_csv(r'/data/archive/5k_movies_bin.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval, 'cast': literal_eval, 'director': literal_eval})
movies = df.values.tolist()