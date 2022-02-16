from Lexico import Lexico
from Sintactico import Sintactico

E=3
d2=2
d3=3
d4=4
r0=-1
r1=-2
r2=-3

tablaLR1=[
    [d2, 0, 0, 1],
    [0, 0, r0, 0],
    [0, d3, 0, 0],
    [d4, 0, 0, 0],
    [0, 0, r1, 0]
]

tablaLR2=[
    [d2, 0, 0, 1],
    [0, 0, r0, 0],
    [0, d3, r2, 0],
    [d2, 0, 0, 4],
    [0, 0, r1, 0]
]

ej1_id=[3]#id de la regla de reducion del primer ejercicio
ej1_regla=[3]#longitud de la regla de reducion del primer ejercicio

ej2_id=[3,3]#id de las reglas de reducion del segundo ejercicio
ej2_regla=[3, 1]#longitud de las reglas de reducion del segundo ejercicio


Analizador=Lexico()


#EJERCICO 1 ANALIZADOR SINTACTICO
ejercicio1="hola+mundo"
listaentrada1=list()
print('\n\nEJERCICO 1 ANALIZADOR SINTACTICO\n\n')
print("Proceso Lexico\n")
while(Analizador.temp!="$"):
    token=Analizador.lex(ejercicio1)

    Analizador.Show_TokenType(token)
    listaentrada1.append(token)


#IDEAAA pasar las tablas y arreglos de una como parametro del constructor del analizador sintactico

print("\nProceso Sintactico\n")
listaentrada1.reverse()

syntax=Sintactico(tablaLR1, ej1_id, ej1_regla)

sies=syntax.prueba(listaentrada1)

if(sies):
    print("\n", ejercicio1, "=Aceptacion")
else:
    print("\n", ejercicio1, "=Denegada")



Analizador2=Lexico()
#EJERCICO 2 ANALIZADOR SINTACTICO
ejercicio2="a+b+c+d+e+f"
listaentrada2=list()
print('\n\nEJERCICO 2 ANALIZADOR SINTACTICO\n\n')
print("Proceso Lexico\n")
while(Analizador2.temp!="$"):
    token=Analizador2.lex(ejercicio2)

    Analizador2.Show_TokenType(token)
    listaentrada2.append(token)


#IDEAAA pasar las tablas y arreglos de una como parametro del constructor del analizador sintactico

print("\nProceso Sintactico\n")
listaentrada2.reverse()

syntax2=Sintactico(tablaLR2, ej2_id, ej2_regla)

sies=syntax2.prueba(listaentrada2)

if(sies):
    print("\n", ejercicio2, "=Aceptacion")
else:
    print("\n", ejercicio2, "=Denegada")
