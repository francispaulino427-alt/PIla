class Cuaderno:
    def __init__(self, numero):
        self.numero = numero
        self.siguiente = None



class PilaCuadernos:
    def __init__(self):
        self.tope = None

    
    def apilar(self, numero):
        nuevo = Cuaderno(numero)
        nuevo.siguiente = self.tope
        self.tope = nuevo

    
    def desapilar(self):
        if self.tope is None:
            print("La pila esta vacia.")
            return None

        cuaderno_retirado = self.tope
        self.tope = self.tope.siguiente

        return cuaderno_retirado.numero

    
    def peek(self):
        if self.tope is None:
            print("La pila esta vacia.")
        else:
            print("Cuaderno en el tope:", self.tope.numero)

    
    def mostrar(self):
        actual = self.tope

        while actual is not None:
            print(actual.numero, end=" -> ")
            actual = actual.siguiente

        print("None")





pila = PilaCuadernos()

pila.apilar(1)
pila.apilar(2)
pila.apilar(3)
pila.apilar(4)


print("Contenido de la pila:")
pila.mostrar()


pila.peek()

retirado = pila.desapilar()
print("Cuaderno retirado:", retirado)


print("Contenido de la pila despues de desapilar:")
pila.mostrar()
