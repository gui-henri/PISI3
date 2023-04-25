import plotly.express as plt
import json
import streamlit as st
from statistics import median

st.title("Incidência de similaridade")
st.markdown("Para auxiliar a definir quais atributos seriam usados na formação do cluster, utilizamos essa seção para observar a incidência dos gráus de similaridade de cada atributo. A similaridade é calculada com base na distância entre os valores dos atributos do par de filmes comparados. A distância é normalizada para que fique entre 0 e 1 sendo limitada a duas casas decimais para realizar a comparação.")
st.markdown("O total de comparações é dado por x²-x/2, ")
st.markdown("Atravez da análise dos gráficos, podemos observar que alguns atributos possuem uma distribuição de similaridade muito concentrada em um único valor, o que pode indicar que esse atributo não é muito relevante para a formação do cluster. Outros atributos possuem uma distribuição mais uniforme, o que pode indicar que esse atributo é mais relevante para a formação do cluster.")
st.markdown("Além disso podemos definir um valor de corte inicial para a formação das arestas do grafo, através da média das medianas resultante dos atributos selecionados. Como resultado, chegamos que as variáveis principais para a formação do cluster desejado foram as seguintes: Gêneros, Palavras-chave, Atores, Diretor, Tempo de duração e Data de lançamento, com o valor de corte de 0.435.")

lista = ['genres', 'keywords', 'budget', 'revenue', 'popularity',
             'vote_average', 'vote_count', 'runtime', 'release_date', 'original_language',
             'production_countries', 'production_companies', 'director', 'cast']

def loadFile(file):
    
    filehandle = open(file, 'r')
    data = json.load(filehandle)
    filehandle.close()
    return data

def plotDist(data, nome):
    trad = {'genres': 'Gêneros', 'keywords': 'Palavras-chave', 'budget': 'Orçamento', 'revenue': 'Receita', 'popularity': 'Popularidade',
                'vote_average': 'Média de votos', 'vote_count': 'Número de votos', 'runtime': 'Duração', 'release_date': 'Data de lançamento', 'original_language': 'Idioma original',
                'production_countries': 'Países de produção', 'production_companies': 'Companhias de produção', 'director': 'Diretor', 'cast': 'Elenco'}
    
    st.header(trad[nome])
    log = st.checkbox("Incidência em log", key=nome)
    st.write(f'Média: {sum([i[0] for i in data])/len(data):.2f}')
    st.write(f'Mediana: {median([i[0] for i in data]):.2f}')
    if len(data) <= 2:
        g = plt.bar(data, x=[i[0] for i in data], y = [i[1] for i in data], log_y= log)
    else:    
        g = plt.line(data, x=[i[0] for i in data], y = [i[1] for i in data], log_y= log)
    g.update_layout(xaxis_title="Similaridade", yaxis_title="Incidência")
    st.plotly_chart(g)
    return 


tag = 'genres_dist'

filehandle = open(f'streamlit_project/data/distData/{tag}.txt', 'r')
data = json.load(filehandle)
filehandle.close()

data = sorted(data, key=lambda x: x[1], reverse=True)

st.header('Distribuição de gêneros')
log = st.checkbox("Incidência em log", key=tag)
g = plt.bar(data, x=[i[0] for i in data], y = [i[1] for i in data], log_y= log)
g.update_layout(xaxis_title="Genero", yaxis_title="Incidência")
st.plotly_chart(g)

tag = 'new_keywords'

filehandle = open(f'streamlit_project/data/distData/{tag}.txt', 'r')
data = json.load(filehandle)
filehandle.close()


st.header('Distribuição de palavras-chave')
log = st.checkbox("Incidência em log", key=tag)
g = plt.bar(data, x=[i[0] for i in data], y = [i[1] for i in data], log_y= log)
g.update_layout(xaxis_title="Similaridade", yaxis_title="Incidência")
st.plotly_chart(g)


st.title("Gráficos de similaridade por atributo")


radio = st.radio("Modo de análise", ['contínuo', 'binário'])
radiodic = {'contínuo': 'cont', 'binário': 'bin'}


for tag in lista:
    data = loadFile(f'data/distData/{radiodic[radio]}/{tag}.txt')
    plotDist(data, tag)