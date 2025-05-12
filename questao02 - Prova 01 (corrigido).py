#Maria Eduarda Borges Pinheiro - Questão 2

altura_geral = []
altura_mulheres = []
verdade = 0

maior = 0
menor = 50
soma_mulheres = 0
soma_geral= 0

while verdade > -1:
    altura = float(input("Altura(em metros): "))
    if altura != -1:
        altura_geral.append(altura)
        soma_geral += altura
        genero = input("f(mulher) e m(homem): ")
        if genero == "f":
            altura_mulheres.append(altura)
            soma_mulheres += altura
    else:
        verdade = -1
media_mulheres = 0
if len(altura_mulheres) == 0:
    print("")
else: 
    media_mulheres = soma_mulheres / len(altura_mulheres)
media_geral = soma_geral / len(altura_geral)

for i in range(len(altura_geral)):
    if altura_geral[i] > maior:
        maior = altura_geral[i]
    if altura_geral[i] < menor:
        menor = altura_geral[i]

print("Maior altura geral: ", maior)
print("Menor altura geral: ", menor)
if media_mulheres == 0:
    print("erro")
else:
    print("Média mulheres: ", media_mulheres)
print("Altura média geral: ", media_geral)

