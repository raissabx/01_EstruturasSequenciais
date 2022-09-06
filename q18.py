import math

arquivo = float(input('Tamanho do arquivo (MB): '))
velocidade = float(input('Velocidade do link de Internet (Mbps): '))
velocidade_MBs = velocidade/8
segundos = arquivo/velocidade_MBs

print('Tempo aproximado de download: ', segundos//60 , 'min', math.ceil(segundos%60), 's')