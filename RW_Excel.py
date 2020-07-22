import xlrd

libro = xlrd.open_workbook("documento_prueba.xlsx")

# Imprime un arreglo con los nombres de las hojas del libro.
print(libro.sheet_names())

hojas = libro.sheets()
filas = []
for hoja in hojas:
    for i in range(hoja.nrows):
        for j in range(hoja.ncols):
            celda = hoja.cell_value(i, j)
            if celda != "":
                print("i = ",i," j = ",j," -- ",celda)
            