#Leia a idade e o tempo de serviço de um trabalhador e escreve se ele pode ou não se aposentar.

idade= int(input('Digite sua idade:'))
tempo= float(input('Digite o tempo trabalhado:'))

if idade>=65:
    print('Você pode se aposentar')
elif tempo>= 30:
    print('Voce pode se aposentar')
elif idade==60 and tempo==25:
    print('Voce pode se aposentar')
else:
    print('Voce nao pode se aposentar')