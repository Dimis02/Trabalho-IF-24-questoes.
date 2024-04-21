#Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima:
# “Empréstimo não concedido”, caso contrário imprima: “Empréstimo concedido”.

salario= float(input('Digite o seu salario:'))
parcela= float(input('Digite o valor da parcela:'))

conta= (salario*20) /100

if parcela>conta:
    print('empréstimo não concendido')
else:
    print('Empréstimo concendido')