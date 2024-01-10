# Define una funcion que tome un número y retorne su factorial

def factorial (numero):
  resultado = 1
  for i in range(1,numero+1):
    resultado *=i   
  return resultado 
num = int(input ('Ingresa un numero: '))
print ("El factorial de ", num, 'es:', factorial(num))


  