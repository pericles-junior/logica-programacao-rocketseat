print('Bem-vindo ao DENTRAN!')
print('---')
print('Este é o novo teste extremamente complexo para liberar ou não a CNH.')
print()
idade = int(input('Digite sua idade: '))

# se a idade for maior ou igual a 18, então:
#   deixa dirigir
# senão
#   não pode dirigir

if idade >= 18:
    print('Pode dirigir!')
else:
    print('Não pode dirigir!')

print('Acabou')