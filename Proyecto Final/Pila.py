from Nodo import *
class EP:
    def __init__(self):
        self.data=""

    #def __init__(self, data):
        #self.data=data

    def getData(self):
        return self.data

    def getTipo(self):
        pass

class T(EP):
    def __init__(self, data):
        self.data=data

    def getTipo(self):
        return "T"

class NT(EP):
    def __init__(self, data):
        self.nodo=Nodo()
        self.data=data
        
    def getTipo(self):
        return "NT"

class E(EP):
    def __init__(self, data):
        self.data=data

    def getTipo(self):
        return "E"

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
        #print('\n')
    
    def mostrar_tipos(self):
        for i in range(len(self.lista)):
            self.lista[i].imprimir()
        print('\n')

