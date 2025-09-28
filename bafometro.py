print('Bem-vindo a blitz da lei seca!')
print('---')
print('Este é um teste para verificar seu teor alcoolico.')

while True:
  try:
    nome = input('Insira seu nome: ')
    alcool = float(input('Simule um teor alcoolico entre 0 e 1.0: '))
    if alcool >= 0.05 and alcool <= 0.33:
      print(f'\n{nome}, seu teor alcoolico está acima do permitido.\n\nVocê cometeu uma infração de trânsito, você será multado!')
    elif alcool >= 0.34:
      print(f'\n{nome}, seu teor alcoolico está acima do permitido.\n\nVocê cometeu uma infração de trânsito grave, você será multado! Além disso, seu carro será detido e sua CNH suspensa.')
    else:
      print(f'\n{nome}, seu teor alcoolico está dentro do permitido.\n\nLiberado!')
  except ValueError:
    print('Digite um valor númerico permitido!')

  teste = input('Deseja realizar o teste no próximo motorista? (S|N)').strip().lower()
  if teste in ['n','nao','não']:
    print('\nFinalizando o teste de bafômetro!')
    break
  elif teste in ['s','sim']:
    print('\nReiniciando o teste...')
  else:
    print('\nValor incorreto... Finalizando o programa!')
    break