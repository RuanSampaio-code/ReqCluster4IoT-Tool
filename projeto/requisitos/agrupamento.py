
import numpy as np
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import pdist, squareform
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram, fcluster
import pandas as pd
import os



def calculate_dissimilarity_matrix(data, metric='euclidean'):
    """
    Calcula a matriz de dissimilaridade usando uma métrica especificada.
    :param data: array-like, lista de vetores.
    :param metric: string, métrica de dissimilaridade ('euclidean', 'cosine', 'manhattan', etc.).
    :return: matriz de dissimilaridade.
    """
    return squareform(pdist(data, metric=metric))

def filter_elements_by_smallest_values(list1, list2, num_smallest=1):
    # Convert lists to numpy arrays for easier manipulation
    array1 = np.array(list1)
    array2 = np.array(list2)
    num_smallest=int(len(list1)/2)
    # Get the indices of the smallest values in list2
    smallest_indices = np.argsort(array2)[:num_smallest]
    
    # Exclude the elements in array1 that correspond to these indices
    filtered_array1 = np.delete(array1, smallest_indices)
    
    return filtered_array1.tolist()
def calculate_silhouette_score(data, num_clusters, Z):
    cluster_labels = fcluster(Z, num_clusters, criterion='maxclust')
    return silhouette_score(data, cluster_labels)

def find_clusters_by_distance(data,Z, num_candidates=10):
    retorno = []
    distances = Z[:, 2]
    differentials = np.diff(distances)
    sorted_indices = np.argsort(differentials)[::-1]
    top_n = num_candidates
    largest_gaps_indices = sorted_indices[:top_n]

    num_clusters = [len(np.unique(fcluster(Z, t = distances[indice]+0.0001, criterion='distance'))) for indice in largest_gaps_indices]
    num_clusters = filter_elements_by_smallest_values(num_clusters,[calculate_silhouette_score(data,t,Z) for t in num_clusters])

    return num_clusters

def group_elements(group_list, element_list):
    grouped_data = {}

    for idx, group in enumerate(group_list):
        element = element_list[idx]
        if group not in grouped_data:
            grouped_data[group] = []
        grouped_data[group].append(element)

    return grouped_data

seed_topics = {"services": ["service", "services", "application, applications", "comput", "computing", "computation", "process", "processing", "processes", "capabl", "capabilities", "capability", "capable", "The value of this contribution comes from articulating the importance of acknowledging the IoT services as value-creating business enablers", "Well-designed services can have pronounced implications for individuals and on a societal level"],

"standardised_technologies": ["technologies", "technology", "technological", "protocol", "protocols", "standard", "standardised", "standardisation", "infrastructur", "infrastructure", "infrastructural", "interfac", "interface", "interfacing", "software", "softwares","The addressing scheme, agreed protocol, architecture, intelligent interfaces and enabling ICT are all related to standardised technologies"],

"ubiquitous": ["worldwide", "ubiquitous", "ubiquitously", "pervas", "pervasive", "ubiqu", "ubiquity", "It is described with terms such as information network, network infrastructure, real-time, pervasive", "anyone, anything, anywhere and anytime", "It is enough to have the ability to connect to the network; it is not necessary to be online all the time"],

"unique": ["uniquely", "unique", "identifiable", "identifier", "identify", "identification", "identity", "identities" "use", "using", "used", "useful", "entity", "entities", "environment", "environments", "based", "enable", "enables", "enabling", "enabled", "provide", "provided", "provider", "including", "includes", "include", "management", "manager", "managing", ". Each physical or virtual thing in the IoT needs to be uniquely addressable", "automatic identification", "clearly identifiable", "intelligent identifying"],

"things": ["things", "Virtual Thing", "device", "devices" "virtual", "virtually", "sensing", "sense", "sensor", "sensors", "actuator", "actuators", "actuating", "digital", "smart object", "embedded electronics", "microcomputer", "sensing object", "object", "physical", "physically", "An object refers to the product to which things are attached or embedded", "connected objects that can sense, actuate, and interact with other objects, systems, or people", "the device must have a processing unit, power source, sensor/actuator, network connection, and a tag/address", "Tags,  sensors,  actuators,  and  all hardware that can replace the computer, expanding the connectivity reach"],

"data": ["smart", "smartness", "intelligence", "intelligently", "data", "cloud computing", "knowledge mining", "data analytics"],

"interaction": ["enabling IoT things to be connected to the Internet or other networks", "must be a connectivity module in each IoT device as well as an appropriate communication protocol that the network and the device can both understand", "it is essential some form of connection, a network for the development of solutions, and our idea is not to limit Internet-only connectivity but to be able to cover other media", "it is  mostly  based  on  wireless  communication technologies that could be divided into Short-Range, Long-Range, and Cellular-based", "o guarantee communication:  HTTP,  XMPP,  TCP,  UDP, CoAP,  MQTT,  and  others", "To  guarantee  to understand:  JSON,  XML,  OWL,  SSN Ontology, COCI"],

"action": ["it refers to the automated actions to be taken by the device or on the device", "includes action from the stakeholders in the IoT ecosystem"],

"ecosystem": ["IoT things themselves, the protocols they use, the platforms on which they run, the communities interested in the data, as well as the goals and aims of interested parties all form the ecosystem"],

"smartness": ["It uses techniques from artificial intelligence,   machine   learning,   neural networking, and fuzzy logic to deal with the data"],

"environment": ["The  problem  and  the  solution  are embedded in a domain, an environment, or a context.This facet seeks to represent such an environment and how the context information can influence its use", "Technologies  like  IoT,  cloud,  smart  objects, middleware’s,  Wireless  Sensor  Networks, Vehicular Ad-hoc Networks, edge computing, artificial  intelligence,  machine  learning,  data mining can be employed on these systems. "],

"heterogeneity": ["The Internet of Things is expected to be made up of heterogeneous devices, working on different platforms on different networks", "must be able to connect, exchange, and present data in a coordinated manner based on a common reference model"]}

