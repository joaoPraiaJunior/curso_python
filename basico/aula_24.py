"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
nome = "João Praia"

print(f"{nome}")
print(f"{nome:>20}")  # Alinha à direita com 20 caracteres
print(f"{nome:<20}.")  # Alinha à esquerda com 20 caracteres
print(f"{nome:^20}.")  # Centraliza com 20 caracteres
print(f"{nome:=^20}.")  # Centraliza com 20 caracteres e pre
print(f"{1000.4546464646:.2f}") # Formata float com 2 casas decimais
print(f'{1000.4873648123746:0=+10,.1f}') # Formata float com 1 casa decimal, preenchendo com zeros à esquerda
print(f'O hexadecimal de 1500 é {1500:08X}') # Formata int como hexadecimal com 8 caracteres, preenchendo com zeros à esquerda
print(f'{nome!r}')