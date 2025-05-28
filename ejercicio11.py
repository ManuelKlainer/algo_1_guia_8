from queue import Queue as Cola
from copiar_cola import copiar_cola

def buscar_nota_minima(c: Cola[tuple[str,int]]) -> tuple[str,int]:
	c2: Cola[tuple[str,int]] = copiar_cola(c)
	res : tuple[str,int] = c2.get()
	while (not (c2.empty())):
		el : tuple[str,int] = c2.get()
		if (el[1] > res[1]):
			res = el
	return res
