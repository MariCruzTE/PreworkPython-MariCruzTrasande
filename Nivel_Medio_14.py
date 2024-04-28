#Define una función que reciba una lista de palabras y un entero n y retorne una lista de palabras que son mas largas que n. 

def medir_palabras(palabras):
  medida= int(input('Ingrese el número que servirá de medida: '))
  for palabra in palabras:
    if len(palabra) > medida :
      print(palabra)
      
mi_lista = ['En','desde','terciopelo','patata','lista','entero','funcion']
medir_palabras(mi_lista)

