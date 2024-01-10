#Define una función que tome una lista y un número n y retorne los primeros n elementos de la lista.add()



def lista_n(lista):
  cantidad =(int(input('Ingrese la cantidad de primeros elementos de la lista que quiera ver: ')))
  while len(lista) <= cantidad :
     elemento = lista.pop(0)
     print(elemento)
    
numeros = [2,4,6,8,10,12,14,16,18,20]
print(lista_n(numeros))
  
#Intente sacarlo pero no lo he conseguido :(
  
