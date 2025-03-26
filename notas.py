print('Bem-vindo ao sistema de aprovaçao escolar!')
print('---')
nota = int(input('Digite uma nota: '))

if nota >= 7:
    print('Aprovado!')
    print('Parabéns!!')
elif nota < 5:
    print('Reprovado!')
else:
    print('Recuperação')
    
print('Acabou!')