from Lexico import Lexico
from Sintactico import Sintactico
from Semantico import Semantico

id_Regla=[]
lon_Regla=[]
nom_NoTerminal=[]
TablaLR=[]


#LEER EL ARCHIVO DE LA GRAMATICA
file=open("compilador.lr")  #Cambiar nombre segun se requiera
cant_reglas=file.readline()

for i in range(int(cant_reglas)):
    line=file.readline()
    regla=line.split()
    id_Regla.append(int(regla[0]))
    lon_Regla.append(int(regla[1]))
    nom_NoTerminal.append(regla[2])

size=file.readline().split()
filas=int(size[0])
columnas=int(size[1])


for i in range(filas):
    line=file.readline().split()
    fila=[]
    for j in range(columnas):
        fila.append(int(line[j]))

    TablaLR.append(fila)

file.close()

Analizador=Lexico()

#ANALISIS LEXICO
#ejercicio='int main (int x, int y) { int a,b,c; a=print(); b=z;} float c;'
ejercicio='int a; int suma (int a, int b){return a+b;} int main () { float a; int b; int c; c=a+b; c=suma(8,9);}'

listaentrada1=list()
print("\nProceso Lexico\n")
while(Analizador.temp!="$"):
    token=Analizador.lex(ejercicio)

    Analizador.Show_TokenType(token)
    listaentrada1.append(token)

#print(listaentrada1)

#ANALISIS SINTACTICO
print("\n\nProceso Sintactico\n\n")
listaentrada1.reverse()#Pila invertida que sirve como cola de entrada

syntax=Sintactico(TablaLR, id_Regla, lon_Regla, nom_NoTerminal) #cargamos la gramatica al analizador sintactico

sies=syntax.prueba(listaentrada1)   #pasamos la lista de entrada dividida en tokens y se prueba si esta sintacticamente correcta

if(sies):
    print("\n\nLa cadena: \n", ejercicio, " tiene el estado de: Aceptacion")

    miarbol=syntax.Arbol

    print("\n\n******************\nARBOL SINTACTICO\n******************\n")
    print(miarbol.getData(), "\n")

    miarbol.nodo.imprimir(0)
    """sangria=0
    aux=miarbol.pop()
    print(aux.GetRegla(), "\n")
    for i in range(len(miarbol)-1):
        aux=miarbol.pop()
        if(aux.GetNum_Elementos()>0):
            if(aux.GetNum_Elementos()>4):
                sangria-=8
                print("  "*sangria, end="")
                aux.imprimir()
                sangria+=6
            else:
                print("    "*sangria, end="")
                aux.imprimir()
            sangria+=int(aux.GetNum_Elementos())"""

    print("\n\n********************\nANALISIS SEMANTICO\n********************")
    Analizador_Seman=Semantico()
    Analizador_Seman.Analizar_Nodo(miarbol.nodo)

    print("\n\nTABLA DE SIMBOLOS\n")
    #Analizador_Seman.iniciaSemantico()
    Analizador_Seman.imprimir_ListaSimbolos()

    print("\n\n\nLISTA DE ERRORES\n")
    Analizador_Seman.imprimir_ListaErrores()
else:
    print("\n", ejercicio, "=Denegada")