import re

def email_validator(urls):
    url_pattern = r'((http|https)(:\/\/))?(www\.)?[a-zA-Z0-9]+\.[a-z]+(\.[a-z]+)?(\/[a-zA-Z0-9]*)*(\?[a-zA-Z0-9]+\=[a-zA-Z0-9]+)*(\&([a-zA-Z0-9]+\=[a-zA-Z0-9]+))?'
    
    with open(urls, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if re.fullmatch(url_pattern, line):
                print(line, '--> Válido')
            else:
                print(line)


email_validator('Practico1/textos-de-ejemplo/urls.txt')