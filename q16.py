area = float(input('Qual é o tamanho em metros quadrados da área a ser pintada? '))
litros = float(area/3)
latas = float(litros/18)
latasArredondado = round(latas + .49)
precoTotal = float(latasArredondado * 80)


print('Quantidades de latas: ', latasArredondado, 'unidade(s)')
print('Preço total: R$ ', precoTotal)

