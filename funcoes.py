def olaPessoa(nome):
  print(f'Olá, {nome}!')

olaPessoa(input('Digite seu nome: '))

def multiplicaDoisNumeros(a, b = 2):
  """ Multiplica dois números """
  return a * b

x = 5 # Variável global
def soma():
  x = 10 # Variável local
  print(x)
  return x + 1
soma()
print(x)