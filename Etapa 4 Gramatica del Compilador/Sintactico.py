from Pila import *
from Lexico import TipoToken


#[TipoToken.identificador, TipoToken.add, TipoToken.pesos, E],

class Sintactico:
    
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

            elif(accion<0):
                if(accion==-1):
                    aceptacion=True
                    break
                else:
                    pos=(accion*-1)-2
                    cant_pops=self.lon_reglas[pos]*2 #idea:pos=(accion * -1)-2
                    for i in range(cant_pops):
                        self.pila.pop()

                    fila=int(self.pila.top().getData())
                    columna=self.id_reglas[pos]#No terminal
                    accion=self.tablaLR1[fila][columna]

                    self.pila.push(NT(self.nom_NoTerminales[pos]))
                    self.pila.push(E(accion))
                    self.pila.mostrar()
                
            else:
                break

            fila=int(self.pila.top().getData()) #Tope de la Pila
            columna=input[-1]['tipo']     #Tipo de simbolo del siguiente elemento de la entrada
            accion=self.tablaLR1[fila][columna]     

        return aceptacion    