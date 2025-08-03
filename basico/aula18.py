# Exercicio de comparação de variáveis

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

primeiro_valor_convertido = int(primeiro_valor)
segundo_valor_convertido = int(segundo_valor)

if( primeiro_valor_convertido > segundo_valor_convertido ):
    print(f'O primeiro valor ({primeiro_valor}) é maior que o segundo valor ({segundo_valor}).')
elif( primeiro_valor_convertido < segundo_valor_convertido ):
    print(f'O primeiro valor ({primeiro_valor}) é menor que o segundo valor ({segundo_valor}).')
else:
    print(f'O primeiro valor ({primeiro_valor}) é igual ao segundo valor ({segundo_valor}).')