#Crea una función a la que, pasandole la base y la altura,
# calcule y devuelva el area de un triángulo.

def calcular_area_triangulo(base,altura):
  return (base*altura)/2
base = float(input('Ingrese la base del triángulo: '))
altura = float(input('Ingrese la base del triángulo: '))
print('El área del triángulo es: ', calcular_area_triangulo(base, altura))
