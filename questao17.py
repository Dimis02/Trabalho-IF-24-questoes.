print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")


opcao = int(input("Digite o número da operação desejada: "))


valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))


if opcao == 1:
    resultado = valor1 + valor2
elif opcao == 2:
    resultado = valor1 - valor2
elif opcao == 3:
    resultado = valor1 * valor2
elif opcao == 4:
    if valor2 != 0:
        resultado = valor1 / valor2
    else:
        resultado = "Erro: divisão por zero."
else:
    resultado = "Opção inválida."


print("O resultado da operação é:", resultado)