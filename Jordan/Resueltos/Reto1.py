# 1
'''
    Crear un Programa que devuelva el acorde mayor de una nota Musical 
    Ejemplo:
    Entrada: Re
    Salida: Re Fa# La
    Aclaracion:
    Los Acordes Mayores se forman de una nota base Eje Re luego 4 
    semitonos hacia arriba (Fa#) y desde el Fa# 3 semitonos hacia arriba (La)
    Notas de una octava:
    0   Do
    1   Do♯ 
    2       Re
    3   Re♯
    4   Mi
    5   Fa
    6       Fa♯
    7   Sol
    8   Sol♯
    9       La
    10  La♯
    11  Si 
    
    Re _ _ _ Fa# _ _ La
'''
# 2, 6, 9
notas = ["Do", "Do♯", "Re", "Re♯", "Mi", "Fa", "Fa♯", "Sol", "Sol♯", "La", "La♯", "Si", "Do", "Do♯", "Re", "Re♯", "Mi", "Fa", "Fa♯"]
for i in range(len(notas)):
            print(i, notas[i])



#   Para copiar el simbolo de sostenido ->      ♯
def AcordeMayor(nota):
    posicion = notas.index(nota)
            
    nota2 = posicion + 4 
    nota3 = posicion + 7
            
    print(nota, notas[nota2], notas[nota3])
    print()
    
while True:
    try:
        nota = input("Ingrese la nota: ")
        AcordeMayor(nota)
    except ValueError():
        continue