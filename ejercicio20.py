def split(texto: str, sep: str) -> list[str]:
	res: list[str] = []
	acum: str = ""
	iniciado: bool = False
	for ch in texto:
		if ch == sep:
			if iniciado and acum != "":
				res.append(acum)
				acum = ""
		else:
			iniciado = True
			acum = acum + ch
	if acum != "":
		res.append(acum)
	return res


def agrupar_por_longitud(nombre_archivo: str) -> dict[int,int]:
	res: dict[int,int] = {}
	archivo = open(nombre_archivo, "r",encoding="utf-8")
	lineas: list[str] = archivo.readlines()
	archivo.close()
	for linea in lineas:
		palabras: list[str] = split(linea, " ")
		for palabra in palabras:
			longitud: int = len(palabra)
			if longitud in res:
				res[longitud] = longitud + 1
			else:
				res[longitud] = 1
	return res