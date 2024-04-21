#Faça um programa que receba dois números e mostra qual deles é o maior.

n1= float(input('Digite um numero:'))
n2= float(input('Digite um numero:'))

if n1>n2:
    print('o primeiro numero é maior', n1)
elif n1<n2:
    print('O segundo numero é maior', n2)
else: 
    print ('Os numeros sao iguais')