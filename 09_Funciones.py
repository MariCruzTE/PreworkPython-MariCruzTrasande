#Define una funcion que reciba una lista de números y retorne la suma de ellos

def num_suma(list_num):
  total = 0
  for numero in list_num:
    total += numero
  return total
  
suma_total = num_suma([5,10,20,35])
print('La suma de la lista de números es : ', suma_total)

