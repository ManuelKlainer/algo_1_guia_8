from queue import Queue as Cola
from copiar_cola import copiar_cola

def buscar_el_maximo(c: Cola[int]) -> int:
	cola_copiada: Cola[int] = copiar_cola(c)
	max_actual : int = cola_copiada.get()
	while (not (cola_copiada.empty())):
		el: int = cola_copiada.get()
		if (el > max_actual):
			max_actual = el
	return max_actual