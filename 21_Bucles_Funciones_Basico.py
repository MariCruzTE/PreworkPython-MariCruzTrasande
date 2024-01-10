#Crea una función que, dado un número, verifique si es primo.add()

def es_primo (numero):
  if numero<=1:
    return False
  for i in range(2,numero):
    if numero % i== 0:
      return False 
  return True
  
num = (int(input('Ingresa un número: ')))
if es_primo(num):
   print('No es un número primo')
else:
   print('Es un número primo')