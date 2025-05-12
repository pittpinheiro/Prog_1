# Questao 1

# vetor =[]
# valor = 1
# while valor == 1:
#     n = int(input(""))
#     if n != -1:
#         vetor.append(n)
#     if n== -1:
#         valor = -1

# maior = 0
# menor = 10000000
# for i in range(len(vetor)):
#     if vetor[i] > maior:
#         maior = vetor[i]
# for i in range(len(vetor)):
#     if vetor[i] <= menor:
#         menor = vetor[i]

# print(vetor)

# print("Maior: ", maior)
# print("Menor: ", menor)

# Questão 1

# valor = 1

# vetor = []
# while valor != -1:
#     n = int(input(""))
#     if n != -1:
#         vetor.append(n)
#     else:
#         valor = -1

# maior = 0
# menor = 10000000
# seg_maior = 0
# seg_menor = 10000000
# for i in range(len(vetor)):
#     if vetor[i] > maior:
#         maior = vetor[i]
# for i in range(len(vetor)):
#     if vetor[i] <= menor:
#         menor = vetor[i]
# for i in range(len(vetor)):
#     if vetor[i]< seg_menor and vetor[i] > menor:
#         seg_menor = vetor[i]
# for i in range(len(vetor)):
#     if vetor[i]> seg_maior and vetor[i] < maior:
#         seg_maior = vetor[i]

# print(vetor)
# print("Menor: ", menor)
# print("Segundo menor: ", seg_menor)
# print("Maior: ",maior)
# print("Segundo maior: ",seg_maior)

# Questão 2
# soma_pos = 0
# soma_neg = 0
# vetor = []
# for i in range(10):
#     valores = int(input(""))
#     vetor.append(valores)
#     if valores >= 0:
#         soma_pos += valores
#     else:
#         soma_neg += valores

# print("Soma positivos: ",soma_pos)
# print("Soma negativos: ",soma_neg)
# print(vetor[::-1])

# # Questão 3

# vetor1 =[]
# vetor2 =[]
# soma =[]

# for i in range(5):
#     n1 = int(input(""))
#     vetor1.append(n1)
#     n2 = int(input(""))
#     vetor2.append(n2)

# for i in range(5):
#     soma1 = vetor1[i] + vetor2[i]
#     soma.append(soma1)

# print(vetor1)
# print(vetor2)
# print(soma)



# Questao 4

# vetorA=[]
# for i in range(5):
#     n = int(input(""))
#     vetorA.append(n)

# vetorB = []

# for i in range(5):
#     fat = 1
#     for i in range(2,vetorA[i]+1):
#         fat = i * fat
#     vetorB.append(fat)

# print(vetorA)
# print(vetorB)

# Questão 5

# import math

# vetor = []
# raiz = []
# for i in range(5):
#     n = int(input(""))
#     vetor.append(n)

# for i in range(len(vetor)):
#     valor = math.sqrt(vetor[i])
#     raiz.append(valor)
# print(vetor)
# print(raiz)

# Questão 6

# poltrona = ["disponivel"] * 8

# nome = input("Nome: ")
# naoatendidos = 0

# while nome != "fim":
#     lugar = int(input("Lugar: "))
#     if poltrona[lugar] == "disponivel":
#         poltrona[lugar]=nome
#     else:
#         naoatendidos += 1
#     nome = input("Nome: ")
# print(poltrona)
# print("Não atendidos: ", naoatendidos)

# Questão 7

# x = []
# y = []
# r = [0] * 10

# for i in range(5):
#     n1 = int(input(""))
#     x.append(n1)
# for i in range(5):
#     n2 = int(input(""))
#     y.append(n2)

# for i in range(5):
#     r[2*i] = x[i]
#     r[2*i+1] = y[i]

# print(x)
# print(y)
# print(r)

# Questão 8

vetor = []
for i in range(7):
    n = float(input("\n"))
    vetor.append(n)
