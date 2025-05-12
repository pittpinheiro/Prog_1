#INSTALE AS DEPENDENCIAS 
# pip install spacy
# python -m spacy download pt_core_news_lg

import spacy
nlp = spacy.load("pt_core_news_lg")
import math
from collections import Counter

caminho_relativo_entrada = "/insira o caminho relativo ao texto de entrada"
caminho_relativo_saida = "/insira o caminho relativo ao texto de saída"

#HELPER FUNCTIONS
def remover_stopwords_pontuacao(sentenca_tokenizada):  
       return [token.text for token in nlp(sentenca_tokenizada) if not token.is_punct and not token.is_stop]

def juntar(i, texto):
    juncao = set() 

    limite = i + 2  

    while i < limite:  
        for palavra in texto[i]:
            juncao.add(palavra)  
        i += 1  

    return list(juncao)

#MAIN FUNCTIONS
def abrir_arquivo(caminho_relativo):
    try:
        with open(caminho_relativo, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return None
    
def processar_texto(texto):
    doc = nlp(texto)
    sentencas_tokenizadas = [sent.text.strip() for sent in doc.sents]

    sentencas_limpas = []
    for sentenca in sentencas_tokenizadas:
        sentenca_limpa = remover_stopwords_pontuacao(sentenca)
        sentencas_limpas.append(sentenca_limpa)

    return (sentencas_limpas,sentencas_tokenizadas)

def similaridade_cosseno(Vetor01, Vetor02):
        
    A = Vetor01
    B = Vetor02

    numerador = 0
    denominadorA = 0
    denominadorB = 0

    for x in range(len(Vetor01)):
        numerador += A[x]*B[x]
        denominadorA += A[x] ** 2
        denominadorB += B[x] ** 2

    denominadorA = math.sqrt(denominadorA)
    denominadorB = math.sqrt(denominadorB)

    if denominadorA == 0 or denominadorB == 0:
            similaridadeAB = 0
    else:
            similaridadeAB = numerador / (denominadorA * denominadorB)

    return similaridadeAB

def concatenar(sentencas_processadas, sentencas_originais):
    limite_similaridade = 0.4

    sentenca_atual = str(sentencas_originais[0])
    resultado = []

    for indice in range(len(sentencas_processadas)-1):

        palavras_unicas_lista  = juntar(indice,sentencas_processadas) 

        representacao_vetorial01 = [0] * len(palavras_unicas_lista)
        representacao_vetorial02 = [0] * len(palavras_unicas_lista) 

        for palavra_setencas in sentencas_processadas[indice]:
            representacao_vetorial01[palavras_unicas_lista.index(palavra_setencas)] += 1

        for palavra_setencas in sentencas_processadas[indice+1]:
            representacao_vetorial02[palavras_unicas_lista.index(palavra_setencas)] += 1

        similaridade = similaridade_cosseno(representacao_vetorial01, representacao_vetorial02)

        if similaridade >= limite_similaridade:
            sentenca_atual += " " + sentencas_originais[indice + 1]
        else:
            resultado.append(sentenca_atual)
            sentenca_atual= str(sentencas_originais[indice + 1])
    
    resultado.append(sentenca_atual)

    return resultado

def pegar_topicos(texto):
    tokens_do_texto = remover_stopwords_pontuacao(texto)

    chaves = Counter(tokens_do_texto)

    chaves_frequentes =  []
    for chave in chaves:
        if chaves[chave] > 1:
            chaves_frequentes.append(chave)
    
    if chaves_frequentes:
        topicos = f"<Tópicos: {', '.join(chaves_frequentes)}>"
        return (texto, topicos)

    else:
        palavras_relevantes = []

        for token in nlp(" ".join(tokens_do_texto)):
            if token.pos_ in ["VERB","ADJ","PROPN","NOUN"]:
                palavras_relevantes.append(token.text)
        
        if palavras_relevantes and len(palavras_relevantes) > 1:
            topicos = []
            topicos.append(str(palavras_relevantes[0]))
            topicos.append(str(palavras_relevantes[1]))
            topicos_gerados = f"<Tópicos: {', '.join(topicos)}>"

            return (texto,topicos_gerados)
        else:
            topico = texto[0]
            topicos_restantes = f"<Tópicos: {', '.join(topico)}>"

            return (texto, topicos_restantes)

def criar_aquivos(lista_sentencas):
    try:
        with open(caminho_relativo_saida, "w", encoding="utf-8") as paragrafos:
            for paragrafo in lista_sentencas:
                paragrafos.write(f"{paragrafo[0]} \n")
                paragrafos.write(f"{paragrafo[1]} \n")
                paragrafos.write(f"\n")
    except FileNotFoundError:
        return print("Arquivo não encontrado.")

def start(): 
    try:
        # Nível 1
        texto = abrir_arquivo(caminho_relativo_entrada)
        texto_processado = processar_texto(texto)
        
        # Nível 2
        sentencas_concatenadas = concatenar(texto_processado[0], texto_processado[1]) 

        #Nível 3
        sentencas_completas = []
        for senteca in sentencas_concatenadas:
            texto_topico = pegar_topicos(senteca)
            sentencas_completas.append(texto_topico)
        
        criar_aquivos(sentencas_completas)

        print("Arquivo de texto processado com sucesso!")
    except Exception as e:
        print(f"Erro ao processar o texto: {e}")

start()