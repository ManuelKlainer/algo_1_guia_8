def invertir_lineas(nombre_entrada: str, nombre_salida: str):
	entrada = open(nombre_entrada, "r",encoding="utf-8")
	salida = open(nombre_salida, "w",encoding="utf-8")
	lineas: list[str] = entrada.readlines()
	lineas_salida: list[str] = []
	for i in range(len(lineas)-1,-1,-1):
		lineas_salida.append(lineas[i])
	salida.writelines(lineas_salida)
	entrada.close()
	salida.close()

