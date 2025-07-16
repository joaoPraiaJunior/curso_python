# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: inicie variáveis com letras minúsculas, pode usar
# números e underline _.
# O sinal de = é o operador de atribuição. Ele é usado para
# atribuir um valor a um nome (variável).
# Uso: nome_variavel = expressão

nome_completo = 'João Praia Junior'
idade = 43
altura = 1.88
peso = 91.5
maior_de_idade = idade >= 18
nacionalidade = 'Brasileiro'

print(nome_completo)
print(idade)
print(altura)
print(peso)
print(maior_de_idade)
print(nacionalidade)

print(type(nome_completo))  # <class 'str'>
print(type(idade))          # <class 'int'>
print(type(altura))        # <class 'float'>
print(type(peso))          # <class 'float'>
print(type(maior_de_idade)) # <class 'bool'>
print(type(nacionalidade)) # <class 'str'>

print(f'{nome_completo} tem {idade} anos, altura de {altura}m, '
      f'pesa {peso}kg, é maior de idade? {maior_de_idade} e é {nacionalidade}.')
