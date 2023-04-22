def AFD(string):
    if string == '':
        return False
    acceptance_states = ['A', 'B', 'C', 'D', 'F', 'G']
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
                current_state = 'D'
            elif character == 'b':
                current_state = 'E'
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
        elif current_state == 'D':
            if character == 'a':
                current_state = 'B'
            elif character == 'b':
                current_state = 'C'
            else:
                print("Error")
                return False
        elif current_state == 'E':
            if character == 'b':
                current_state = 'F'
            else:
                print("Error")
                return False
        elif current_state == 'F':
            if character == 'a':
                current_state = 'G'
            elif character == 'b':
                current_state = 'E'
            else:
                print("Error")
                return False
        elif current_state == 'G':
            if character == 'a':
                current_state = 'G'
            elif character == 'b':
                current_state = 'E'
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
