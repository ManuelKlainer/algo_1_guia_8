from queue import LifoQueue as Pila
def buscar_el_maximo (p:Pila[int]):
    maximo = p.get()
    aux:Pila[int] = Pila()
    aux.put(maximo)
    while (not p.empty()):
        el : int = p.get()
        if (el > maximo):
            maximo = el
        aux.put(el)
        
    while (not aux.empty()):
        p.put(aux.get())
    return maximo
