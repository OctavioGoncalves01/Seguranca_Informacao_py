import hashlib

# resultado = hashlib.md5(b'Python Security')
# print("O hash da string é: ",resultado.hexdigest())

# string = input("Digite o texto a ser gerado a hash:\n")
# resultado = hashlib.md5(string.encode('utf-8'))
# print("O hash da string é: ",resultado.hexdigest())


texto = input("Digite o texto para gerer seu hash:\n<>")
menu = int(input('''### Menu - ESCOLHA o TIPO de HASH ###
                    1- MD5
                    2- SHA1
                    3- SHA256
                    4- SHA512
                    Digite o número do hash a ser gerado:\n<>'''))

if menu == 1:
    resultado = hashlib.md5(texto.encode('utf-8'))
    print("A hash MD5 da string é: ",resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(texto.encode('utf-8'))
    print("A hash SHA1 da string é: ",resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(texto.encode('utf-8'))
    print("A hash SHA256 da string é: ",resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(texto.encode('utf-8'))
    print("A hash SHA512 da string é: ",resultado.hexdigest())
else:
    print("Algo de errado não deu certo!!")