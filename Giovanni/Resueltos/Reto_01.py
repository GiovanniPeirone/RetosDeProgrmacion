
def entero_a_romano(numero):
    # Lista de símbolos romanos y sus valores correspondientes
    simbolos = [
        ["M", 1000],
        ["D", 500],
        ["C", 100],
        ["L", 50],
        ["X", 10],
        ["V", 5],
        ["I", 1]
    ]

    numero_romano = ""  # Cadena para construir el número romano

    # Mientras el número a convertir sea mayor que 0
    for simbolo, valor in simbolos:
        while numero >= valor:
            numero_romano += simbolo
            numero -= valor

    return numero_romano

# Ejemplo de uso
numero_a_convertir = 679
resultado = entero_a_romano(numero_a_convertir)
print(f"El número {numero_a_convertir} en romano es: {resultado}")