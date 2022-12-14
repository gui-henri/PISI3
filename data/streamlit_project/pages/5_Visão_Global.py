import pandas as pd
import streamlit as st
import seaborn as sns

df = pd.read_csv('../archive/TMDB_5000_movies.csv')
df.set_index('original_title', inplace=True)

st.title("Visão global")

sns.set_theme(style="whitegrid")
cmap = sns.cubehelix_palette(rot=-.2, as_cmap=True)
g = sns.relplot(
    data=df,
    x="budget", y="revenue", hue= "revenue"-"budget", legend="auto", 
    palette=cmap,
)

g.set(xscale="linear", yscale="linear")
g.ax.xaxis.grid(True, "minor", linewidth=.25)
g.ax.yaxis.grid(True, "minor", linewidth=.25)
g.despine(left=True, bottom=True)
st.pyplot(g)

st.subheader("Plot de todos os filmes no banco de dados, em realação ao seu orçamento (eixo horizontal) e lucro (eixo vertical).")