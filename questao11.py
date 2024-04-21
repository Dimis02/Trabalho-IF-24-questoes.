#Ler um número inteiro. Se o número lido for negativo, escreva a mensagem “Número inválido”. 
#Se o numero for positivo, calcular o logaritmo deste número.

import math

n1= float(input('Digite um número inteiro:'))

if n1<0:
    print('Numero invalido')
else: 
    logaritmo= math.log(n1)
    print(f'O logaritmo de {n1} é {logaritmo}')