

def romano_a_entero():

    numeroAComvertir = 679

    simbolos = [
        ["I", 1],
        ["V", 5],
        ["X", 10],
        ["L", 50],
        ["C", 100],
        ["D", 500],
        ["M", 1000]
    ]

    nuevoNmeroRomano = ""

    while True:

        if nuevoNmeroRomano == 0:
            break

        for i in simbolos:
            if numeroAComvertir >= simbolos[1][i]:
                nuevoNmeroRomano += simbolos[0][i]
                numeroAComvertir = numeroAComvertir - simbolos[1][i]


    return nuevoNmeroRomano

romano_a_entero()