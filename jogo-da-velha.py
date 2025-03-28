tabuleiro = [
  [' ',' ',' '],
  [' ',' ',' '],
  [' ',' ',' ']
]

jogador = 'X'
def mostraTabuleiro():
  for linha in tabuleiro:
    print('|'.join(linha))
    print('-' * 5) 

def jogada(linha, coluna):
  tabuleiro[linha][coluna] = jogador
  return 'O' if jogador == 'X' else 'X'

jogador = jogada(1,2)
jogador = jogada(1,1)
mostraTabuleiro()