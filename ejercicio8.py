from queue import Queue as Cola
import random

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
	res: Cola[int] = Cola()
	for _ in range(cantidad):
		res.put(random.randint(desde,hasta))
	return res
