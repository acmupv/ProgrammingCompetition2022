# Alquimia para principiantes
Los diseñadores quieren que, llegados a una parte del juego, puedas utilizar las plantas del huerto para fabricar pociones. En función de la calidad de las plantas que uses, el elixir será mejor o peor, pero este sistema tiene dos limitaciones:

1. Cada marmita tiene una cantidad máxima de plantas que se pueden echar dentro, porque sinó, desbordará.
2. Hay determinadas plantas que no se pueden poner juntas en la misma poción, pues son incompatibles y la echarían a perder.

Para poder realizar un correcto balance del juego, nos piden que hagamos un programa, que calcule la calidad máxima alcanzable para una poción (suma de las calidades de todas sus plantas) dado un input como el que sigue:

    3
    
    belladonna 5
    mandragora 2
    loto 3
    muerdago 15
    tejo 7
    albahaca 9
    jazmin 9
    
    muerdago albahaca
    muerdago tejo 
    belladonna muerdago 
    mandragora belladonna 
    muerdago jazmin 

La primera sección se compone de una única línea que contiene un entero, representando la capacidad máxima de la marmita.

Separada por una línea en blanco, la segunda sección, que especifica para cada planta disponible su nivel de calidad.

Y la última sección, también separada por una línea en blanco de la anterior, contiene los pares de plantas que son incompatibles.

Dado este input, el programa deberá devolver la calidad máxima alcanzable para una poción y sus ingredientes (ordenados alfabéticamente), para el caso anterior, sería:

    25
    
    albahaca
    jazmin
    tejo

