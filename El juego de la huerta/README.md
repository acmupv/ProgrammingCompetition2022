# El juego de la huerta

Para que nuestro juego de gestión de granjas tenga sentido, los cultivos deben poder nacer, crecer y morir. Desde el departamento de diseño nos han pasado las siguientes directrices:

1. Nacerá un brote en una cuadrícula de terreno si tiene a otra planta adulta en cualquier casilla adyacente (8-adyacente).
2. Un brote morirá por falta de agua si tiene 3 plantas adultas o más en casillas adyacentes y crecerá (convirtiéndose en una planta adulta) en caso contrario.
3. Una planta adulta morirá si tiene 6 plantas (de cualquier tipo, brotes o adultas) en casillas adyacentes.

Dadas estas normas, nuestro programa recibirá una entrada similar a esta:
	
    #####
    ##O##
    #·###
    #####
	
Siendo ```#``` un espacio de terreno vacío, ```·``` un brote y ```O``` una planta adulta.

Tras 6 iteraciones el campo se encontrará en el siguiente estado:

    OOOOO
    ··###
    O·##O
    OOOOO

Y en la siguiente iteración el campo se encontrará en este estado:

    OOOOO
    ##···
    O#··O
    OOOOO

Pero para la siguiente iteración volverá al estado anterior:

    OOOOO
    ··###
    O·##O
    OOOOO

Hemos alcanzado un bucle. Una vez alcanzado un bucle, para comprobar que nuestra implementación ha sido correcta debemos calcular la biodiversidad máxima del campo, para ello cogemos todos los estados que forman parte del bucle, y calculamos su biodiversidad (el terreno vacío vale 0, los brotes 1 y las plantas adultas 2), en nuestro caso obtenemos las siguientes biodiversidades:

    OOOOO                   OOOOO
    ··###                   ##···
    O·##O                   O#··O
    OOOOO                   OOOOO

    Biodiversidad: 27       Biodiversidad: 29

Y nuestro programa devolverá el campo con el mayor índice de biodiversidad, en este caso:

    OOOOO
    ##···
    O#··O
    OOOOO
