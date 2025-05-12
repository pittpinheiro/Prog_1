#Maria Eduarda Borges Pinheiro - Questão 1

temperaturas = []
soma = 0
maior_temp = 0
acima_media = 0
for i in range(7):
    valores = float(input("Insira temperaturas: "))
    temperaturas.append(valores)
    soma += valores

media = soma / 7

for i in range(7):
    if temperaturas[i] > media:
        acima_media +=1
    if temperaturas[i] >= maior_temp:
        maior_temp = temperaturas[i]

print("Média: ", media)
print("Dias acima da média: ", acima_media)
print("Maior temperatura: ", maior_temp)

