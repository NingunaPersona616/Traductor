from Lexico import Lexico

Analizador=Lexico()

cadena="a+b+c+d+e+f"
listaentrada=list()

while(Analizador.temp!="$"):
    token=Analizador.lex(cadena)

    Analizador.Show_TokenType(token)
    listaentrada.append(token)