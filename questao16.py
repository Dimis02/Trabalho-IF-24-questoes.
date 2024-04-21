#Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: 𝐴 = (𝑏𝑎𝑠𝑒𝑚𝑎𝑖𝑜𝑟+𝑏𝑎𝑠𝑒𝑚𝑒𝑛𝑜𝑟∗𝑎𝑙𝑡𝑢𝑟𝑎 2 , 
#lembre-se que a base maior e a base menor devem ser  números maiores que zero.

basemaior= float(input('Digite o valor da base maior:'))
basemenor= float(input('Digite o valor da base menor:'))
altura=  float(input('Digite a altura:'))

conta= ((basemaior+basemenor)*altura) /2

if basemaior<=0 and basemenor <=0:
    print('As bases devem ter valor maior que zero')
else:
    print(f'A aréa do trapesio é {conta}')