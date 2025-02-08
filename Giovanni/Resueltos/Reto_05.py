
def encontrarSubconjuntos(conjunto, objetivo):
    for i in range(conjunto):
        if conjunto[i] == objetivo:
            return [[objetivo], conjunto - i]

print(encontrarSubconjuntos([2,4,6,10],16))
