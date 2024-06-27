import Ejercicios.Graficas as graf 
import Ejercicios.Tabla as tbl
import Ejercicios.DigCont as digCont

datosEj12 = [
    250,790,470,510,500,330,300,750,580,740,420,260,440,770,400,540,530,330,390,380,340,460,530,260,410,360,270,510,630,330
]
print(len(datosEj12))

print("A. Son datos continuos")


clases, limsInf, limsSup, mrksClases, fa, fr, frAc = digCont.generateGroupedData(datosEj12,2,6)
frStr, frAcStr = tbl.datosStrPorcentaje(fr, frAc)
print(sum(fa))

encabezados = ["Clases", "Límites inferiores", "Límites superiores", "Marca de clase", "Fa", "Fr", "FrAcum."]
contenido = [clases, limsInf, limsSup, mrksClases, fa, frStr, frAcStr]
tbl.printHTMLTable(encabezados, contenido)


graf.createHistogram(mrksClases, fr) 
graf.createOjiva(mrksClases, frAc)