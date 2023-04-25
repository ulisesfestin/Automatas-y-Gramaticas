# A.F.N de (a|b)*

def function(string):
    for k in range(len(string)):
        if string[k] == "a" or string[k] == "b":
            pass
        else:
            return print("La cadena no pertenece a la expresión regular.")
    return print("Sí, pertenece a la expresión regular")


while True:
    cadena = input("Ingrese una cadena de caracteres: ")
    function(cadena)
