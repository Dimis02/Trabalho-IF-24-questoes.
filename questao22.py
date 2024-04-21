#Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado
#possui uma taxa diferente de imposto sobre o produto (MG 7%; SP 12%.; RJ 15%; MS
#8%). Faça um programa em que o usuário entre com o valor e o estado destino do
#produto e o programa retorne o preço final do produto acrescido do imposto do
#estado em que ele será vendido. Se o estado digitado não for valido, mostrar uma
#mensagem de erro.

taxa_MG = 0.07
taxa_SP = 0.12
taxa_RJ = 0.15
taxa_MS = 0.08

valor_produto = float(input("Digite o valor do produto: "))
estado_destino = input("Digite a sigla do estado destino (MG, SP, RJ, MS): ").upper()

if estado_destino == 'MG':
    preco_final = valor_produto * (1 + taxa_MG)
    print(f"O preço final do produto para o estado {estado_destino} é R${preco_final:.2f}.")
elif estado_destino == 'SP':
    preco_final = valor_produto * (1 + taxa_SP)
    print(f"O preço final do produto para o estado {estado_destino} é R${preco_final:.2f}.")
elif estado_destino == 'RJ':
    preco_final = valor_produto * (1 + taxa_RJ)
    print(f"O preço final do produto para o estado {estado_destino} é R${preco_final:.2f}.")
elif estado_destino == 'MS':
    preco_final = valor_produto * (1 + taxa_MS)
    print(f"O preço final do produto para o estado {estado_destino} é R${preco_final:.2f}.")
else:
    print("Erro: Estado destino inválido.")