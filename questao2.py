#Leia um número fornecido pelo usuário. Se esse numero for positivo, calcule a raiz quadrada do número.
#Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
import math
 
n1= float(input('Digite um número:'))

raiz= math.sqrt(n1)
calculo= n1*n1

if n1 >= 1: 
    print(f' a raiz de {n1} é {raiz} ')
else:
    print('numero invalido')