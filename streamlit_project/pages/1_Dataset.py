import io
import streamlit as st
import pandas as pd

df = pd.read_csv('data/archive/all/tmdb_5000_movies.csv')

st.title("Dataset")

st.markdown(
    """
    Aqui serão encontrados detalhes a respeito do Dataset. O link para o site onde o dataset foi obtido é [este](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv). 

    #### Background

    Este dataset foi criado originalmente como uma forma de tentar prever quais filmes seriam um sucesso comércial ou que seriam bem avaliados pela crítica. Tudo isso a partir de informações como enredo, atores, orçamento e descrição de milhares de filmes. Os dados foram extraídos do site TMDB.

    """
)

with st.expander("Descrição das colunas"):
    st.markdown(
        """
        #### Colunas

        * Orçamento: o dinheiro investido para a produção do filme.
        * Gêneros: uma lista com os gêneros do filme.
        * Página inicial: link direto para o site oficial do filme.
        * Id: identificador único na plataforma TMDB.
        * Palavras-chave: lista de palavras que descrevem o filme.
        * Língua original: Em que língua o filme foi gravado
        * Título original: título do filme na língua original.
        * Resumo: sinopse do filme.
        * Popularidade: O quão popular é o filme.
        * Empresa produtora: empresa(s) que financiou a produção do filme.
        * País de produção: lista de países onde o filme foi produzido.
        * Data de lançamento.
        * Faturamento: o quanto que o filme arrecadou nos cinemas.
        * Tempo de tela: duração do filme.
        * Línguas faladas: lista de linguas para qual o filme foi traduzido.
        * Etiqueta: frase de efeito usada para marketing do filme.
        * Título: nome do filme.
        * Média de votos: nota média dos filmes.
        * Número de votos: número de pessoas que avaliaram o filme.
        * Atores: Todos os atores envolvidos no filme.
        * Funcionários: Todas as pessoas que participaram da produção do filme.
        """
    )

with st.expander("Visualizar cabeçalho dos dados"):
    st.write(df.head())
    st.write("É importante ressaltar que esse cabeçalho foi feito utilizando uma versão do dataset antes de ser pré-processado.")

with st.expander("Análise inicial do Dataset"):

    st.write("As análises foram realizadas utilizando python, em conjunto com a biblioteca Pandas. O dataset foi carregado da seguinte forma: ")
    st.write("`df = pd.read_csv('../archive/TMDB_5000_movies.csv')`")

    st.markdown("#### Informações básicas")

    st.write("Utilizando a função `info()` de um DataFrame Pandas, as seguintes informações são obtidas: ")

    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)

    st.write("O dataset possui poucos valores faltantes. Com exceção das coluna 'homepage' e 'tagline', nenhuma outra coluna apresentou mais que 3 valores faltantes. Em se tratando das colunas mencionadas, nenhuma delas foi utilizada nas análises.")

    st.markdown("#### Descrição do dataset")

    st.write("Abaixo segue o resultado da função `describe()` do dataframe.")
    st.write(df.describe())

    st.markdown("#### Correlação entre as colunas")
    st.write("Abaixo, segue uma matriz que mostra a correlação de pearson entre várias das colunas do dataset.")
    st.write(df.corr())
    st.write("Os principais destaques vão para as colunas com correlação positiva mais altas. Dentre estas, o faturamento tem grande destaque, pois tem uma alta correlação com o orçamento e com a quantidade de votos, além de uma moderada correlação com a popularidade. Vemos também que a correlação da média dos votos com as demais colunas não passa de moderada, o que reforça a ideia de que um filme não precisa ser um sucesso de crítica para ser um sucesso comercial, e mesmo que seja um sucesso de crítica, ainda pode fracassar comercialmente.")
