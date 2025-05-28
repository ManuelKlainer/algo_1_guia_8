def palabra_mas_frecuente(nombre_archivo: str) -> str:
	archivo = open(nombre_archivo, "r",encoding="utf-8")
	lineas: list[str] = archivo.readlines()
	archivo.close()
	palabras: dict[str,int] = {}
	for linea in lineas:
		palabra: str = ""
		for c in linea:
			if (c == " "):
				if palabra != "":
					if (palabra in palabras):
						palabras[palabra] += 1
					else:
						palabras[palabra] = 1
			if palabra != "":
				if (palabra in palabras):
						palabras[palabra] += 1
				else:
						palabras[palabra] = 1

	res: str = ""
	freq: int = 0
	for palabra,frecuencia in palabras.items():
		if frecuencia > freq:
			res = palabra
			freq = frecuencia
	return res


