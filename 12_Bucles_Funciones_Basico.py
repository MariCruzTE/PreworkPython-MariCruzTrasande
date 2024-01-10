#Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado

def factorial (numero):
  resultado = 1
  for i in range(1,numero+1):
    resultado *=i   
  return resultado 
num = int(input ('Ingresa un numero: '))
print ("El factorial de ", num, 'es:', factorial(num))
