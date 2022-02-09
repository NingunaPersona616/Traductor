import enum

cadena="1324.56"

class TipoToken(enum.Enum):
    identificador=0
    entero=1
    real=2

class Lexico:
    edo=0
    index=0
    continua=False
    tipo=-1
    
    def lex(self,cadena):
        edo=0
        self.continua=True
        self.temp=""
        #En simples palabras es el automata, termina si encuentra un caracter no valido o fin de cadena
        while(self.continua and self.index<len(cadena)):
            c=cadena[self.index]
            if(edo==0):
                if(c>='0' and c<='9'):
                    edo=1
                    self.temp+=c

                elif(c>='a' and c<='z' or c>='A' and c<='Z' or c=='_'):
                    edo=100
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

            elif(edo==100):
                if(c>='a' and c<='z' or c>='A' and c<='Z' or c=='_'):
                    edo=100 
                    self.temp+=c

                else:
                    self.continua=False
                    self.index-=1

            self.index+=1
        

        #Se verifica que tipo de token es y se guarda en un diccionario
        if(edo==1):
            self.tipo=TipoToken.entero

        elif(edo==3):
            self.tipo=TipoToken.real

        elif(edo==100):
            self.tipo=TipoToken.identificador

        print(self.temp)

        TablaSalida={'lexema':self.temp, 'tipo':self.tipo}

        return TablaSalida

    def Show_TokenType(self,TokenEntrada):
        if(TokenEntrada['tipo']==TipoToken.entero):
            print(TokenEntrada['lexema'], " Es un entero")

        elif(TokenEntrada['tipo']==TipoToken.real):
            print(TokenEntrada['lexema'], " Es un real")

        elif(TokenEntrada['tipo']==TipoToken.identificador):
            print(TokenEntrada['lexema'], " : Es un identificador")