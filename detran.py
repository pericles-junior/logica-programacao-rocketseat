print('Bem-vindo ao DENTRAN!')
print('---')
print('Este é o novo teste extremamente complexo para liberar ou não a CNH.')
print()
# se a idade for maior ou igual a 18, então:
#   deixa dirigir
# senão
#   não pode dirigir
while True:
    try:
        idade = int(input('Digite sua idade: '))
        if idade >= 18:
            print('✅ Pode dirigir!')
        else:
            print('❌ Não pode dirigir!')
    except ValueError:
        print('⚠️  Por favor, digite um número válido para a idade.')
        continue

    pergunta = input('Deseja realizar um novo teste? (S/N): ').strip().lower()
    if pergunta in ['n','não','nao']:
        print('\nFinalizando o programa... Obrigado por realizar o teste conosco.')
        break
    elif pergunta in ['s','sim']:
        print('\nReiniciando o teste...\n')
    else:
        print('\nResposta não conhecida. Encerrando por segurança.')
        break