# import pickle
# valor = 123
# arquivo = "binário"
# with open(arquivo,"wb") as arq:
#   pickle.dump(valor, arq)
# print("Gravado")

# import pickle
# compras = []
# total = int(input("Quantos produtos vai cadastrar? "))
# for i in range(total):
#     compras.append({})
#     compras[i]["produto"] = input("Nome do produto: ")
#     compras[i]["quantidade"] = int(input("Quantos? "))


# with open("compras.txt", "w") as arq:
#     for i in compras:
#         arq.write(i["produto"] +" "+ str(i["quantidade"])+ "\n")

# nomearquivobin = "arquivobinario"
# with open("arquivobinario","wb")as arqbin:
#     pickle.dump(compras,arqbin)

# import pickle
# arquivo = "compras.txt"
# with open(arquivo,"rb") as arquivo:
#     n = pickle.load (arquivo)
#     print(n)
#     print(type(n))

# leitura="questao04.txt"
# lista =[]
# def lendo (leitura, lista):
#     with open (leitura,"r") as arq:
#         j=0
#         for i in arq:
#             lista.append({})
#             aux = i.split()
#             lista[j]["produto"] =aux[0]
#             lista[j]["total"] = int(aux[1])
#             j+=1
            
# lendo (leitura,lista)
# print(lista)

#questão 7

# entrada = int(input("Digite o valor inicial: "))
# valor = entrada
# cem = valor//100
# if cem !=0:
#     valor = valor - (100*cem)

# cinquenta = valor // 50
# if cinquenta != 0:
#     valor = valor - (50*cinquenta)

# vinte = valor // 20
# if vinte != 0:
#     valor = valor - (20*vinte)

# dez = valor // 10
# if dez != 0:
#     valor = valor - (10*dez)

# cinco = valor // 5

# dois = valor % 2
# if cinco != 0:
#     valor = valor - (5*cinco)
# if dois != 0:
#     valor = valor - (2*dois)
# um = valor
# if um < 0:
#     um = 0


# saida=[cem, cinquenta, vinte, dez, cinco, dois, um]

# with open("notas.txt", "w") as arq:
#     for i in saida:
#         arq.write(str(i)+"\n")

# questao 8

numero = int(input("Insira um número: "))

for i in range(1, numero + 1):
    for j in range(1, i+ 1):
        print(str(j), end=" ")
    print()

