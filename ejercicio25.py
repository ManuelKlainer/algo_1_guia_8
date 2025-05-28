def agregar_fase_al_principio(nombre_archivo: str, frase:str):
	archivo = open(nombre_archivo, 'r', encoding='utf-8')
	lineas: list[str] = archivo.readlines()
	archivo.close()
	lineas.insert(0,frase+'\n')
	archivo = open(nombre_archivo, 'w', encoding='utf-8')
	archivo.writelines(lineas)