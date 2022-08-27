nome = str(input('Informe seu nome? '))
nota1 = float(input(f'{nome} informe sua primeira nota: '))
nota2 = float(input(f'{nome} informe sua segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'{nome} Parabéns! foi você aprovado, sua média foi {media}')
elif media < 7:
    print(f'{nome} você foi reprovado!, sua média foi {media}')
elif media == 10:
    print(f'{nome} você foi aprovado com distinção!, sua média foi {media}')