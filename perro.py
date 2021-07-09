class Perro():
    def __init__(self, n, e, p):
        self.nombre = n
        self.edad = e
        self.peso = p
        
        
    def ladrar(self):
        if self.peso >= 8:
            print("GUAU, GUAU")
        else:
            print("guau", "guau")
            
    def __str__ (self):
        return "Soy el perro {}".format(self.nombre)

        
clay = Perro("Clay", 100, 10)
print(clay)
gofio = Perro("Gofio", 2, 2)
clay.ladrar()

print(gofio.nombre)
gofio.ladrar()

print(clay)