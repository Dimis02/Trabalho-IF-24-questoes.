#Escreva um programa que, dada a idade de um atleta da categoria bocha rolada em
#cancha de terra, classifique-o em uma das seguintes categorias:

idade = int(input("Digite a idade do atleta: "))

if 18 <= idade <= 30:
    categoria = "Categoria Adulto"
elif 31 <= idade <= 40:
    categoria = "Categoria Sênior"
elif 41 <= idade <= 50:
    categoria = "Categoria Master"
else:
    categoria = "Categoria Não Disponível"

print(f"O atleta de {idade} anos está na {categoria}.")