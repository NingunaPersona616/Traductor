from Lexico import Lexico

Analizador=Lexico()

cadena="132456"

token=Analizador.lex(cadena)

print(token)

Analizador.Show_TokenType(token)