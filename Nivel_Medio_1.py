#Define una función que utilice un bucle para imrimir los primeros n números de la serie de Fibonacci.

def primeros_fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(primeros_fibonacci(n-1) + primeros_fibonacci(n-2))  
     
serie = int(input("Introduce el número de primeros números que deseas ver: "))
  
if serie <= 0:
   print("Por favor, ingresa un número positivo: ")  
else:  
   print("Serie de Fibonacci:")  
   for i in range(serie):  
       print(primeros_fibonacci(i))
  