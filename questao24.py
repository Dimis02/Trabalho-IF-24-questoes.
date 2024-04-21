#A tarifas de certo parque de estacionamento são as seguintes:
#a. 1ª e 2ª hora – R$ 1,00 cada
#c. 5ª hora e seguintes R$ 2,00 cada
#O numero de horas a pagar é sempre inteiro arredondado por excesso. Deste modo,
#quem estacionar durante 61 minutos pagará por duas horas, que é o mesmo que
#pagaria se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e
#partida são apresentados na foram de pares de inteiros, representando horas e
#minutos. Por exemplo, o par 12 50 representará “dez para a uma da tarde”. Pretendese criar um programa que, lidos pelo teclado
#s momento de chegada e de partida,
#escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chega e a
#partida se dão com intervalor não superior a 24 horas. Portanto, se uma dada hora de
#chegada for superior à partida, isso não é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.

chegada = input("Digite o momento de chegada (hh:mm): ").split(":")
partida = input("Digite o momento de partida (hh:mm): ").split(":")

# Calcula o tempo total em minutos
tempo_chegada = int(chegada[0]) * 60 + int(chegada[1])
tempo_partida = int(partida[0]) * 60 + int(partida[1])
tempo_total = tempo_partida - tempo_chegada

horas_estacionadas = -(-tempo_total // 60)  

if horas_estacionadas <= 2:
    preco = horas_estacionadas * 1
elif horas_estacionadas <= 4:
    preco = 2 * 1 + (horas_estacionadas - 2) * 1.4
else:
    preco = 2 * 1 + 2 * 1.4 + (horas_estacionadas - 4) * 2

print(f"O preço cobrado pelo estacionamento é R${preco:.2f}.")