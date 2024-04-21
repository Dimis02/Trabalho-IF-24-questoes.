#. Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o número ao quadrado.

import math

numero = float(input("Digite um número real: "))

if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é:", raiz_quadrada)
else:
    numero_quadrado = numero ** 2
    print("O número", numero, "ao quadrado é:", numero_quadrado)