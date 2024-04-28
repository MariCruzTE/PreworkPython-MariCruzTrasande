# Define una funcion que reciba un numero y retorne su representacion en binario.

def binario(num):
  return bin(num)

numero = int(input('Ingrese el número: '))
print('La representacion en binario del número ', (numero), 'es: ', (binario(numero)))
