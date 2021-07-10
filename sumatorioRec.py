def sumatorio(n):
    
    if n > 0:
        return n + sumatorio(n-1)
    else:
        return 0
    
s = sumatorio(5)
print(s)


def factorial(n):
    
    if n > 0:
        return n * factorial(n-1)
    else:
        return 1
    
f = factorial(5)
print(f)