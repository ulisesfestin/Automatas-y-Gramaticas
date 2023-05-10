import re

def check_ipv4(ips_file):

    #Expresión regular para detectar números enteros de a lo sumo tres cifras entre puntos:  num.num.num.num
    ipv4_pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

    with open(ips_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if re.match(ipv4_pattern, line):
                # Separar la dirección IPv4 en octetos
                octets = line.split('.')
                # Validar que cada octeto se encuentre en el rango de 0 a 255
                if all(0 <= int(octet) <= 255 for octet in octets):
                    print(line, "--> VÁLIDA")
                else:
                    print(line)
            else:
                print(line)

check_ipv4('Practico1/textos-de-ejemplo/ips1.txt')