import ipaddress

ip = '192.168.0.1'
rede = "192.168.0.0/24"

endereco = ipaddress.ip_address(ip)
print(endereco + 152)

rede = ipaddress.ip_network(rede, strict=False)
for ip in rede:
    print(ip)

