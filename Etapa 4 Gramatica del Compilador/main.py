from Lexico import Lexico
from Sintactico import Sintactico

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
ejercicio='void main ( ) {a="Hola Mundo";}'
listaentrada1=list()
print('\n\nEJERCICO 1 ANALIZADOR SINTACTICO\n\n')
print("Proceso Lexico\n")
while(Analizador.temp!="$"):
    token=Analizador.lex(ejercicio)

    Analizador.Show_TokenType(token)
    listaentrada1.append(token)


#ANALISIS SINTACTICO
print("\nProceso Sintactico\n")
listaentrada1.reverse()#Pila invertida que sirve como cola de entrada

syntax=Sintactico(TablaLR, id_Regla, lon_Regla, nom_NoTerminal) #cargamos la gramatica al analizador sintactico

sies=syntax.prueba(listaentrada1)   #pasamos la lista de entrada dividida en tokens y se prueba si esta sintacticamente correcta

if(sies):
    print("\n", ejercicio, "=Aceptacion")
else:
    print("\n", ejercicio, "=Denegada")

