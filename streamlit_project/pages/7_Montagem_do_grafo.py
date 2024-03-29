import itertools
import pandas as pd
from sklearn.cluster import SpectralClustering
import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import mpld3
import networkx as nx
from networkx.algorithms import community
from ast import literal_eval
from node2vec import Node2Vec as n2v
from sklearn.decomposition import PCA
from sklearn.metrics import pairwise_distances
import numpy as np
import plotly.express as ply
import plotly.graph_objects as go
from math import sqrt


from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from matrix_generation.matriz_de_similaridade import generate_matrix

st.markdown(
    """

    # Grafo de relacionamento entre os filmes

    O principal diferencial desta página é o uso de grafos para facilitar a visualização da similaridade entre filmes. Iniciaremos explicando passo a passo o processo de montagem do grafo e depois forneceremos as ferramentas de visualização que surgiram a partir dele.

    ## Criação do grafo

    A primeira etapa na concepção do grafo foi decidir de que forma ele seria representado. Optamos por representar cada filme como um vértice, e para cada atributo em comum entre dois filmes, haverá uma conexão. Alguns atributos são compostos por listas, então a medida para a conexão será um valor entre 0 e 1, sendo 0 listas sem nenhum item em comum e 1 listas com os mesmos valores. Para filmes com múltiplas conexões, adicionaremos pesos as arestas.

    Após estruturarmos como seria o grafo, nossa primeira ação foi a de pré-processar os pesos das arestas, e por consequência, os atributos das arestas. Graças a isso, o ato de remontar o grafo inteiro caso algum erro ocorra se torna menos custoso.

    Com os pesos processados, utilizamos a biblioteca NetworkX para montar o grafo. Ela é compatível com as bibliotecas de machine learning que usaremos futuramente e também vem com dezenas de funções built-in que podemos utilizar para analisar o grafo.

    ## Ferramentas para visualização do grafo

    Podemos utilizar os dados de nosso dataset diretamente para obter uma visualização do grafo em tempo real. Podemos adicionar os filmes que desejamos, filtrar por atributo e também filtrar por peso da conexão.

    """
)
t = pd.read_csv('streamlit_project/data/archive/tmdb_3000_binario.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval, 'cast': literal_eval, 'director': literal_eval})


c = ["binario", "trinario", "discreto"]
cc = ["binario", "vizinhos", "distancia"]

cl1, cl2 = st.columns(2)

with cl1:
    #select_data = st.multiselect("Selecione o DataFrame:", c , default= "3 Faixas" , max_selections=1)
    select_data = st.radio("Selecione o DataFrame:", c , index=0)
    
    
with cl2:
    #select_compare = st.multiselect("Selecione a função de comparação:", cc , default= "vizinhos" , max_selections=1)
    select_compare = st.radio("Selecione a função de comparação:", cc , index=0)

if select_compare[:] == cc[0]:
    fun = "A"
elif select_compare[:] == cc[1]:
    fun = "B"
else:
    fun = "C"


df = pd.read_csv(f'streamlit_project/data/archive/tmdb_3000_{select_data}.csv', converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval, 'cast': literal_eval, 'director': literal_eval})

selected_movies = st.multiselect("Selecione filmes para comparar: ", t['title'])
movies = df[t['title'].isin(selected_movies)].values.tolist()

