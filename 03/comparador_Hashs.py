import hashlib

arquivo01 = 'a.txt'
arquivo02 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo01, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo02, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo {arquivo01} é diferente do arquivo {arquivo02}')
    print(f'O hash do arquivo {arquivo01} é: {hash1.hexdigest()}')
    print(f'O hash do arquivo {arquivo02} é: {hash2.hexdigest()}')
else:
    print(f'O arquivo {arquivo01} é igual do arquivo {arquivo02}')
    print(f'O hash do arquivo {arquivo01} é: {hash1.hexdigest()}')
    print(f'O hash do arquivo {arquivo02} é: {hash2.hexdigest()}')
