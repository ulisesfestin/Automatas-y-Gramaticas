import re

def contador(directory):
    word_pattern = re.compile(r'\b[a-zA-Záéíóú]+\b', re.X)
    with open(directory, "r") as file:
        content = file.read()
        words = word_pattern.findall(content)
    total_words = len(words)
    repeticiones = {}
    for word in words:
        if word in repeticiones :
            repeticiones[word] += 1
        else:
            repeticiones[word] = 0
    print(total_words)
    print(repeticiones)


contador(r'Practico1/textos-de-ejemplo/mariposas.txt')