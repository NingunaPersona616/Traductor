from urllib.request import AbstractBasicAuthHandler
from Pila import *
from Lexico import TipoToken
from Nodo import *
from collections import deque

#[TipoToken.identificador, TipoToken.add, TipoToken.pesos, E],

class Sintactico:
    
    Arbol=EP()

    def __init__(self, tablaLR, ids, lon, noms):
        self.pila = Pila()
        self.pila.push(T('$'))
        self.pila.push(E(0))
        self.tablaLR1=tablaLR
        self.id_reglas=ids
        self.lon_reglas=lon
        self.nom_NoTerminales=noms


    def prueba(self, input):
        aceptacion=False

        fila=int(self.pila.top().getData())
        columna=input[-1]['tipo']
        accion=self.tablaLR1[fila][columna]

        while(aceptacion==False and accion!=0):
            if(accion>0):
                simbolo=input.pop()#Siguiente elemento de la entrada
                self.pila.push(T(simbolo['lexema'])) #Terminal
                self.pila.push(E(accion)) #Estado
                self.pila.mostrar()
                print("\n")

            elif(accion<0):
                if(accion==-1):
                    aceptacion=True
                    self.pila.pop()
                    self.Arbol=self.pila.pop()
                    print(self.Arbol.getData())
                    break
                else:
                    nodo = Nodo()
                    pos=(accion*-1)-2
                    cant_pops=self.lon_reglas[pos]*2 #idea:pos=(accion * -1)-2
                    
                    if(cant_pops>0):
                        for i in range(cant_pops):
                            if(i%2 != 0):
                                nodo.insertarElemento(self.pila.top())  #Se insertan los elementos de la regla en el nodo
                            self.pila.pop()

                    fila=int(self.pila.top().getData())
                    columna=self.id_reglas[pos]#No terminal
                    accion=self.tablaLR1[fila][columna]

                    #Se define el nombre de la regla, su id, y la cant de elementos que contiene
                    nodo.SetRegla(self.nom_NoTerminales[pos])
                    #nodo.SetNum_Regla(self.id_reglas[pos])
                    nodo.SetNum_Regla(pos+1)
                    nodo.SetNum_Elementos(int(cant_pops/2))

                    #Se inserta el nodo en el arbol
                    #self.Arbol.append(nodo)
                    noTerminal=NT(self.nom_NoTerminales[pos])
                    noTerminal.nodo=nodo
                    #nodo=""

                    self.pila.push(noTerminal)
                    self.pila.push(E(accion))
                    self.pila.mostrar()
                    print("--R"+str(self.id_reglas[pos]), "\n")
                
            else:
                break

            fila=int(self.pila.top().getData()) #Tope de la Pila
            columna=input[-1]['tipo']     #Tipo de simbolo del siguiente elemento de la entrada
            accion=self.tablaLR1[fila][columna]     

        return aceptacion    