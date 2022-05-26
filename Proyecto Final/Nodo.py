from collections import deque

class Nodo:
    #elementos=[]
    nodo=""
    num_regla=""
    regla=""
    num_elementos=""
    sangria=0

    def __init__(self):
        self.elementos=deque()
    
    def imprimir(self, san):
        self.sangria=san

        for i in range(len(self.elementos)):#Imprime los elementos del nodo hasta encontrar otro nodo y de ahi imprime recursivamente los elementos del nodo hijo
            print(self.elementos[i].getData(), end=" ")
            if(self.elementos[i].getTipo()=="NT"):
                print("\n")
                san+=1
                print("  "*self.sangria, end="")
                self.elementos[i].nodo.imprimir(san)
        
        #print("\n")
     
    def insertarElemento(self, e):
        self.elementos.appendleft(e)

    def GetElemento(self, index):
        return self.elementos[index]

    def SetRegla(self, r):
        self.regla=r

    def GetRegla(self):
        return self.regla

    def SetNum_Regla(self, r):
        self.num_regla=r

    def GetNum_Regla(self):
        return self.num_regla

    def SetNum_Elementos(self, num):
        self.num_elementos=num

    def GetNum_Elementos(self):
        return self.num_elementos