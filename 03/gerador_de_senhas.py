import random, string

tamanho = int(input("Digite o tamanho de senha que voce deseja:\n"))

chars = string.ascii_letters + string.digits + 'Çç@#$%&*()_+-/;:><!'

rnd = random.SystemRandom()
print(''.join(rnd.choice(chars) for i in range(tamanho)))