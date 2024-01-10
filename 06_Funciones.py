# Define una funcion que tome dos números y devuelva su suma

def num_suma(list_num):
  total = 0
  for numero in list_num:
    total += numero
  return total

suma_total = num_suma([5,4995])
print('La suma de los numeros ingresados es : ',suma_total)
  

  