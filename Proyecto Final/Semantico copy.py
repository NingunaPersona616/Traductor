from math import fabs
from numpy import amax, true_divide
from Nodo import Nodo

class Simbolo:
    #1 - PARA VARIABLE, 2 -  PARA FUNCION, 3 Parametros

    def __init__(self):
        id=0
        nombre=""
        tipo=""
        ambito=""

    def setId(self, id):
        self.id=id

    def setNombre(self, n):
        self.nombre=n

    def setTipo(self, t):
        self.tipo=t

    def setAmbito(self, a):
        self.ambito=a

    def getId(self):
        return self.id
	
    def getNombre(self):
        return self.nombre
    
    def getTipo(self):
        return self.tipo
    
    def getAmbito(self):
        return self.ambito

    def imprimir(self):
        print("Tipo:", self.tipo, ", Nombre: ", self.nombre)

class Semantico:
    def __init__(self):
        self.Arbol=Nodo()
        self.ListaSimbolos=list()
        self.ListaErrores=list()
    
    def Analizar_Nodo(self, nodo):
        AmbitoActual="Global"
        TipoDato_Actual=""
        for i in range(len(self.Arbol)):
            #Tomar el primer nodo
            nodo_aux=self.Arbol.pop()
            #toma el numero de la regla
            regla=nodo_aux.GetNum_Regla()

            print("Num_Regla=",regla,", Nom_Regla=",nodo_aux.GetRegla(),", Cant Elemts=",str(nodo_aux.GetNum_Elementos()))

            #Switchea la regla y busca definiciones de variables, funciones y parametros
            if(regla==29):
                #Declara el tipo de Simbolo(Funcion) y le asigna el ambito actual
                simbolo=""
                simbolo=Simbolo()
                simbolo.setId(2)
                simbolo.setAmbito(AmbitoActual)

                #Toma el terminal y de ahi el tipo de dato que regresa la funcion
                ep_aux=nodo_aux.GetElemento()
                nodo_aux.PopElemento()
                simbolo.setTipo(ep_aux.getData())

                #Declara el nuevo ambiente con el nombre de la funcion
                ep_aux=nodo_aux.GetElemento()
                nodo_aux.PopElemento()
                simbolo.setNombre(ep_aux.getData())
                AmbitoActual=simbolo.getNombre()

                simbolo.imprimir()
                #Si la funcion ya ha sido declarada se agrega un error
                if(self.buscaSimbolo(simbolo.getNombre(), simbolo.getAmbito())==True):
                    error="La funcion"+simbolo.getNombre()+"Ya ha sido declarada anteriormente en el ambito: "+simbolo.getAmbito()
                    self.ListaErrores.append(error)
                #Si no ha sido declarada se agrega a la lista de simbolos
                else:
                    self.ListaSimbolos.append(simbolo)

            if(regla==27):
                if(nodo_aux.GetNum_Elementos()==4):
                    #Declara el tipo de simbolo(VAR)
                    new_var=""
                    new_var=Simbolo()
                    new_var.setId(1)

                    #Declara el ambito de la variable
                    new_var.setAmbito(AmbitoActual)

                    #Toma el Terminal y Declara el tipo de dato de la variable
                    ep_aux=nodo_aux.PopElemento()
                    new_var.setTipo(ep_aux.getData())
                    TipoDato_Actual=new_var.getTipo()

                    #Toma el nombre de la variable
                    ep_aux=nodo_aux.PopElemento()
                    new_var.setNombre(ep_aux.getData())

                    new_var.imprimir()
                    if(self.buscaSimbolo(new_var.getNombre(), new_var.getAmbito())==True):
                        error="La variable"+new_var.getNombre()+"Ya ha sido declarada anteriormente en el ambito: "+new_var.getAmbito()
                        self.ListaErrores.append(error)
                    #Si no ha sido declarada se agrega a la lista de simbolos
                    else:
                        self.ListaSimbolos.append(new_var)

            if(regla==28):
                if(nodo_aux.GetNum_Elementos()==3):
                    new_var=Simbolo()
                    new_var.setId(1)

                    #Declara el ambito de la variable y el tipo de dato
                    new_var.setAmbito(AmbitoActual)
                    new_var.setTipo(TipoDato_Actual)

                    #quita la coma
                    nodo_aux.PopElemento()
                    
                    #Toma el nombre de la variable
                    ep_aux=nodo_aux.PopElemento()
                    new_var.setNombre(ep_aux.getData())

                    new_var.imprimir()
                    if(self.buscaSimbolo(new_var.getNombre(), new_var.getAmbito())==True):
                        error="La variable"+new_var.getNombre()+"Ya ha sido declarada anteriormente en el ambito: "+new_var.getAmbito()
                        self.ListaErrores.append(error)
                    #Si no ha sido declarada se agrega a la lista de simbolos
                    else:
                        self.ListaSimbolos.append(new_var)

            if(regla==30):
                if(nodo_aux.GetNum_Elementos()==3):
                    #Declaramos el tipo de simbolo
                    new_var=Simbolo()
                    new_var.setId(1)

                    #Declaramos el ambito del simbolo(VAR)
                    new_var.setAmbito(AmbitoActual)

                    #Toma el terminal y declara el tipo de dato
                    ep_aux=nodo_aux.PopElemento()
                    new_var.setTipo(ep_aux.getData())

                    #Toma otro terminal y declara el nombre de la variable
                    ep_aux=nodo_aux.PopElemento()
                    new_var.setNombre(ep_aux.getData())

                    new_var.imprimir()
                    if(self.buscaSimbolo(new_var.getNombre(), new_var.getAmbito())==True):
                        error="La variable"+new_var.getNombre()+"Ya ha sido declarada anteriormente en el ambito: "+new_var.getAmbito()
                        self.ListaErrores.append(error)
                    #Si no ha sido declarada se agrega a la lista de simbolos
                    else:
                        self.ListaSimbolos.append(new_var)

            if(regla==31):
                if(nodo_aux.GetNum_Elementos()==4):
                    #Declaramos el tipo de simbolo
                    new_var=Simbolo()
                    new_var.setId(1)

                    #Declaramos el ambito del simbolo(VAR)
                    new_var.setAmbito(AmbitoActual)

                    #Quita una coma
                    nodo_aux.PopElemento()

                    #Toma el terminal y declara el tipo de dato
                    ep_aux=nodo_aux.PopElemento()
                    new_var.setTipo(ep_aux.getData())

                    #Toma otro terminal y declara el nombre de la variable
                    ep_aux=nodo_aux.PopElemento()
                    new_var.setNombre(ep_aux.getData())

                    new_var.imprimir()
                    if(self.buscaSimbolo(new_var.getNombre(), new_var.getAmbito())==True):
                        error="La variable"+new_var.getNombre()+"Ya ha sido declarada anteriormente en el ambito: "+new_var.getAmbito()
                        self.ListaErrores.append(error)
                    #Si no ha sido declarada se agrega a la lista de simbolos
                    else:
                        self.ListaSimbolos.append(new_var)

    def buscaSimbolo(self, nombre, ambito):
        for i in range(len(self.ListaSimbolos)):
            if(self.ListaSimbolos[i].getNombre()==nombre and self.ListaSimbolos[i].getAmbito == ambito):
                return True
        return False

    def printTabalSimbolos(self):
        for i in range(len(self.ListaSimbolos)):
            self.ListaSimbolos[i].imprimir()

lista=[]

lista.append('1')
lista.append('2')
lista.append('3')
lista.append('4')
lista.append('5')

print(lista)

lista.pop()

print(lista)