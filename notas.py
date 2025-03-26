print('Bem-vindo ao sistema de aprovaçao escolar!')
print('---')
nota = int(input('Digite uma nota: '))

if nota >= 7:
    print('Aprovado!!!')
elif nota < 5:
    print('Reprovado! :( ')
else:
    print('Recuperação!')