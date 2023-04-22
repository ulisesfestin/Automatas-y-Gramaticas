import re

def email_validator(emails):
    #patron = re.compile(r'\b[\w._-]+@[domains]+\.[a-zA-Z]{2,6}\b', re.x)
    regex_nombre = r'^[a-zA-Z][a-zA-Z0-9._-]*$'
    #regex_dominio = 
    regex_dominio_nivel_superior = r'^(com|net|org|edu|gob)$'
    regex_dominio_pais = r'^(ar|cl|co|br|pe)$'

def lexical_analyzer(file):
    pass

mails = """raul.lopez@relopezbriega.com, Raul Lopez Briega,
foo bar, relopezbriega@relopezbriega.com.ar, raul@github.io, 
https://relopezbriega.com.ar, https://relopezbriega.github.io, 
python@python, river@riverplate.com.ar, pythonAR@python.pythonAR
"""
print(email_validator(mails))
