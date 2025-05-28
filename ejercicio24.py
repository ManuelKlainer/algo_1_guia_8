def agregar_frase_al_final(nombre_archivo: str, frase:str):
	archivo = open(nombre_archivo, 'r', encoding='utf-8')
	lineas: list[str] = archivo.readlines()
	archivo.close()

	if (not ('\n' in lineas[len(lineas)-1])):
		lineas[len(lineas)-1] += '\n'
	lineas.append(frase)
	archivo = open(nombre_archivo, 'w', encoding='utf-8')
	archivo.writelines(lineas)

