#Escribe un programa que imprima los números del 1 al 50, pero para los multiplos de tres imprima"Fizz"en lugar del numero y para los multiplos de cinco imprima"Buzz".Para los numeros que son multiplos tanto de 3 como de 5, que imprima "FizzBuzz". 

for i in range (1,51):   
  if (i % 3 == 0) and (i % 5 == 0):
    print('FizzBuzz')
  elif (i % 3 == 0):
    print('Fizz')
  elif (i % 5 == 0):
    print('Buzz')
  else:
    print(i)
 

    
    
  