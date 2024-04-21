# Ler as notas do trabalho de laboratório, avaliação semestral e exame final
lab = float(input("Digite a nota do trabalho de laboratório (0 a 10): "))
av_semestral = float(input("Digite a nota da avaliação semestral (0 a 10): "))
ex_final = float(input("Digite a nota do exame final (0 a 10): "))


media = (lab * 2 + av_semestral * 3 + ex_final * 5) / 10


if media < 3:
    situacao = "reprovado"
elif media < 5:
    situacao = "em recuperação"
else:
    situacao = "aprovado"


print("A média do aluno é:", media)
print("O aluno está", situacao)