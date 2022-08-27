nome = input('Qual o seu nome? ')
print(f'{nome} me informe o turno em que você estuda!')
turno = str(input('M para Matutino, V para vespertino e N para noturno.')).upper()
if turno == 'M':
    print(f'Bom dia {nome}, tenha um ótimo dia')
elif turno == 'V':
    print(f'Boa tarde {nome}, tenha uma ótima tarde.')
elif turno == 'N':
    print(f'Boa noite {nome}, tenha excelente noite.')
else:
    print(f'O valor {turno} é inválido, por favor informar [M, V, N].')
