#Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.

n1= float(input('Digite um  numero:'))
n2= float(input('Digite um numero:'))

calculo= n1-n2
calculo2= n2-n1

if n1>n2:
    maior=n1
    diferenca= n1-n2
elif n2>n1:
    maior=n2
    diferenca= n2-n1
else: print('os numeros sao iguais')

print(f' O numero é {maior} é maior ')
print(f'A diferença entre eles é de {diferenca}')