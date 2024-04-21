#Faça um programa para verificar se um determinado número inteiro é divisível por 3 ou por 5, mas não simultaneamente pelos dois.


numero = int(input("Digite um número inteiro: "))


if numero % 3 == 0 and numero % 5 == 0:
    print("O número é divisível por 3 e por 5 ao mesmo tempo.")

elif numero % 3 == 0:
    print("O número é divisível apenas por 3.")

elif numero % 5 == 0:
    print("O número é divisível apenas por 5.")
    
else:
    print("O número não é divisível por 3 nem por 5.")