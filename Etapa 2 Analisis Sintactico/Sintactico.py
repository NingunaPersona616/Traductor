from Pila import Pila
from Lexico import TipoToken


#[TipoToken.identificador, TipoToken.add, TipoToken.pesos, E],

class Sintactico:
    pila = Pila()
    entrada=""
    tablaLR1=[]
    id_reglas=[]
    lon_reglas=[]

    def __init__(self, tablaLR, ids, lon):
        self.pila.push("$")
        self.pila.push("0")
        self.tablaLR1=tablaLR
        self.id_reglas=ids
        self.lon_reglas=lon

    def ejercicio1(self, input):
        aceptacion=False

        fila=int(self.pila.top())
        columna=input[-1]['tipo']
        accion=tablaLR1[fila][columna]

        simbolo=input.pop()
        self.pila.push(simbolo['lexema'])
        self.pila.push(accion)
        self.pila.mostrar()

        fila=int(self.pila.top())
        columna=input[-1]['tipo']
        accion=tablaLR1[fila][columna]

        simbolo=input.pop()
        self.pila.push(simbolo['lexema'])
        self.pila.push(accion)
        self.pila.mostrar()

        fila=int(self.pila.top())
        columna=input[-1]['tipo']
        accion=tablaLR1[fila][columna]

        simbolo=input.pop()
        self.pila.push(simbolo['lexema'])
        self.pila.push(accion)
        self.pila.mostrar()

        fila=int(self.pila.top())
        columna=input[-1]['tipo']
        accion=tablaLR1[fila][columna]

        if(accion<0):
            cant_pops=ej1_regla*2
            for i in range(cant_pops):
                self.pila.pop()

            fila=int(self.pila.top())
            columna=E
            accion=tablaLR1[fila][columna]
            self.pila.push("E")
            self.pila.push(accion)

        self.pila.mostrar()

        fila=int(self.pila.top())
        columna=input[-1]['tipo']
        accion=tablaLR1[fila][columna]
        if(accion==-1):
            aceptacion=True

        return aceptacion

    def prueba(self, input):
        aceptacion=False

        fila=int(self.pila.top())
        columna=input[-1]['tipo']
        accion=self.tablaLR1[fila][columna]#self
        while(aceptacion==False and accion!=0):
            if(accion>0):
                simbolo=input.pop()
                self.pila.push(simbolo['lexema'])
                self.pila.push(accion)
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

                    fila=int(self.pila.top())
                    columna=self.id_reglas[pos]#No terminal
                    accion=self.tablaLR1[fila][columna]#self
                    self.pila.push(self.id_reglas[pos])
                    self.pila.push(accion)
                    self.pila.mostrar()
                
            else:
                break

            fila=int(self.pila.top())
            columna=input[-1]['tipo']
            accion=self.tablaLR1[fila][columna]#self

        return aceptacion    