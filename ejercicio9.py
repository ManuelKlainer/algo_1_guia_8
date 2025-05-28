from queue import Queue as Cola
from copiar_cola import copiar_cola

def cantidad_elementos(cola: Cola) -> int:
	res: int = 0
	cola_copiada: Cola = copiar_cola(cola)
	while (not (cola_copiada.empty())):
		cola.get()
		res = res+1
	return res