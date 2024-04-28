# Dada una lista de numeros, crea una funcíon que devuelva
# el número maximo de la lista.add()

def encontrar_maximo(lista):
  maximo = lista[0]
  for numero in lista:
    if numero > maximo: 
      maximo=numero
      return maximo
    
numeros=[5,12,3,8,9]
print('El numero maximo es: ',encontrar_maximo(numeros))