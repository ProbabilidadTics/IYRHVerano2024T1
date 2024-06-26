import Ejercicios.Graficas as graf 
import Ejercicios.Tabla as tbl
import Ejercicios.DigDisyCua as disCua


datosDecimal = [
    2.5,4.5,5.8,2.2,5.7,5.3,4.0,0.9,2.5,2.3,3.2,4.9,2.7,3.7,3.8,4.9,2.8,3.6,4.2,3.1,7.2,1.9,5.9,3.3,2.9,1.1,1.7,2.6,3.1,4.4
]

print("A. Son datos continuos")

clases, limsInf, limsSup, mrksClases, fa, fr, frAc = disCua.generateGroupedData(datosDecimal,1,6)
frStr, frAcStr = tbl.datosStrPorcentaje(fr, frAc)


encabezados = ["Clases", "L. Inferior", "L. Superior", "M. Clase", "F. Absoluta", "F. Relativa", "F. Acumulada"]
contenido = [clases, limsInf, limsSup, mrksClases, fa, frStr, frAcStr]
tbl.printHTMLTable(encabezados, contenido)


graf.createHistogram(mrksClases, fr) 
graf.createOjiva(mrksClases, frAc)
