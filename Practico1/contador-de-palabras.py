import re

def contador(directory):
    word_pattern = re.compile(r'\b[a-zA-Záéíóú]+\b', re.X)
    with open(directory, 'r') as file:
        content = file.read()
        words = word_pattern.findall(content)
    total_words = len(words)
    repeticiones = {}
    max = ('', 0)
    for word in words:
        if word in repeticiones :
            repeticiones[word] += 1
        else:
            repeticiones[word] = 0
    for n in repeticiones:
        if repeticiones[n] > max[1]:
            max = (n, repeticiones[n])
        else:
            pass
    print('Cantidad de palabras:', total_words)
    print(f'Palabra que más se repite "{max[0]}", repeticiones: {max[1]}')


contador(r'Practico1/textos-de-ejemplo/mariposas.txt')