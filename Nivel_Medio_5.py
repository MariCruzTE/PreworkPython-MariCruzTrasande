#Define una función qu etome una cadena y cuente el numero de vocales en la cadena

def cuenta_vocales(cadena,):
  contador = 0
  for letra in cadena:
    if letra.lower() in 'aeiou':
      contador +=1
  return contador
mi_cadena = 'madre mia cuantos ejercicios de funciones llevo hasta ahora'
cantidad = cuenta_vocales(mi_cadena)
print('En la cadena', mi_cadena,'hay',cantidad, 'vocales')
