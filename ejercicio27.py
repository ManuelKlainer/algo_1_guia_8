def calcular_promedio_estudiantes(notas: list[tuple[str,float]]) -> dict[str,float]:
	cantidad_notas: dict[str,float] = {}
	suma_notas:dict[str,float] = {}
	for alumno,nota in notas:
		if alumno in cantidad_notas:
			cantidad_notas[alumno] = cantidad_notas[alumno] + 1
			suma_notas[alumno] = suma_notas[alumno] + nota
		else:
			cantidad_notas[alumno] = 1
			suma_notas[alumno] = nota

	promedio_notas:dict[str,float] = {}
	for alumno in cantidad_notas:
		promedio_notas[alumno] = suma_notas[alumno] / cantidad_notas[alumno]
	return promedio_notas

def split(texto: str, delimitador: str) -> list[str]:
    res: list[str] = []
    acum: str = ""
    for c in texto:
        if (c == delimitador):
            if (acum != ""):
                res.append(acum)
            acum = ""
        else:
            acum += c
    if (acum != ""):
        res.append(acum)
    return res


def calcular_promedio_por_estudiante(nombre_archivo_notas: str, nombre_archivo_promedios: str):
    archivo = open(nombre_archivo_notas, 'r')
    contenido: list[str] = archivo.readlines()
    archivo.close()
    notas: list[tuple[str,float]] = []
    for linea in contenido:
        elementos: list[str] = split(linea,",")
        lu: str = elementos[0]
        nota: float = float(elementos[3])
        registro: tuple[str,float] = (lu,nota)
        notas.append(registro)
    promedios: dict[str,float] = calcular_promedio_estudiantes(notas)
    salida = open(nombre_archivo_promedios, 'w')
    lineas: list[str] = []
    for alumno,promedio in promedios.items():
        linea: str = alumno+","+str(promedio)+'\n'
        lineas.append(linea)
    salida.writelines(lineas)
    salida.close()
        

calcular_promedio_por_estudiante("file.csv","file2.csv")
