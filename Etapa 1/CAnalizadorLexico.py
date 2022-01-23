
class CAnalizadorLexico:
    Input=""
    StillContinue=False
    Index=0
    AnalizedString=""

    def CAnalizadorLexico(self, Input):
        self.Input=Input
    
    def ReadInput(self, Input):
        self.Input=Input

    def NextChar(self):
        c=self.Input[self.Index]
        self.Index+=1

        return c

    def Analize(self):
        State=0
        simbol=""
        StillContinue=True

        #Aqui deberia ir un automata?

        
        #Encuentra Identificadores y palabras reservadas
        if(self.Input[0].isalpha()):
            isIdentifier=True
            for i in range(1, len(self.Input)):
                if((self.Input[i].isalpha()==False) and (self.Input[i].isnumeric()==False)):
                    isIdentifier=False

            if(isIdentifier==True):
                if(self.Input=="if"):
                    return 19

                elif(self.Input=="while"):
                    return 20

                elif(self.Input=="return"):
                    return 21
                
                elif(self.Input=="else"):
                    return 22
                
                elif(self.Input=="int" or self.Input=="float" or self.Input=="void"):
                    return 4

                else:
                    return 0
            
            else:
                print('Mamo')
                return 23
        
        #Encuentra Enteros
        elif(self.Input.isnumeric()==True):
            return 1

        #Encuentra Reales
        elif(self.Input.find('.') != -1):
            isReal=True
            StrAux=self.Input.split('.', 1)

            for i in range(len(StrAux)):
                for j in range(len(StrAux[i])):
                    if(StrAux[i][j].isnumeric()==False):
                        isReal=False

            if(isReal):
                return 2
            
            else:
                return 23

        #Encuentra Cadenas
        elif(self.Input[0]=='"'):
            if(self.Input[len(self.Input)-1]=='"'):
                return 3
            
            return 23

        #Encuentra OpSuma
        elif(self.Input=='+' or self.Input=='-'):
            return 5
        
        #Encuentra OpMul
        elif(self.Input=='/' or self.Input=='*'):
            return 6

        #Encuentra OpRel
        elif(self.Input=='<' or self.Input=='>' or self.Input=='<=' or self.Input=='>='):
            return 7
        
        #Encuentra OpOR
        elif(self.Input=='||'):
            return 8

        #Encuentra OpAND
        elif(self.Input=='&&'):
            return 9

        #Encuentra OpNOT
        elif(self.Input=='!'):
            return 10

        #Encuentra OpIgualdad
        elif(self.Input=='!=' or self.Input=='=='):
            return 11

        #Encuentra ;
        elif(self.Input==';'):
            return 12

        #Encuentra '
        elif(self.Input=="'"):
            return 13

        #Encuentra (
        elif(self.Input=="("):
            return 14

        #Encuentra )
        elif(self.Input==")"):
            return 15

        #Encuentra {
        elif(self.Input=="{"):
            return 16

        #Encuentra }
        elif(self.Input=="}"):
            return 17

        #Encuentra }
        elif(self.Input=="="):
            return 18

        else:
            return 23

    
    def ShowType(self, Type):

        print("\n-------------------------------------------------------------------")
        print("Entrada: ", self.Input, "\n\nTipo:")

        if(Type==0):
            print("Identificador")

        elif(Type==1):
            print("Entero")

        elif(Type==2):
            print("Real")

        elif(Type==3):
            print("Cadena")

        elif(Type==4):
            print("Tipo de Dato")

        elif(Type==5):
            print("Operador de Suma")

        elif(Type==6):
            print("Operador de Multiplicacion/Division")

        elif(Type==7):
            print("Operadores Relacionales")

        elif(Type==8):
            print("Operador OR")

        elif(Type==9):
            print("Operador AND")
        
        elif(Type==10):
            print("Operador NOT")

        elif(Type==11):
            print("Operador Igualdad")

        elif(Type==12):
            print("Punto y coma")

        elif(Type==13):
            print("Comilla")

        elif(Type==14):
            print("Parentesis Inicial")

        elif(Type==15):
            print("Parentesis Final")

        elif(Type==16):
            print("Llave inicial")

        elif(Type==17):
            print("Llave final")

        elif(Type==18):
            print("Igualdad")

        elif(Type==19):
            print("Palabra reservada: IF")

        elif(Type==20):
            print("Palabra reservada: WHILE")

        elif(Type==21):
            print("Palabra reservada: RETURN")

        elif(Type==22):
            print("Palabra reservada: ELSE")

        elif(Type==23):
            print("Error o Fin de Entrada")