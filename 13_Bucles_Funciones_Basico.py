# Crea una funcion a la que se le pase un número como argumento,
# calcule la cantidad de digitos y haga print de 
# "La cantidad de digitos es:" y es resultado total de digitos

def contar_digitos(numero):
  return len(str(numero))

num = int(input('Ingresa un número: '))
print('La cantidad de digitos es:' , contar_digitos(num))