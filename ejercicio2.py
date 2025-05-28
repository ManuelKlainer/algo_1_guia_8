from queue import LifoQueue as Pila
def cantidad_elementos(p:Pila):
    aux:list = []
    while (not p.empty()):
        aux.append(p.get())
    for i in range(len(aux)-1,-1,-1):
        p.put(aux[i])
    return len(aux)