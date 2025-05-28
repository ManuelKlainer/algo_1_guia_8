from queue import Queue as Cola
from copiar_cola import copiar_cola
import random

def armar_secuencia_de_bingo() -> Cola[int]:
	res: Cola[int] = Cola()
	nums: list[int] = list(range(1,100))
	random.shuffle(nums)
	for el in nums:
		res.put(el)
	return res


def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
	res: int = 0
	acum: int = 0
	bolilleroAux: Cola[int] = copiar_cola(bolillero)
	while (acum < len(carton) and (not bolilleroAux.empty())):
		res = res + 1
		el : int = bolilleroAux.get()
		if (el in carton):
			acum = acum + 1

	return acum
