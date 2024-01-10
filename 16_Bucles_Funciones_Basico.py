#Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento de la funcion.add()

def mcm(a,b):
  if a ==0 or b==0:
    return 0
  else:
    maximo = max(a, b)
    while True:
      if maximo % a == 0 and maximo % b == 0:
        return maximo
      maximo += 1
num1 = (int(input('Ingrese el primer numero: ')))
num2 = (int(input('Ingrese el segundo numero: ')))
print('El MCM es: ',mcm(num1,num2))


