Un granjero tiene un campo de zanahorias. En cada fila de zanahorias habitan conejos
de diferentes nacionalidades. Cada nacionalidad vendrá representada por la letra inicial
de la palabra ‘conejo’ en su respectivo idioma, pudiendo haber únicamente estas
nacionalidades:

```
“Conejo”  -> España
“Lepurin” -> Albania
“Hase”    -> Alemania
“Rabbit”  -> Inglaterra
“Dovsan”  -> Azerbaijan
“Zec”     -> Bosnia y Herzegovina
“Králik”  -> Estonia
```

| c | l | h | l | c |
|---|---|---|---|---|
| z | d | r | l |   |
| k | k | d | d |   |
| c | h | r | z | c |

El Input contendrá en la primera línea el número N de filas que tiene el campo de
zanahorias. A continuación, N líneas de cadenas que representarán cada fila del campo
del granjero y que contendrá la nacionalidad de cada conejo según la letra inicial dada
de la palabra “conejo” en su respectivo idioma.

Tu objetivo es ayudar al granjero a reubicar conejos, pudiendo quitar a uno de cada fila.
Si en cada fila hay M conejos, hay también M posiciones.

Los conejitos siempre cavan su madriguera de tal manera que entrando por la posición
en la que estén, salgan por otra posición. El que tenga la posición más alta querrá salir
por la posición más baja, y viceversa. El que tenga la segunda posición más alta querrá
salir por la segunda posición más baja, y viceversa. Y así… Esperan encontrar a un
conejito de su misma nacionalidad. El granjero se puede permitir tener como mucho un
conejo mal ubicado.
Por ejemplo:

Input:
```
3
"clc"
"clhc"
"clhrrhkc"
```

Output:
```
"conejos bien ubicados"
"conejos bien ubicados"
"demasiados conejos deben reubicarse"
```