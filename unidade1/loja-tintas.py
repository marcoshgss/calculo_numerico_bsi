# Faça um Programa para uma loja de tintas. 
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. MARCOS

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

# 1) comprar apenas latas de 18 litros;
# 2) comprar apenas galões de 3,6 litros;
# 3) misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

print("================ LOJA DE TINTAS ==================\n\n")
                # Pedindo o tamanho em m².
tamanhoemMetros = input("Quantos metros ou m² deseja pintar: ")
tamanhoemMetros = int(tamanhoemMetros)
litrosMetros = (tamanhoemMetros / 6) * 1.1   # O 1.1 é os 10% de folga... peguei tamanhoemMetros e dividi por 6.

latas = math.ceil(litrosMetros / 18) # o math.ceil serve para arredondar, em seguida peguei os litrosMetros e dividi por 18.
valorLata = latas * 80  # multiplicando as latas pelo o valor, no caso o R$ 80,00.

galao = math.ceil(litrosMetros / 3.6) # em seguida peguei os litrosMetros e dividi por 3.6.
valorGalao = galao * 25 # multiplicando os galões pelo o valor, no caso o R$ 25,00.

# Misturar latas e galões, de forma que o desperdício de tinta seja menor.
misturaLatas = round(litrosMetros / 18) # O comando round serve para arredondar, depois litrosMetros vai ser divido por 18
misturaGaloes = round((litrosMetros - misturaLatas * 18) / 3.6) # peguei o litrosMetros menos o misturaLatas e multipliquei por 18, em seguida peguei isso tudo e dividi por 3,6.



if ((litrosMetros - (misturaLatas * 18) % 3.6 != 0)): # Se os litrosMetros menos o misturaLatas multiplicado por 18 e o resto da divisão for diferente de zero. 
  misturaGaloes += 1  # vai somar mais um, para acrecentar os galões até chegar no que precisa.
  totaldeMistura = (misturaLatas * 80) + (misturaGaloes * 25) # Agora irei fazer o total deles, pegar o misturaLatas * 80 + misturaGaloes * 25


print(f"\nSe deseja comprar apenas latas de 18 litros, tu vai precisar de {latas} latas e vai custar R$ {valorLata:.2f}.")

print(f"\nSe deseja comprar apenas galões de 3,6 litros, tu vai precisar de {galao} galões e vai custar R$ {valorGalao:.2f}.")

print(f"\nAgora se quiser misturar latas e galões para dar o que precisar, realmente será necessário {misturaLatas} latas"
      
    f"\ne {misturaGaloes} galões e tudo isso irá custar R$ {totaldeMistura:.2f}.")