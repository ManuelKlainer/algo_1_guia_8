def contar_lineas(nombre_archivo: str) -> int:
	archivo = open(nombre_archivo, "r",encoding="utf-8")
	lineas: list[str] = archivo.readlines()
	archivo.close()
	return len(lineas)

def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
	archivo = open(nombre_archivo, "r",encoding="utf-8")
	contenido: str = archivo.read()
	archivo.close()
	return (palabra in contenido)

def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
	archivo = open(nombre_archivo, "r",encoding="utf-8")
	contenido: str = archivo.read()
	archivo.close()
	return contenido.count(palabra)
