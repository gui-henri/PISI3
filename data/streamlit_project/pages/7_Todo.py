import streamlit as st

st.markdown(
    """

# ESTE ARQUIVO DEVE SER APENAS UMA FORMA DE ANOTAÇÃO E NÃO DEVE ESTAR NA APRESENTAÇÃO FINAL

Nesse documento será discutido os fazeres, não fazeres, objetivos e metas para a apresentação da disciplina PISI 3, no dia 8 de março de 2023. Como tivemos pouco progresso desde a última apresentação, temos pouco tempo para realizar as implementações e tomar as decisões mais importantes.

## Streamlit e a análise dos dados

Há algumas analises que ainda podemos realizar nos dados. Estas são importantes pois dão um contexto melhor do funcionamento da indústria. Além disso, há um esforço inicial para analise dos dados *após* estarem dispostos em um grafo. Esse esforço consiste de uma série de funcionalidades gráficas que permitirão a observação do grafo. Futuramente, podemos utilizar métricas como Centrality Analysis, Community Detection, Connectivity Analysis, Patter Matching, entre outros, para obter informações a respeito do grafo, mas estas estão fora do escopo no momento e só deverão ser pensadas caso tenhamos tempo sobrando.  

* Análise de filmes baseada em categoria de orçamento (grande, médio e baixo orçamento)
	* Apresentar a quantidade de filmes de cada categoria por ano
	* Visualizar o ROE médio de cada categoria
	* Ferramenta para visualizar o ROE de cada filme individualmente
* Visualização de um grafo com as ligações entre os filmes
	* O grafo deve ter opção para filtrar as conexões por categoria(gênero, diretor, keywords, etc).
	* O grafo deve ter opção para manipular a quantidade de vértices mostrados.
	* O grafo *pode* ter uma função para você ir adicionando os filmes que você quiser nele.

Também é importante lembrar que todo nosso processo deve ser documentado no streamlit, pois este é essencialmente o veículo principal que teremos para mostrar o que estamos fazendo durante a apresentação.

* Documentar todo o processo de tratamento de dados, análise dos dados e machine learning.
	* Adicionar imagens
	* Adicionar formulação matemática e explicação dos algoritmos utilizados
	* Descrever o metodo utilizado na concepção do algoritmo de machine learning

## Machine Learning

Nossa **prioridade** agora é dispormos nossos dados em um grafo. Isso é a tarefa que requer mais complexidade, mas que a implementação não é tão difícil. Ainda assim, esta é a etapa que permitirá que possamos realizar todas as outras, justificando sua importância. Também vale observar o que foi realizado em [[Processo de concepção do algoritmo de ML]], pois será de grande utilidade na apresentação.

* Criação do grafo
	* Adicionar os vértices
	* Adicionar as arestas
	* Exportar o grafo para que possamos plotar e desenvolver funcionalidades do streamlit mais facilmente 

Após a discussão que tivemos no dia 02/03/2023, decidimos que iremos utilizar a biblioteca Node2Vec para transformar o grafo em algo plotável em duas dimensões, e depois seguiremos com a clusterização utilizando K-means. Essa etapa não deve nos exigir um grande tempo de implementação, mas ela será um importante na etapa de criação de uma possível API que realize as operações de recomendação no aplicativo.

* Aplicar algoritmo Node2Vec
* Aplicar um algoritmo de clustering(k-means) para criarmos o modelo de previsão em si
	* Exportar o modelo para que possamos utiliza-lo futuramente
* Estudar implementação de uma API que possa fazer as recomendações

## Aplicativo

#### ATUALIZAÇÃO: O APLICATIVO AGORA SERÁ PARA O DIA 09-03-2023

Em termos de aplicativo, teremos um foco em entregar funcionalidades. Talvez isso venha em detrimento da beleza do aplicativo, mas no curto prazo que temos, é necessário para que sejamos capazes de entregar tudo o que planejamos. Com as funcionalidade de pesquisa e login prontas, nossa proxima etapa é criar um banco de dados para armazenar os filmes que o usuário favoritou. Em termos de UI, isso deve ser feito de forma simples, mas que garanta a funcionalidade. Na tela principal, também iniciaremos nossos esforços em fazer o Card de recomendações

* Criar banco de dados no firebase.
	* O banco de dados precisa armazenar o id de todos os filmes que um usuário possui.
* Fazer o botão de favoritos efetivamente adicionar um filme ao banco de dados
* Criar a tela de favoritos
	* Deve ser capaz de mostrar o título do filme e imagem 
* Criar Card do tinder na tela inicial

Como apontado por Lucas, não poderemos realizar login com o Google caso as chaves SHA não estejam configuradas, então tornou-se uma urgência adicionar todas as chaves de todos os membros do grupo para garantir que a totalidade dos membros possa trabalhar tranquilamente.

* Configurar chaves SHA para que todos os membros do grupo sejam capazes de realizar login no ambiente de desenvolvimento.

## Artigo

Na gelareira.

## Roteiro da apresentação

A apresentação será feita mostrando a documentação que fizemos das etapas do processo. Segue abaixo a estrutura da apresentação como uma forma de melhor visualizarmos o que será dito:

* Mostrar novas analises feitas nos dados
* Processo de criação do grafo
* Visualização do grafo no streamlit
* Analise do grafo (se possível)
* Processo de concepção do algoritmo de ML
* Mostrar implementação do algoritmo Node2Vec (se pronto)
* Mostrar implementação do algoritmo de clustering (se pronto)

No dia seguinte, na disciplina de DSI:

* Showcase do App
	* Tela de login
	* Navegação na tela principal
	* Card do Tinder
	* Barra de busca
	* Tela de detalhes de um filme
	* Adicionando um filme aos favoritos
	* Tela de favoritos
    """
)