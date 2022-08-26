#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
#Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê: salário bruto.
#quanto pagou ao INSS. quanto pagou ao sindicato. o salário líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
ganha_hora = float(input('Quanto você ganha por hora? '))
trab_mes = float(input('Quantas horas você trabalha por mês? '))
salario_bruto = ganha_hora * trab_mes
imposto_renda = salario_bruto * (11/100)
inss = salario_bruto * (8/100)
sindicato = salario_bruto * (5/100)
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)
print(f'Salário bruto: R${salario_bruto}\nimposto de renda: R${imposto_renda}\ninss: R${inss}\nsindicato: R${sindicato}\nValor liquido: R${salario_liquido} ')