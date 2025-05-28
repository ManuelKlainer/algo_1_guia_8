from queue import LifoQueue as Pila
from copiar_pila import copiar_pila
def buscar_nota_maxima (p:Pila[tuple[str,int]]):
    pila_copiada:Pila[tuple[str,int]] = copiar_pila(p)
    maximo = pila_copiada.get()
    while (not pila_copiada.empty()):
        el : tuple[str,int] = pila_copiada.get()
        if (el[1] > maximo[1]):
            maximo = el
    return maximo
