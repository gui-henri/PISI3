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
from Introdução import filesLocation
from sklearn.metrics import pairwise_distances
import numpy as np

from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))

from matrix_generation.matriz_de_similaridade import generate_matrix
    
tags = ['budget', 'genres', 'id', 'keywords', 'original_language', 'original_title', 'overview',
        'popularity', 'production_companies', 'production_countries', 'release_date', 'revenue',
        'runtime', 'title', 'vote_average', 'vote_count']

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
df = pd.read_csv(filesLocation(r'\tmdb_3000_movies.csv'), converters={'genres': literal_eval, 'keywords': literal_eval, 'production_companies': literal_eval, 'production_countries': literal_eval,})

selected_movies = st.multiselect("Selecione filmes para comparar: ", df['title'])
movies = df[df['title'].isin(selected_movies)].values.tolist()
if len(movies) > 1:

    c1, c2 = st.columns(2)
    cut_value = 0.0
    layout = ""

    with c1:
        cut_value = st.slider("Valor mínimo para conexão: ", 0.0, 1.0, step=0.01)

    with c2:
        possibilities = ["Shell", "Spiral", "Random", "Spring"]
        layout = st.selectbox("Selecionar formato do grafo", possibilities)

    gen_b = st.checkbox("Gêneros")
    pop_b = st.checkbox("Popularidade")
    pdc_b = st.checkbox("Produtoras")
    o_b = st.checkbox("Orçamento")
    pc_b = st.checkbox("Palavras-chave")

    gen = 0
    if gen_b == True:
        gen = 1

    pop = 0
    if pop_b == True:
        pop = 1
    
    pdc = 0
    if pdc_b == True:
        pdc = 1
    
    o = 0
    if o_b == True:
        o = 1

    pc = 0
    if pc_b == True:
        pc = 1

    pesos = {'budget': o, 'genres': gen, 'id': 0, 'keywords': pc, 'original_language': 0, 'original_title': 0, 'overview': 0,
        'popularity': pop, 'production_companies': pdc, 'production_countries': 0, 'release_date': 0, 'revenue': 0,
        'runtime': 0, 'title': 0, 'vote_average': 0, 'vote_count': 0}

    lista_matriz = generate_matrix(movies, tags, pesos)
    
    G = nx.Graph()
    for i, node in enumerate([i[5] for i in movies]):
        G.add_node(i, name=f'{node}')

    #newDf = pd.DataFrame(data= lista_matriz, columns=[i for i in movies], index=[i for i in movies])
    #print(newDf)
        
    for i, column in enumerate(lista_matriz):
        for j, item in enumerate(column):
            if item != None and item >= cut_value and i != j:
                G.add_edge(i, j, weight=item)

    fig, ax = plt.subplots()

    layouts = {
        "Shell": nx.shell_layout(G),
        "Random": nx.random_layout(G),
        "Spiral": nx.spiral_layout(G),
        "Spring": nx.spring_layout(G)
    }
    pos=layouts[layout]

    film_names = [i[13] for i in movies]
    node_names = dict(zip(range(len(selected_movies)), film_names))
    nx.draw(G, pos=pos, labels=node_names, with_labels=True, edge_color= 'b', font_weight='bold', font_size=16)

    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, label_pos=0.4, font_weight='bold', )

    fig_html = mpld3.fig_to_html(fig)

    components.html(fig_html, height=500)

    st.write(f"Similaridade máxima: {gen + pop + pdc + o + pc}")

    st.write(pd.DataFrame(lista_matriz))

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
            DIMENSIONS = st.slider("Dimensões (número de dimensões usadas para representar cada nó): ", 4, 256, step=4)

        g_emb = n2v(G, dimensions=DIMENSIONS, seed=128)
        mdl = g_emb.fit(
            vector_size=DIMENSIONS,
            window=WINDOW,
            min_count=MIN_COUNT,
            batch_words=BATCH_WORDS
        )

        nodes_and_index = G.nodes.data('name')

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
            Verificamos então que esta é uma técnica viável de detecção de comunidades, e que poderia(e pode), de fato, ser a escolhida para ser implementada no Movie Picker. O principal fator que nos leva a considerar outras técnicas é o fato de que este método não leva em consideração a representação avançada do Node2Vec, e pode deixar filmes sem conexão em um cluster próprio, ao invés de agrupa-los(coisa que nos pode ser interessante).

            ### Detecção de comunidades por Spectral Clustering

            Graças ao Node2Vec, podemos utilizar técnicas de Clustering convencionais, como Spectral Clustering, em grafos. Decidimos por utilizar o Spectral Clustering nesse trabalho. Demos preferência a esta técnica pois, como será mostrado abaixo, ela permite uma representação mais visual capaz de fornecer dados importantes a respeito do modelo.
            """
        )

        X = emb_df.values

        clustering = SpectralClustering(
            n_clusters=4,
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

        st.write(clustered_movies)
        
        st.markdown(
            """
            Como dito na seção de Detecção de comunidades por Spectral Clustering, essa representação pode nos fornecer rapidamente informações importantes a respeito do grafo e da representação gerada pelo Node2Vec. 
            
            Por exemplo, se os pontos estiverem muito esparços e distribuidos de forma aparentemente aleatória, isso é um sinal de que talvez a montagem do grafo esteja sendo feita de uma maneira não muito efetiva. Da mesma forma, é possível notar problemas no processo Clustering e corrigí-las, como por exemplo, insuficiência ou excesso de clusters.

            ### Método do 'Cotovelo' para achar número ótimo de clusters

            O método do cotovelo, ou Elbow Method em inglês, é uma abordagem comum para determinar o número ideal de clusters em algoritmos de clustering, incluindo o Spectral Clustering. Este método ajuda a identificar o número de clusters que oferece um bom equilíbrio entre a redução da distorção e a manutenção da interpretabilidade dos clusters. Vale lembrar que este é apenas uma heurística, e pode não apresentar os melhores resultados sempre.

            """
        )

        ks = [2, 3, 4, 5]
        # Executa o Spectral Clustering para cada valor de K
        for k in ks:
            sc = SpectralClustering(n_clusters=k, affinity='nearest_neighbors', assign_labels='cluster_qr', random_state=128)
            sc.fit(X)
            # Calcula os centróides para cada cluster
            centroids = np.array([np.mean(X[sc.labels_ == j], axis=0) for j in range(k)])
            # Calcula a distorção total para cada cluster
            total_distortion = calculate_total_distortion(X, sc.labels_, centroids)
            st.write(f"K = {k}, Distorção Total = {total_distortion}")

        st.markdown(
            """

            Como estes valores são dinâmicos, não temos como discorrer sobre os resultados acima, mas podemos realizar certas predições a respeito dos resultados e do comportamento dos valores. Cada valor de K é um número de clusters, e o valor de distorção é uma métrica que calcula a distância média de cada elemento do cluster para seu centróide. O número ideal de clusters, segundo essa técnica, é aquele que apresentou a última melhora substâncial em comparação com os outros.    

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

        st.write(emb_df_PCA)

        plt.clf()
        fig = plt.figure(figsize=(6, 4))
        plt.scatter(
            x=emb_df_PCA['x'],
            y=emb_df_PCA['y'],
            s=20,
            c=clustering.labels_,
            alpha=1
        )
        st.pyplot(fig)

        st.markdown(
            """
            Temos aqui uma representação visual do funcionamento do Clustering. Pela disposição das cores, podemos ver que a conversão reflete precisamente o resultado tanto da recomendação por Node2Vec quanto o trabalho de Clustering realizado anteriormente. 
            
            Como dito na seção de Detecção de comunidades por Spectral Clustering, essa representação pode nos fornecer rapidamente informações importantes a respeito do grafo e da representação gerada pelo Node2Vec. 
            
            Por exemplo, se os pontos estiverem muito esparços e distribuidos de forma aparentemente aleatória, isso é um sinal de que talvez a montagem do grafo esteja sendo feita de uma maneira não muito efetiva. Da mesma forma, é possível notar problemas no processo Clustering e corrigí-las, como por exemplo, insuficiência ou excesso de clusters.

            """
        )

        