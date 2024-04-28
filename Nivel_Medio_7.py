#Define una función que tome una cadena y retorne la cantidad de letras mayusculas y minusculas.

def voc_cons (cadena):
  minuscu = 0
  mayuscu = 0
  for letra in cadena : 
    if letra.islower():
      minuscu +=1
    else:
      mayuscu += 1
  return minuscu, mayuscu

lacadena ='Esparrago Verde en Conserva'
minusculas, mayusculas = voc_cons(lacadena)
print(f'En la cadena', (lacadena),'hay',(minusculas), 'minusculas y ', (mayusculas), ' mayusculas. ')

# output incorrecto "En la cadena Esparrago Verde en Conserva hay 21 minusculas y & mayusculas"

