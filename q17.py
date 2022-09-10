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

print ('a) Comprar apenas latas de 18 litros: R$ ', round(math.ceil(litros/18)*80,2))
print ('b) Comprar apenas galões de 3.6 litros: R$ ', round(math.ceil(litros/3.6)*25,2))
print ('Comprar latas e galões:')
print ('    Latas: R$ ', round(latao*80,2))
print ('    Galões: R$ ', round(latinhas_arredondado*25,2))
print('='*14)