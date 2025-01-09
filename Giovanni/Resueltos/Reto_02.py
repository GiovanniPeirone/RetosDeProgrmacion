



def ordenador(lista1, lista2):
    listaFinal = []

    for i in range(lista1 + lista2):

        if lista1 == i:
            listaFinal += lista1
        if lista2 == i:
            listaFinal += lista2
    return listaFinal


lista1 = [1,2,4]

lista2 = [1,3,4]

print(ordenador(lista1,lista2))