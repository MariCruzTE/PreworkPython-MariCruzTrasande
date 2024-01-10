#Crea una función que, dada una lista de nùmeros, convierta la lista de números a su valor absoluto. 

def valor_absoluto(lista):
  for i in range(len(lista)):
    lista[i] = abs(lista[i])
  return lista
  
numeros =[5,-12,3,-8,9]
print('Lista con valores absolutos: ', valor_absoluto(numeros))
