# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  Otávio
# -6-5-4-3-2-1

nome = "Otávio"

print(nome[2])
print(nome[-4])

print('á' in nome)
print('a' in nome)
print('-' * 10)
print('vio' not in nome)
print('zero' not in nome)

palavra = input('Digite uma palavra: ')
encontrar = input('Digite uma letra ou palavra para encontrar: ')

if encontrar in palavra:
    print(f'A letra ou palavra "{encontrar}" foi encontrada na palavra "{palavra}".')
else:
    print(f'A letra ou palavra "{encontrar}" não foi encontrada na palavra "{palavra}".')
print('-' * 10)
# Verificando se uma letra ou palavra está presente em uma string
