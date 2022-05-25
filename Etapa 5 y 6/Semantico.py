from Nodo import Nodo

R6=6
R8=8
R9=9
R11=11
R13=13
R14=14
R21=21
R36=36
R40=40
R47=47

class Simbolo:
    #V - PARA VARIABLE, F -  PARA FUNCION, P -PARA Parametros

    def __init__(self):
        id=""
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
        if(self.getId()=="F"):
            print("Funcion: " + self.tipo + " " + self.nombre + ", Ambito:" + self.ambito+".")
        elif(self.getId()=="V"):
            print("Variable: " + self.tipo + " " + self.nombre + ", Ambito:" + self.ambito+".")
        if(self.getId()=="P"):
            print("Parametro: " + self.tipo + " " + self.nombre + ", Ambito:" + self.ambito+".")

class Semantico:
    def __init__(self):
        self.Arbol=Nodo()
        self.ListaSimbolos=list()
        self.ListaErrores=list()
        self.AmbitoActual="Global"
        self.TipoDato_Actual=""
    
    def Analizar_Nodo(self, nodo_aux):
        
        #print("Num_Regla=",nodo_aux.GetNum_Regla(),", Nom_Regla=",nodo_aux.GetRegla(),", Cant Elemts=",str(nodo_aux.GetNum_Elementos()))
        for elemento in (nodo_aux.elementos):   #Revisa en los hijos del nodo si hay otro nodo

            # si es el fin de una funcion setea el ambito a global
            if(elemento.getData()=='}' and nodo_aux.GetNum_Regla()==R14):
                self.AmbitoActual="Global"

            #Revisa si es un nodo(No terminal)
            if(elemento.getTipo()=="NT"):#Si sí es un nodo revisa si es una de las reglas a validar y si es asi revisa los elemento del nodo hijo y sigue le recorrido por el nodo hijo
                regla=elemento.nodo.GetNum_Regla()#toma el numero de la regla

                #Switchea la regla y busca definiciones de variables, funciones y parametros
                if(regla==R9):#R9 <DefFunc> ::= tipo identificador ( <Parametros> ) <BloqFunc>
                    #Declara el tipo de Simbolo(Funcion) y le asigna el ambito actual
                    simbolo=""
                    simbolo=Simbolo()
                    simbolo.setId("F")
                    simbolo.setAmbito("Global")

                    #Toma el terminal y de ahi el tipo de dato que regresa la funcion
                    ep_aux=elemento.nodo.GetElemento(0)#0
                    simbolo.setTipo(ep_aux.getData())

                    #Declara el nuevo ambito con el nombre de la funcion
                    ep_aux=elemento.nodo.GetElemento(1)#1
                    simbolo.setNombre(ep_aux.getData())
                    self.AmbitoActual=simbolo.getNombre()

                    #simbolo.imprimir()
                    #Si la funcion ya ha sido declarada se agrega un error
                    if(self.buscaSimbolo(simbolo.getNombre(), simbolo.getAmbito(), simbolo.getTipo())==True):
                        error="La funcion: "+ simbolo.getTipo()+ " " +simbolo.getNombre()+"() Ya ha sido declarada anteriormente en el ambito: "+simbolo.getAmbito()
                        self.ListaErrores.append(error)
                    #Si no ha sido declarada se agrega a la lista de simbolos
                    else:
                        self.ListaSimbolos.append(simbolo)

                if(regla==R6):#R6 <DefVar> ::= tipo identificador <ListaVar> ;
                    #if(elemento.nodo.GetNum_Elementos()==4):
                    #Declara el tipo de simbolo(VAR)
                    new_var=""
                    new_var=Simbolo()
                    new_var.setId("V")

                    #Declara el ambito de la variable
                    new_var.setAmbito(self.AmbitoActual)

                    #Toma el Terminal y Declara el tipo de dato de la variable
                    ep_aux=elemento.nodo.GetElemento(0)#0
                    new_var.setTipo(ep_aux.getData())
                    self.TipoDato_Actual=new_var.getTipo()

                    #Toma el nombre de la variable
                    ep_aux=elemento.nodo.GetElemento(1)#1
                    new_var.setNombre(ep_aux.getData())

                    #new_var.imprimir()
                    if(self.buscaSimbolo(new_var.getNombre(), new_var.getAmbito())==True):
                        error="La variable: "+ new_var.getTipo()+ " " +new_var.getNombre()+", Ya ha sido declarada anteriormente en el ambito: "+new_var.getAmbito()
                        self.ListaErrores.append(error)
                    #Si no ha sido declarada se agrega a la lista de simbolos
                    else:
                        self.ListaSimbolos.append(new_var)

                if(regla==R8):#R8 <ListaVar> ::= , identificador <ListaVar>
                    #if(elemento.nodo.GetNum_Elementos()==3):
                    new_var=Simbolo()
                    new_var.setId("V")

                    #Declara el ambito de la variable y el tipo de dato
                    new_var.setAmbito(self.AmbitoActual)
                    new_var.setTipo(self.TipoDato_Actual)

                    #quita la coma
                    #Toma el nombre de la variable
                    ep_aux=elemento.nodo.GetElemento(1)#1
                    new_var.setNombre(ep_aux.getData())

                    #new_var.imprimir()
                    if(self.buscaSimbolo(new_var.getNombre(), new_var.getAmbito())==True):
                        error="La variable: "+ new_var.getTipo()+ " " +new_var.getNombre()+", Ya ha sido declarada anteriormente en el ambito: "+new_var.getAmbito()
                        self.ListaErrores.append(error)
                    #Si no ha sido declarada se agrega a la lista de simbolos
                    else:
                        self.ListaSimbolos.append(new_var)

                if(regla==R11):#R11 <Parametros> ::= tipo identificador <ListaParam>
                    #if(elemento.nodo.GetNum_Elementos()==3):
                    #Declaramos el tipo de simbolo
                    new_var=Simbolo()
                    new_var.setId("P")

                    #Declaramos el ambito del simbolo(VAR)
                    new_var.setAmbito(self.AmbitoActual)

                    #Toma el terminal y declara el tipo de dato
                    ep_aux=elemento.nodo.GetElemento(0)#0
                    new_var.setTipo(ep_aux.getData())

                    #Toma otro terminal y declara el nombre de la variable
                    ep_aux=elemento.nodo.GetElemento(1)#1
                    new_var.setNombre(ep_aux.getData())

                    #new_var.imprimir()
                    if(self.buscaSimbolo(new_var.getNombre(), new_var.getAmbito())==True):
                        error="La variable: "+ new_var.getTipo()+ " " +new_var.getNombre()+", Ya ha sido declarada anteriormente en el ambito: "+new_var.getAmbito()
                        self.ListaErrores.append(error)
                    #Si no ha sido declarada se agrega a la lista de simbolos
                    else:
                        self.ListaSimbolos.append(new_var)

                if(regla==R13):#R13 <ListaParam> ::= , tipo identificador <ListaParam>
                    #if(elemento.nodo.GetNum_Elementos()==4):
                    #Declaramos el tipo de simbolo
                    new_var=Simbolo()
                    new_var.setId("P")

                    #Declaramos el ambito del simbolo(VAR)
                    new_var.setAmbito(self.AmbitoActual)

                    #Quita una coma
                    #Toma el terminal y declara el tipo de dato
                    ep_aux=elemento.nodo.GetElemento(1)#1
                    new_var.setTipo(ep_aux.getData())

                    #Toma otro terminal y declara el nombre de la variable
                    ep_aux=elemento.nodo.GetElemento(2)#2
                    new_var.setNombre(ep_aux.getData())

                    #new_var.imprimir()
                    if(self.buscaSimbolo(new_var.getNombre(), new_var.getAmbito())==True):
                        error="La variable: "+ new_var.getTipo()+ " " +new_var.getNombre()+", Ya ha sido declarada anteriormente en el ambito: "+new_var.getAmbito()
                        self.ListaErrores.append(error)
                    #Si no ha sido declarada se agrega a la lista de simbolos
                    else:
                        self.ListaSimbolos.append(new_var)

                if (regla==R21):#R21 <Sentencia> ::= identificador = <Expresion> ;
                    identificador=elemento.nodo.GetElemento(0)
                    if(self.buscaSimbolo(identificador.getData(), self.AmbitoActual)==False):
                        error="La variable: "+ identificador.getData() +" no ha sido declarada anteriormente"
                        self.ListaErrores.append(error)

                if (regla==R36):#R36 <Termino> ::= identificador
                    identificador=elemento.nodo.GetElemento(0)
                    if(self.buscaSimbolo(identificador.getData(), self.AmbitoActual)==False):
                        error="La variable: "+ identificador.getData() +" no ha sido declarada anteriormente"
                        self.ListaErrores.append(error)

                if(regla==R40):#R40 <LlamadaFunc> ::= identificador ( <Argumentos> ) 
                    identificador=elemento.nodo.GetElemento(0)
                    if(self.buscaSimbolo(identificador.getData(), "Global")==False):
                        error="La funcion: "+ identificador.getData() +"() no ha sido declarada anteriormente"
                        self.ListaErrores.append(error)


                #Continua con el recorrido del arbol
                self.Analizar_Nodo(elemento.nodo)


    def buscaSimbolo(self, nombre, ambito, tipo="int"):
        #print("????????????" + nombre + ", " + ambito + ".")
        existe=False
        for i in range(len(self.ListaSimbolos)):
            #print("????????????", end="")
            #self.ListaSimbolos[i].imprimir()
            if(self.ListaSimbolos[i].getNombre()==nombre and self.ListaSimbolos[i].getAmbito() == ambito):
                if(self.ListaSimbolos[i].getId()=="V" or self.ListaSimbolos[i].getId()=="P"):   #Si una variable o un parametro tienen el mismo nombre o el nombre de una funcion en el mismo ambito ES QUE YA EXISTE
                    return True
                if(self.ListaSimbolos[i].getId()=="F" and self.ListaSimbolos[i].getTipo()==tipo):   #Si una funcion tien el mismo nombre y tipo de dato ES QUE YA EXISTE
                    return True
                #else:
                    #existe=False
                #return True
        return False
        #return existe

    def imprimir_ListaSimbolos(self):
        for i in range(len(self.ListaSimbolos)):
            self.ListaSimbolos[i].imprimir()

    def imprimir_ListaErrores(self):
        for i in range(len(self.ListaErrores)):
            print(self.ListaErrores[i])
