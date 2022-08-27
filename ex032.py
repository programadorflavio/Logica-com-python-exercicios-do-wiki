nota1 = float(input('Qual sua primeira nota: '))
nota2 = float(input('Qual sua segunda nota: '))
media = (nota1 + nota2) / 2
if (media < 10) and (9 < media):
    print(f'Aprovado média  [A], média:{media}')
elif (media < 9) and (media > 7.5):
    print(f'Aprovado média  [B], média:{media}')
elif (media > 6) and (media < 7.5):
    print(f'Aprovado média  [C], média:{media}')
elif (media > 4) and (media < 6):
    print(f'Reprovado média [D], média:{media}')
elif (media < 4) and (media >= 0):
    print(f'Reprovado média [E], média:{media}')