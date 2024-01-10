#Define una funciòn que tome un numero y retorne la suma de sus digitos

def sumar_digitos(numero):
  suma=0
  while numero > 0:
    suma += numero % 10
    numero //=10
  return suma
num = int(input('Ingresa un número: '))
print('La suma de los digitos es:', sumar_digitos(num))