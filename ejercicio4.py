from queue import LifoQueue as Pila
def buscar_nota_maxima (p:Pila[tuple[str,int]]) -> tuple[str,int]:
    maximo = p.get()
    aux:Pila[tuple[str,int]] = Pila()
    aux.put(maximo)
    while (not p.empty()):
        el : tuple[str,int] = p.get()
        if (el[1] > maximo[1]):
            maximo = el
        aux.put(p.get())
        
    while (not aux.empty()):
        el : tuple[str,int] = aux.get()
        p.put(el)
    return maximo
