#Faça um algoritmo que calcule a média ponderada das notas de 2 provas. 
#A primeira prova tem peso 1 e a segunda tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
#A nota para aprovação deve ser igual o superior a 70 pontos.

n1= float(input('Digite a nota 1:'))
n2= float(input('Digite a nota 2:'))

calculo= (n1*1+n2*2) /3
 
if calculo>= 7.0:
    print('Voce esta aprovado')
else:
    print('Voce esta reprovado')