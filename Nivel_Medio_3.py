#Define una funciòn que tome una lista y retorne una nueva lista con
# los elementos únicos de la lista original. = [2, 2, 3, 1, 4, 2, 5]

lista_original = [25,12,5,62,18,3,62,9,4,5]

def devol_unic(lista):
  unicos = []
  for x in lista:
    if x not in unicos:
      unicos.append(x)
      return(unicos)

print(devol_unic(lista_original))     