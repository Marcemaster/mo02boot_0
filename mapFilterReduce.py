from functools import reduce

lista = [1, 2, 3, 4]

listaDobles = map(lambda x: x*2, lista)


listaPares = filter(lambda x: x % 2 == 0, lista)

sumatorio = reduce(lambda x, y: x + y, lista)

suma100 = reduce(lambda x, y: x + y, range(101))


print(list(listaPares))

print(suma100)