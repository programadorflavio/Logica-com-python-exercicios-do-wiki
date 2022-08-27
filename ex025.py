choveiro1 = float(input('Qual o preço do choveiro1? '))
choveiro2 = float(input('Qual o preço do choveiro2? '))
choveiro3 = float(input('Qual o preço do choveiro3? '))
if choveiro1 < choveiro2 < choveiro3:
    print(f'O choveiro1 {choveiro1} é mais barato que os choveiros de {choveiro2} e {choveiro3}')
elif choveiro1 < choveiro3 < choveiro2:
    print(f'O choveiro1 {choveiro1} é mais barato que os choveiros de {choveiro3} e {choveiro2}')
elif choveiro2 < choveiro3 < choveiro1:
    print(f'O choveiro2 {choveiro2} é mais barato que os choveiros de {choveiro3} e {choveiro1}')
elif choveiro2 < choveiro1 < choveiro3:
    print(f'O choveiro2 {choveiro2} é mais barato que os choveiros de {choveiro1} e {choveiro3}')
elif choveiro3 < choveiro1 < choveiro2:
    print(f'O choveiro3 {choveiro3} é mais barato que os choveiros de {choveiro1} e {choveiro2}')
elif choveiro3 < choveiro2 < choveiro1:
    print(f'O choeveiro3 {choveiro3} é mais barato que os choveiros de {choveiro2} e {choveiro1}')