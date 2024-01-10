#Crea una función que , dada una palabra, cuente la cantidad de letras en ella. 

def contar_letras(palabra):
  contador = 0
  for letra in palabra:
    if letra.isalpha():
      contador +=1
  return contador
    
palabra = (input('Ingresa una palabra: '))
print('La cantidad de letras es: ', contar_letras(palabra))

