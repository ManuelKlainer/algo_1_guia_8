from queue import LifoQueue as Pila
import random
def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    res: Pila[int] = Pila()
    for _ in range(cantidad):
        res.put(random.randint(desde,hasta))
    return res