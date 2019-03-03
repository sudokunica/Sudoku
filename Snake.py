import random

#Se importa un modulo de Python para crear una interfaz gráfica y manejar el teclado desde la consola
import curses 

'''
Las siguientes lineas crearán una ventana donde se desarrollara el juego, para 
lo cual se posiciona el cursor en 0 y por medio de la función getmaxyx se obtiene 
el tamaño de la ventana de la consola, después se crea la ventana con la función
newwin (alto_max, ancho_max, alto_min, ancho_min)
'''
s=curses.initscr() #Se inciializa la aplicación de curses.
curses.curs_set(0)
sh,sw=s.getmaxyx()
w=curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

'''
Aquí se crea la serpiente, la serpiente será una lista de listas donde se 
almacenará las coordenadas de cada parte de su cuerpo, snk_x y snk_y son la
posicion inicial de la serpiente.
'''

snk_x=sw/4
snk_y=sh/2
snake=[
	[snk_y,snk_x],
	[snk_y,snk_x-1],
	[snk_y,snk_x-2]
]

'''
Se crea la comida de la serpiente, en este caso será el simbolo "•", y se posicionara 
en la ventana
'''
food=[sh/2,sw/2]
w.addch(food[0],food[1],"•")

key=curses.KEY_RIGHT
#Definimos la direccion inicial de la serpiente, ya sea arriba, abajo, izquierda o derecha

#El juego se desarrolla dentro de este while
while True:
    next_key = w.getch()
    #w.getch() espera un caracter, cuando sea introducido se guardara en next_key

    key = key if next_key == -1 else next_key
    #La llave va a permanecer igual si no se introduce nada, si si se introduce entonces tomara el valor de lo que se introdujo

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:]:
        #Si la serpiente choca en el limite de arriba o de abajo; o si choca con el de la derecha o izquierda
        #o si la serpiente se encuentra con si misma

        curses.endwin()
        quit()
        #Entonces se acaba el juego y se regresa a la terminal

    new_head = [snake[0][0], snake[0][1]]
    #la direccion de la serpiente primero se define como su posicion inicial/actual

    if key == curses.KEY_DOWN:
        #Si se presiona la tecla flecha de Abajo 

        new_head[0] += 1
        #Entonces la "posicion Y" de la serpiente se le sumara 1, indicando que va hacia arriba

    if key == curses.KEY_UP:
        #Si se presiona la tecla flecha de Arriba

        new_head[0] -= 1
        #Entonces la "posicion Y" de la serpiente se le resta 1, indicando que va hacia abajo

    if key == curses.KEY_LEFT:
        #Si se presiona la tecla flecha de la Izquierda

        new_head[1] -= 1
        #Entonces la "posicion X" de la serpiente se le restara 1, indicando que va hacia a la izquierda


