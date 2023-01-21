import pandas as pd
import streamlit as st
import plotly.express as plt

df = pd.read_csv('data/archive/tmdb_5000_movies.csv')
df.set_index('original_title', inplace=True)

st.title("Visão global")

g = plt.scatter(data_frame= df, x="budget", y= "revenue", hover_name= "title", labels={"revenue":"Arrecadado", "budget":"Faturamento"})

st.plotly_chart(g)
st.subheader("Plot de todos os filmes no banco de dados, em realação ao seu orçamento (eixo horizontal) e Faturamento (eixo vertical).")