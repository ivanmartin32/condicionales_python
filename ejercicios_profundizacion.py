#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    print('Ingrese primer numero')
    numero_1 = float(input())
    print('Ingrese segundo numero')
    numero_2 = float(input())
    resultado = numero_1 - numero_2
    if resultado > 0:
        print('El resultado es positivo')
    elif resultado < 0:
        print('El resultado es negativo')
    else:
        print('El resultado es cero')

def ej2():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    numero_1 = int(input('Ingrese primer numero:\n'))
    numero_2 = int(input('Ingrese segundo numero:\n'))
    numero_3 = int(input('Ingrese tercer numero:\n'))
    
    if numero_1 % 2 == 0:
        print('primer numero es par')
    else:
        print('primer numero es impar')
    if numero_2 % 2 == 0:
        print('segundo numero es par')
    else:
        print('segundo numero es impar')
    if numero_3 % 2 == 0:
        print('tercer numero es par')
    else:
        print('tercer numero es impar')

def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    print('Ingrese primer numero')
    numero1 = float(input())
    print('Ingrese Operador')
    operador = str(input())
    print('Ingrese segundo numero')
    numero2 = float(input())
    if operador == '+':
        resultado = numero1 + numero2
        print('{} {} {} es {}'.format(numero1,operador,numero2,resultado))
    elif operador == '-':
        resultado = numero1 - numero2
        print('{} {} {} es {}'.format(numero1,operador,numero2,resultado))
    elif operador == '*':
        resultado = numero1 * numero2
        print('{} {} {} es {}'.format(numero1,operador,numero2,resultado))
    elif operador == '/':
        resultado = numero1 / numero2
        print('{} {} {} es {}'.format(numero1,operador,numero2,resultado))
    elif operador == '**':
        resultado = numero1 ** numero2
        print('{} {}(Elevado) a {} es {}'.format(numero1,operador,numero2,resultado))

def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    # Use array/listas para este caso

    palabras = [str(input('Ingrese primera palabra \n')),
    str(input('Ingrese segunda palabra \n')),str(input('Ingrese tercera palabra \n'))]
    orden = int(input('Presione 1 para ordenar alfabeticamente de (A-Z) \n'
                      'Presione 2 para ordenar alfabeticamente de (Z-A) \n'
                      'Presione 3 para ordenar por cantidad de letras (-/+) \n'
                      'Presione 4 para ordenar por cantidad de letras (+/-) \n'))
    # En este caso se me ocurrio usarlo con el metodo sort no con operador >
    # y agregar mas opciones
    
    if orden == 1:
        palabras.sort()
        print(palabras)
    elif orden == 2:
        palabras.sort(reverse=True)
        print(palabras)
    elif orden == 3:
        palabras.sort(key=len)
        print(palabras)
    elif orden == 4:
        palabras.sort(key=len, reverse=True)
        print(palabras)

def ej5():
        
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''
    temperatura_1 = float(input('Ingrese primer temperatura \n'))
    temperatura_2 = float(input('Ingrese segunda temperatura \n'))
    temperatura_3 = float(input('Ingrese tercer temperatura \n'))
    datos = int(input('Ingrese 1 para saber la temperatura maxima: \n'
                  'Ingrese 2 para saber la temperatura minima: \n'
                  'Ingrese 3 para saber el promedio: \n'))
    if datos == 1:
        print ('La temperatura maxima es', max(temperatura_1,temperatura_2,temperatura_3))
    elif datos == 2:
        print ('La temperatura minima es', min(temperatura_1,temperatura_2,temperatura_3))
    elif datos == 3:
        print('La temperatura promedio es', (temperatura_1 + temperatura_2 + temperatura_3) / 3)
    
    
if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
