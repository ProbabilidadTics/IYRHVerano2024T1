import Ejercicios.Frecuencias as frec 
import Ejercicios.DigDisyCua as disCua 
import Ejercicios.DigCont as digCont
import Ejercicios.Graficas as graf 
import Ejercicios.Tabla as tbl

datosEje15 = [
    "Ramirez","Garcia","González","Rodriguez","Pérez","Rodríguez","Martinez","Flodriguez","Hernández","Garcia",
    "Hernández","López","Pérez","González","Martinez","Hernández","González","Rodriguez","Sánchez","Hernández","Rodriguez",
    "Martinez","Ramirez","Pérez","Sanchez","Rodriguez","López","Sánchez","Rodriguez","Ramirez","González","López","Martinez",
    "López","Garcia","González","González","López","Martinez","González","Ramirez","Gutiérrez ","Sánchez","Flores","Garcia",
    "Hernández","Martinez","Garcia","Hernández","Flores","Martinez","Garcia","López","Gutiérrez","López","Garcia","González",
    "Hernández","Garcia","Gutiérrez","Ramirez","Garcia","Rodriguez","Hernández","Sánchez","González","Gutiérrez","Martinez",
    "González","Rodriguez","Hernández","Hernández","González","Garcia","Hernández","López","Martinez","García","Garcia",
    "Hernández","Sánchez","Garcia","Hernández","Flores","Pérez","Martinez","Hernández","Ramírez","López","Sánchez","Martinez",
    "Garcia","Flores","Pérez","López","Pérez","González","Hernández","Sánchez","Martinez"
]

# Datos
clases, fa, faAc, fr, frAc = disCua.generateQualitativeData(datosEje15)
frStr, frAcStr = tbl.datosStrPorcentaje(fr, frAc)

# Tabla
encabezados = ["Clases", "Fa", "Fr", "Fr Acum"]
contenido = [clases, fa, frStr, frAcStr]
tbl.printHTMLTable(encabezados, contenido)

# Gráficas
graf.createBarDiagram(clases, fa)