from .comparar import comp

def generate_matrix(filmes, pesos, maxPeso):
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
            temp.append(comp(filmeA, filmeB, tags, pesos, maxPeso))
            #temp.append(f'({filmeA[5]}, {filmeB[5]})') #debugOnly
        matriz.append(temp)
        temp = []
        
    return matriz

"""
temp = df['original_title']
newDf = pd.DataFrame(data= matriz[:-1], columns=[i for i in temp[1:]], index=[i for i in temp[:-1]])
newDf.to_csv('../data/archive/results/processed_10test.csv')
"""
