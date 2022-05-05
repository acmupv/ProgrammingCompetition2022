# Función generadora de los strings codificados:
def encode(x, pos, sum):
 ''' Para generar los inputs'''
 if ord(x) == 32:
   sum += 1
   return sum, 32
 res = ord(x) + pos + sum
 if res > 126:
   res = res % 126 + 33
 return sum, res


# Función decodificadora:
def decode(x, pos, sum):
 ''' Para comprobar que es correcto (solución)'''
 if ord(x) == 32:
   sum += 1
   return sum, 32
 res = ord(x) - pos - sum
 if res <= 32:
   res = (res - 33) % 126
 
 return sum, res
