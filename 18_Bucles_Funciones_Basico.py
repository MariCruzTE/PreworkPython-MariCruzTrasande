#Crea una función que, dado un número, verifique si es un número es positivo, negativo o cero. 

def verificar_signo(num):
  if num > 0:
    return 'positivo'
  elif num < 0:
    return 'negativo'
  else:
    return 'cero'
  
num = float(input('Ingresa un número: '))
print ('El número es: ', verificar_signo(num))
  