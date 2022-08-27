nu1 = int(input('Informe um número inteiro: '))
nu2 = int(input('Informe um segundo número inteiro: '))
nu3 = int(input('Informe o terceiro número inteiro: '))
if nu1 > nu2 > nu3:
    print(f'O número maior é {nu1} e na sequência: {nu2} e {nu3}')
elif nu1 > nu3 > nu2:
    print(f'O número maior é {nu1} e na sequência: {nu3} e {nu2}')
elif nu2 > nu1 > nu3:
    print(f'O número maior é {nu2} e na sequência: {nu1} e {nu3}')
elif nu2 > nu3 > nu1:
    print(f'O número maior é {nu2} e na sequência: {nu3} e {nu1}')
elif nu3 > nu1 > nu2:
    print(f'O número maior é {nu3} e na sequência: {nu1} e {nu2}')
elif nu3 > nu2 > nu1:
    print(f'O número maior é {nu3} e na sequência: {nu2} e {nu1}')
