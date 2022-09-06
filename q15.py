print('===============================================')
print('CALCULADORA DE SALÁRIO LÍQUIDO')
print('===============================================')

valorHora=float(input('Digite o valor da sua hora trabalhada: '))
hora=float(input('Quantas horas você trabalha por mês? '))
salarioBruto=(valorHora * hora)
inss = float((salarioBruto * 8)/100)
sindicato = float((salarioBruto * 5)/100)
ir = float((salarioBruto * 11)/100)
salarioLiquido = float(salarioBruto - inss - sindicato - ir)


print('a) Seu salário bruto este mês é de: R$', salarioBruto)
print('b) Quanto pagou de INSS: R$ ', inss)
print('c) Quanto pagou ao sindicado: R$ ', sindicato)
print('d) Quanto pagou de IR: R$ ', ir)
print('e) salário líquido: R$ ', round(salarioLiquido,2))
print('===============================================')