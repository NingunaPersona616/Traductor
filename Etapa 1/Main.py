from CAnalizadorLexico import CAnalizadorLexico

CadenaEntrada='int segssss = split ( )'
SubCadenas=CadenaEntrada.split(' ')
Analizador=CAnalizadorLexico()

for i in range(len(SubCadenas)):
    Analizador.ReadInput(SubCadenas[i])
    tipo=Analizador.Analize()
    Analizador.ShowType(tipo)