if len(movies) > 1:

    c1, c2 = st.columns(2)
    cut_value = 0.0
    layout = ""

    with c1:
        cut_value = st.slider("Valor mínimo para conexão: ", 0.0, 1.0, step=0.01, value=0.4)

    with c2:
        possibilities = ["Shell", "Spiral", "Random", "Spring"]
        layout = st.selectbox("Selecionar formato do grafo", possibilities, index=3)

    cl1, cl2, cl3 = st.columns(3)
    
    with cl1:
        gen = int(st.checkbox("Gêneros", value=True))
        pop = int(st.checkbox("Popularidade"))
        pdc = int(st.checkbox("Produtoras"))
        o = int(st.checkbox("Orçamento"))
    with cl2:
        pc = int(st.checkbox("Palavras-chave", value = True))
        at = int(st.checkbox("Atores", value = True))
        dt = int(st.checkbox("Diretores", value = True))
        lc = int(st.checkbox("Lucro"))
    with cl3:
        vt = int(st.checkbox("Votos"))
        tv = int(st.checkbox("total de votos"))
        dr = int(st.checkbox("Tempo de duração", value = True))
        dt = int(st.checkbox("Data de lançamento", value = True))
    
        
    pesos = {'index': 0, 'movie_id': 0, 'title': 0, 'genres': gen, 'keywords': pc, 'budget': o, 'revenue': lc, 'popularity': pop,
             'vote_average': vt, 'vote_count': tv, 'runtime': dr, 'release_date': dt, 'original_language': 0,
             'production_countries': 0, 'production_companies': pdc, 'director': dt, 'cast': at}


    maxPesos = sum(pesos.values())
    
    lista_matriz = generate_matrix(movies, pesos, maxPesos, fun)
    
    G = nx.Graph()
    for i, node in enumerate([i[2] for i in movies]):
        G.add_node(i, name=f'{node}')

    #newDf = pd.DataFrame(data= lista_matriz, columns=[i for i in movies], index=[i for i in movies])
    #print(newDf)
        
    for i, column in enumerate(lista_matriz):
        for j, item in enumerate(column):
            if item != None and item > cut_value and i != j:
                G.add_edge(i, j, weight=item)

    fig, ax = plt.subplots()

    layouts = {
        "Shell": nx.shell_layout(G),
        "Random": nx.random_layout(G),
        "Spiral": nx.spiral_layout(G),
        "Spring": nx.spring_layout(G)
    }
    pos=layouts[layout]

    film_names = [i[2] for i in movies]
    node_names = dict(zip(range(len(selected_movies)), film_names))
    nx.draw(G, pos=pos, labels=node_names, with_labels=True, edge_color= 'b', font_weight='bold', font_size=16)

    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, label_pos=0.4, font_weight='bold', )
    
    html = mpld3.fig_to_html(fig)
    components.html(html, height=500)

    matrix_to_show = pd.DataFrame(lista_matriz, columns=(x := [i[2] for i in movies]), index=x)
    
    #st.write(matrix_to_show)
    
    heatMap = ply.imshow(matrix_to_show, aspect='auto')
    heatMap.update_layout(title='Matriz de similaridade', height= 800)
    st.plotly_chart(heatMap, use_container_width=True)

    nodes_and_index = G.nodes.data('name')

    cl1, cl2 = st.columns(2)
    
    with cl1:
        st.write(f'Número de arestas: {G.number_of_edges()}')
        st.write(f'Número de nós: {G.number_of_nodes()}')
        st.write(f'Média de graus dos nós: {round(sum(dict(G.degree()).values()) / float(len(G)),2)}')

    with cl2:
        st.subheader('Grau médio dos vizinhos')
        st.write('Representa a média da quantidade de vizinhos de cada nó. ')
        z = zip(x, nx.average_neighbor_degree(G).values())
        st.write(pd.DataFrame(z, columns=['Nó', 'Grau médio dos vizinhos']))
        #st.write(pd.DataFrame(z, columns=['Nó', 'Grau médio dos vizinhos']))

    cl1, cl2 = st.columns(2)
    
    with cl1:
        st.subheader('Conectividade média')
        st.write('Representa a média da conectividade de cada nó. A conectividade entre dois nós é a quantidade de arestas que devem ser removidas até que não haja um caminho entre dois nós.')
        st.write(round(nx.average_node_connectivity(G), 2))

    with cl2:
        st.subheader('Centralidade de grau')
        st.write('Representa a centralidade de grau de cada nó. A centralidade de grau de um nó é calculada dividindo o grau de um nó pelo grau máximo possível.')
        z = zip(x, nx.degree_centrality(G).values())
        st.write(pd.DataFrame(z, columns=['Nó', 'Conectividade média']))
    

    cl1, cl2 = st.columns(2)
    
    with cl1:
        st.subheader('Centralidade por betweeness')
        st.write('Representa a centralidade de grau de cada nó. A centralidade por betweeness de um nó é calculada buscando os nós onde há o maior número de caminhos mais curtos.')
        z = zip(x, nx.betweenness_centrality(G).values())
        st.write(pd.DataFrame(z, columns=['Nó', 'Conectividade média']))

    with cl2:
        st.subheader('Densidade')
        st.write('Representa o quão denso é o grafo. O valor é 0 para grafos sem conexões e 1 para um grafo completo.')
        st.write(round(nx.density(G), 2))

    apply_node2vec = st.checkbox("Deseja aplicar Node2Vec a este grafo?")

    if apply_node2vec:

        st.markdown(
            """
            ## Machine Learning com Node2Vec

            Node2Vec é um algoritmo capaz de aprender a representar um grafo como um conjunto de vetores de N dimensões. Ele usa como base o **Word2Vec**, uma técnica de processamento de linguagem natural que usa como base a máxima de que palavras em contextos semelhantes tendem a ter significados semelhantes. O principal motivo para o uso do Node2Vec é o fato de que a representação do grafo retornada por ele **pode ser utilizada em algoritmos de Machine Learning tradicionais para realizar tarefas como Node Classification ou Clustering**. 

            #### Representação em vetores do Grafo (Node2Vec)

            Este é o resultado da aplicação do Node2Vec no Grafo anterior. O nome dos filmes foi usado como índice para podermos identificar cada vetor.
            """
        )

        c3, c4, c5, c6 = st.columns(4)

        WINDOW = 1
        MIN_COUNT = 1
        BATCH_WORDS = 4
        DIMENSIONS = 16

        with c3:
            WINDOW = st.slider("Janela (distância máxima entre entre nós): ", 1, 25, step=1)
        with c4:
            MIN_COUNT = st.slider("Valor mínimo (ignora nós com frequência total menor que esta): ", 1, 25, step=1)
        with c5:
            BATCH_WORDS = st.slider("Tamanho do lote (tamanho dos conjunto de nós que serão passados para serem processados paralelamente): ", 1, 25, step=1)
        with c6:
            DIMENSIONS = st.slider("Dimensões (número de dimensões usadas para representar cada nó): ", 2, 256, step=1, value=4)

        g_emb = n2v(G, dimensions=DIMENSIONS, seed=128, weight_key='weight', walk_length=120, num_walks=15)
        mdl = g_emb.fit(
            vector_size=DIMENSIONS,
            window=WINDOW,
            min_count=MIN_COUNT,
            batch_words=BATCH_WORDS,
        )

        st.write(mdl.get_latest_training_loss())

        emb_df = (
            pd.DataFrame(
                [mdl.wv.get_vector(str(n)) for n in G.nodes()],
                index = nodes_and_index
            )
        )

        st.write(emb_df)

        st.markdown(
            """
            #### Grau de centralidade dos nós

            O resultado da função Node2Vec retorna um modelo Word2Vec. Com base nesse modelo, podemos tirar diversas informações a respeito da representação, incluíndo o grau de centralidade de uma certa lista de nós.

            """
        )

        to_rank_by_centrality = st.multiselect('Selecione filmes para ranquear por centralidade: ', film_names)
        if len(to_rank_by_centrality) > 1:    
            film_index_to_rank = []  
            for film in to_rank_by_centrality:
                for node in nodes_and_index:
                    if node[1] == film:
                        film_index_to_rank.append(str(node[0]))
            ranked_indexes = mdl.wv.rank_by_centrality(film_index_to_rank)
            ranked_movies = []
            for i in ranked_indexes:
                for node in nodes_and_index:
                    if str(node[0]) == i[1]:
                        ranked_movies.append((i[0], node[1]))
            st.write(ranked_movies)

        st.markdown(
            """

            O ranqueamento com base no valor de centralidade é geralmente usado para encontrar nós mais 'influentes' em uma rede. Num sistema de recomendação com base em conteúdo como o Movie Picker, podemos utilizar essa informação para decidirmos quais filmes são mais importantes na hora de buscar por uma recomendação. Por exemplo, se um filme possui grau de centralidade 0.8 e outro possui 0.2, podemos recomendar com mais frequência filmes relacionados ao com grau de centralidade 0.8.

            ## Recomendação de filmes com base na semelhança de vetores

            Calculando a Similaridade de Cosseno entre a média da projeção dos vetores do nó fornecido e de todos os outros nós, podemos ordenar os N nós mais próximos de um determinado nó. Na prática, percebemos que isso pode funcionar como um sistema de recomendação. Ao selecionar um filme utilizando a ferramenta abaixo, temos em ordem decrescente a lista de filmes mais semelhantes ao escolhido.
            """
        )

        base_film = st.selectbox("Selecione um filme para encontrar os mais próximos: ", film_names)

        if base_film:
            base_film_index = ""
            for node in nodes_and_index:
                if base_film == node[1]:
                    base_film_index = node[0]
            similars = mdl.wv.most_similar(str(base_film_index), topn=10)
            similars_list = [int(item[0]) for item in similars]
            df_closest = emb_df.loc[similars_list]

            st.write(df_closest)

        st.markdown(
            """

            Os resultados variam bastante dependendo dos parâmetros em que o grafo foi montado, mas ainda assim se mostraram satisfatórios. Vemos que palavras-chave geralmente tem os resultados mais precisos de todos, principalmente quando comparado com os gêneros. Esta funcionalidade acabou por se tornar uma forte candidata a ser implementação do sistema de recomendação com base em conteúdo do Movie Picker.

            ## Clustering/detecção de comunidades no grafo

            Como explicado anteriormente, podemos usar a representação gerada pelo Node2Vec em algoritmos de Machine Learning tradicionais para realizar tarefas como classificação de vértices e detecção de comunidades. Porém, antes de utilizar Node2Vec para este propósito, nós procuramos verificar a viabilidade de algoritmos tradicionais para grafos na realização dessa tarefa.

            ### Detecção de comunidade por algoritmo de Girvan-Newman

            O algoritmo de Girvan-Newman serve para encontrar comunidades em grafos. Para realizar essa tarefa, ele progressivamente remove as arestas mais "importantes" do grafo, sendo estas as que conectam comunidades. No fim, apenas os nós de uma certa comunidade devem estar conectados. 

            As comunidades encontradas pelo algoritmo sendo executado no grafo anterior estão representadas no DataFrame abaixo:
            """
        )

        comp = community.girvan_newman(G)
        k = 1
        named_comm = []
        for communities in itertools.islice(comp, k):
            comm = (tuple(sorted(c) for c in communities))
            for item in comm:
                named_item = []
                for element in item:
                    for node in nodes_and_index:
                        if node[0] == element:
                            named_item.append(node[1])
                named_comm.append(named_item)
            named_comm_df = pd.DataFrame(named_comm)
            st.write(named_comm_df)

        st.markdown(
            """
            Verificamos então que esta é uma técnica viável de detecção de comunidades, mas que tende a mostrar resultados insatisfatórios, nos levando a não implementa-lo no Movie Picker. Este método não leva em consideração a representação avançada do Node2Vec, e pode deixar filmes sem conexão em um cluster próprio, ao invés de agrupa-los(coisa que nos pode ser interessante). Além disso, em grafos com muitas conexões, ele tende a não funcionar corretamente.

            ### Detecção de comunidades por Spectral Clustering

            Graças ao Node2Vec, podemos utilizar técnicas de Clustering convencionais, como Spectral Clustering, em grafos. Decidimos por utilizar o Spectral Clustering nesse trabalho. Demos preferência a esta técnica pois, como será mostrado abaixo, ela permite uma representação mais visual capaz de fornecer dados importantes a respeito do modelo.
            """
        )

        X = emb_df.values

        ks = range(1, len(film_names))

        NUM_CLUSTERS = st.selectbox('Número de clusters: ', ks, index=round(sqrt(len(film_names)/2)))

        clustering = SpectralClustering(
            n_clusters=NUM_CLUSTERS,
            assign_labels='cluster_qr',
            random_state=128
        ).fit(X)

        def calculate_total_distortion(X, labels, centroids):
            # Calcula a distância euclidiana entre cada ponto e o seu respectivo centróide
            distances = pairwise_distances(X, centroids, metric='euclidean')
            # Calcula a soma das distâncias euclidianas ao quadrado para cada cluster
            cluster_sums = np.array([np.sum(distances[labels == k, k]**2) for k in range(len(centroids))])
            # Calcula a distorção total como a soma das distâncias euclidianas ao quadrado de todos os pontos
            total_distortion = np.sum(cluster_sums)
            return total_distortion

        clustered_movies = pd.DataFrame(
            clustering.labels_,
            index=nodes_and_index
        )

        st.write(clustered_movies.rename(columns = {0: 'Cluster'}))
        
        st.markdown(
            """
            Como dito na seção de Detecção de comunidades por Spectral Clustering, essa representação pode nos fornecer rapidamente informações importantes a respeito do grafo e da representação gerada pelo Node2Vec. 
            
            Por exemplo, se os pontos estiverem muito esparços e distribuidos de forma aparentemente aleatória, isso é um sinal de que talvez a montagem do grafo esteja sendo feita de uma maneira não muito efetiva. Da mesma forma, é possível notar problemas no processo Clustering e corrigí-las, como por exemplo, insuficiência ou excesso de clusters.

            ### Método do 'Cotovelo' para achar número ótimo de clusters

            O método do cotovelo, ou Elbow Method em inglês, é uma abordagem comum para determinar o número ideal de clusters em algoritmos de clustering, incluindo o Spectral Clustering. Este método ajuda a identificar o número de clusters que oferece um bom equilíbrio entre a redução da distorção e a manutenção da interpretabilidade dos clusters. Vale lembrar que este é apenas uma heurística, e pode não apresentar os melhores resultados sempre.

            """
        )

        total_distortion_list = []
        # Executa o Spectral Clustering para cada valor de K
        for k in ks:
            sc = SpectralClustering(n_clusters=k, affinity='nearest_neighbors', assign_labels='cluster_qr', random_state=128)
            sc.fit(X)
            # Calcula os centróides para cada cluster
            centroids = np.array([np.mean(X[sc.labels_ == j], axis=0) for j in range(k)])
            # Calcula a distorção total para cada cluster
            total_distortion = calculate_total_distortion(X, sc.labels_, centroids)
            total_distortion_list.append(total_distortion)

        fig = ply.bar(total_distortion_list , x=[i for i in range(1,1+len(total_distortion_list))], y=total_distortion_list, title="Distorção X Cluster", )
        fig.update_layout(xaxis_title="Número de Clusters", yaxis_title="Distorção")
        
        st.plotly_chart(fig)

        st.markdown(
            """
            Como estes valores são dinâmicos, não temos como discorrer sobre os resultados acima, mas podemos realizar certas predições a respeito dos resultados e do comportamento dos valores. Cada valor de K é um número de clusters, e o valor de distorção é uma métrica que calcula a distância média de cada elemento do cluster para seu centróide. O número ideal de clusters, segundo essa técnica, é aquele que apresentou a última melhora substâncial em comparação com os outros.    

            Uma observação interessante é que mesmo quando agrupamos filmes por vários fatores, como gêneros e produtoras juntos, o número de clusters tende a se manter similar ao número de clusters quando utilizamos apenas keywords.

            ### Representação em 2 dimensões utilizando PCA

            No caso do Spectral Clustering, podemos utilizar vetores de qualquer número dimensões para fazer a classificação. Isso vem as custas de não termos uma forma fácil de visualizar os dados. Felizmente, há técnicas que permitem a realização dessa tarefa. Utilizaremos Principal component analysis(PCA), um algoritmo de redução de dimensionalidade, para transformar o conteúdo gerado pelo Node2Vec em algo visível em 2 dimensões. Então, utilizaremos o resultado do Clustering para colorir cada nó. 

            """
        )

        

        pca = PCA(n_components=2, random_state=7)
        pca_mdl = pca.fit_transform(emb_df)
        
        emb_df_PCA = (
            pd.DataFrame(
            pca_mdl,
            columns=['x', 'y'],
            index= emb_df.index
            )
        )
        emb_df_PCA.reset_index(inplace=True, level=1)
        emb_df_PCA.rename(columns={'level_1': 'Title'}, inplace=True)
        st.write(emb_df_PCA)
        
        fig = ply.scatter(emb_df_PCA, x='x', y='y', color=clustering.labels_.astype(str), hover_name='Title', title="Representação em 2 dimensões")
        fig.update_xaxes(showgrid=False, zeroline=False, showticklabels=False,)
        fig.update_yaxes(showgrid=False, zeroline=False, showticklabels=False,)
        
        st.plotly_chart(fig)

        st.markdown(
            """
            Temos aqui uma representação visual do funcionamento do Clustering. Pela disposição das cores, podemos ver que a conversão reflete precisamente o resultado tanto da recomendação por Node2Vec quanto o trabalho de Clustering realizado anteriormente. 
            
            Como dito na seção de Detecção de comunidades por Spectral Clustering, essa representação pode nos fornecer rapidamente informações importantes a respeito do grafo e da representação gerada pelo Node2Vec. 

            """
        )

        adj_cls = SpectralClustering(n_clusters=5, affinity='nearest_neighbors', assign_labels='cluster_qr', random_state=128)
        adj_cls.fit(matrix_to_show)

        adj_clustered_movies = pd.DataFrame(
            adj_cls.labels_,
            index=nodes_and_index
        )

        st.write(adj_clustered_movies.rename(columns = {0: 'Cluster'}))

        fig = ply.scatter(emb_df_PCA, x='x', y='y', color=adj_cls.labels_.astype(str), hover_name='Title', title="Representação em 2 dimensões")
        fig.update_xaxes(showgrid=False, zeroline=False, showticklabels=False,)
        fig.update_yaxes(showgrid=False, zeroline=False, showticklabels=False,)

        st.plotly_chart(fig)

        total_distortion_list = []
        # Executa o Spectral Clustering para cada valor de K
        for k in ks:
            sc = SpectralClustering(n_clusters=k, affinity='nearest_neighbors', assign_labels='cluster_qr', random_state=128)
            sc.fit(matrix_to_show)
            # Calcula os centróides para cada cluster
            centroids = np.array([np.mean(X[sc.labels_ == j], axis=0) for j in range(k)])
            # Calcula a distorção total para cada cluster
            total_distortion = calculate_total_distortion(X, sc.labels_, centroids)
            total_distortion_list.append(total_distortion)

        fig = ply.bar(total_distortion_list , x=[i for i in range(1,1+len(total_distortion_list))], y=total_distortion_list, title="Distorção X Cluster", )
        fig.update_layout(xaxis_title="Número de Clusters", yaxis_title="Distorção")
        
        st.plotly_chart(fig)

        