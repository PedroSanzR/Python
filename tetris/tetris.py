# cuanto tenemos una serie de parametros que solo pueden tener unos parametros concretos
from enum import Enum
import keyboard

class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4


def tetris():

    # vamos a tener que hacer una matriz de 10 * 10 para lo que va a ser el campo

    screen = [

    ["🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
    ["🔳","🔳","🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
    ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
    ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
    ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
    ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
    ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
    ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
    ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
    ["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
    ]
    print_screen(screen)
    rotation = 0

    while True:
        event = keyboard.read_event()

        if event.name == "esc":
            break
        elif event.event_type == keyboard.KEY_DOWN:
            if event.name == "x":
                print('1')
                (screen, rotation) = move_piece(screen, Movement.DOWN, rotation)
            elif event.name == "d":
                print('2')
                (screen, rotation) = move_piece(screen, Movement.RIGHT, rotation)
            elif event.name == "a":
                print('3')
                (screen, rotation) = move_piece(screen, Movement.LEFT, rotation)
            elif event.name == "space":
                print('4')
                (screen, rotation) = move_piece(screen, Movement.ROTATE, rotation)

# función capaz de mover la pieza...
# la flecha significa que va a retornar una lista
def move_piece(screen: list, movement: Movement, rotation: int) -> (list, int):

    new_screen = [["🔲"] * 10 for _ in range(10)]
    # vamos a crear un array con las coordenadas de cada una de las piezas
    # con esto va a decir que indice de rotación tenemos al moverlo en angulo de 45º
    rotation_item = 0
    rotations = [
        [(1, 1), (0, 0), (-2, 0), (-1, -1)],
        [(0, 1), (-1, 0), (0, -1), (1, -2)],
        [(0, 2), (1, 1), (-1, 1), (-2, -0)],
        [(0, 1), (1, 0), (2, -1), (1, -2)]
    ]

    # para cambiar el estado de rotacion
    new_rotation = rotation
    if movement is Movement.ROTATE:
        new_rotation = 0 if rotation == 3 else rotation + 1

    # vamos a recorrer el array para ver donde estan los cuadraditos de la figura

    for row_index, row in enumerate(screen):
        # item es el cuadrado negro
        for column_index, item in enumerate(row):
            if item == "🔳":
                new_row_index = 0
                new_column_index = 0
                match movement:
                    case Movement.DOWN:
                        new_row_index = row_index + 1
                        new_column_index = column_index

                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_column_index = column_index + 1
                    case Movement.LEFT:
                        new_row_index = row_index
                        new_column_index = column_index - 1
                    case Movement.ROTATE:
                        new_row_index = row_index + rotations[new_rotation][rotation_item][0]
                        new_column_index = column_index + rotations[new_rotation][rotation_item][1]
                        rotation_item += 1
                if new_row_index > 9 or new_column_index > 9 or new_column_index < 0:
                    print("\nNo se puede hacer el movimiento")
                    return screen, rotation
                else:

                    new_screen[new_row_index][new_column_index] = "🔳"

    print_screen(new_screen)

    return new_screen, new_rotation


def print_screen(screen: list):
    print("\nPantalla Tetris:\n")
    for row in screen:
        # la funcion map lo que va a servir es para juntar todo en una única variable
        print("".join(map(str, row)))


tetris()
# al poner los cursores a,d,x, space lo habrá que iniciar el juego dentro de """
"""

"""
