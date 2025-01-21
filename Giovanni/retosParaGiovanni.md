Retos para Giovanni


# 1

El primer desafio es hacer un programa para convertir numeros enteros a numeros romanos
Simbolo 	Valor
    I	        1
    V	        5
    X	        10
    L	        50
    C	        100
    D	        500
    M	        1000
Con el cual si yo ingreso el valor 679 = DCLXXIX

------------------------------------------------
# 2

El segundo desafio es hacer un programa para ordenar los valores de dos listas ordenadas, podes optar por usar listas enlazadas.

    Test1
    lista1 = [1,2,4]
    lista2 = [1,3,4]

    Salida Esperada: [1,1,2,3,4,4]

    Test2
    lista1 = []
    lista2 = [0]
    Salida Esperada: [0]

Restricciones: 
    - Ambas listas deben estar en orden no decreciente

------------------------------------------------
# 3

El tercer desafio es hacer un programa para encontrar la mediana de dos listas ordenadas nums1 y nums2 de tamaño m y n respectivamente.
m -> nums1
n -> nums2

    Test1
    nums1 = [1,3]
    nums2 = [2]
    Salida Esperada: 2.0

    Test2
    nums1 = [1,2]
    nums2 = [3,4]
    Salida Esperada: 2.5

# 4

El cuarto desafio es hacer un programa para encontrar el valor restante de las divisiones que realizara una funcion.

numero -> Argumento que se va a usar para ser el numero a dividir
veces  -> Argumento que se va a usar para ser la cantidad de veces que se dividira el numero

La función debe ser llamada dividiendo(numero, veces)

    Test1
    numero = 38
    veces  = 4
    Salida Esperada = 2

Esto por que salteamos los numeros decimales, siendo que los pasos:
    38 / 2 = 19
    19 / 2 = 9.5
    9  / 2 = 4.5
    4  / 2 = 2
    Y se completan las 4 divisiones

    Test2
    numero = 10
    veces  = 1
    Salida Esperada = 5

TODOS LOS numero SE DEBEN DIVIDIR POR 2