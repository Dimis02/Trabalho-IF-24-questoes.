#Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre: a. O número digitado ao quadrado b. 
#A raiz quadrada do número digitado.
import math

n1= float (input('Digite um numero:'))
raiz=math.sqrt(n1)
soma1= n1**2
if n1>=0:
    print(f' O quadrado do seu número é {soma1}')
    print(f' A raiz quadrada de {n1} é {raiz}')