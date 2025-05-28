def calcular_promedio_por_estudiante(notas: list[tuple[str,float]]) -> dict[str,float]:
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
