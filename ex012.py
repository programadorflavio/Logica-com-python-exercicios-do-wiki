"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
alt = float(input('Informe sua altura: '))
pid = (72.7 * alt) - 58
print(f'Seu peso ideal é {pid}')