import enum

class TipoToken():
    identificador=0
    entero=1
    real=2
    string=3
    tipo=4
    opSuma=5
    opMul=6
    opRel=7
    opOR=8
    opAND=9
    opNOT=10
    opIgualdad=11
    puntoComa=12
    coma=13
    parent_ini=14
    parent_fin=15
    llave_ini=16
    llave_fin=17
    equal=18
    IF=19
    WHILE=20
    RETURN=21
    ELSE=22
    pesos=23

class Lexico:
    edo=0
    index=0
    continua=False
    tipo=-1
    temp=""
    
    def lex(self,cadena):
        edo=0
        self.continua=True
        self.temp=""
        #En simples palabras es el automata, termina si encuentra un caracter no valido o fin de cadena
        while(self.continua and self.index<len(cadena)):
            c=cadena[self.index]

            if((c==' ' or c=='\n') and edo!=4):
                #print("q pedo")
                self.index+=1
                break

            if(edo==0):
                if(c>='0' and c<='9'):
                    edo=1
                    self.temp+=c

                elif(c>='a' and c<='z' or c>='A' and c<='Z' or c=='_'):
                    #print("hola?", c)
                    edo=100
                    self.temp+=c

                elif(c=='"'):
                    edo=4
                    self.temp+=c

                elif(c=='+' or c=='-'):
                    #print("a")
                    edo=6
                    self.temp+=c

                elif(c=='*' or c=='/'):
                    edo=7
                    self.temp+=c

                elif(c=='='):
                    edo=8
                    self.temp+=c

                elif(c=='<' or c=='>'):
                    edo=9
                    self.temp+=c

                elif(c=='!'):
                    edo=10
                    self.temp+=c

                elif(c=='&'):
                    edo=12
                    self.temp+=c

                elif(c=='|'):
                    edo=14
                    self.temp+=c

                elif(c==';'):
                    edo=16
                    self.temp+=c

                elif(c==','):
                    edo=17
                    self.temp+=c

                elif(c=='('):
                    edo=18
                    self.temp+=c

                elif(c==')'):
                    edo=19
                    self.temp+=c

                elif(c=='{'):
                    edo=20
                    self.temp+=c

                elif(c=='}'):
                    edo=21
                    self.temp+=c

                else:
                    self.continua=False
                    self.index-=1
            
            elif(edo==1):
                if(c>='0' and c<='9'):
                    edo=1
                    self.temp+=c

                elif(c=='.'):
                    edo=2
                    self.temp+=c

                else:
                    self.continua=False
                    self.index-=1
            
            elif(edo==2):
                if(c>='0' and c<='9'):
                    edo=3
                    self.temp+=c

                else:
                    self.continua=False
                    self.index-=1

            elif(edo==3):
                if(c>='0' and c<='9'):
                    edo=3
                    self.temp+=c
                
                else:
                    self.continua=False
                    self.index-=1

            elif(edo==4):
                if(c=='"'):
                    edo=5
                    self.temp+=c
                    self.continua=False
                elif(c!='"'):
                    edo=4
                    self.temp+=c
                else:
                    self.continua=False
                    self.index-=1

            elif(edo==6):
                self.continua=False
                self.index-=1

            elif(edo==7):
                self.continua=False
                self.index-=1

            elif(edo==8 or edo==9 or edo==10):
                if(c=='='):
                    edo=11
                    self.temp+=c
                else:
                    self.continua=False
                    self.index-=1

            elif(edo==11):
                self.continua=False
                self.index-=1

            elif(edo==12):
                if(c=='&'):
                    edo=13
                    self.temp+=c
                else:
                    self.continua=False
                    self.index-=1

            elif(edo==13):
                self.continua=False
                self.index-=1

            elif(edo==14):
                if(c=='|'):
                    edo=15
                    self.temp+=c
                else:
                    self.continua=False
                    self.index-=1

            elif(edo==15):
                self.continua=False
                self.index-=1

            elif(edo==16):
                self.continua=False
                self.index-=1

            elif(edo==17):
                self.continua=False
                self.index-=1

            elif(edo==18):
                self.continua=False
                self.index-=1

            elif(edo==19):
                self.continua=False
                self.index-=1

            elif(edo==20):
                self.continua=False
                self.index-=1

            elif(edo==21):
                self.continua=False
                self.index-=1

            elif(edo==100):
                if(c>='a' and c<='z' or c>='A' and c<='Z' or c=='_'):
                    edo=100 
                    self.temp+=c
                    #print("hola?", c)
                else:
                    self.continua=False
                    self.index-=1

            self.index+=1
        

        #Se verifica que tipo de token es y se guarda en un diccionario

        if(edo==1):
            self.tipo=TipoToken.entero

        elif(edo==3):
            self.tipo=TipoToken.real

        elif(edo==5):
            self.tipo=TipoToken.string
            
        elif(edo==6):
            self.tipo=TipoToken.opSuma

        elif(edo==7):
            self.tipo=TipoToken.opMul

        elif(edo==8):
            self.tipo=TipoToken.equal

        elif(edo==9 or edo==11):
            self.tipo=TipoToken.opRel

        elif(edo==10):
            self.tipo=TipoToken.opNOT

        elif(edo==13):
            self.tipo=TipoToken.opAND

        elif(edo==15):
            self.tipo=TipoToken.opOR

        elif(edo==16):
            self.tipo=TipoToken.puntoComa

        elif(edo==17):
            self.tipo=TipoToken.coma

        elif(edo==18):
            self.tipo=TipoToken.parent_ini

        elif(edo==19):
            self.tipo=TipoToken.parent_fin

        elif(edo==20):
            self.tipo=TipoToken.llave_ini

        elif(edo==21):
            self.tipo=TipoToken.llave_fin

        elif(edo==100):#Aqui va todo lo del if y tipos de datos
            if(self.temp=="int" or self.temp=="float" or self.temp=="void"):
                self.tipo=TipoToken.tipo

            elif(self.temp=="if"):
                self.tipo=TipoToken.IF

            elif(self.temp=="while"):
                self.tipo=TipoToken.WHILE

            elif(self.temp=="return"):
                self.tipo=TipoToken.RETURN

            elif(self.temp=="else"):
                self.tipo=TipoToken.ELSE

            else:
                self.tipo=TipoToken.identificador

        elif(self.index>=len(cadena)):
            self.tipo=TipoToken.pesos
            self.temp="$"
        #print(self.temp)

        else:
            self.tipo=TipoToken.pesos
            self.temp="$"

        TablaSalida={'lexema':self.temp, 'tipo':self.tipo}

        return TablaSalida

    def Show_TokenType(self,TokenEntrada):
        if(TokenEntrada['tipo']==TipoToken.entero):
            print(TokenEntrada['lexema'], " Es un entero")

        elif(TokenEntrada['tipo']==TipoToken.real):
            print(TokenEntrada['lexema'], " Es un real")

        elif(TokenEntrada['tipo']==TipoToken.identificador):
            print(TokenEntrada['lexema'], " : Es un identificador")

        elif(TokenEntrada['tipo']==TipoToken.string):
            print(TokenEntrada['lexema'], " : Es una cadena")

        elif(TokenEntrada['tipo']==TipoToken.opSuma):
            print(TokenEntrada['lexema'], " : Es un simbolo adicion")
        
        elif(TokenEntrada['tipo']==TipoToken.opMul):
            print(TokenEntrada['lexema'], " : Es un simbolo MUL")

        elif(TokenEntrada['tipo']==TipoToken.opRel):
            print(TokenEntrada['lexema'], " : Es un operador relacional")

        elif(TokenEntrada['tipo']==TipoToken.opAND):
            print(TokenEntrada['lexema'], " : Es un operador AND")

        elif(TokenEntrada['tipo']==TipoToken.opOR):
            print(TokenEntrada['lexema'], " : Es un operador OR")

        elif(TokenEntrada['tipo']==TipoToken.opNOT):
            print(TokenEntrada['lexema'], " : Es un operador NOT")

        elif(TokenEntrada['tipo']==TipoToken.equal):
            print(TokenEntrada['lexema'], " : Es un simbolo de asignacion")

        elif(TokenEntrada['tipo']==TipoToken.puntoComa):
            print(TokenEntrada['lexema'], " : Es un simbolo de punto y coma")
        
        elif(TokenEntrada['tipo']==TipoToken.coma):
            print(TokenEntrada['lexema'], " : Es un simbolo coma")

        elif(TokenEntrada['tipo']==TipoToken.parent_ini):
            print(TokenEntrada['lexema'], " : Es un parentesis inicial")

        elif(TokenEntrada['tipo']==TipoToken.parent_fin):
            print(TokenEntrada['lexema'], " : Es un parentesis final")

        elif(TokenEntrada['tipo']==TipoToken.llave_ini):
            print(TokenEntrada['lexema'], " : Es un llave inicial")

        elif(TokenEntrada['tipo']==TipoToken.llave_fin):
            print(TokenEntrada['lexema'], " : Es un llave final")

        elif(TokenEntrada['tipo']==TipoToken.IF):
            print(TokenEntrada['lexema'], " : Es una palabra resrvada")

        elif(TokenEntrada['tipo']==TipoToken.WHILE):
            print(TokenEntrada['lexema'], " : Es una palabra resrvada")

        elif(TokenEntrada['tipo']==TipoToken.RETURN):
            print(TokenEntrada['lexema'], " : Es una palabra resrvada")

        elif(TokenEntrada['tipo']==TipoToken.ELSE):
            print(TokenEntrada['lexema'], " : Es una palabra resrvada")

        elif(TokenEntrada['tipo']==TipoToken.tipo):
            print(TokenEntrada['lexema'], " : Es un tipo de dato")

        elif(TokenEntrada['tipo']==TipoToken.pesos):
            print(TokenEntrada['lexema'], " : Fin de cadena")