# lista = "compras.txt"

# with open(lista,"w") as arquivo:
#     item = input("Nome de um item de compras: ")
#     while item != "fim":
#         arquivo.write(item+"\n")
#         item = input("Nome de um item de compras: ")

# with open("compras.txt", "r") as arquivo:
#     palavras = 0
#     for i in arquivo:
#         print(i)
#         palavras += 1
#     print(f"A quantidade de itens da lista é {palavras}")

palavras = "palavras.txt"

with open(palavras,"w") as arquivo:
    palavarinhas = input("Insira uma palavra: ")
    while palavarinhas != "fim":
        arquivo.write(palavarinhas+"\n")
        palavarinhas = input("Insira uma palavra: ")


with open("palavras.txt","r") as arquivo:
    conteudo = arquivo.readlines()
    vogal = ["a","e","i","o","u"]
    vogais_qntdade = 0
    for i in conteudo:
        for j in i:
            if j in vogal:
                vogais_qntdade = vogais_qntdade + 1
    print(vogais_qntdade)


