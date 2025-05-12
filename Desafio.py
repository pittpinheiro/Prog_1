
contador = 0
primos = []
valor = 2
def numeros_primos(n):
    divisoes = 0
    for i in range(1, n+1):
        if valor%i == 0:
            divisoes += 1
    if divisoes ==2:
        return True
    return False

numero = int(input("Insira o valor da quantidade: "))
while contador < numero:
    if numeros_primos(valor) == True:
        primos.append(valor)
        contador +=1
    valor +=1

print(primos)

with open("primos.txt", "w") as arquivo:
    for i in primos:
        arquivo.write(str(i) + " ")

