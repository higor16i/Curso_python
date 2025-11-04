import os

os.system("cls")

largura=float(input("Digite a largura do terreno em metros: "))
comprimento=float(input("Digite a altura do terreno em metros: "))
valor=float(input("Digite o valor do metro quadrado do terreno: "))

area=largura*comprimento
preco=area*valor

print(f"A area do terreno é de {area} metros quadrados.")
print(f"O preço total do terreno é de R$ {preco:.2f}.")

