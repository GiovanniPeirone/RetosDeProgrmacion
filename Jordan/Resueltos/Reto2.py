#1
'''
    Crear un progrma que devulva el codigo ASCI de un texto ejemplo:

    Entrada:

    Hola 

    Salida:

    H   o    l  a
    72 111 108 97
'''
import string


text = "Hola" #Esto se puede cambiar

texto = []
for i in text:
    print(ord(i))


AsciiDict = {
    "A" : 66,
    "Z" : 96
    "a" : 97,
    "z" : 122
}

#https://codescracker.com/python/program/python-program-print-ascii-values.htm
#Ese chabon es un genio 