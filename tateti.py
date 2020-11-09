from random import randrange

def iteracion_tablero(board, c, f):
    contador = 0
    for columnas in board:
        for filas in range(len(columnas)):
                                                                    
            if contador <= 2:                       
                c_aux = 0                               
            elif contador >= 3 and contador <= 5:   
                c_aux = 1                               
            else:                                   
                c_aux = 2                               

            if c_aux == c and filas == f:
                valor = columnas[filas]
                return valor
            else:
                contador += 1

def iteracion_tablero_for_machine(board, c, f, sign_machine):
    contador = 0
    for columnas in board:
        for filas in range(len(columnas)):
                                                                    
            if contador <= 2:                       
                c_aux = 0                               
            elif contador >= 3 and contador <= 5:   
                c_aux = 1                               
            else:                                   
                c_aux = 2                               

            if c_aux == c and filas == f:
                columnas[filas] = sign_machine
            else:
                contador += 1

def DisplayBoard(board):
        print(board)
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#

def EnterMove(board):
    movimiento_Disponible = True
    movimiento_simbolo = simbolo_usado
    while movimiento_Disponible == True:
        
        movimiento_espacio_elegido = int(input("Elija entre los números del tablero para hacer su jugada: "))
        movimiento_contador = 0
        c = 0
        for movimiento_columnas in board:
            for movimiento_filas in range(len(movimiento_columnas)):
                movimiento_contador += 1
                                                                                #################################################
                if movimiento_contador <= 3:                                    # Esta condición corrige que                    #
                    c = 0                                                       # las movimiento_columnas sean las correctas.   #
                elif movimiento_contador >= 4 and movimiento_contador <= 6:     #                                               #
                    c = 1                                                       #                                               #
                else:                                                           #                                               #
                    c = 2                                                       #                                               #
                                                                                #################################################
                
                if movimiento_contador == movimiento_espacio_elegido and movimiento_columnas[movimiento_filas] != "O":
                    board[c][movimiento_filas], movimiento_simbolo = movimiento_simbolo, board[c][movimiento_filas]
                    movimiento_Disponible = False
                    break
#
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento, 
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario
#

def MakeListOfFreeFields(board):
    print("Espacios disponibles: ", end=" ")
    for examinar_espacio_vacio in board:
        for i in range(len(examinar_espacio_vacio)):
            if examinar_espacio_vacio[i] != "X" and examinar_espacio_vacio[i] != "O":
                print(examinar_espacio_vacio[i], end=" ", sep=" ")
#
# la función examina el tablero y construye una lista de todos los cuadros vacíos 
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna
#

def VictoryFor(board, sign):


    contador_horizontal = 0
    contador_vertical = 0


    for espacio in board:
        for i in espacio:
            auxvar = i
            if auxvar == sign:
                contador_horizontal += 1

                if contador_horizontal == 3:
                    print("El ganador es: ", sign)
                    return True
            elif auxvar != sign:
                contador_horizontal = 0


    colum_verti = 0
    while colum_verti <= 3:
        for fila_0 in range(3):
            if iteracion_tablero(tateti, fila_0, colum_verti) == sign:
                contador_vertical += 1
                
                if contador_vertical == 3:
                    print("El ganador es: ", sign)
                    return True
            elif iteracion_tablero(tateti,fila_0, colum_verti) != sign:
                contador_vertical = 0
        if fila_0 == 2:
            colum_verti += 1


    if iteracion_tablero(tateti, 0, 0) == sign and iteracion_tablero(tateti, 1, 1) == sign and iteracion_tablero(tateti, 2, 2) == sign:
        print("El ganador es: ", sign)
        return True
    elif iteracion_tablero(tateti, 0, 2) == sign and iteracion_tablero(tateti, 1, 1) == sign and iteracion_tablero(tateti, 2, 0) == sign:
        print("El ganador es: ", sign)
        return True
#
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
#


def DrawMove(board):
    movimiento_Maquina_Disp = True
    while movimiento_Maquina_Disp:
        c_machine = randrange(0, 3)
        f_machine = randrange(0, 3)
        if iteracion_tablero(tateti, c_machine, f_machine) != "X" and iteracion_tablero(tateti, c_machine, f_machine) != "O":
            iteracion_tablero_for_machine(tateti,c_machine,f_machine, "O")
            break
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#

tateti = []
for columnas in range(3):
    filas = [1 for filas in range(3)]
    tateti.append(filas)

tateti [0] [0] = 1
tateti [0] [1] = 2
tateti [0] [2] = 3
tateti [1] [0] = 4
tateti [1] [1] = "O"
tateti [1] [2] = 6
tateti [2] [0] = 7
tateti [2] [1] = 8
tateti [2] [2] = 9



while True:
    simbolo_usado = input('¿Quieres usar "O" o "X" para jugar? ->')
    if simbolo_usado != "X" and simbolo_usado != "O":
        print("Elige una opción correcta.")
    else:
        break
    

juego = True
while juego == True: 
    DisplayBoard(tateti)

    EnterMove(tateti)
    DrawMove(tateti)

    if VictoryFor(tateti, simbolo_usado) == True:
        break
    if VictoryFor(tateti, "O") == True:
        break

    consultar_Tablero = input("¿Deseas consultar el estado del tablero? (y/n) ")

    if consultar_Tablero == "y":
        MakeListOfFreeFields(tateti)
        continue
    elif consultar_Tablero == "n":
        continue
    else:
        print("Disculpa, no entendí tu respuesta.")


    
