# questão 4

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

# # questão 5
# contador = 0

# for i in lista:
#    contador += i["total"]

# print("total: ", contador)


#questão do pedror 01

# leitura = "questao6.txt"

# with open("questao6.txt","r") as arquivo:
#    linha = arquivo.readline()
#    contador = 0
#    while linha:
#       linha = linha.rstrip()
#       contador+=1
#       linha = arquivo.readline()
#    print(contador)

# questao 6

leitura = "questao6.txt"

with open("questao6.txt","r") as arquivo:

   ...


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
with open("piramide.txt","w+") as arquivo:
   for i in range(1, numero + 1):
      for j in range(1, i+ 1):
         arquivo.write(str(j) + " ")
      arquivo.write("\n")
   
   for i in range(numero, 1, -1):
      for j in range(1,i):
         arquivo.write(str(j) + " ")
      arquivo.write("\n")
