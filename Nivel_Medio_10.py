#Define una función que reciba dos listas y retorne la interseccion de ambas (los elementos que estan en las dos listas).



def inter(lista1,lista2):
  lista3=[]
  for numero in lista1:
    if numero in lista2:
      lista3.append(numero)
  return lista3

listaa=[5,10,15,20,25,30]
listab=[10,20,30,40]      
print('Los elementos comunes en las dos listas son: ', inter(listaa,listab))
