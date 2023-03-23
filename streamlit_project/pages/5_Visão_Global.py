import pandas as pd
import streamlit as st
import plotly.express as plt


df = pd.read_csv(r'data\archive\tmdb_3000_movies_merged.csv')

st.title("Visão global")

g = plt.scatter(data_frame= df, x="budget", y= "revenue", hover_name= "title", labels={"revenue":"Faturamento USD", "budget":"Orçamento USD"})
st.plotly_chart(g)
st.markdown("Plot de todos os filmes no banco de dados, em realação ao seu orçamento (eixo horizontal) e Faturamento (eixo vertical).")

'''
lista = ['budget', 'genres', 'keywords', 'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue', 'runtime', 'vote_average', 'vote_count']

def loadFile(file):
    filehandle = open(file, 'r')
    data = json.load(filehandle)
    filehandle.close()
    return data

def plotDist(data, nome):
    st.header(nome)
    log = st.checkbox("Incidência em log", key=nome)
    g = plt.line(data, x=[i[0] for i in data], y = [i[1] for i in data], log_y= log)
    g.update_layout(xaxis_title="Similaridade", yaxis_title="Incidência")
    st.plotly_chart(g)
    return 

tag = 'keywords_dist'
data = loadFile(f'distData/{tag}.txt')
plotDist(data, tag)
'''


