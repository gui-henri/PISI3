from .comparar import comp
import pandas as pd


def generate_matrix(filmes, pesos, maxPeso, fun):
    if maxPeso == 0:
        maxPeso = 1
        
    matriz = []
    temp = []
    t = len(filmes)
    tags = [i for i in pesos]
    
    for i, filmeA in enumerate(filmes):
        print(f"Processando... {i}/{t}", end = '\r')
        for j in range(i):
           temp.append(None)
        for filmeB in filmes[i:]:
            temp.append(round(comp(filmeA, filmeB, tags, pesos, maxPeso, fun), 4))
            #temp.append(f'({filmeA[5]}, {filmeB[5]})') #debugOnly
        matriz.append(temp)
        temp = []
        
    return matriz


def generate_sim(df, pesos, maxPeso, fun, custom):
    
    filmes = df.values.tolist()
    
    if maxPeso == 0:
        maxPeso = 1
        
    lista = []
    tags = [i for i in pesos]
    
    for i, filmeA in enumerate(filmes):
        lista.append(comp(filmeA, custom, tags, pesos, maxPeso, fun))
    
    for i, v in enumerate(filmes):
        v.insert(0, lista[i])
       
    tags.insert(0, 'Score')
    
    df = pd.DataFrame(filmes, columns=tags)
    df.sort_values(by=['Score'], inplace=True, ascending=False)
    
    return df
    
    
    
    
        
    
    
    

"""
temp = df['original_title']
newDf = pd.DataFrame(data= matriz[:-1], columns=[i for i in temp[1:]], index=[i for i in temp[:-1]])
newDf.to_csv('../data/archive/results/processed_10test.csv')
"""
