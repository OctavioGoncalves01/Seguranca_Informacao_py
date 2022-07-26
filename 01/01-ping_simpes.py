import os

print("#"*60)

ip_host = input("Digite o IP ou hoste a ser verificado:\n")

print("-"*60)
#os.system('ping -n 6 {}'.format(ip_host))
os.system(f'ping -n 6 {ip_host}')
print("\n")
print("#"*60)
