import sys
import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

print('Olhe as cartas abaixo e escolha uma:')
print('---')
print('Q♣️  K♦️  J♥️  Q♥️  J♣️  K♠️')
input()

os.system('cls')
print('A carta que você pensou...')
input()

print()
print('Desapareceu!')
print()
print('J♠️  Q♦️  J♦️  Q♠️  K♥️')
input()