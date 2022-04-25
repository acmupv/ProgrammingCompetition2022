El Calendario Juliano Revisado es un sistema de calendario muy similar al conocido Calendario Gregoriano, pero 
ligeramente más preciso en cuanto a la duración media del año. El Calendario Juliano Revisado tiene un día bisiesto 
el 29 de febrero de los años bisiestos como sigue:

- Los años que son divisibles por 4 son bisiestos.
- Excepción: Los años que son divisibles por 100 no son bisiestos.
- Excepción a la excepción: Los años en los que el resto dividido por 900 es 200 o 600 son bisiestos.

- Por ejemplo, el año 2000 es una excepción a la excepción: el resto al dividir 2000 entre 900 es 200. Por lo tanto, 
- el año 2000 es bisiesto en el calendario juliano revisado.

Desafío

Dados dos números de años positivos (con el segundo mayor o igual que el primero), averigüe cuántos días bisiestos 
(29 de febrero) aparecen entre el 1 de enero del primer año y el 1 de enero del segundo año en el Calendario Juliano 
Revisado. Esto equivale a preguntar cuántos años bisiestos hay en el intervalo entre los dos años, incluyendo el 
primero, pero excluyendo el segundo.

Por ejemplo, dado el input:
```
2016 2017
2019 2020
2000 2001
1234 5678
```

El output debería ser:
```
1
0
1
1077
```

(Pista: hay 218 años bisiestos cada 900 años) Si es muy fácil esto no hace falta ponerlo (ACM opina que no se ponga)
