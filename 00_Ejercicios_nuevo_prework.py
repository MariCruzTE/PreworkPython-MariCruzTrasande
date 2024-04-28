#Ejercicio1: Conversor de temperatura:
#Escribe un programa que convierta una temperatura de grados Celsius a grados Fahrenheit

'''def conversor_temperatura(gradosC):
  gradosF = (gradosC * 9/5) + 32
  return gradosF

temperaturaCelsius = float(input('Escribe los grados Celsius que quieras convertir a Fahrenheit: '))
temperaturaFahrenheit = conversor_temperatura(temperaturaCelsius)
print(f'Corresponde a: {temperaturaFahrenheit} grados Fahrenheit') 

# Ejercicio 2: Calculadora de propina
# Programa que calcule el total a pagar, con un apropina del 15% sobre el total de la cuenta

def calcula_propina (cuenta):
  prop = (cuenta * 0.15) + cuenta
  return prop

subtotal = float(input('¿Cuál es el importe inicial?: '))
factura = calcula_propina(subtotal)
print(f'El total de la factura, incluyendo 15% de propina es de: {factura} € ')

# Ejercicio 3: Verificación de edad
# Programa que solicite edad usuario y devuelva si es mayor de edad o no

edad = int(input('Ingrese su edad: \n'))
if edad < 18 :
  print('Es usted menor de edad')
else:
  print('Es usted mayor de edad')

# Ejercicio 4: Contador de vocales
# Programa que cuente nº de vocales en una palabra ingresada por el usuario

palabra = str(input('Escriba una palabra: \n'))
vocales = 0
for p in palabra:
  if p.islower():
    vocales += 1
  print(f'El número de vocales de la palabra ingresada es: {vocales}')

# Ejercicio 5: Suma de números pares
# Programa que calcule la suma de todos los numeros pares del 1 al 100

n = 1
suma_pares = 0
while n <= 100:
  if n % 2 == 0:
    suma_pares += n
  n += 1
print(f'La suma de todos los númros pares entre 1 y 100 es: {suma_pares} ')

# Ejercicio 6: verificacion de palindromo
# Programa que verifique si una palabra ingresada por el usuario es un palindromo

def es_palindromo(palabra):
  palabra = palabra.lower()
  if str(palabra) == str(palabra)[::-1]:
    print(palabra,'es un palindromo \nse puede leer igual de izda a dcha y dcha a izda')
  else:
    print(palabra, 'no es un palindromo\nno se puede leer igual de izda a dcha que de dcha a izda')
palabra_usuario = str(input('Escriba una palabra: '))
es_palindromo(palabra_usuario)  

# Ejercicio 7: Calculadora simple
# Programa que realice operaciones simples (suma, resta, multiplicacion, division)
def calculadora():
  print('suma, resta, multiplicación o división \n')
  operacion = (input('¿Qué operacion de las anteriores quieres realizar?\n'))
  num1 = float(input('Ingresa la primera cifra para la operacion: \n'))
  num2 = float(input('Ingresa la segunda cifra para la operacion: \n')) 
  if operacion == 'suma':
    resultado = num1 + num2
  elif operacion == 'resta':
    resultado = num1 - num2
  elif operacion == 'multiplicacion':
    resultado = num1 * num2
  elif operacion == 'division':
    if num2 != 0:
      resultado = num1 / num2
    else:
      print('No se puede dividir un número entre 0')
  else:
    print('Operacion no admitida, elija entre: suma, resta, multiplicacion y division')
  print('Resultado de la operacion:', resultado)   
calculadora()

# Ejercicio 8: Calculo de IMC
# Programa que calcule indide de masa corporal de una persona

def calculo_imc():
  peso = float(input('Indique su peso: '))
  altura = float(input('Indique su altura: '))
  imc = peso / altura**2
  print('Su indice de masa corporal es:', (imc))

calculo_imc()

# Ejercicio 9: Conversor de divisas
# Programa que convierta dolares a euros $ = 0.85€

def conv_divisas():
  dolar = float(input('Indique cantidad en $: '))
  euro = dolar * 0.85
  print((dolar), 'dolares, corresponden a: ',(euro), 'Euros')
  
conv_divisas()

# Ejercicio 10: Dia de la semana
# Programa que determine el dia de la semana correspondiente a
# un numero ingresado por usu. (1lunes, 2martes...)

def dia_sem():
  num_usu = int(input('Ingrese un número del 1 al 7: '))
  if num_usu == 1:
    d_sem = 'lunes'
  elif num_usu == 2:
    d_sem = 'martes'
  elif num_usu == 3:
    d_sem = 'miercoles'
  elif num_usu == 4:
    d_sem = 'jueves'  
  elif num_usu == 5:
    d_sem = 'viernes'
  elif num_usu == 6:
    d_sem = 'sabado'
  elif num_usu == 7:
    d_sem = 'domingo'
  else:
    print('Número incorrecto, ingrese nº del 1 al 7: ')

  print('El dia de la semana que corresponde al nº ', (num_usu), 'es: ', (d_sem))
  
dia_sem()

# Ejercicio 11: Calculadora de edad
# Programa que pida año de nacimiento y calcule su edad actual

def calc_edad():
  año_usu = int(input('Indique su año de nacimiento: '))
  año_act = 2024
  edad = año_act - año_usu
  print('Actualmente Ud. tiene ', (edad), 'años.\n')
  
calc_edad()

# Ejercicio 12: Calculadora area rectangulo
# programa que calcule area rectangulo, usu. ingresa long y base

def rect_area():
  base = float(input('Ingrese la medida de la base del rectangulo: '))
  altura = float(input('Ingrese la medida de la altura del rectangulo: '))
  area = base * altura
  print('El area del rectangulo con base ', (base),'Y altura ', (altura),' Es:', (area))
  
rect_area()

# Ejercicio 13: Verificacion numero primo
# programa que determine si nº ingresado por usu es primo

def es_primo (numero):
  if numero<=1:
    return False
  for i in range(2,numero):
    if numero % i== 0:
      return False 
  return True
  
num = (int(input('Ingresa un número: ')))
if es_primo(num):
   print('Es un número primo')
else:
   print('No es un número primo')
  
# Ejercicio 14: calculadora descuento
# Programa que calcule precio final de articulo con -15% dto

def total_reba():
  precio_ini = float(input('¿Precio inicial del artículo?'))
  rebaja = precio_ini - (precio_ini * 0.15)
  print ('El articulo esta rebajado, su precio final es de:',(rebaja))

total_reba()

# Ejercicio 15: Conversor de tiempo
# Programa que convierta numero de minutos en horas y minutos
# Ej: 145 min son 2 horas 25 minutos

def conv_min():
  cifra_min = int(input('Ingrese el numero total de minutos'))
  horas = cifra_min // 60
  minutos = cifra_min % 60
  print('Los ',(cifra_min),'minutos totales, corresponden a ', (horas), 'horas, ',(minutos), 'minutos. ')

conv_min()
  
# Ejercicio16: Contador de pares impares
# programa que cuente y muestre nº de impares y pares de una lista 
# ingresada por el usuario
def par_impar():
  num_list =[]
  pares = 0
  impares = 0
  numeros_usu = (input('ingrese 10 numeros separados por espacios: '))
  for n in numeros_usu:
    numero = int(n)
    num_list.append(n)
    for n in num_list:
      if n % 2 == 0:
        pares += 1
      else:
       impares += 1
      print('Entre los 10 numeros proporcionados, hay', (pares),'numeros pares y', (impares),'numeros impares')

par_impar()

# Ejercicio 17: Conversor de millas a kms
# Programa que convierta millas a kms 1 milla = 1.60934 km

def conv_distancia():
  millas = float(input('Ingrese la distancia en millas: '))   
  kms = millas * 1.60934
  print((millas),' millas, corresponde a ', (kms), ' kilometros')'''

conv_distancia() 

# Ejercicio 18: Contador de palabras
# Programa que cuente cantidad de palabras de 1 oracion 
# ingresada por usuario

def count_word():
  frase = input('ingrese una frase: ')
  conteo = 0
  for palabra in frase:
    if len (palabra) > 0 :
     conteo +=1
  print(conteo)
count_word()

# Ejercicio 19: Verificcion de año bisiesto
# Programa que verifique si es visiesto un año que de usuario

def es_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        return True
    else:
        return False
año_usuario = int(input("Ingrese un año: "))
if es_bisiesto(año_usuario):
    print((año_usuario), 'si es un año bisiesto.')
else:
    print((año_usuario), 'no es un año bisiesto.')


      
  
    

