#Define una funcion que tome una lista de números y retorne el número mas grande de la lista.  

def maximo_lista(numeros):
  maximo = numeros[0]
  for número in numeros:
    if número > maximo:
      maximo = número
  print (maximo)

lista = [52,63,87,94,125,241,3,8,45,16]
maximo_lista(lista)

#Hasta aqui, el resto de ejercicios de nivel medio no he conseguido ver la info de como poder sacarlos, sorry