#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#, utilizando as seguintes fórmulas: Para homens: (72.7h) - 58 Para mulheres: (62.1h) - 44.7

altura = float(input('Informe a sua altura: '))
peso_idealh = (72.7 * altura) - 58
peso_idealm = (62.1 * altura) - 44.7
print(f'Com uma altura de {altura} seu peso ideal caso você seja homem é {peso_idealh}')
print(f'Com uma altura de {altura} seu peso ideal caso você seja mulher é de {peso_idealm}')
