#Define una función que tome una cadena y retorne la cantidad de letras mayusculas y minusculas.

def voc_cons (cadena):
  contador = 0
  for letra in cadena : 
    if letra.lower() in 'aeiou':
      contador +=1
  return contador

      
lacadena =('pandereta')
cantidad = voc_cons(lacadena)
print('En la cadena', lacadena,'hay',cantidad, 'vocales, y', len(lacadena)-cantidad,'consonantes.')



