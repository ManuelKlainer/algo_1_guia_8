def quitar_espacios_iniciales(linea: str) -> str:
	res: str = ""
	pasados_espacio: bool = False
	for c in linea:
		if not pasados_espacio:
			if c != ' ':
				pasados_espacio = True
				res += c
		else:
			res += c
	return res	


def clonar_sin_comentarios(nombre_archivo: str, nombre_salida: str):
	entrada = open(nombre_archivo, "r",encoding="utf-8")
	salida = open(nombre_salida, "w",encoding="utf-8")
	lineas: list[str] = entrada.readlines()
	lineas_sin_comentarios: list[str] = []
	for linea in lineas:
		linea_sin_espacios: str = quitar_espacios_iniciales(linea)
		if linea_sin_espacios[0] != "#":
			lineas_sin_comentarios.append(linea)
	salida.writelines(lineas_sin_comentarios)
	entrada.close()
	salida.close()
