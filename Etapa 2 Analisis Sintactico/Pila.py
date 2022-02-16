class Pila:
    lista = list()

    def push(self, x):
        self.lista.append(x)

    def pop(self):
        x=self.lista.pop()
        return x
    
    def top(self):
        return self.lista[-1]

    def mostrar(self):
        print(self.lista)