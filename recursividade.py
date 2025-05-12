#exemplo

# def soma(n):
#     if n == 1:
#         return n
#     else:
#         return n + soma(n-1)
    
# n = int(input("Insira valor: "))

# print(soma(n))

# exemplo potência

# def potencia(expoente,base):
#     if expoente == 0:
#         return 1
#     else:
#         return base * potencia(expoente -1, base)
    
# expoente = int(input("Expoente: "))
# base = int(input("Base: "))

# print(potencia(expoente,base))

#Questão 03

# def somavetor(vetor):
#     if len(vetor) == 0:
#         return 0
#     else:
#         return vetor[0] + somavetor(vetor[1:])

# vetor = [3,4,5,6,8,3]
# print(somavetor(vetor))

# #Questão 05

# def mdc(x,y):
#     if y == 0:
#         return x
#     else:
#         return mdc(y, x%y)
    
# x = int(input("Valor: "))
# y = int(input("Valor: "))

# print(mdc(x,y))

# Questão 07

# Questão 08

# def ricci(n):
#     if n == 0:
#         return 0
#     elif n ==1:
#         return 1
#     else:
#         return ricci(n-1) + ricci(n-2)

# valor1= int(input(" "))
# valor2= int(input(" "))
# quantidade= int(input(" "))

# for i in range(quantidade):
#     print(ricci(valor1))
#     valor1 += 1


# v=[3,15,70,80,150,461]
# k=int(input())
# inicio = 0
# fim = len(v)-1
# achou=False
# while inicio<=fim and not achou:
#     meio = (inicio + fim)//2
#     if v[meio] == k:
#         achou=True
#     else:
#         if k < v[meio]:
#             fim = meio-1
#         else:
#             inicio=meio+1
# print(achou,meio)

#Exercício slide

# vetor = [1,2,3,4,5]

# tamanho = int(input())
# for i in range(tamanho):
#     numero = int(input("Valor: "))
#     vetor.append(numero)

# valor = int(input("Insira valor: "))
# contador = 0
# inicio = 0
# fim = len(vetor)-1 #4
# achou=False
# while inicio<=fim and not achou:
#     meio = (inicio + fim)//2
#     if vetor[meio] == valor:
#         achou=True
#         contador += 1
#     else:
#         if valor < vetor[meio]:
#             fim = meio-1
        
#         else:
#             inicio=meio+1
            
# print(meio,contador)

# Exemplo do DeepSeek

# def soma(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return n + soma(n-1)

# print(soma(4))

# Outra questão do deepseek

# def contagem_regressiva(n):
#     if n < 0:
#         return
#     print(n)
#     contagem_regressiva(n - 1)

# contagem_regressiva(5)

# def potencia(x,n):
#     if n == 0:
#         return 1
#     else:
#         return x * potencia(x, n - 1)
    
# print(potencia(3,2))
