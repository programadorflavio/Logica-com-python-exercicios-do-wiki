num1 = int(input('Informe um número: '))
num2 = int(input('Informe um segundo: '))
num3 = int(input('Informe um terceiro: '))
if num1 < num2 < num3:
    print(f'A ordem decrescente {num1} e na sequência {num2} e {num3}')
elif num1 < num3 < num2:
    print(f'A ordem decrescente {num1} e na sequência {num3} e {num2}')
elif num2 < num1 < num3:
    print(f'A ordem decrescente {num2} e na sequência {num1} e {num3}')
elif num2 < num3 < num1:
    print(f'A ordem decrescente {num2} e na sequência {num3} e {num1}')
elif num3 < num1 < num2:
    print(f'A ordem decrescente {num3} e na sequência {num1} e {num2}')
elif num3 < num2 < num1:
    print(f'A ordem decrescente {num3} e na sequência {num2} e {num1}')