import streamlit as st


st.markdown(
    """
    ## Processo de concepção do algoritmo de ML

Ante as dificuldades enfrentadas pelo grupo para a formulação de um algoritmo de Machine Learning que atingisse tanto os critérios necessários para a aprovação como nossos próprios critérios de qualidade, foi decidido que seria adequado registrar as opções, tentativas e passo a passo do nosso processo. Este documento conterá justamente os registros atualizados de tais etapas, e será útil no processo de concepção, bem como nos momentos reservados para tirar dúvidas com os professores.

## Tentativas iniciais

Uma diversidade de abordagens foram idealizadas, estas que foram sendo cortadas no decorrer do desenvolvimento por diversos motivos. Aqui listaremos algumas das que se destacaram e chegaram a ser cogitadas como possível implementação.

### Montagem do Grafo

Cada vértice do grafo será um filme. Este é representado por um vetor com suas características, por exemplo, gênero, diretor, orçamento, etc.

Para a composição das arestas, há duas possibilidades:
* 1. Criar uma aresta entre dois vértices para cada característica entre eles: esse processo criaria um número enorme de arestas, mas permitiria o funcionamento de algoritmos como o Async Fluid, da biblioteca NetworkX, que infelizmente não funcionam em grafos com pesos nas arestas.
* 2. Contar o número de semelhanças entre dois filmes e então adicionar uma aresta com peso: isso reduziria drasticamente o número de arestas. Apesar de alguns algoritmos deixarem de funcionar, irá melhorar a visualização e consumo de memória.

### Técnica pré machine learning

Um poderia supor que, com base no grafo, bastaria procurarmos os vértices com maior número de conexões/maior peso na aresta. Essa abordagem pode funcionar, mas foge completamente do propósito do trabalho, que seria de estabelecer um modelo de machine learning que resolvesse o problema de uma forma efetiva. 

### Técnicas de Machine Learning

* #### 1. Função harmônica da biblioteca NetworkX

	A biblioteca NetworkX é uma maneira popular de interagir com grafos utilizando a linguagem Python. Nela já estão presentes diversas implementações de algoritmos de Machine Learning que nos permitem realizar tarefas comuns, como Node Classification. A função harmônica é justamente um desses algoritmos. Nela, podemos prever a característica de um vértice a partir das características de seus vizinhos.

	Por exemplo, se um vértice tem a característica "Usuário Gostou" e outro tem a característica "Usuário Não Gostou", poderiamos aplicar o algoritmo para distribuir essas características a outros vértices, e então achar aqueles que o usuário iria gostar ou não.

	O problema dessa abordagem está no alto consumo de poder de processamento e memória que ela pode exigir, já que esse método produz apenas uma lista como resposta, não um objeto na qual podemos fazer predições posteriormente. Isso significa precisariamos armazenar um grafo para cada usuário e para cada vez que uma previsão precisasse ser feita, executariamos a função harmônica novamente.

	Não sabemos se o algoritmo performaria de forma ruim, mas as chances são que sim. A ideia foi colocada de lado até que resultados empíricos demonstrem que o problema de desempenho pode ser contornado.

* #### 2. Clustering ingênuo

	A técnica de Clustering é uma forte candidata a ser implementada, apesar de que inicialmente tivemos dificuldade para encontrar uma forma eficiente de fazê-lo. O principal problema está no fato de que um grafo não pode ser facilmente representado em 2 dimensões, o que dificulta nosso processo.

	A primeira tentativa de contornar esse problema foi escolher uma única característica para ser o eixo X, e adicionar todas as outras num eixo Y. Por exemplo, o eixo X poderia ser os diretores dos filmes, e o eixo Y todas as outras características. Apesar da convicção de que esta técnica funciona, outras opções melhores de representação surgiram.

## Abordagens de Machine Learning candidatas

Continuamos buscando novas abordagens e as encontramos. Estamos agora avaliando quais alternativas se mostrarão mais eficientes (por mais eficiente, considere 'menor dificuldade de implementação' X 'Chance de agradar os professores'). 

* ### 1. Algoritmo de Girvan-Newman

	Seguindo a linha de algoritmos implementados diretamente pela biblioteca NetworkX, temos o algoritmo de Girvan-Newman. Este algoritmo busca as arestas com maior número de caminhos mais curtos(Betweeness Centrality) que passam por ela e as remove. Na prática, isso significa que a cada iteração, as conexões entre as comunidades estão sendo cortadas. No fim, é retornada uma lista com as comunidades e cada vértice que pertence a ela.

	Para realizar previsões nesse tipo de arquitetura, poderiamos usar um filme que o usuário gostou como entrada, obter a comunidade a que esse filme pertence e ordená-la com base em algum critério, como por exemplo, a proximidade entre os vértice (lembrando que quanto maior o peso das arestas, mais próximos são os vértices).

* ### 2. Clustering por Node2Vec

	Node2Vec é um algoritmo capaz de transformar um grafo em um conjunto de vetores. É implementado nativamente em Python, e permite a aplicação de algoritmos clássicos da área de machine learning, como k-means, para grafos.

	A implementação seguiria da seguinte forma:
	1. Transformariamos o grafo em um conjunto de vetores utilizando Node2Vec
	2. A partir desses dados, treinariamos um modelo utilizando k-means.
	3. Com o modelo pronto, seriamos capazes de realizar prever qual seria o cluster de uma determinada entrada.

	A principal vantagem dessa técnica é que teremos a capacidade de prever o cluster de um filme que não está presente no dataset, permitindo que o sistema recomende filmes baseados nesses.

* ### 3. Node2Vec puro

	Uma consequência indireta da utilização do Node2Vec é que, como agora os vértices estão alinhados num espaço bidimensional, isso significa que agora podemos traçar uma posição para o vértice no plano cartesiano. Obter a posição de um vértice torna-se uma tarefa relativamente fácil, e com isso, calcular a distância entre dois vértices torna-se uma possibilidade. Como vértices similares produzem vetores similares, bastaria procurar vértices que produziram um vetor parecido, ou até mesmo, procurar os vértices com menor distância e ordená-los. A própria biblioteca do Node2Vec fornece uma função que retorna os N vértices mais próximos a um vértice de entrada. 

	Essa alternativa pode apresentar resultados melhores do que apenas clusterizar, mas o algoritmo perderia a capacidade de realizar previsões a respeito de filmes que não estão presentes no banco de dados. 

## Conclusão

Analisar as alternativas é um complicado, mas estamos nos processos finais de decisão. Somos capazes de implementar os algoritmos de Machine Learning e muito mais até a próxima apresentação.
    """
)