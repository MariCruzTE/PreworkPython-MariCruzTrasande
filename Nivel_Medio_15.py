#Define una función que tome un número y calcule su serie de Fibonacci. 

def fib(n):
  if n < 2:
    return n
  else:
    return fib(n-1) + fib(n-2)
  
a =(int(input('Ingrese un numero: ')))
for x in range(a):
  print (fib(x))
   