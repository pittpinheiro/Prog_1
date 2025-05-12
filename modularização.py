# n = int(input())
# fatorial = 1
# c = 1

# while c <= n:
#     fatorial = fatorial * c
#     c = c+1
# print(n,"! = ",fatorial)

# n = int(input())
# def fatorial(numero):
#     fatorial = 1
#     c = 1
#     while c <= numero:
#         fatorial = fatorial * c
#         c = c+1
#     return fatorial

# resposta = fatorial(n)

# print(n,"! = ",resposta)

#Questão 1

# def arrednd_baixo(valor):
#     arred = int(valor)
#     return arred

# def arrednd_cima(valor):
#     if (valor - valor//1) == 0:
#         return int(valor)
#     else:
#         return int((valor+1)//1)
        
    
# def arrednd_padrao(valor):
#     if (valor - valor//1) >= 0.5:
#         return int((valor//1) + 1)
#     else:
#         return int(valor)

# numero = float(input("Insira valor: "))

# resposta_baixo = arrednd_baixo(numero)
# print(resposta_baixo)
# resposta_cima = arrednd_cima(numero)
# print(resposta_cima)
# resposta_normal = arrednd_padrao(numero)
# print(resposta_normal)

# Questão 2

# def tamanho(palavrinha,palavrona):
#     medicao_inha = len(palavrinha)
#     medicao_ona = len(palavrona)

#     if medicao_inha > medicao_ona:
#         return palavrinha
#     if medicao_ona > medicao_inha:
#         return palavrona
#     if medicao_inha == medicao_ona:
#         return palavrinha

# palavra1 = input("Insira uma palavra: ")
# palavra2 = input("Insira uma outra palavra: ")

# resposta = tamanho(palavra1, palavra2)

# print(resposta)

# Questão 3

def fatorial(numero):
    fatorial = 1
    c = 1
    while c <= numero:
        fatorial = fatorial * c
        c = c+1
    return fatorial

numero1 = int(input())
operacao1 = input("[+] soma, [-] subtração, [*] multiplicação ou [/] divisão: ")
numero2 = int(input())

def operacao(numero1,numero2):
    if operacao1 == "+":
        soma = fatorial(numero1) + fatorial(numero2)
        return soma
    if operacao1 == "-":
        if fatorial(numero1) > fatorial(numero2):
            diferenca = fatorial(numero1) - fatorial(numero2)
            return diferenca
        else:
            diferenca = fatorial(numero2) - fatorial(numero1)
            return diferenca
    if operacao1 == "*":
        multi = fatorial(numero1) * fatorial(numero2)
        return multi
    if operacao1 == "/":
        if (fatorial(numero1) > fatorial(numero2)) and fatorial(numero2) != 0:
            divisao = fatorial(numero1) / fatorial(numero2)
            return int(divisao)
        elif (fatorial(numero2) > fatorial(numero1)) and fatorial(numero1) != 0:
            divisao = fatorial(numero2) / fatorial(numero1)
            return int(diferenca)

resultado = operacao(numero1,numero2)
print(resultado)