#Crear un programa que pueda recibir un string de calculos ejemplos "2*2-1"
#la funcion deve ser capas de agarrar el calculo y devolver el resultado
while True:
    def StringToInt(ingreso):
        print(ingreso)
            
    datos = []
    operadores = ['*','+','/','-']

    ingreso = input("ingrese lo que quiere hacer ")

    for i in ingreso:
        if i == '':
            pass
        datos.append(i)




    print(datos)
    StringToInt(ingreso)