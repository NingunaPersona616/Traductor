# Traductor de la materia Sem. Trad. 2

## Primera etapa del proyecto: Analizador Lexico
Mini analizador lexico que acepta los ismbolos de simbolos_lexicos.pdf

## Mini generador lexico: Analizador lexico arreglado
Mini genarador lexico que el profesor dejó terminaramos, y que reconoce ids, '+', floats e ints y los guarda para el analizador sintactico

## Etapa 2 Analisis Sintactico
Analizador sintactico que trabaja en conjunto con el analizador lexico para resolver los ejercicios 1 y 2 

19/02/20222 No me di cuenta que las listas fuera del constructor se comparten con todas las instancias, aunque no genera ningun problema porque el constructor vuelve a pushear '$' y '0' y el algoritmo vuelve a funcionar como si fuera una pila vacia jajaja. Funciona correctamente simplemente es raro de ver.

## Etapa 3
Analizador Sintáctico (Implementación usando Objetos)

IDEA: checar con más tablas LR

## Etapa 4: Gramatica del Compilador
Se lee una gramatica desde un arhivo externo y se pasa a la gramatica del analizador sintactico

IDEA: Checar las reglas a fondo, espero que el analizador lexico ya no tenga bugs

## Etapa 5 Arbol Sintactico
Creacion del arbol sintactico a partir de nodos (sin la creacion de las 52 clases) y una lista que almacena los nodos como si se tratara de un arbol. Arregle el lexico ya que dejaba pasar tokens que no debian entrar al sintactico.

## Etapa 6 Analisis Semantico
Recorrido del arbol sintactico comprobando la semantica de cada uno de los nodos y sus posibles errores, utilizando un arbol de nodos genericos y no los 52 nodos que se habian pedido.