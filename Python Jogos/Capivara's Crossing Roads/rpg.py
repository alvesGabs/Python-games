#Sistema para conversão de moedas do nosso rpg!
#Digite em minúsculo todas as palavras: cobre, prata e ouro 

tipo = input("cobre, prata e ouro. Quais dessas moedas você busca fazer a conversão?  ")
numeros = int(input("Quantas são?  "))

#Conversão do cobre
CuAg = int(numeros / 100)

#Desnecessário a do ouro

#Conversão da prata
AgCu = int(numeros * 100)
AgAu = (numeros / 100)

#Conversão do ouro
AuCu = (numeros * 10000)
AuAg = (numeros * 100)

match tipo:
    case "cobre":
        print(f"Para moedas de prata ficou: {CuAg}")
    case "prata":
        print(f"Para moedas de cobre ficou: {AgCu} e para moedas de ouro: {AgAu}")
    case "ouro":
        print(f"Para moedas de cobre ficou: {AuCu} e para moedas de prata {AuAg}")

if [CuAg, AgCu, AgAu, AuCu, AuAg, ]is not int:
    print("Não conseguimos fazer este processo! ")