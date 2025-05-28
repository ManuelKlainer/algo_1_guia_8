from queue import Queue as Cola
from copiar_cola import copiar_cola

def pacientes_urgentes(c:Cola[tuple[int,str,str]]):
	res: int = 0
	c2:Cola[tuple[int,str,str]] = copiar_cola(c)
	while (not c2.empty()):
		paciente: tuple[int,str,str] = c2.get()
		x, _, _ = paciente
		if x < 4:
			res = res + 1
	return res
