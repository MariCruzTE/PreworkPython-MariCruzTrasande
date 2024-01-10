'''1. Dado un número, imprime si es positivo o negativo. 
2. Dado un número, imprime si es par o impar. 
3. Dado tres números, encuentra y muestra el mayor de ellos.  '''

# Ejercicio 1:
a = 23
if a > 0:
  print ( (a) ,'es positivo')
else:
  print ( (a) , 'es negativo)')
 
 
 # Ejercicio 2:
if a % 2 == 0 :
  print ((a) , 'es un número par')
else:
  print ((a) , 'es un número impar')
  
  
  # Ejercicio 3:
  b = 3
  c = 8
  d = 1
  if b > c and b >d :
    print ('El número mayor es', (b))
  elif c > d and c > b :
    print ('El número mayor es' , (c))
  elif d > b and d > d :
    print('El número mayor es' , (d))
    
    
  
  