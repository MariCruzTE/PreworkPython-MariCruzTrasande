

print("introduzca el numero")
numero = int(input()) 
contador = 0
lista=[]

for divisor in range(1,numero+1):
    if (numero % divisor) == 0 :
        lista.append(divisor)
        contador += 1
       
print("el numero ",numero," tiene ",contador,"divisores")
print(lista)
