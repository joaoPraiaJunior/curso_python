# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Senha não informada')
else:
    print('Entrou')


# Inverter a expressão
print(not True)  # False 
print(not False)  # True
