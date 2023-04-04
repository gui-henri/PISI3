import plotly.express as plt
import json
import streamlit as st
from statistics import median

st.title("Incidência de similaridade")
st.markdown("Para auxiliar na definição dos pesos de cada atributo, utilizamos essa seção para observar a incidência dos gráus de similaridade para cada atributo. A similaridade é calculada com base na distância entre os valores dos atributos do par de filmes comparados. A distância é normalizada para que fique entre 0 e 1 sendo limitada a duas casas decimais.")
st.markdown("Comparando todos os ~3000 filmes no banco de dados entre si (x²-x/2), totalizando aproximadamente 4.5M de comparações.")
st.markdown("Podemos notar os atributos que apresentam maior distinção entre os filmes, como por exemplo, o atributo 'keywords', priorizando atributos com caracteristicas parecidas podemos aumentar a acurácia do modelo. Ainda podemos aprovetar alguns atributos que apresentam menos distinção, se reduzirmos seu peso ou criar um valor de corte para sua similaridade para evitar a maldição de Bellmanr.")

lista = ['budget', 'genres', 'keywords', 'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'vote_average', 'vote_count']

def loadFile(file):
    filehandle = open(file, 'r')
    data = json.load(filehandle)
    filehandle.close()
    return data

def plotDist(data, nome):
    st.header(nome)
    log = st.checkbox("Incidência em log", key=nome)
    st.write(f'Média: {sum([i[0] for i in data])/len(data):.2f}')
    st.write(f'Mediana: {median([i[0] for i in data]):.2f}')
    g = plt.line(data, x=[i[0] for i in data], y = [i[1] for i in data], log_y= log)
    g.update_layout(xaxis_title="Similaridade", yaxis_title="Incidência")
    st.plotly_chart(g)
    return 

for tag in lista:
    data = loadFile(f'streamlit_project/data/distData/{tag}.txt')
    plotDist(data, tag)

tag = 'genres_dist'

filehandle = open(f'streamlit_project/data/distData/{tag}.txt', 'r')
data = json.load(filehandle)
filehandle.close()

data = sorted(data, key=lambda x: x[1], reverse=True)

st.header(tag)
log = st.checkbox("Incidência em log", key=tag)
g = plt.bar(data, x=[i[0] for i in data], y = [i[1] for i in data], log_y= log)
g.update_layout(xaxis_title="Genero", yaxis_title="Incidência")
st.plotly_chart(g)

tag = 'new_keywords'

filehandle = open(f'streamlit_project/data/distData/{tag}.txt', 'r')
data = json.load(filehandle)
filehandle.close()

data = sorted(data, key=lambda x: x[1], reverse=True)

st.header(tag)
log = st.checkbox("Incidência em log", key=tag)
g = plt.bar(data, x=[i[0] for i in data], y = [i[1] for i in data], log_y= log)
g.update_layout(xaxis_title="Similaridade", yaxis_title="Incidência")
st.plotly_chart(g)