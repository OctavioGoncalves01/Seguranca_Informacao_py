import itertools

texto = input("Digite o texto a ser permutado:\n")

resultado = itertools.permutations(texto, len(texto))
for i in resultado:
    print(''.join(i))