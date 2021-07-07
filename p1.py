def sumaTodos(limiTo):
    resultado = 0
    for i in range(0, limiTo+1):
        resultado += 1
        
    return resultado

def sumaTodosCuadrados(limiTo):
    resultado = 0
    for i in range(0, limiTo+1):
        resultado += 1*i
        
    return resultado

print(sumaTodosCuadrados(100))
print(sumaTodos(100))