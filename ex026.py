num1 = int(input('Informe um número inteiro: '))
num2 = int(input('Informe o segundo número inteiro: '))
num3 = int(input('Informe o terceiro número inteiro: '))
if num1 > num2 > num3:
    print(f'O número {num1} é o maior dentre os citados.')
elif num1 > num3 > num2:
    print(f'O número {num1} é o maior dentre os citados.')
elif num2 > num1 > num3:
    print(f'O número {num2} é o maior dentre os citados.')
elif num2 > num3 > num1:
    print(f'O número {num2} é o maior dentre os citados.')
elif num3 > num1 > num2:
    print(f'O número {num3} é o maior dentre os citados.')
elif num3 > num2 > num1:
    print(f'O número {num3} é o maior dentre os citados.')