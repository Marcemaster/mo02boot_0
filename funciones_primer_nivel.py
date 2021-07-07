def normal(x):
    return x
def cuadrado(x):
    return x * x


def sumaTodos(limiTo, f):
    resultado = 0
    for i in range (limiTo+1):
        resultado += f(i)
        
    return resultado 
    
if __name__ == '__main__':
    print(sumaTodos(100, normal))
    print(sumaTodos(100, cuadrado))
