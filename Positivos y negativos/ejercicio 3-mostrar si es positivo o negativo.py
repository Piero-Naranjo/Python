'''
    Realizar un programa que solicite al usuario un numero entero y mostrar si el numero ingresado 
    es positivo o negativo
'''

digito = 0

digito = int((input)("Ingresar un numero : "))


if(digito > 0):
    print(f"El numero {digito} es positivo")
    
if(digito < 0):
    print(f"El numero {digito} es negativo")
    
if(digito ==0):
    print("El numero es cero, vuelva a ingresar el numero ")