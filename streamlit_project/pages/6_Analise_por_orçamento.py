import pandas as pd
import streamlit as st
import plotly.express as px
from datetime import datetime
import cpi

df = pd.read_csv('data/archive/all/tmdb_5000_movies.csv')

st.title("Análise por orçamento")

st.markdown(
    """
    A indústria do cinema costuma categorizar filmes por seu orçamento, sendo dessas as classes de baixo, médio e grande orçamento. Essa categoria é importante na hora de analisar um filme, pois ela revela que tipo de ferramentas a produção tinha disponível durante a produção.

    Não há um consenso onde uma categoria acaba e outra começa, mas em nosso trabalho, utilizaremos baixo orçamento como 'menos de 5 milhões de orçamento', médio orçamento como 'entre 5 e 75 milhões de orçamento' e grande orçamento como 'acima de 75 milhões de orçamento'. Os valores do orçamento foram corrigidos pela inflação.

    ## Quantidade de filmes lançados por ano

    Primeiro, faremos uma análise a respeito da quantidade de filmes lançados por ano em cada categoria, afim de verificar o comportamento da indústria com o passar do tempo.
    """
)

base_year = 2023

st.markdown(
    """
    ## Correção pela inflação
    Antes de fazer as comparações, primeiro corrigir o valor dos filmes pela inflação. Utilizando a biblioteca cpi, que adquire as informações mais atuais a respeito da inflação e fornece métodos para corrigir os valores facilmente, confeccionamos o trecho de código abaixo, que deve aplicar a correção de orçamento em todo o dataframe:
    
    ``` Python
    def inflation_correction(row):
        launch_year = row['release_date']
        dt = datetime.strptime(launch_year, '%y-%m-%d')
        return round(cpi.inflate(row['budget'], dt.year))
    ```

    """
    )
# Único filme sem data de lançamento. Pesquisei no Google e atualizei manualmente
df.loc[4553, 'release_date'] = '2003-01-01'

def inflation_correction(row):
    launch_year = row['release_date']
    dt = datetime.strptime(launch_year, '%Y-%m-%d')
    return round(cpi.inflate(row['budget'], dt.year))

df['corrected_budget'] = df.apply(inflation_correction, axis=1)

low_budget_films = df.query('corrected_budget < 5000000 and corrected_budget > 400')
mid_budget_films = df.query('corrected_budget > 5000000 and corrected_budget < 75000000')
high_budget_films = df.query('corrected_budget > 75000000')

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
    """
    #### Filmes de baixo orçamento
    """
    )
    st.write(low_budget_films[['title', 'corrected_budget']].head())

with col2:
    st.markdown(
    """
    #### Filmes de médio orçamento
    """
    )
    st.write(mid_budget_films[['title', 'corrected_budget']].head())

with col3:
    st.markdown(
    """
    #### Filmes de grande orçamento
    """
    )
    st.write(high_budget_films[['title', 'corrected_budget']].head())

# Pegar os filmes do ano x de cada categoria, adicionar numa lista
ano_inicial = 1987      # 1987 é o ano mínimo
ano_final = 2017        # 2017 é o ano máximo

anos = []

low_budget_films['release_date'] = pd.to_datetime(low_budget_films['release_date'])
mid_budget_films['release_date'] = pd.to_datetime(mid_budget_films['release_date'])
high_budget_films['release_date'] = pd.to_datetime(high_budget_films['release_date'])

for ano in range(ano_inicial, ano_final):
    low_budget_count = (low_budget_films['release_date'].dt.year == ano).value_counts()[True]
    mid_budget_count = (mid_budget_films['release_date'].dt.year == ano).value_counts()[True]
    high_budget_count = (high_budget_films['release_date'].dt.year == ano).value_counts()[True]

    anos.append([ano, low_budget_count, mid_budget_count, high_budget_count])
stream = pd.DataFrame(anos, columns=("Ano", "Baixo Orçamento", "Médio Orçamento", "Grande Orçamento"))

st.markdown(
    """
    ## Crescimento da quantidade de filmes de cada categoria com o tempo

    O gráfico a seguir representa a quantidade de filmes lançados em cada categoria no decorrer dos anos.

    """
)

st.plotly_chart(px.line(data_frame=stream, x="Ano", y=["Baixo Orçamento", "Médio Orçamento", "Grande Orçamento"], labels={"Ano": "Anos", "value": "Quantidade"}))

