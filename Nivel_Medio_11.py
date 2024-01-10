#Define una función que tome una cadena y determine si es un palindromo. 

def es_palindromo(palabra):
  palabra = palabra.lower()
  if str(palabra) == str(palabra)[::-1]:
    print(palabra,'es un palindromo')
  else:
    print(palabra, 'no es un palindromo')
    
print(es_palindromo('radar'))
