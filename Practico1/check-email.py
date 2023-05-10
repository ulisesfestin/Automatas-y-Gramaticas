import re

def email_validator(emails):
    regex_nombre = r'[a-zA-Z0-9._/]+'
    regex_dominio_email = r'[a-zA-Z]+'
    regex_dominio_nivel_superior = r'\.(com|net|org|edu|gob)'
    regex_dominio_pais = r'(\.(ar|cl|co|br|pe))?'
    mail_pattern = f'{regex_nombre}@{regex_dominio_email}{regex_dominio_nivel_superior}{regex_dominio_pais}'
    
    with open(emails, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if re.fullmatch(mail_pattern, line):
                print(line, '--> Válido')
            else:
                print(line)


email_validator('Practico1/textos-de-ejemplo/mails.txt')