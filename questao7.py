#Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem “Números iguais”.

n1= float(input('Digite um numero:'))

n2= float(input('Digite um numero:'))

if n1>n2:
    print(f'{n1} é maior')
elif n2>n1:
    print(f'{n2} é maior')
else:
    print('os numero sao iguais')