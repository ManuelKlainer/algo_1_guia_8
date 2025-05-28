from queue import LifoQueue as Pila
from copiar_pila import copiar_pila
def buscar_el_maximo (p:Pila[int]):
    pila_copiada: Pila[int] = copiar_pila(p)
    maximo = pila_copiada.get()
    while not pila_copiada.empty():
        el: int = pila_copiada.get()
        if el > maximo:
            maximo = el
    return maximo
