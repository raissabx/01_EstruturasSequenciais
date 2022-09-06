import math
print('='*14)
print('LOJA DE TINTAS')
print('='*14)

area = float(input('Qual é o tamanho em metros quadrados da área a ser pintada? '))
litros = area/6
litros_folga = litros + litros * .10
latao = litros_folga // 18
latinhas = (litros_folga - 18 * latao) / 3.6
latinhas_arredondado = math.ceil(latinhas)
preco = latao * 80 + latinhas_arredondado * 25

print ('a) Comprar apenas latas de 18 litros', math.ceil(litros/18))
print ('b) Comprar apenas galões de 3.6 litros', math.ceil(litros/3.6))
print ('Comprar latas e galões')
print ('    Latas: ', latao)
print ('    Galões: ', latinhas_arredondado)
print('='*14)