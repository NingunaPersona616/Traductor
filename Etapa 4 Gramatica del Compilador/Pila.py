class EP:
    def __init__(self, data):
        self.data=data

    def getData(self):
        return self.data

    def imprimir(self):
        pass

class T(EP):
    def imprimir(self):
        print("T", end=" ")

class NT(EP):
    def imprimir(self):
        print("NT", end=" ")

class E(EP):
    def imprimir(self):
        print("E", end=" ")

class Pila:
    def __init__(self):
        self.lista = list()

    def push(self, x):
        self.lista.append(x)

    def pop(self):
        x=self.lista.pop()
        return x
    
    def top(self):
        return self.lista[-1]

    def mostrar(self):
        for i in range(len(self.lista)):
            print(self.lista[i].getData(), end=" ")
        print('\n')
    
    def mostrar_tipos(self):
        for i in range(len(self.lista)):
            self.lista[i].imprimir()
        print('\n')

