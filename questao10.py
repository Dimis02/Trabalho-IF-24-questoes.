#Escreva um programa que leia um número inteiro maior do que zera e devolva, na tela, a soma de todos os seus algarismos. 
#Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará 
#com a mensagem “Número inválido”.

numero = int(input("Digite um número inteiro maior que zero: "))

if numero <= 0:
    print("Número inválido")
else:
    soma = sum(int(digito) for digito in str(numero))
    print("A soma dos algarismos do número é:", soma)