st.markdown(
    """

    Observamos que a indústria como um todo cresceu consideravelmente no período, com destaque para os filmes de médio orçamento. Como forma de investigar esse comportamento, iremos verificar o ROI médio dessas categorias de filmes para verificar se elas justificam esse crescimento.

    ## ROI médio dos filmes por categoria

    O gráfico a seguir representa a média do ROI de todos os filmes em uma categoria.
 
    """
)
df.set_index('original_title', inplace=True)

def calc_roi(row):
    budget = row['budget']
    revenue = row['revenue']
    return round(((revenue - budget)/budget) * 100, 10)

low_budget_films['ROI'] = low_budget_films.apply(calc_roi, axis=1)
mid_budget_films['ROI'] = mid_budget_films.apply(calc_roi, axis=1)
high_budget_films['ROI'] = high_budget_films.apply(calc_roi, axis=1)

values = [["Baixo Orçamento", low_budget_films['ROI'].mean()], ["Médio Orçamento", mid_budget_films['ROI'].mean()], ["Grande Orçamento", high_budget_films['ROI'].mean()]]
roi_stream = pd.DataFrame(values, columns=("Categoria", "Valores"))
st.plotly_chart(px.bar(data_frame=roi_stream, x="Categoria", y="Valores"))

st.markdown(
    """
    Como é possível ver no gráfico, filmes com menor orçamento possuem um ROI elevadíssimo, apesar de ser a categoria com menos investimento e apesar de o faturamento do filme ter uma forte correlação com o orçamento. Vemos também que filmes de médio orçamento tem um ROI de aproximadamente 100% a mais que os filmes de grande orçamento, o que parece justificar a preferencia dessa categoria pelas empresas.
    """
)

st.markdown(
    """
    ### Ferramenta de comparação de ROI

    Durante o processo de implementar o cálculo do ROI, fizemos uma ferramenta que permite compararmos diretamente o ROI de quantos filmes quisermos.   
    """
)

selected_movies = st.multiselect("Filmes para comparar", df['title'])

if len(selected_movies) > 0:
    partial_data = [df.loc[film] for film in selected_movies]
    lista = [[f["title"], f["budget"], f["revenue"]] for f in partial_data]
    for l in lista:
        l.append(round(((l[2] - l[1])/l[1]) * 100, 1))
    to_stream = pd.DataFrame(lista, columns=("Títulos", "Orçamento", "Faturamento", "ROI"))    
    st.plotly_chart(px.bar(data_frame=to_stream, x=["ROI"], title="Porcentagem de filmes que conseguiram pagar seus custos de produção", y="Títulos", barmode='group', labels={"value":"%"}))

st.markdown("""
    ### Porcentagem de filmes que conseguem pagar seus custos de produção por categoria

    A partir da análise anterior, concluimos que filmes da categoria de baixo orçamento possuem um ROI extremamente elevado se comparado com as demais categorias. Apesar disso, vimos também que são os filmes com menor quantidade de novos lançamentos e crescimento lento. Afim de investigar por que as grandes empresas geralmente não focam nessa categoria de filmes, montamos o gráfico abaixo.

    """)

low_budget_percent = round((low_budget_films['revenue'] > low_budget_films['budget']).mean() * 100, 1)
mid_budget_percent = round((mid_budget_films['revenue'] > mid_budget_films['budget']).mean() * 100, 1)
high_budget_percent = round((high_budget_films['revenue'] > high_budget_films['budget']).mean() * 100, 1)

values = [["Baixo Orçamento", low_budget_percent], ["Médio Orçamento", mid_budget_percent], ["Grande Orçamento", high_budget_percent]]

payoff_stream = pd.DataFrame(values, columns=("Categoria", "Porcentagem"))
st.plotly_chart(px.bar(data_frame=payoff_stream, x="Categoria", y="Porcentagem"))

st.markdown("O gráfico mostra que filmes de grande orçamento historicamente tem uma chance muito maior de arcarem com seus custos, enquanto que filmes de baixo orçamento não conseguem nem arcar com os custos de produção em aproximadamente 55% das vezes. Filmes de médio orçamento apresentam um meio-termo entre as duas categorias, possivelmente sendo a opção com melhor risco-retorno.")