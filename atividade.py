# Questao 1

# paozinho = int(input("Qual a quantidade de pãozinhos vendidos no dia? "))
# broa = int(input("Qual a quantidade de broas vendidos no dia? "))

# total_valor = (paozinho * 0.82) + (broa * 2.5)
# poupança = total_valor * 1/10

# print(f"""
# Valor total = {total_valor}
# Para a poupança = {poupança}
# """)


# Questão 2

# hora = int(input("Insira as horas: "))
# minutos = int(input("Insira os minutos: "))

# calculo = (hora * 3600) + (minutos * 60)

# print(calculo)

# Questão 3

# valor = int(input("Insira um valor: "))

# por_cem = valor // 100
# valor = valor % 100

# por_cinquenta = valor // 50
# valor = valor % 50

# por_vinte = valor //20
# valor = valor % 20

# por_dez = valor // 10
# valor = valor % 10

# por_cinco = valor // 5
# valor = valor % 5

# por_dois = valor // 2
# valor = valor % 2

# por_um = valor // 1
# valor = valor % 1

# print(por_cem)
# print(por_cinquenta)
# print(por_vinte)
# print(por_dez)
# print(por_cinco)
# print(por_dois)
# print(por_um)

# Questao 4

# dias = int(input("Insira a quantidade de dias trabalhados: "))

# salario = dias * 90

# imposto = salario * 1/8

# liquido = salario - imposto

# print(f"""
# Dias trabalhados: {dias}
# Salário total: {salario}
# Salário com descontos: {liquido}
# """)

# Questão 5

import math

print("""
x = – b ± √Δ
      2a

Δ = b2 – 4ac
""")

a = int(input("Coloque um valor para a: "))
b = int(input("Coloque um valor para b: "))
c = int(input("Coloque um valor para c: "))

delta = math.exp2(b) - (4 * a * c)
x = ((- b) + math.sqrt(delta)) / 2 * a
y = ((- b) - math.sqrt(delta)) / 2 * a

if delta < 0:
    print("Não existe raiz.")

if delta == 0:
    if x == 0:
        print(y)
    else:
        print(x)
if delta >= 0:
    print(x,y)

# Questão 6

# pedra_estado = input("'MOLHADA' ou 'SECA'? ")
# pedra_sensacao = input("'QUENTE' ou 'FRIA'? ")
# temperatura = float(input("Temperatura da pedra: "))

# if pedra_estado == 'MOLHADA' and pedra_sensacao == 'QUENTE':
#     print("PRIMAVERA")
#     sensacao = temperatura + (temperatura * 1/10)
#     print(sensacao)
# if pedra_estado == 'MOLHADA' and pedra_sensacao == 'FRIA':
#     print("INVERNO")
#     sensacao = temperatura - (temperatura * 1/10)
#     print(sensacao)
# if pedra_estado == 'SECA' and pedra_sensacao == 'QUENTE':
#     print("VERÃO")
#     sensacao = temperatura + (temperatura * 1/20)
#     print(sensacao)
# if pedra_estado == 'SECA' and pedra_sensacao == 'FRIA':
#     print("OUTONO")
#     print(temperatura)

