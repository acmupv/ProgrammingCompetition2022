#Farm-code
Para que nuestro juego funcione necesitamos poder mover al jugador y realizar acciones básicas, para ello el departamento de diseño nos ha dado las siguientes instrucciones a implementar:

1. ```mv dx dy```   La instrucción mv (move) recibe dos números enteros ‘dx’ y ‘dy’, desplazando al jugador esos valores en el eje x e y respectivamente.
2. ```pk```             La instrucción pk (pick) comprueba si en la posición actual del jugador hay una planta madura, en el caso de que si la haya, la recoge.
3. ```sd```              La instrucción sd (seed) comprueba si la posición actual del jugador está vacía (si no hay nada plantado) y si al jugador le queda alguna semilla, en caso de que ambas condiciones se cumplan el jugador planta una semilla en su posición actual (descontando-la también de su inventario).
4. ```wt```              La instrucción wt (water) comprueba si en la posición actual del jugador hay una semilla plantada y en caso positivo la hace crecer.

Dado un input de la siguiente forma:

    #####
    ##o##
    O#ooO
    OoOoO

    0 0
    4
    
    mv 1 3
    wt
    mv 0 -2
    sd
    mv 0 2
    pk
    mv -1 0
    sd
    pk

Compuesto por una primera sección que representa el huerto, siendo ```#``` un espacio de terreno vacío, ```o``` una semilla plantada y ```O``` una planta madura.

Una segunda sección, separada de la primera por una línea en blanco y compuesta por una línea con dos números enteros positivos separados por un espacio en blanco, que representan la posición del jugador al inicio del juego ‘x y’, siendo el (0, 0) la esquina superior izquierda y una segunda línea con un único entero positivo representando el número de semillas de las que dispone el jugador.

Y por último, la sección de código, separada de la anterior también por una línea en blanco, se compone de una lista de instrucciones a ejecutar en orden, dado el huerto y la posición del jugador de las secciones anteriores.

Tras ejecutar el código anterior, el programa debe devolver el número de plantas maduras que ha recogido el jugador, en el caso del ejemplo anterior: 

    2
