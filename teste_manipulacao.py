# Leitura de arquivo
# arquivo = open("teste.txt","r")
# conteudo = arquivo.read() #retorna string
# print(conteudo)

# arquivo.close()

# Leitura de arquivo linha por linha
# arquivo = open("teste.txt","r")
# conteudo = arquivo.readline()
# while conteudo:
#     print(conteudo.rstrip())
#     conteudo = arquivo.readline() #retorna uma linha na forma de string

# arquivo.close()

# Leitura de arquivo linha por linha contando os caractéres das palavras

# arquivo = open("teste.txt","r")
# conteudo = arquivo.readline()
# while conteudo:
#     conteudo = conteudo.rstrip()
#     quantidade_letras = len(conteudo.rstrip())
#     print(conteudo,quantidade_letras)
#     conteudo = arquivo.readline() #retorna uma linha na forma de string

# arquivo.close()

# Maneira de abrir o arquivo chamado de "with" que não precisa de "arquivo.close()" ao final

# with open("teste.txt","r") as arquivo:
#     conteudo = arquivo.readline()
#     while conteudo:
#         conteudo = conteudo.rstrip()
#         quantidade_letras = len(conteudo.rstrip())
#         print(conteudo,quantidade_letras)
#         conteudo = arquivo.readline() #retorna uma linha na forma de string

# Outra maneira de fazer o código acima

# with open("teste.txt","r") as arquivo:
#     for i in arquivo:
#         print(i)

# Armazenar em lista com os itens do arquivo

# with open("numero.txt") as arquivo:
#     linha = arquivo.readline()
#     print(linha)
#     print(type(linha))
#     lista1 = linha.split()
#     print(lista1)
#     lista1 = list(map(int,lista1))
#     print(lista1)

#     linha2 = arquivo.readline()
#     lista2 = list(map(int,linha2.split()))
#     print(lista2)

#     for i in range(len(lista2)):
#         print(lista1[i])

#Outra maneira de puxar todos os valores, porém as linhas precisam ter apenas UM número por linha

with open ("numero.txt") as arquivo:
    conteudo = arquivo.readline()
    lista = list(map(int,conteudo.split()))
    for i in arquivo:
        lista.append(int(i)) #Torna os valores em inteiro, só serve para quando ter UM valor por linha
    print(lista)
