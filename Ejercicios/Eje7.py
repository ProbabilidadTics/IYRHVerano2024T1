import Ejercicios.Graficas as graf 
import Ejercicios.Tabla as tbl
import Ejercicios.DigDisyCua as disCua


datosEquipos = [
    'Pumas','América','Chivas','Pumas','Chivas','Chivas','América','Toluca','Toluca','Pumas',
    'Santos','Necaxa','América','América','América','Pumas','Santos','Pumas','Pumas','Pumas',
    'América','Chivas','América','Pumas','Necaxa','Toluca','Chivas','América','Toluca','Santos'
]

clases, fa, faAc, fr, frAc = disCua.generateQualitativeData(datosEquipos)
frStr, frAcStr = tbl.datosStrPorcentaje(fr, frAc)

encabezados = ["Clases", "F.Absoluta", "F.Relativa", "F.Acumulada"]
contenido = [clases, fa, frStr, frAcStr]
tbl.printHTMLTable(encabezados, contenido)

graf.createBarDiagram(clases, fa)
graf.createPieChart(clases, fa, fr)