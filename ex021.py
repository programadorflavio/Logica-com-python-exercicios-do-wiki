ler = str(input('Informe M para masculino e F para feminino: ')).upper()
if ler == 'M':
    print(f'Você informou {ler}, portanto masculino.')
elif ler == 'F':
    print(f'Você informou {ler}, portanto você informou feminino.')
else:
    print(f'Você não informou nenhum dos dois valores, então escolha: M ou F')