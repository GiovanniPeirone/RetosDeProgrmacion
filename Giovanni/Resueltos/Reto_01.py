def entero_a_romano(numero):
    simbolos = [
        ["M", 1000],
        ["CM", 900],
        ["D", 500],
        ["CD", 400],
        ["C", 100],
        ["XC", 90],
        ["L", 50],
        ["XL", 40],
        ["X", 10],
        ["IX", 9],
        ["V", 5],
        ["IV", 4],
        ["I", 1]
    ]

    numero_romano = ""

    for simbolo, valor in simbolos:
        while numero >= valor:
            

            numero_romano += simbolo  # Agrega el símbolo correspondiente
            numero -= valor  # Resta el valor correspondiente del número



    return numero_romano

# Ejemplo de uso
numero = 679
resultado = entero_a_romano(numero)
print(f"El número {numero} en romano es: {resultado}")