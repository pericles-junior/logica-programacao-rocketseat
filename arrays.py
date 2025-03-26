notas = [10, 9.5, 9, 9.8]
media = 0
for nota in notas:
    media += nota

media /= len(notas)

print(f'A média de é {media}')