distance_metrics = [
        'euclidean',        # Distância Euclidiana
        'cosine',           # Distância de Cosseno
    ]

linkage_methods = [
    'single',    # Single Linkage
    'complete',  # Complete Linkage
    'average',   # Average Linkage
    'weighted',  # Weighted Linkage
    'centroid',  # Centroid Linkage
    'median',    # Median Linkage
    'ward'       # Ward Linkage
]


def agrupamento(requisitos,indices):

     # Obtém o diretório atual onde o script está sendo executado
    diretorio_atual = os.getcwd()

    # Nome da pasta que está na mesma raiz
    nome_da_pasta = "/projeto/requisitos/modelo_similaridade"

    # Constrói o caminho completo adicionando o nome da pasta
    model_path = os.path.join(diretorio_atual, nome_da_pasta)




    from sentence_transformers import SentenceTransformer
    trained_model = SentenceTransformer(model_path)
    data = trained_model.encode(requisitos)
    print(len(data))
    metricas = []
    metodos = []
    qtde_grupos_encontrados = []
    scores = []
    for metric in distance_metrics:
        dissimilarity_matrix = calculate_dissimilarity_matrix(data, metric=metric)
        print(dissimilarity_matrix)
        for method in linkage_methods:
            try:
                Z = linkage(dissimilarity_matrix, method=method)
                candidates = find_clusters_by_distance(data,Z)
                
                best_score = -1
                best_n_clusters = None
                for n_clusters in candidates:
                    score = calculate_silhouette_score(data, n_clusters, Z)
                    if score > best_score:
                        best_score = score
                        best_n_clusters = n_clusters
                metricas.append(metric)
                metodos.append(method)
                scores.append(best_score)
                qtde_grupos_encontrados.append(best_n_clusters)
                cluster_labels = fcluster(Z, best_n_clusters, criterion='maxclust')
                centroides = calcular_centroides(data,cluster_labels)
                distancias = calcular_distancias(data,centroides)

            except Exception as e:
                print(e)
                
                continue
    dados= {
        'metric': metricas,
        'method': metodos,
        'c_cluster': qtde_grupos_encontrados,
        'scores': scores
    }

    df = pd.DataFrame(dados)
    ocorrencias = df.groupby(['method', 'metric']).size().reset_index(name='ocorrencia')
    media_metricas_ordenado = df.sort_values(by=['scores','c_cluster'], ascending=False).reset_index(drop=True)[:1]
    print(media_metricas_ordenado)
    metric = media_metricas_ordenado["metric"][0]
    method = media_metricas_ordenado["method"][0]
    qtde_cluster = media_metricas_ordenado["c_cluster"][0]
    dissimilarity_matrix = calculate_dissimilarity_matrix(data, metric=metric)
    Z = linkage(dissimilarity_matrix, method=method)
    cluster_labels = fcluster(Z, qtde_cluster, criterion='maxclust')

    documentos = group_elements(cluster_labels,indices)
    

    import gensim
    from gensim import corpora
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    import string
    import nltk
    import numpy as np
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')

    def preprocess(text):
        stop_words = set(stopwords.words('english'))
        text = text.lower()  # Converter para minúsculas
        tokens = word_tokenize(text)  # Tokenizar
        tokens = [word for word in tokens if word not in stop_words and word not in string.punctuation]  # Remover stopwords e pontuação
        return tokens

    # Pré-processando os documentos
    processed_docs = [preprocess(" ".join(doc)) for doc in documentos.values()]
    # Criando o dicionário
    dictionary = corpora.Dictionary(processed_docs)

    # Criando o corpus
    corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

    # Ajustando parâmetros de alpha e eta
    lda_model = gensim.models.LdaModel(
        corpus,
        num_topics=5,
        id2word=dictionary,
        passes=50,
        random_state=42
    )

    # Exibindo os tópicos

    topics = lda_model.print_topics(num_words=20)
    lista_topicos = []
    # Atribuindo tópicos aos documentos
    for doc in processed_docs:
        bow = dictionary.doc2bow(doc)
        topic_probabilities = lda_model[bow]
        lista_topicos.append(topic_probabilities[0][0])

    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.feature_extraction.text import CountVectorizer
    import nltk
    from nltk.corpus import stopwords
    from sentence_transformers import SentenceTransformer
    # Função para calcular a similaridade de cosseno
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Ou qualquer modelo que você preferir

    # Função para calcular a similaridade de cosseno
    def get_cosine_similarity(vec1, vec2):
        return cosine_similarity([vec1], [vec2])[0][0]

    # Função para gerar embeddings dos tópicos
    def get_embedding_for_topic(words, model):
        return model.encode(' '.join(words))  # Gera o embedding do texto

    # Vetores dos seed_topics
    seed_topic_vectors = {key: get_embedding_for_topic(words, model) for key, words in seed_topics.items()}

    # Supondo que seed_topic_vectors seja um dicionário de seed_topics com seus vetores correspondentes
    used_seed_topics = set()  # Conjunto para armazenar os seed_topics já usados

    for topic_id, topic in topics:
        topic_words = topic.split(" + ")
        topic_words = [word.split('*')[1].strip('"') for word in topic_words]  # Extrair as palavras
        topic_vector = get_embedding_for_topic(topic_words, model)
        
        # Comparar com os seed_topics
        similarities = {key: get_cosine_similarity(topic_vector, seed_vector) 
                        for key, seed_vector in seed_topic_vectors.items() if key not in used_seed_topics}
        
        # Verificar se há seed_topics restantes para comparar
        if similarities:
            # Encontrar o seed_topic mais próximo (não usado)
            most_similar_topic = max(similarities, key=similarities.get)
            
            # Marcar o seed_topic como usado
            used_seed_topics.add(most_similar_topic)
            for topico in lista_topicos:
                if topico==topic_id:
                    indice = lista_topicos.index(topic_id)
                    lista_topicos.pop(indice)
                    lista_topicos.insert(indice, most_similar_topic)

        from collections import defaultdict
        def processar_topicos(lista_topicos, documentos):
            # Dicionário para contar a ocorrência de cada tópico
            contador_topicos = defaultdict(int)
            lista_topicos_unicos = []

            for topico in lista_topicos:
                # Incrementa o contador para o tópico atual
                contador_topicos[topico] += 1

                # Se o tópico já apareceu antes, adiciona um sufixo numérico
                if contador_topicos[topico] > 1:
                    topico_renomeado = f"{topico}-{contador_topicos[topico] - 1}"
                else:
                    topico_renomeado = topico

                lista_topicos_unicos.append(topico_renomeado)
            
            # Retorna um dicionário com os tópicos renomeados e os documentos correspondentes
            return dict(zip(lista_topicos_unicos, documentos.values()))
    print(documentos.keys())
    return processar_topicos(lista_topicos, documentos)

    