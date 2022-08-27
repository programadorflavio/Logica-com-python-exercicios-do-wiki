hora_valor = float(input('Qual valor da sua hora trabalhada? '))
hora_mes = float(input('Quantas horas você trabalha por mês? '))
salario_bruto = hora_mes * hora_valor
if salario_bruto <= 900:
    inss = (10/100) * salario_bruto
    fgts = (11/100) * salario_bruto
    desc = inss + fgts
    salario_liquido = salario_bruto - desc
    print(f'Salário bruto      : R${salario_bruto}')
    print(f'(-) INSS (10%)     : R${inss}')
    print(f'(-) FGTS (11%)     : R${fgts}')
    print(f'Total de descontos : R${desc}')
    print(f'Salário Liquido    : R${salario_liquido}')
elif salario_bruto <= 1500:
    ir = (5/100) * salario_bruto
    inss = (10/100) * salario_bruto
    fgts = (11/100) * salario_bruto
    desc = ir + inss + fgts
    salario_liquido = salario_bruto - desc
    print(f'Salário bruto      : R${salario_bruto}')
    print(f'(-)IR   (10%)      : R${ir}')
    print(f'(-)INSS (10%)      : R${inss}')
    print(f'(-)FGTS (11%)      : R${fgts}')
    print(f'Total de descontos : R${desc}')
    print(f'Salário Liquido    : R${salario_liquido}')
elif salario_bruto <= 2500:
    ir = (10/100) * salario_bruto
    inss = (10/100) * salario_bruto
    fgts = (11/100) * salario_bruto
    desc = ir + inss + fgts
    salario_liquido = salario_bruto - desc
    print(f'Salário bruto      : R${salario_bruto}')
    print(f'(-)IR   (10%)      : R${ir}')
    print(f'(-)INSS (10%)      : R${inss}')
    print(f'(-)FGTS (11%)      : R${fgts}')
    print(f'Total de descontos : R${desc}')
    print(f'Salário Liquido    : R${salario_liquido}')
else:
    ir = (15/100) * salario_bruto
    inss = (10/100) * salario_bruto
    fgts = (11/100) * salario_bruto
    desc = ir + inss + fgts
    salario_liquido = salario_bruto - desc
    print(f'Salário bruto      : R${salario_liquido}')
    print(f'(-)IR   (15%)      : R${ir}')
    print(f'(-)INSS (10%)      : R${inss}')
    print(f'(-)FGTS (11%)      : R${fgts}')
    print(f'Total de descontos : R${desc}')
    print(f'Salário Liquido    : R${salario_liquido}')
