def find(lista1, lista2):
    listaUnificada = []

    listaUnificada += lista1 + lista2
    listaUnificada = sorted(listaUnificada)  
    
    n = len(listaUnificada)
    
    if n % 2 == 1:  
        return listaUnificada[n // 2]  
    else:  
        return (listaUnificada[n // 2 - 1] + listaUnificada[n // 2]) / 2  

# Ejemplo de uso
lista1 = [1, 2]
lista2 = [3 ,4]

print(find(lista1, lista2))  # Debería devolver 2