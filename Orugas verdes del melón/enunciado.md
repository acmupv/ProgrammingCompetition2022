#Orugas verdes del melón
Para añadir algo de dificultad al juego, se ha incorporado un nuevo enemigo, la terrible oruga verde del melón, aunque parezca contradictorio, esta criatura ataca a las plantaciones de calabazas. 

Pero los diseñadores no quieren que el juego se vuelva demasiado difícil, así que nos piden que hagamos un programa para comprobar la dificultad de cada nivel.

Nuestro programa recibirá un input de la siguiente forma:

    ##################S#
    # o  1   2#  o # # #
    #   #   ###    # # #
    # ###  1      ## # #
    # #o#    o    2  # #
    # # #####     #### #
    #o          o  3   #
    ####################

Este input representa un huerto, siendo ```#``` las vallas del huerto, las cuales nuestro jugador no puede cruzar, ``` ``` un trozo de terreno vacío, ```o``` una calabaza, ```S``` la entrada y salida del huerto y ```n``` siendo n un número representará un cúmulo de n orugas.

Nuestro objetivo es encontrar un camino que salga de la salida, recoja todas las calabazas, pasando por el menor número de orugas posibles (para minimizar el riesgo de infectar a la cosecha) y vuelva a la salida.
(Si se pasa dos veces por el mismo cúmulo de orugas, se tiene en cuenta las dos veces)

Nuestro programa deberá devolver el número de orugas por el que ha sido inevitable pasar, en este caso:

    6
