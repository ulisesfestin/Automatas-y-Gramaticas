# A.F.N de (aa|b)*(a|bb)*

def AFN(string):
    string2 = ' '.join(string)
    lista = string2.split(' ')

    while lista:
        if len(lista) > 1:
            if lista[0] == 'a' == lista[1]:
                lista.pop(0)
                lista.pop(0)
            elif lista[0] == 'b':
                lista.pop(0)
                pass
            else:
                break
        else:
            if lista[0] == 'b':
                lista.pop(0)
                pass
            else:
                break

    while lista:
        if len(lista) > 1:
            if lista[0] == 'b' == lista[1]:
                lista.pop(0)
                lista.pop(0)
            elif lista[0] == 'a':
                lista.pop(0)
                pass
            else:
                print("No pertenece...")
                return
        else:
            if lista[0] == 'a':
                lista.pop(0)
                pass
            else:
                print("No pertenece...")
                return
    
    print("La cadena pertenece a la expresión regular.")
    return


while True:
    cadena = input("Ingrese una cadena de caracteres: ")
    AFN(cadena)
