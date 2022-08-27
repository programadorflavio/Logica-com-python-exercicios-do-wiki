salario = float(input('Informe o salário: '))
if salario <= 280:
    reajuste1 = (20/100) * salario
    print(f'O salário antes do reajuste; {salario}')
    print(f'O percentual aplicado foi 20%')
    print(f'O valor do aumento; {reajuste1}')
    print(f'O valor do seu salário reajustado será {salario + reajuste1}')
elif (salario > 280) and (salario < 700):
    reajuste2 = (15/100) * salario
    print(f'O salário antes do reajuste; {salario}')
    print(f'O percentual aplicado foi 15%')
    print(f'O valor do aumento; {reajuste2}')
    print(f'O valor do seu salário reajustado será {salario + reajuste2}')
elif (salario > 700) and (salario < 1500):
    reajuste3 = (10/100) * salario
    print(f'O salário anates do reajuste {salario}')
    print(f'O percentual aplicado foi 10%')
    print(f'O valor do aumento; {reajuste3}')
    print(f'O valor do seu salário reajustado será {salario + reajuste3}')
elif salario > 1500:
    reajuste4 = (5/100) * salario
    print(f'O salário antes do reajuste {salario}')
    print(f'O percentual aplicado foi 5%')
    print(f'O valor do aumento {reajuste4}')
    print(f'O valor do seu salário reajustadoo será {salario + reajuste4}')
