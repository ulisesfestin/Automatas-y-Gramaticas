def AFD(string):
    if string == '':
        return False
    acceptance_states = ['A', 'B', 'C']
    current_state = 'A'
    for character in string:
        if current_state == 'A':
            if character == 'a':
                current_state = 'B'
            elif character == 'b':
                current_state = 'C'
            else:
                print("Error")
                return False
        elif current_state == 'B':
            if character == 'a':
                current_state = 'C'
            elif character == 'b':
                current_state = 'B'
            else:
                print("Error")
                return False
        elif current_state == 'C':
            if character == 'a':
                current_state = 'B'
            elif character == 'b':
                current_state = 'C'
            else:
                print("Error")
                return False
    
    final_state = current_state
    
    if final_state in acceptance_states:
        return True
    else:
        return False


while True:
    string = input("Ingrese una cadena de caracteres: ")
    if AFD(string):
        print("La cadena pertenece.")
    else:
        print("La cadena NO pertenece.")
